#Linux Bridge

##1. Giới thiệu Linux bridge.

###a. Architect.

- Linux bridge là một soft-switch, một trong ba công nghệ cung cấp switch ảo trong hệ thống Linux (bên cạnh macvlan và OpenvSwitch), giải quyết vấn đề ảo hóa network bên trong các máy vật lý. 
- Bản chất, linux bridge sẽ tạo ra các switch layer 2 kết nối các máy ảo (VM) để các VM đó giao tiếp được với nhau và có thể kết nối được ra mạng ngoài. Linux bridge thường sử dụng kết hợp với hệ thống ảo hóa KVM-QEMU.

###b. Components.

![1bfffc.png](http://www.upsieutoc.com/images/2016/07/14/1bfffc.png)

- Kiến trúc linux bridge minh họa như hình vẽ trên. Một số khái niệm liên quan tới linux bridge:
 <ul>
 <li>Port: tương đương với port của switch thật</li>
 <li>Bridge: tương đương với switch layer 2</li>
 <li>Tap: hay tap interface có thể hiểu là giao diện mạng để các VM kết nối với bridge cho linux bridge tạo ra</li>
 <li>FDB: chuyển tiếp các gói tin theo database để nâng cao hiệu năng switch</li>
 </ul>

##2. Lab các tính năng của Bridge.

- Để sử dụng được Linux Bridge chúng ta cần phải cài đặt `bridge-ultis` để có thể sử dụng công cụ `brctl`:

```sh
apt-get install bridge-utils
```

- Khi cài đặt gói này thành công, ta có thể sử dụng công cụ brctl để tạo và sửa các switch ảo:

![Screenshot_1.png](http://www.upsieutoc.com/images/2016/07/14/Screenshot_1.png)

- Tạo switch ảo và gắn các card mạng:

```sh
brctl addbr {bridgename} //tao bridge ao
brctl delbr {bridgename} //xoa bridge ao
brctl addif {bridgename} {device} //them card mang vao bridge
brctl delif {bridgename} {device} //go card mang khoi bridge
```
- Show cấu hình :

```sh
brctl show
brctl showmacs bridgename
```

- Để có thể sử dụng lâu dài chúng ta phải cấu hình từ bên trong interfaces. `/etc/network/interfaces`

```sh
auto bridgename
iface bridgename inet static
    address 10.10.10.10
    netmask 255.255.255.0
    gateway 10.10.10.1
    bridge_ports eth0 eth1
    bridge_maxwait 5
    bridge_fd 1
    bridge_stp on
```

**Cấu hình VLAN**

- Để sử dụng tính năng VLAN, ta cần cài đặt gói vlan để sử dụng ở mức người dùng:

```sh
apt-get install vlan
```

- Nạp module vlan vào trong nhân:

```sh
modprobe 8021q
echo "8021q" >> /etc/modules
```

- Sau khi nạp thành công module vlan, thư mục cấu hình vlan sẽ xuất hiện ở `/proc/net/vlan/config`
- Tạo các vlan:

```sh
vconfig add eth1 10 --->tạo ra VLAN có ID 10 và gán vào card mạng eth1

vconfig add eth1 20 --->tạo ra VLAN có ID 20 và gán vào card mạng eth1
```

- Xóa VLan:

```sh
vconfig rem eth1.10 --->remove VLAN 10 trên interface eth1
```

- Gắn các vlan interface vào bridge ảo:

```sh
brctl addbr bridgename
brctl addif bridgename eth1.10
brctl addif bridgename eth1.20
```

- Để sử dụng lâu dài cấu hình này, cần khai báo trong `/etc/network/interfaces`

```sh
auto eth1.10
iface eth1.10 inet static
    address 10.10.10.10
    netmask 255.255.255.0
    vlan-raw-device eth1

auto eth1.20
iface eth1.20 inet static
    address 10.10.10.2
    netmask 255.255.255.0
    vlan-raw-device eth1

auto bridgename
iface bridgename inet static
    bridge_ports eth1.10 eth1.20
    bridge_maxwait 5
    bridge_fd 1
    bridge_stp on 
```

**Bonding**

- Để sử dụng tính năng bonding, cần cài đặt gói ifenslave và nạp module bonding vào nhân:

```sh
modprobe bonding
echo bonding >> etc/modules
```

- Sau khi nạp thành công module vào nhân, thư mục cấu hình bonding sẽ xuất hiện ở `/proc/net/bonding`

#####Các tùy chọn bonding
- bond-mode: Linux bridge hỗ trợ các mode bonding sau:
 <ul> 
 <li>mode 1: actice-backup</li>
 <li>mode 2: balance-xor</li>
 <li>mode 3: broadcast</li>
 <li>mode 4: 802.3ad - Là chuẩn cho việc triển khai LACP</li>
 <li>mode 5: balance-tlb</li>
 <li>mode 6: balance-alb</li>
 </ul>
 
- bond-slave: danh sách các interface được bond
- bond-miimon: thời gian kiểm tra downlink
- bond-use-carrier: cách xác định trạng thái đường link
- bond-xmit-hash-policy: thuật toán xác định link sẽ dùng khi truyền thông
- bond-min-links: số đương link tối thiểu cần trong trạng thái active

- Sau khi bond, các inteface slave sẽ có chung MAC của bond interface. Thông thường, interface nào được add vào bond đầu tiên sẽ có MAC được dùng làm MAC cho bond interface.
- Tạo bond interface:

```sh
ifenslave bond0 eth1
ifenslave bond0 eth2
```

- Gán bond interface vào bridge:

```sh
brctl addif bridgename bond0
```

- Để lưu lại cấu hình này, cần khai báo trong file `/etc/network/interfaces`:

```sh
auto eth0
iface eth0 inet manual
bond-master bond0

auto eth1
iface eth1 inet manual
bond-master bond0

auto bond0
iface bond0 inet manual
  bond-slaves none
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1

auto bridgename
iface bridgename inet static
  bridge_ports bond0
  address 172.22.0.6
  netmask 255.255.240.0
  gateway 172.22.0.1
  bridge_fd 0
  bridge_hello 2
  bridge_maxage 12
  bridge_stp off
```

- Kiểm tra lại cấu hình:

```sh
sudo brctl show
```

###Nguồn:

- https://github.com/thaihust/Thuc-tap-thang-03-2016/blob/master/ThaiPH/Linux-bridge/ThaiPH_tim_hieu_linux_bridge.md
- https://github.com/dthanh142/Linux-bridge/blob/master/Linux-bridge.md
- http://www.innervoice.in/blogs/2013/12/02/linux-bridge-virtual-networking/
- https://github.com/hocchudong/Linux-bridge