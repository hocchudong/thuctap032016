## MỤC LỤC
[I. Cài đặt DHCP](#I)
- [1. Thiết lập mô hình test DHCP](#I.1)
- [2. Thiết lập cấu hình DHCP cho server](#I.2)  
- [3. Thiết lập mô hình DHCP Relay Server](#I.3)

[II. Thiết lập LAB thử nghiệm bắt gói tin DHCP](#II)
[III. Tìm hiểu TCP Dump](#III)

<a name="I"></a>
### I. Cài đặt DHCP

<a name="I.1"></a>
#### 1. Thiết lập mô hình test DHCP:
- Tạo 2 máy ảo: 1 máy DHCP Server và 1 máy client để test
- Máy DHCP Server có 1 card mạng NAT và 1 card mạng ảo, card mạng ảo Disable chế độ tự động cấp IP DHCP, card mạng NAT để bình thường.
- Máy client có 3 card mạng, 1 card mạng NAT, 1 card mạng ảo bên trên của máy DHCP Server, và 1 cạng mạng ảo khác

<a name="I.2"></a>
#### 2. Thiết lập cấu hình DHCP cho server
##### a. Cấu hình IP bất kì (Máy client được chọn IP)
- cài đặt DHCP với quyền root

```
sudo apt-get install isc-dhcp-server
```

- Trên ubuntu, file config của DHCP nằm tại 

```
/etc/dhcp/dhcpd.conf
```
Trước hết, Cần assign Interface, đó là card mạng chung ở phần 1 bên trên của máy DHCP server lẫn Client 

```
sudo nano /etc/default/isc-dhcp-server
```

Mục interface nhập interface card mạng muốn thiết lập DHCP Server

```
# On what interfaces should the DHCP server (dhcpd) serve DHCP requests?
# Separate multiple interfaces with spaces, e.g. "eth0 eth1".
INTERFACES="eth1"

```
Sau đó vào sửa tệp tin config cấu hình cấp DHCP

```
sudo nano /etc/dhcp/dhcpd.conf
```
Config cấu hình DHCP Server, với subnet và netmask tương ứng với card chung VMware

```
subnet 192.168.25.0 netmask 255.255.255.0 {
  range 192.168.25.10 192.168.25.30;
  option domain-name-servers ns1.internal.example.org;
  option domain-name "internal.example.org";
  option routers 192.168.25.1;
  option broadcast-address 192.168.25.40;
  default-lease-time 600;
  max-lease-time 7200;
}

```

Restart lại Service DHCP Server 

```
root@ubuntu:/# service isc-dhcp-server restart
stop: Unknown instance:
isc-dhcp-server start/running, process 1570
```
Tắt chế độ tự cấp DHCP trong card ảo của VMware
<img src="http://i.imgur.com/hHd6AI5.png">

Bật máy client lên và test

```
eth2      Link encap:Ethernet  HWaddr 00:0c:29:57:a7:d0
          inet addr:192.168.25.10  Bcast:192.168.25.40  Mask:255.255.255.0
          inet6 addr: fe80::20c:29ff:fe57:a7d0/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:7 errors:0 dropped:0 overruns:0 frame:0
          TX packets:13 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:986 (986.0 B)  TX bytes:1514 (1.5 KB)

```
-> ta thu được IP tương xứng với dải mạng đã khai báo
##### b. Cấu hình chính xác máy client nhận IP gì
Thêm dòng sau vào sau khai báo subnet ở phần a

```
host ubuntu {
    option host-name ubuntu;
    hardware ethernet 00:0c:29:57:a7:d0; //MAC của card mạng chung cấp DHCP
    fixed-address 192.168.25.13; //IP muốn cấp trong dải IP định sẵn ở subnet bên trên
}
```
Vậy máy client sẽ nhận IP được cấp cho nó.
<img src="http://i.imgur.com/bIr3eRq.png">

#### Shared network Decl.
- Khi bạn muốn cấp nhiều ip cho nhiều subnet mạng của bạn, mà bạn chỉ có 1 DHCP server thì bạn sẽ dùng phương pháp này.
- Tiết kiệm được chi phí nhưng hiệu năng của dhcp server sẽ kém đi.
- Tiến hành: ở Vmware clone thêm một máy nữa, ta sẽ có 2 client test dhcp
- Máy DHCP server được config 2 card, mỗi máy client sẽ được cấp 1 trong 2 card đó
- Khai báo trên file config

```
shared-network 25-50{
        subnet 192.168.25.0 netmask 255.255.255.0{
        default-lease-time 600;
        max-lease-time 7200;
        pool {
        option routers 192.168.25.1;
        range 192.168.25.10 192.168.25.20;
        }
        }

        subnet 192.168.50.0 netmask 255.255.255.0{
        default-lease-time 600;
        max-lease-time 7200;
        pool{
        option routers 192.168.50.1;
        range 192.168.50.20 192.168.50.30;
        }
        }
}

```
<a name="I.3"></a>
#### 3. Thiết lập DHCP relay server
- Chuẩn bị: 4 máy ảo, 1 máy DHCP srv, 1 máy DHCP relay srv và 2 máy client để test
- DHCP relay srv được nối với DHCP srv qua card VMnet1 và được gán IP tĩnh 10.10.10.3 (relay srv) và 10.10.10.2 (srv)
- 2 client được nối với DHCP relay server qua card VMnet2 và DHCP relay server được gán ip tĩnh 10.10.20.3
- Thực hiện config: 
    - Gán IP tĩnh cho DHCP server và DHCP relay srv
    - DHCP server cài isc-dhcp-config và config tại /etc/default/isc-dhcp-server (card) và /etc/dhcp/dhcpd.conf

    ```
    subnet 10.10.20.0 netmask 255.255.255.0 {
        option routers 10.10.20.1;
        option subnet-mask 255.255.255.0;
        option domain-name-servers 8.8.8.8;
        range 10.10.20.40 10.10.20.60;
}

    ```  
    - 

        
    


<a name="II"></a>
### II.Thiết lập LAB thử nghiệm bắt gói tin DHCP
Công cụ:  
- VMware workstation 12 với một máy ảo cài sẵn Ubuntu server 14.04
- Wireshark (Máy Host: Windows 10 Pro) Wireshark Version: 2.0.2 (v2.0.2-0-ga16e22e from master-2.0) 

Các bước: 
- Ở trong Virtual Network Editor thiết lập một card mạng ảo VD VMnet1, Để type là Host Only, Enabled DHCP lên, gán cho nó một subnet address như trong hình, Apply, OK
<img src="http://i.imgur.com/LsXbfRr.png">


- Khởi động wireshark lên rồi chọn bắt gói tin từ card mạng ảo VMnet1 vừa tạo ra
<img src="http://i.imgur.com/IirrdDI.png">

Chúng ta sẽ bắt 4 Loại bản tin cơ bản của DHCP trước : Discover, Offer, Request, ACK. để bắt được 4 loại gói tin này thì ta nhập vào khung filter của wireshark filter sau:

```
bootp
```
<img src="http://i.imgur.com/2CPvnap.png">


- Bật máy ảo Ubuntu 14.04 lên
- gõ lệnh để truy cập với quyền của sudoer

```
sudo su
```
- Khi máy ảo bật lên thì sẽ được cấp IP nằm trong dải đã được config bởi virtual Network Editor. Để demo các gói tin, ta tiến hành nhả ip bằng câu lệnh 

```
dhclient -r
```
Đây cũng chính là DHCP Release. Hủy bỏ địa chỉ IP và thời gian sử dụng còn lại

- sau đó tiến hành cấp lại IP bằng câu lệnh

```
dhclient
```

Đồng thời quay lại wireshark, ta sẽ bắt được 4 gói tin cơ bản DHCP Discover, Offer, Request, ACK
<img src="http://i.imgur.com/lKmft9A.png">

 - Discover: Khi chưa được cấp IP, client broadcast gói tin Discover(port 68) đến destination DHCP server (Port 67). IP nguồn 0.0.0.0
 <img src="http://i.imgur.com/iEJuh78.png">
 
 - Offer: DHCP Server unicast lại một gói tin gồm thông số đề nghị cấp cho DHCP Client. Hai bên vẫn giao tiếp qua cổng 67 và 68
 <img src="http://i.imgur.com/6GJ68ag.png">
 
 - Request: Xác nhận thông tin từ server. Giao tiếp qua cổng 68 (client) 67(server)
 <img src="http://i.imgur.com/NwWlSDM.png">
 
 - ACK: Xác nhận request từ client. Cấu hình IP được gửi về cho client, kết thúc quá trình cấp phát
 <img src="http://i.imgur.com/aw08wZl.png">
 
 
 <a name="III"></a>
 ### III. Tìm hiểu TCP Dump
Tcpdump là công cụ trụ cột trong việc gỡ rối và kiểm tra vấn đề kết nối mạng và bảo mật trước đây, nó đã từng là công cụ đã được các chuyên gia trên khắp thế giới tín nhiệm về sự hữu dụng. Một công cụ dòng lệnh không thực sự có nhiều các họa tiết đẹp mắt so với các công phân tích lưu lượng khác như Ettercap và Wireshark, cả hai sản phẩm này đều cung cấp các chức năng kiểm tra gói dữ liệu bằng một giao diện khá thuận tiện. Tương phản lại với các công cụ như vậy, tcpdump lại chỉ là một công cụ dòng lệnh với các tùy chọn được chỉ định tại thời điểm đó và cho ra các kết quả dưới dang đầu ra chuẩn. Điều này tạo một cảm giác khá nguyên thủy với một số người dùng và khó sử dụng đối với họ, tuy nhiên tiện ích này lại thực sự là một công cụ mạnh và linh hoạt.

Các tùy chọn

Tiện ích tcpdump cung cấp một khá nhiều các tùy chọn, ở đây chúng tôi chỉ giới thiệu cho các bạn một số trong chúng:

-A: In các gói theo mã ASCII.
-c N: Ký tự N ở đây là số, tùy chọn này thông báo cho tcpdump biết để thoát sau gói N.
-i interface: Capturre các gói trên giao diện mạng nào đó.
-n: Không giải quyết các địa chỉ cho các tên.
-q: Cung cấp đầu ra ngắn để các dòng đầu ra ngắn hơn.
-r filename: Đọc các gói từ một file cụ thể thay cho một giao diện mạng, thường được sử dụng sau khi các gói dữ liệu thô đã được ghi vào một file với tùy chọn –w.
-t: Không in tem thời gian trên mỗi dòng đầu ra.
-v: Cung cấp đầu ra dài hơn. Dài hơn nữa với -vv, vào thậm chí còn cả -vvv.
-w filename: Ghi các gói dữ liệu thô vào một file nào đó
Các biểu thức

Tiện ích tcpdump cũng hỗ trợ các biểu thức dòng lệnh, vẫn được sử dụng để định nghĩa các nguyên tắc lọc để bạn có được chính xác lưu lượng muốn xem, bỏ qua các gói không cần quan tâm đến. Các biểu thức gồm có một số các primitive (mẫu), các thuật ngữ modifier (từ bổ nghĩa) và tùy chọn. Các primitive và modifier không thiết lập một danh sách đầy đủ nhưng chúng chính là những gì hữu dụng nhất.

Primitive (mẫu)

 - dst foo: Chỉ định một địa chỉ hoặc một hostname nhằm hạn chế các gói được capture về mặt lưu lượng gửi đến một host nào đó.
 - host foo: Chỉ định một địa chỉ hoặc một hostname nhằm hạn chế các gói đã được capture về mặt lưu lượng đến và đi đối với một host nào đó.
 - net foo: Chỉ định một mạng hoặc một đoạn mạng sử dụng ghi chú CIDR để hạn chế sự capture gói.
 - proto foo: Chỉ định một giao thức nhằm hạn chế các gói đã được capturre về mặt lưu lượng mạng đang sử dụng giao thứ đó.
 - src foo: Chỉ định một địa chỉ hoặc một hostname nhằm hạn chế các gói được capture đối với lưu lượng được gửi bởi một host nào đó.
Modifiers (từ bổ nghĩa)

 - and: Sử dụng modifier này nhằm trói buộc các mẫu cùng nhau khi bạn muốn hạn chế các gói đã được capture để có được các yêu cầu cần thiết của các biểu thức trên cả hai phía của and.
 - not: Sử dụng từ bổ nghĩa này trước một mẫu khi bạn muốn hạn chế các gói đã được capturre để không có được các yêu cầu của biểu thức theo sau.
 - or: Sử dụng nhằm nhằm trói buộc các mẫu cùng nhau khi bạn muốn hạn chế các gói đã được capture để có được các yêu cầu cần thiết của một hoặc nhiều biểu thức trên phía của or.

#### 1. Bắt gói tin từ một giao diện ethernet cụ thể thông qua tcpdump -i

Khi bạn thực thi lệnh tcpdumpmà không có tùy chọn cụ thể, nó sẽ bắt tất cả các gói tin lưu thông qua card mạng. Tùy chọn -i sẽ cho phép bạn lọc một Interface (giao diện/card mạng) ethernet cụ thể.

```
$ tcpdump -i eth1
14:59:26.608728 IP xx.domain.netbcp.net.52497 > valh4.lell.net.ssh: . ack 540 win 16554
14:59:26.610602 IP resolver.lell.net.domain > valh4.lell.net.24151:  4278 1/0/0 (73)
14:59:26.611262 IP valh4.lell.net.38527 > resolver.lell.net.domain:  26364+ PTR? 244.207.104.10.in-addr.arpa. (45)
```
Trong ví dụ trên, tcpdump bắt tất cả các gói tin trong eth1 và hiển thị theo chuẩn đầu ra.  
#### 2. Chỉ bắt số lượng N gói tin thông qua lệnh tcpdump -c
Khi bạn thực thi lệnh tcpdump, nó sẽ thực hiện đến khi bạn hủy bỏ lệnh. Sử dụng tùy chọn -c bạn sẽ có thể lựa chọn cụ thể số lượng gói tin được bắt.  

```
$ tcpdump -c 2 -i eth0
listening on eth0, link-type EN10MB (Ethernet), capture size 96 bytes
14:38:38.184913 IP valh4.lell.net.ssh > yy.domain.innetbcp.net.11006: P 1457255642:1457255758(116) ack 1561463966 win 63652
14:38:38.690919 IP valh4.lell.net.ssh > yy.domain.innetbcp.net.11006: P 116:232(116) ack 1 win 63652
2 packets captured
13 packets received by filter
0 packets dropped by kernel
```
Ví dụ trên cho thấy lệnh tcpdump chỉ bắt 2 gói tin từ giao diện eth0.
#### 3. Hiển thị các gói tin được bắt trong hệ ASCII thông qua tcpdump -A

```
$ tcpdump -A -i eth0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 96 bytes
14:34:50.913995 IP valh4.lell.net.ssh > yy.domain.innetbcp.net.11006: P 1457239478:1457239594(116) ack 1561461262 win 63652
E.....@.@..]..i...9...*.V...]...P....h....E...>{..U=...g.
......G..7\+KA....A...L.
14:34:51.423640 IP valh4.lell.net.ssh > yy.domain.innetbcp.net.11006: P 116:232(116) ack 1 win 63652
E.....@.@..\..i...9...*.V..*]...P....h....7......X..!....Im.S.g.u:*..O&....^#Ba...
E..(R.@.|.....9...i.*...]...V..*P..OWp........
```

#### 4.Hiển thị các gói tin được bắt dưới dạng HEX và ASCII thông qua tcpdump -XX

```
$tcpdump -XX -i eth0
18:52:54.859697 IP zz.domain.innetbcp.net.63897 > valh4.lell.net.ssh: . ack 232 win 16511
        0x0000:  0050 569c 35a3 0019 bb1c 0c00 0800 4500  .PV.5.........E.
        0x0010:  0028 042a 4000 7906 c89c 10b5 aaf6 0f9a  .(.*@.y.........
        0x0020:  69c4 f999 0016 57db 6e08 c712 ea2e 5010  i.....W.n.....P.
        0x0030:  407f c976 0000 0000 0000 0000            @..v........
18:52:54.877713 IP 10.0.0.0 > all-systems.mcast.net: igmp query v3 [max resp time 1s]
        0x0000:  0050 569c 35a3 0000 0000 0000 0800 4600  .PV.5.........F.
        0x0010:  0024 0000 0000 0102 3ad3 0a00 0000 e000  .$......:.......
        0x0020:  0001 9404 0000 1101 ebfe 0000 0000 0300  ................
        0x0030:  0000 0000 0000 0000 0000 0000            ............
```
#### 5.Bắt gói tin và ghi vào một file thông qua tcpdump -w
tcpdump cho phép bạn lưu gói tin thành một file, và sau đó bạn có thể sử dụng với mục đích phân tích khác.

```
$ tcpdump -w 08232010.pcap -i eth0
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 96 bytes
32 packets captured
32 packets received by filter
0 packets dropped by kernel
```

Tùy chọn -w ghi các gói tin vào một file cho trước. Phần mở rộng của file nên là .pcap để có thể đọc được bởi các phần mềm phân tích giao thức mạng.

#### 6. Đọc các gói tin từ một file thông qua tcpdump -r

```
$tcpdump -tttt -r data.pcap
2010-08-22 21:35:26.571793 00:50:56:9c:69:38 (oui Unknown) > Broadcast, ethertype Unknown (0xcafe), length 74:
        0x0000:  0200 000a ffff 0000 ffff 0c00 3c00 0000  .............).....
        0x0020:  0000 0000 ffff ffff ad00 996b 0600 0050  ...........k...P
        0x0030:  569c 6938 0000 0000 8e07 0000            V.i8........
2010-08-22 21:35:26.571797 IP valh4.lell.net.ssh > zz.domain.innetbcp.net.50570: P 800464396:800464448(52) ack 203316566 win 71
2010-08-22 21:35:26.571800 IP valh4.lell.net.ssh > zz.domain.innetbcp.net.50570: P 52:168(116) ack 1 win 71
2010-08-22 21:35:26.584865 IP valh5.lell.net.ssh > 11.154.12.255.netbios-ns: NBT UDP PACKET(137): QUERY; REQUEST; BROADC
```

#### 7. Bắt các gói tin với địa chỉ IP thông qua tcpdump -n
Trong các ví dụ phía trên hiển thị gói tin với địa chỉ DNS chứ không phải địa chỉ IP/ Ví dụ dưới đây bắt các gói tin và hiển thị địa chỉ IP của thiết bị liên quan.

```
$ tcpdump -n -i eth0
15:01:35.170763 IP 10.0.19.121.52497 > 11.154.12.121.ssh: P 105:157(52) ack 18060 win 16549
15:01:35.170776 IP 11.154.12.121.ssh > 10.0.19.121.52497: P 23988:24136(148) ack 157 win 113
15:01:35.170894 IP 11.154.12.121.ssh > 10.0.19.121.52497: P 24136:24380(244) ack 157 win 113
```

#### 8. Bắt các gói tin với các dấu thời gian thông quan tcpdump -tttt

```
$ tcpdump -n -tttt -i eth0
2010-08-22 15:10:39.162830 IP 10.0.19.121.52497 > 11.154.12.121.ssh: . ack 49800 win 16390
2010-08-22 15:10:39.162833 IP 10.0.19.121.52497 > 11.154.12.121.ssh: . ack 50288 win 16660
2010-08-22 15:10:39.162867 IP 10.0.19.121.52497 > 11.154.12.121.ssh: . ack 50584 win 16586
```

#### 9. Đọc các gói tin lớn hơn N byte
Bạn có thể chỉ nhận những gói tin lớn hơn N byte thông qua một bộ lọc “greater”.

```
$ tcpdump -w g_1024.pcap greater 1024
```
#### 10.  Chỉ nhận những gói tin trong với một kiểu giao thức cụ thể.
Bạn có thể lọc các gói tin dựa vào kiểu giao thức. Bạn có thể chọn một trong những giao thức — fddi, tr, wlan, ip, ip6, arp, rarp, decnet, tcp và udp. Ví dụ dưới đây chỉ bắt các gói tin arp thông qua giao diện eth0.

```
$ tcpdump -i eth0 arp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 96 bytes
19:41:52.809642 arp who-has valh5.lell.net tell valh9.lell.net
19:41:52.863689 arp who-has 11.154.12.1 tell valh6.lell.net
19:41:53.024769 arp who-has 11.154.12.1 tell valh7.lell.net
```

#### 11. Đọc các gói tin nhỏ hơn N byte.
Bạn có thể chỉ nhận những gói tin nhỏ hơn N byte thông qua bộ lọc “less”.

```
$ tcpdump -w l_1024.pcap  less 1024
```

#### 12. Nhận các gói tin trên một cổng cụ thể thông qua tcpdump port.
Nếu bạn muốn biết tất cả gói tin nhận được trên một cổng cụ thể trên thiết bị, bạn có thể sử dụng lệnh như sau

```
$ tcpdump -i eth0 port 22
19:44:44.934459 IP valh4.lell.net.ssh > zz.domain.innetbcp.net.63897: P 18932:19096(164) ack 105 win 71
19:44:44.934533 IP valh4.lell.net.ssh > zz.domain.innetbcp.net.63897: P 19096:19260(164) ack 105 win 71
19:44:44.934612 IP valh4.lell.net.ssh > zz.domain.innetbcp.net.63897: P 19260:19424(164) ack 105 win 71
```


#### 13. Bắt các gói tin trên địa chỉ IP và cổng đích.
Các gói tin có địa chỉ IP và cổng nguồn và đích. Sử dụng tcpdump chúng ta có thể áp dụng bộ lọc trên địa chỉ IP và cổng nguồn hoặc đích. Lệnh dưới đây bắt các gói tin trong eth0 với địa chỉ đích IP và cổng 22.

```
$ tcpdump -w xpackets.pcap -i eth0 dst 10.181.140.216 and port 22
```
#### 14. Bắt các gói tin kết nối TCP giữa hai host.
Nếu hai tiến trình từ hai thiết bị kết nối thông qua giao thức TCP, chúng ta sẽ có thể bắt những gói tin thông qua lệnh dưới đây:

```
$tcpdump -w comm.pcap -i eth0 dst 16.181.170.246 and port 22
```
Bạn có thể mở file comm.pcap để debug bất cứ vấn đề tiềm tàng nào.

#### 15 Bộ lọc gói tin tcpdump – Bắt tất cả các gói tin ngoại trừ arp và rarp
Trong lệnh tcpdump bạn có thể sử dụng điều kiện “and”, “or” hoặc “not” để lọc các gói tin.

```
$ tcpdump -i eth0 not arp and not rarp
20:33:15.479278 IP resolver.lell.net.domain > valh4.lell.net.64639:  26929 1/0/0 (73)
20:33:15.479890 IP valh4.lell.net.16053 > resolver.lell.net.domain:  56556+ PTR? 255.107.154.15.in-addr.arpa. (45)
20:33:15.480197 IP valh4.lell.net.ssh > zz.domain.innetbcp.net.63897: P 540:1504(964) ack 1 win 96
20:33:15.487118 IP zz.domain.innetbcp.net.63897 > valh4.lell.net.ssh: . ack 540 win 16486
20:33:15.668599 IP 10.0.0.0 > all-systems.mcast.net: igmp query v3 [max resp time 1s]
```







