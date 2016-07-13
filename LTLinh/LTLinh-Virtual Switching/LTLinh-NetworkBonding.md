#Network Bonding
Cho phép kết hợp nhiều network interface vào thành 1 interface sử dụng bonding module của Linux kernel và một interface bonding. Điều này cho phép 2 network interface hoạt động như 1 interface. Điều này đem lại 2 lợi ích:
- Tăng độ tin cậy. Bonding module có thể cho phép 2 interface hoạt động ở chế độ active-standby. Khi đường truyền active interface bị lỗi, dẫn đến việc không truyền tải được nội dung, Linux kernel sẽ tự động chuyển qua standby interface.
- Tăng bandwidth. Nếu là cable G thì thông lượng tối đa của 1 Giga NIC là 1Gbps. Bằng việc load-balancing qua 2 NIC, ta có thể tăng thông lượng truyền tải lên 2Gbps.

#1. Các chế độ Network Bonding
Các chế độ này xác định cách thức mà lưu lượng gửi ra bởi interface bonded được thực sự phân tán qua các interface thật.

##1.1 Mode=0 (balance-rr)
Round-robin : Là chế độ mặc định. Nó truyền các gói tin theo thứ tự tuần tự từ slave đầu tiên đến cuối cùng.Nếu có 2 interface thật và 2 gói tin đến, thì gói tin đầu tiên sẽ đi vào interface1 và gói tin thứ 2 sẽ đi vào interface2. Chế độ này cung cấp cân bằng tải và chịu lỗi.

##1.2 Mode 1 (active-backup):
Chế độ này đặt một trong các interface vào trạng thái backup và sẽ chỉ hoạt động nếu interface đang hoạt động bị lỗi. Chỉ có một slave hoạt động trong một thời điểm. Một slave khác nhau sẽ được kích hoạt chỉ khi slave đang hoạt động bị lỗi. Chế độ này cung cấp khả năng chịu lỗi.

##1.3 Mode=2 (balance-xor)
Truyền traffic thông qua phép toán XOR giữa source MAC nguồn với source MAC đích. Nó sẽ lựa chọn cùng 1 slave cho 1 địa chỉ MAC. Cung cấp cân bằng tải và khả năng chịu lỗi.

##1.4 Mode=3 (broadcast)
Toàn bộ gói tin sẽ được truyền trên tất cả slave interface. Chế độ này ít được sử dụng. Cung cấp khả năng chịu lỗi.

##1.5 Mode=4 (802.3ad)
IEEE 802.3ad Dynamic link aggregation: Tạo nhóm tập hợp có các thiết lập cùng speed và chế độ duplex. Sử dụng tất cả các slave ở trình tập hợp hoạt động theo các đặc điểm kỹ thuật 802.3ad.

LACP cân bằng tải lưu lượng gửi đi qua các cổng hoạt động dựa trên thông tin giao thức băm và chấp nhận lưu lượng đến từ bất kỳ cổng nào đang hoạt động. Các băm bao gồm các nguồn Ethernet và địa chỉ đích và nếu có, VLAN tag, và nguồn và đích IPv4 / IPv6 địa chỉ. Điều này được tính toán phụ thuộc vào tham số `transmit-hash-policy`.

Điều kiện tiên quyết:
- Ethtool hỗ trợ trong các trình điều khiển cơ sở để lấy tốc độ và duplex của mỗi slave.
- Một switch có hỗ trợ IEEE 802.3ad Dynamic link aggregation. Hầu hết các switch sẽ yêu cầu một số loại cấu hình để kích hoạt chế độ 802.3ad.

###1.5.1 LACP:
802.3ad mode is an IEEE standard được gọi là LACP (Link Aggregation Control Protocol).

LACP là chuẩn mở của IEEE. Nó cho phép tạo Etherchannel (Công nghệ EtherChannel của Cisco cho phép kết hợp các kết nối Etheret thành một bó (bundle) để tăng băng thông.) với những thiết bị non-Cisco. Hoạt động ở 4 mode sau :
- ON: Cho phép tạo Etherchannel mà không cần chạy LACP.
- OFF: Không cho phép tạo Etherchannel.
- ACTIVE: chủ động gửi LACP message để tạo Etherchannel.
- PASSIVE: Chỉ lắng nghe LACP message mà không gửi ra LACP message.

Các chế độ hoạt động tương ứng để tạo được Etherchannel: on-on , active-active , active-passive .

Đối với LACP cho phép chúng ta nhóm nhiều link lại thành 1 bundle nhưng cũng cho phép chúng ta chỉ sử dụng một số link trong bundle đó mà thôi. Các link còn lại trong bundle sẽ ở trạng thái stanby, sẽ up lên khi các link đang active bị down .

##1.6 Mode=5 (balance-tlb)
Adaptive transmit load balancing: Các lưu lượng gửi đi được phân phối theo tải trọng hiện tại (tính tương đối so với tốc độ) trên mỗi slave. Lưu lượng đến đến được nhận bởi các slave hiện hành. Nếu một slave tiếp nhận thất bại, slave khác sẽ tiếp quản các địa chỉ MAC của các slave thất bại.

Yêu cầu:
  - Hỗ trợ ethtool trong các trình điều khiển cơ sở để lấy tốc độ của mỗi slave.


##1.7 Mode=6 (balance-alb)
Adaptive load balancing: Là sự kết hợp giữa balance-tlb và receive load balancing(rlb) cho lưu lượng của ipv4. Việc cân bằng tải nhận được đạt được bằng thương lượng ARP. The bonding driver chặn ARP Trả lời được gửi bởi các máy chủ trên đường ra và ghi đè địa chỉ HW SRC với địa chỉ HW của một trong những người slave như vậy mà các khách hàng khác nhau sử dụng các địa chỉ hw khác nhau cho các máy chủ.


#2. LAB cấu hình Bonding theo mode 2 (active-backup)
##2.1 Mô hình
![](http://i.imgur.com/ReJmZM4.png)

##2.2 Cài đặt
###2.2.1 Cài gói ifenslave để attach và detach các NIC slave vào đường bond:
```sh
apt-get install ifenslave
```
###2.2.2 Nạp module bonding vào kernel:
```sh
echo bonding >> /etc/modules
modprobe bonding
```
###2.2.3 Cấu hình bonding network theo mode 2.
- Cấu hình interface eth0
```sh
auto eth0
iface eth0 inet manual
  bond-master bond0
  bond-primary eth0
```

- Cấu hình interface eth1
```sh
auto eth1
iface eth1 inet manual
  bond-master bond0
```

- Cấu hình interface bond0
```sh
auto bond0
iface bond0 inet dhcp
  mtu 1500 #Kich thuoc MTU frame
  bond-miimon 100 # Specifies the MII link monitoring frequency in milliseconds. This determines how often the link state of each slave is inspected for link failures.
  bond-downdelay 200 # Specifies the time, in milliseconds, to wait before disabling a slave after a link failure has been detected.
  bond-updelay 200 # Specifies the time, in milliseconds, to wait before enabling a slave after a link recovery has been detected.
  bond-mode active-backup #Che do 2, active-backup
  bond-slaves none # we already defined the interfaces above with bond-master
```

- Khởi động lại các card mạng
```sh
ifdown -a && ifup -a
```

- Kiểm tra lại cấu hình bonding: `cat /proc/net/bonding/bond0`
```sh
Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)

Bonding Mode: fault-tolerance (active-backup)
Primary Slave: eth0 (primary_reselect always)
Currently Active Slave: eth0
MII Status: up
MII Polling Interval (ms): 0
Up Delay (ms): 0
Down Delay (ms): 0

Slave Interface: eth0
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 00:0c:29:e7:54:66
Slave queue ID: 0

Slave Interface: eth1
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 00:0c:29:e7:54:70
Slave queue ID: 0
```

- Thử down card eth0 và check log để xem kết quả.
```sh
ifdown eth0
```

```sh
root@adk:/var/log# tail -f syslog
Jul 12 14:57:39 adk kernel: [ 1998.086184] bond0: Adding slave eth0
Jul 12 14:57:39 adk kernel: [ 1998.090458] e1000: eth0 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: None
Jul 12 14:57:39 adk kernel: [ 1998.092869] bond0: making interface eth0 the new active one
Jul 12 14:57:39 adk kernel: [ 1998.098382] bond0: Enslaving eth0 as an active interface with an up link
Jul 12 14:57:39 adk kernel: [ 1998.101007] bond0: Setting eth0 as primary slave
Jul 12 14:57:59 adk ntpdate[3311]: Can't find host ntp.ubuntu.com: Name or service not known (-2)
Jul 12 14:57:59 adk ntpdate[3311]: no servers can be used, exiting
Jul 12 14:59:25 adk dhclient: DHCPREQUEST of 10.10.10.7 on bond0 to 10.10.10.254 port 67 (xid=0x5dbfe8b2)
Jul 12 14:59:25 adk dhclient: DHCPACK of 10.10.10.7 from 10.10.10.254
Jul 12 14:59:25 adk dhclient: bound to 10.10.10.7 -- renewal in 811 seconds.
Jul 12 14:59:56 adk kernel: [ 2134.472022] bond0: Removing slave eth0
Jul 12 14:59:56 adk kernel: [ 2134.472561] bond0: Releasing active interface eth0
Jul 12 14:59:56 adk kernel: [ 2134.472804] bond0: making interface eth1 the new active one
```

**Chú ý các phần tô màu đỏ.**

![](http://image.prntscr.com/image/0cc52fa5c4f642d9a0e08702e6d2fb89.png)


Nhìn log ta thấy khi card eth0 down, thì card bond0 lập tức remove card eth0 và chuyển card eth1 từ trạng thái `standby` sang `active`


#Tài liệu tham khảo
https://www.kernel.org/doc/Documentation/networking/bonding.txt


#3. LAB Linux Bridge kết hợp Bonding
##3.1 Mô hình
![](http://i.imgur.com/c9si160.png)


=> **Mục đích: Khi một trong 2 đường mạng eth0 hoặc eth1 bị down, thì máy ảo của khách hàng vẫn có thể kết nối với mạng.**
##3.2 Tạo bond interfaces tên là bond0 kết hợp hai interfaces eth0 và eth1:
```sh
ifenslave bond0 eth0
ifenslave bond0 eth1
```

**=> Bước này thực chất là bước cấu hình `bond-master bond0` trong file `/etc/network/interfaces`**

##3.3 Tạo switch ảo br0 và gán bond0 interface vào switch đó:
```sh
brctl addbr br0
brctl addif br0 bond0
```

- Gán hai con ubuntu vào switch br0

![](http://image.prntscr.com/image/3ff0fdb257b24e76aef0d9735d6a6fd8.png)

![](http://image.prntscr.com/image/e70ec59b42294203a7983051dea18ba6.png)

- Kiểm tra lại cấu hình: `brctl show`
```sh
root@adk:~# brctl show
bridge name	bridge id		STP enabled	interfaces
br0		8000.000c297c7fef	no		bond0
							                vnet0
							                vnet1
```

##3.4 Cấu hình này trong file `/etc/network/interfaces`
```sh
###############
auto eth0
iface eth0 inet manual
bond-master bond0
bond-primary eth0
################
auto eth1
iface eth1 inet manual
bond-master bond0
################
auto bond0
iface bond0 inet manual
bond-slaves none
bond-mode active-backup
bond-miimon 100
bond-downdelay 200
bond-updelay 200
##############
auto br0
iface br0 inet static
address 10.10.10.195
netmask 255.255.255.0
bridge_ports bond0
bridge_fd 9
bridge_hello 2
bridge_maxage 12
bridge_stp off
```

- Khởi động các card mạng:
```sh
ifdown -a && ifup -a
```


- Kiểm tra cấu hình bonding: `/proc/net/bonding/bond0`
```sh
root@adk:~# cat /proc/net/bonding/bond0
Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)

Bonding Mode: fault-tolerance (active-backup)
Primary Slave: eth0 (primary_reselect always)
Currently Active Slave: eth0
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 200
Down Delay (ms): 200

Slave Interface: eth1
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 00:0c:29:7c:7f:f9
Slave queue ID: 0

Slave Interface: eth0
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 00:0c:29:7c:7f:ef
Slave queue ID: 0
```

4. Tham khảo
