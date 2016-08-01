#OpenVSwitch
#Mục Lục
**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [1. Giới thiệu](#gioithieu)
- [2. Kiến trúc - các thành phần.](#kientruc)
- [3. Các chức năng mà OpenVSwitch hỗ trợ](#tinhnang)
- [4. LAB cấu hình GRE Tunnels.](#lab)
- [Tài liệu tham khảo.](#thamkhao)

<a name="gioithieu"></a>
#1. Giới thiệu
![](http://networkstatic.net/wp-content/uploads/2012/06/open-vswitch-lab.png)


Cũng giống như Linux Bridge, OpenVSwitch là phần mềm cung cấp các giải pháp ảo hóa network.

- Là phần mềm mã nguồn mở, sử dụng cho ảo hóa vswitch trong môi trường ảo hóa của server.
- vswitch có thể forwards traffic giữa các máy VM trên cùng một máy chủ vật lý và forwards traffic giữa các máy VM và máy vật lý.
- OpenVSwitch được thiết kế tương thích với các switch hiện đại.
- OpenVSwitch có thể chạy trên các Linux-based virtualization platform (KVM,VirtualBox, Xen, Xen Cloud Platform, XenServer).
- OpenVSwitch có thể chạy trên các nền tảng Linux, FreeBSD, Windows, non-POSIX embedded Systems,...

<a name="kientruc"></a>
#2. Kiến trúc - các thành phần.

![](https://camo.githubusercontent.com/c700cb8cb0eb3b651bb66ebe69d39365384258e9/687474703a2f2f686162726173746f726167652e6f72672f67657470726f2f686162722f706f73745f696d616765732f3336652f3064342f6137352f33366530643461373530626332313230336433316437316466383566303839312e6a7067)

- ovs-vswitchd, a daemon that implements the switch, along with a companion Linux kernel module for flow-based switching.
- ovsdb-server, a lightweight database server that ovs-vswitchd queries to obtain its configuration.
- ovs-dpctl, a tool for configuring the switch kernel module.
- ovs-vsctl, a utility for querying and updating the configuration of ovs-vswitchd.
- ovs-appctl, a utility that sends commands to running Open vSwitch daemons.


<a name="tinhnang"></a>
#3. Các chức năng mà OpenVSwitch hỗ trợ

![](http://openvswitch.org/assets/featured-image.jpg)

- Visibility into inter-VM communication via NetFlow, sFlow(R), IPFIX, SPAN, RSPAN, and GRE-tunneled mirrors
- LACP (IEEE 802.1AX-2008)
- Standard 802.1Q VLAN model with trunking
- BFD and 802.1ag link monitoring
- STP (IEEE 802.1D-1998)
- Fine-grained QoS control
- Support for HFSC qdisc
- Per VM interface traffic policing
- NIC bonding with source-MAC load balancing, active backup, and L4 hashing
- OpenFlow protocol support (including many extensions for virtualization)
- IPv6 support
- Multiple tunneling protocols (GRE, VXLAN, IPsec, GRE and VXLAN over IPsec)
- Remote configuration protocol with C and Python bindings
- Kernel and user-space forwarding engine options
- Multi-table forwarding pipeline with flow-caching engine
- Forwarding layer abstraction to ease porting to new software and hardware platforms

<a name="lab"></a>
#4. LAB cấu hình GRE Tunnels.
##4.1 Mô hình
![](http://i.imgur.com/eFh29bb.jpg)

**Mục đích: Hai máy ảo trên hai máy chủ vật lý khác nhau có thể nói chuyện được với nhau.**

##4.2 Cấu hình

- Trên Physical server 1
```sh
sudo ovs-vsctl add-br br1
sudo ovs-vsctl add-br br2
sudo ovs-vsctl add-port br1 eth1
sudo ifconfig br1 10.10.10.129 netmask 255.255.255.0
sudo ifconfig br2 192.168.200.1 netmask 255.255.255.0
sudo ovs-vsctl add-port br2 gre0 -- set interface gre0 type=gre options:remote_ip=10.10.10.150
```

- Trên Physical server 2
```sh
sudo ovs-vsctl add-br br1
sudo ovs-vsctl add-br br2
sudo ovs-vsctl add-port br1 eth1
sudo ifconfig br1 10.10.10.150 netmask 255.255.255.0
sudo ifconfig br2 192.168.200.2 netmask 255.255.255.0
sudo ovs-vsctl add-port br2 gre0 -- set interface gre0 type=gre options:remote_ip=10.10.10.129
```

- Gán máy ảo vào card mạng br2
![](http://image.prntscr.com/image/b7af36df1f7942f89ce60a67cc66239c.png)

![](http://image.prntscr.com/image/5622e5b0c5ab4400bcc41c39c68cce5e.png)

- Kết quả

![](http://image.prntscr.com/image/8ca4921e7b98434ab6b88d9e3f9d8661.png)

<a name="thamkhao"></a>
#Tài liệu tham khảo.
- [1] http://openvswitch.org/support/dist-docs-2.5/FAQ.md.html
- [2] http://www.slideshare.net/teyenliu/the-basic-introduction-of-open-vswitch?from_action=save
- [3] http://blog.scottlowe.org/2013/05/07/using-gre-tunnels-with-open-vswitch/
