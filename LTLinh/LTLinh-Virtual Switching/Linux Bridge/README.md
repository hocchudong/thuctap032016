#Linux Bridge
#Mục lục
#1. Khái niệm - Chức năng.
- Bridge là một cách để kết nối hai đoạn Ethernet với nhau một cách độc lập các giao thức. Các gói tin được chuyển tiếp dựa trên địa chỉ Ethernet (MAC Address), chứ không phải là địa chỉ IP.Khi bạn nối hai mạng Ethernet, hai mạng trở thành một mạng Ethernetđơn (lớn hơn).
- Linux bridge là một phần mềm đươc tích hợp vào trong nhân Linux để giải quyết vấn đề ảo hóa phần network trong các máy vật lý.
- Linux bridge sẽ tạo ra các switch layer 2 kết nối các máy ảo (VM) để các VM đó giao tiếp được với nhau và có thể kết nối được ra mạng ngoài.
- `bridge-utils`: Gói bridge-utils chứa một tiện ích cần thiết để tạo và quản lý các thiết bị bridge. Điều này rất hữu ích trong việc thiết lập hệ thống mạng cho một máy ảo được lưu trữ.
- Linux bridge thường sử dụng kết hợp với hệ thống ảo hóa KVM-QEMU.
#2. Kiến trúc.
![](http://image.prntscr.com/image/f2e8a840f7e547e298649f3d9c22377b.png)

##2.1 Linux Bridge với KVM
![](http://i.imgur.com/t15QQny.png)

- `Bridge`: tương đương với switch layer 2
- `Port`: tương đương với port của switch thật
- `Tap (tap interface)`: có thể hiểu là giao diện mạng để các VM kết nối với bridge cho linux bridge tạo ra
- `fd (forward data)`: chuyển tiếp dữ liệu từ máy ảo tới bridge

#3. Các tính năng
- STP: Spanning Tree Protocol - giao thức chống lặp gói tin trong mạng
- VLAN: chia switch (do linux bridge tạo ra) thành các mạng LAN ảo, cô lập traffic giữa các VM trên các VLAN khác nhau của cùng một switch.
- FDB (forwarding database): chuyển tiếp các gói tin theo database để nâng cao hiệu năng switch. Database lưu các địa chỉ MAC mà nó học được. Khi gói tin Ethernet đến, bridge sẽ tìm kiếm trong database có chứa MAC address không. Nếu không, nó sẽ gửi gói tin đến tất cả các cổng.

#4. So sánh với các giải pháp khác.

#5. LAB.
- note: Đường dẫn cấu hình card mạng trong kvm. `/var/lib/libvirt/network`

##5.0 Mô hình.
![](http://i.imgur.com/aq6uBqO.png))

- Máy host cài ubuntu 14.04, có một card mạng (eth2)
- Cấu hình 2 VLAN subinterfaces 101 và 102 trên card mạng (eth2) của máy host
- Cấu hình 2 switch (do linux bridge tạo ra) và gán 2 VLAN subinterfaces ở trên tương ứng vào 2 bridge này
- Cài đặt một số VM và gắn card mạng của các VM này vào các tap interfaces của 2 switch ảo trên để kiểm tra kết nối


##5.1 Cài các gói phần mềm cần thiết
Cài đặt các gói sau để hỗ trợ vlan
```sh
apt-get install vlan
```

##5.2 Nạp module 8021q vào kernel:
```sh
echo 8021q >> /etc/modules
modprobe 8021q
```

##5.3 Cấu hình VLAN

- Cấu hình 2 VLAN subinterfaces trên card eth2 và up 2 interfaces này lên:
```sh
vconfig add eth2 101
vconfig add eth2 102
ifconfig eth2.101 up
ifconfig eth2.102 up
```

- Kết quả khi tạo thành công
```sh
Added VLAN with VID == 101 to IF -:eth2:-
Added VLAN with VID == 102 to IF -:eth2:-
```

- Kiểm tra: `cat /proc/net/vlan/config`
```sh
VLAN Dev name    | VLAN ID
Name-Type: VLAN_NAME_TYPE_RAW_PLUS_VID_NO_PAD
eth2.101       | 101  | eth2
eth2.102       | 102  | eth2
```

- Tạo hai switch ảo và gán 2 VLAN subinterfaces trên vào hai switch tương ứng này:
```sh
brctl addbr br-vl101
brctl addbr br-vl102
brctl addif br-vl101 eth2.101
brctl addif br-vl102 eth2.102
```

- Kiểm tra việc gán interfaces đã thành công chưa sử dụng lệnh:`brctl show`
```sh
bridge name bridge id       STP enabled interfaces
br-vl101    8000.000c29586f38   yes         eth2.101
br-vl102    8000.000c29586f38   yes         eth2.102
br0      8000.000c29586f24  yes         eth0
lxcbr0    8000.000000000000 no
```

- Lưu giữ lại cấu hình này để tránh bị mất khi khởi động lại bằng cách chỉnh sửa trong file `/etc/network/interfaces:`
```sh
# config vlan 101
auto eth2.101
iface eth2.101 inet manual
vlan-raw-device eth2

auto br-vl101
iface br-vl101 inet static
address 10.10.10.141/24
bridge_ports eth2.101
bridge_stp on
bridge_fd 9
bridge_maxwait 0
up /sbin/ifconfig $IFACE up || /bin/true

# config vlan 102
auto eth2.102
iface eth2.102 inet manual
vlan-raw-device eth2

auto br-vl102
iface br-vl102 inet static
address 10.10.10.152/24
bridge_ports eth2.102
bridge_stp on
bridge_fd 9
bridge_maxwait 0
up /sbin/ifconfig $IFACE up || /bin/true
```

- Khởi động lại các interfaces để áp dụng thay đổi:
```sh
ifdown -a && ifup -a
```

##5.4 Cấu hình mỗi máy thuộc 1 dải vlan khác nhau.
![](http://image.prntscr.com/image/4968ad9fe2904a098e98d5804ee34063.png)

![](http://image.prntscr.com/image/9c94cb54b1f04a9eae09b3c5f8175222.png)


##5.5 Kết quả

![](http://image.prntscr.com/image/10bc671578984dcd9702a5aeca48b987.png)

#Tài liệu tham khảo.
https://wiki.debian.org/BridgeNetworkConnections

https://github.com/thaihust/Thuc-tap-thang-03-2016/blob/master/ThaiPH/Linux-bridge/ThaiPH_linux_bridge_VLAN.md
