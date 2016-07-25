# Linux Network Namespaces
# Mục lục 
<h3><a href="#concept">1. Khái niệm Linux Network Namespaces</a></h3>
<h3><a href="#labs">2. Lab thử nghiệm tính năng Linux Network Namespaces</a></h3>
<ul>
    <li><a href="#simple">2.1. Kết nối hai host trên 2 namespaces sử dụng OpenvSwitch</a></li>
    <li><a href="#complex">2.2. Lab DHCP cấp IP cho các host thuộc các namespaces khác nhau</a></li>
</ul>
<h3><a href="#ref">3. Tham khảo</a></h3>
---

<h2><a name="concept">1. Khái niệm Linux Network Namespaces</a></h2>
<div>
    Thông thường, một bản cài đặt Linux sẽ chia sẻ chung tập hợp các network interfaces và các bản ghi trên bảng định tuyến. Ta có thể chỉnh sửa bảng định tuyến sử dụng các chính sách định tuyến, tuy nhiên về căn bản thì điều đó không thay đổi thực tế là các network interfaces và các bảng định tuyến vẫn chia sẻ chung khi xét trên toàn bộ hệ điều hành. 
    <br>
    Linux network namespaces được đưa ra để giải quyết vấn đề đó. Với linux namespaces, ta có thể có các máy ảo tách biệt nhau về network interfaces cũng như bảng định tuyến khi mà các máy ảo này vận hành trên các namespaces khác nhau. Mỗi network namespaces có bản định tuyến riêng, các thiết lập iptables riêng cung cấp cơ chế NAT và lọc đối với các máy ảo thuộc namespace đó. Linux network namespaces cũng cung cấp thêm khả năng để chạy các tiến trình riêng biệt trong nội bộ mỗi namespace.
</div>
<h2><a name="labs">2. Lab thử nghiệm tính năng Linux Network Namespaces</a></h2>
<i><b>Chú ý: </b>Cả hai bài lab đều thực hiện trên Ubuntu 14.04 có cài sẵn OpenvSwitch.</i>
<ul>
    <li><h3><a name="simple">2.1. Kết nối hai host trên 2 namespaces sử dụng OpenvSwitch</a></h3>
    <ul>
        <li><b>a. Topology</b>
        <br>
        Kết nối 2 interfaces trên 2 namespace thông qua OpenvSwitch. Tạo 2 network namespaces:
        <ul>
            <li>RED Namespace: kết nối với OpenvSwitch thông qua virtual pair interface <b>eth0-r - veth-r</b>.</li>
            <li>GREEN Namespace: kết nối với OpenvSwitch thông qua virtual pair interface <b>eth0-g - veth-g</b>.</li>
        </ul>
        Thiết lập địa chỉ IP dải 10.0.0.0/24 cho hai interfaces <b>eth0-r</b> và <b>eth0-g</b> rồi tiến hành ping giữa hai interfaces này kiểm tra kết nối.
            <br><br>
            <img src="http://i.imgur.com/PKUVWtm.png">
            <br><br>
        </li>
        <li><b>b. Cấu hình</b>
        <ul>
            <li>
            Tạo switch ảo
                <pre>
                    <code>
ovs-vsctl add-br ovs
                    </code>
                </pre>
            </li>            
            <li>
            Tạo 2 network namespaces
                <pre>
                    <code>
ip netns add red
ip netns add green
                    </code>
                </pre>
            </li>  
                    
            <li>
            Tạo cặp interface ảo <code>eth0-r - veth-r</code> kết nối giữa RED namespace và switch ảo. (Gán eth0-r vào RED namespace, gán port veth-r vào switch <b>ovs</b>)  
                <pre>
                    <code>
ip link add eth0-r type veth peer name veth-r
ip link set eth0-r netns red
ovs-vsctl add-port ovs veth-r
                    </code>
                </pre>
            </li>
                     
            <li>
            Tạo cặp interface ảo <code>eth0-g - veth-g</code> kết nối giữa GREEN namespace và switch ảo. (Gán eth0-g vào GREEN namespace, gán port veth-g vào switch <b>ovs</b>) 
                <pre>
                    <code>
ip link add eth0-g type veth peer name veth-g
ip link set eth0-g netns green
ovs-vsctl add-port ovs veth-g
                    </code>
                </pre>
            </li>

            <li>
            Kiểm tra cấu hình các interface trên switch ảo
<pre>
    <code>
ovs-vsctl show
# ket qua tuong tu nhu sau
535fabc5-dd02-4d18-a5d9-11ad46d47dec
    Bridge ovs
        Port ovs
            Interface ovs
                type: internal
        Port veth-r
            Interface veth-r
        Port veth-g
            Interface veth-g
    ovs_version: "2.0.2"
    </code>
</pre>
            </li>

            <li>
            Mặc định mỗi namespace tạo ra chỉ có một interface loopback và interface này ở trạng thái down. Tiến hành up interface loopback và interface eth0-r trong RED namespace lên. Sau đó gán IP tĩnh cho interface eth0-r.
<pre>
    <code>
ip link set veth-r up
ip netns exec red ip link set dev lo up
ip netns exec red ip link set dev eth0-r up
ip netns exec red ip address add 10.0.0.1/24 dev eth0-r # thiet lap IP tinh cho eth0-r
    </code>
</pre>

            Kiểm tra địa chỉ IP các interface và bảng định tuyến của red namespace sẽ tương tự như sau:
<pre>
    <code>
# kiem tra dia chi cac interface trong red namespace
ip netns exec red ip a 
# ket qua
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
11: eth0-r: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether c2:bc:ef:12:b3:13 brd ff:ff:ff:ff:ff:ff
    inet 10.0.0.1/24 scope global eth0-r
       valid_lft forever preferred_lft forever
    inet6 fe80::c0bc:efff:fe12:b313/64 scope link tentative
       valid_lft forever preferred_lft forever

# kiem tra bang dinh tuyen cua red namespace
ip netns exec red ip route    
# ket qua
10.0.0.0/24 dev eth0-r  proto kernel  scope link  src 10.0.0.1     
    </code>
</pre>            
            </li>

            <li>
            Tiến hành up interface loopback và interface eth0-g trong GREEN namespace lên. Sau đó gán IP tĩnh cho interface eth0-g.
<pre>
    <code>
ip link set veth-g up
ip netns exec green bash # truy cap vao green namespace de thuc hien kiem tra cac interface
ip link set dev lo up
ip link set dev eth0-g up
ip address add 10.0.0.2/24 dev eth0-g        
    </code>
</pre>
            Kiểm tra địa chỉ IP các interface và bảng định tuyến của green namespace sẽ tương tự như sau:
<pre>
    <code>
# kiem tra dia chi cac interface trong green namespace
ip netns exec green ip a
# ket qua
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
13: eth0-g: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 7e:55:3d:4d:b0:2b brd ff:ff:ff:ff:ff:ff
    inet 10.0.0.2/24 scope global eth0-g
       valid_lft forever preferred_lft forever
    inet6 fe80::7c55:3dff:fe4d:b02b/64 scope link
       valid_lft forever preferred_lft forever

# kiem tra bang dinh tuyen cua green namespace
ip netns exec green ip route
# ket qua
10.0.0.0/24 dev eth0-g  proto kernel  scope link  src 10.0.0.2
    </code>
</pre>
            Tiến hành ping thử sang địa chỉ của interface eth0-r (10.0.0.1)
<pre>
    <code>
ping 10.0.0.1
# ket qua
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=1.00 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.149 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.145 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.121 ms
    </code>
</pre>
            </li>

        </ul>
        </li>
    </ul>
    </li>
    <li><h3><a name="complex">2.2. Lab DHCP cấp IP cho các host thuộc các namespaces khác nhau</a></h3>
    <li><b>a. Topology</b>
    <br>
    Topology sau đây lấy ý tưởng từ hệ thống OpenStack. Trên mỗi máy Compute, các máy ảo thuộc về mỗi vlan đại diện cho các máy của một tenant. Chúng tách biệt về layer 2 và được cấp phát IP bởi các DHCP server ảo cùng VLAN (các DHCP server ảo này thuộc về các namespaces khác nhau và không cùng namespace với các máy ảo của các tenant, được cung cấp bởi dịch vụ dnsmasq). Các DHCP server này hoàn toàn có thể cấp dải địa chỉ trùng nhau do tính chất của namespace. Sau đây mà mô hình:
    <br><br>
    <img src="http://i.imgur.com/fbnJ94q.png">
    <br><br>
    Mô hình bài lab bao gồm 2 DHCP namespace (dhcp-r, dhcp-g) và hai namespaces dành cho các máy ảo của 2 tenant (red, green), các máy ảo trên 2 tenant này thuộc về hai vlan khác nhau (vlan 100 và vlan 200). DHCP server trên các namespace dhcp-r, dhcp-g sẽ cấp địa chỉ IP cho các máy ảo của 2 tenant trên 2 namespace tương ứng là red và green. 
    </li>

    <li><b>b. Cấu hình</b><br>
Trước hết cấu hình theo các bước của bài lab trên. Sau đó tiến hành xóa cấu hình địa chỉ IP của 2 interfaces <b>eth0-r</b> và <b>eth0-g</b>. Gán 2 interfaces <b>veth-r</b> và <b>veth-g</b> vào 2 VLAN tương ứng là 100 và 200.
<pre>
    <code>
ovs-vsctl set port veth-r tag=100
ovs-vsctl set port veth-g tag=200
ip netns exec red ip address del 10.0.0.1/24 dev eth0-r
ip netns exec green ip address del 10.0.0.2/24 dev eth0-g
    </code>
</pre>
Tạo 2 namespace cho 2 DHCP server:
<pre>
    <code>
ip netns add dhcp-r
ip netns add dhcp-g
    </code>
</pre>
    </li>
Trên switch ảo <b>ovs</b> tạo 2 internal interface là <b>tap-r</b> và <b>tap-g</b> để kết nối với 2 namespaces tương ứng là dhcp-r và dhcp-g. Chú ý gán tap-r vào vlan 100, tap-g vào vlan 200.
<pre>
    <code>
# cau hinh tap-r
ovs-vsctl add-port ovs tap-r
ovs-vsctl set interface tap-r type=internal
ovs-vsctl set port tap-r tag=100
# cau hinh tap-g
ovs-vsctl add-port ovs tap-g
ovs-vsctl set interface tap-g type=internal
ovs-vsctl set port tap-g tag=200
    </code>
</pre>
Kiểm tra cấu hình các interfaces của switch <b>ovs</b>. Kết quả tương tự như sau:
<pre>
    <code>
ovs-vsctl show
# result
535fabc5-dd02-4d18-a5d9-11ad46d47dec
    Bridge ovs
        Port ovs
            Interface ovs
                type: internal
        Port tap-r
            tag: 100
            Interface tap-r
                type: internal
        Port veth-r
            tag: 100
            Interface veth-r
        Port veth-g
            tag: 200
            Interface veth-g
        Port tap-g
            tag: 200
            Interface tap-g
                type: internal
    ovs_version: "2.0.2"
    </code>
</pre>
Gán 2 internal interface <b>tap-r</b> và <b>tap-g</b> trên lần lượt vào các namespace <b>dhcp-r</b> và <b>dhcp-g</b>. Chú ý là thực hiện hai thao tác này trên bash của root namespace. Nếu đang thao tác trong các namespace <b>red</b> và <b>green</b> thì phải thoát ra bằng lệnh <code>exit</code> cho tới khi trở về root namespace.
<pre>
    <code>
ip link set tap-r netns dhcp-r
ip link set tap-g netns dhcp-g
    </code>
</pre>
Thiết lập IP cho các internal interfaces <b>tap-r</b> và <b>tap-g</b>. Thiết lập dải địa chỉ cấp phát cho các máy ảo trên các các tenant namespaces tương ứng <b>red</b> và <b>green</b>
<br>
Cấu hình cho <b>tap-r</b>
<pre>
    <code>
# cau hinh IP cho tap-r
ip netns exec dhcp-r bash 
ip link set dev lo up
ip link set dev tap-r up
ip address add 10.50.50.2/24 dev tap-r
# cau hinh dai dia chi cap phat cho cac may ao trong namespace red
ip netns exec dhcp-r dnsmasq --interface=tap-r \
--dhcp-range=10.50.50.10,10.50.50.100,255.255.255.0
    </code>
</pre>
Cấu hình cho <b>tap-g</b>
<pre>
    <code>
# cau hinh IP cho tap-g
ip netns exec dhcp-g bash
ip link set dev lo up
ip link set dev tap-g up
ip address add 10.50.50.2/24 dev tap-g
# cau hinh dai dia chi cap phat cho cac may ao trong namespace green
ip netns exec dhcp-g dnsmasq --interface=tap-g \
--dhcp-range=10.50.50.10,10.50.50.100,255.255.255.0
    </code>
</pre>
Kiểm tra các tiến trình đang sử dụng <b>dnsmasq</b>
<pre>
    <code>
ps aux | grep dnsmasq
# ket qua
nobody     3671  0.0  0.1  31032  2332 ?        S    15:17   0:00 dnsmasq --interface=tap-r --dhcp-range=10.50.50.10,10.50.50.100,255.255.255.0
nobody     3674  0.0  0.1  31032  2400 ?        S    15:19   0:00 dnsmasq --interface=tap-g --dhcp-range=10.50.50.10,10.50.50.100,255.255.255.0
    </code>
</pre>
Như kết quả kiểm tra ở trên, có thể thấy hai tiến trình có PID <b>3671</b> và <b>3674</b> đang sử dụng dịch vụ dnsmasq. Kiểm tra xem các tiến trình đó thuộc về namespaces nào:
<pre>
    <code>
# PID = 3671
ip netns identify 3671
# ket qua
dhcp-r

# PID = 3674
ip netns identify 3674
# ket qua
dhcp-g
    </code>
</pre>
Như vậy hai tiến trình này thuộc về 2 namespaces tương ứng là <b>dhcp-r</b> và <b>dhcp-g</b>. Giờ ta tiến hành cấp địa chỉ IP cho các máy ảo tương ứng trên 2 tenant namespaces <b>red</b> và <b>green</b>.
<br>
Ở đây không sử dụng máy ảo nên ta sẽ cấp phát IP cho các virtual interfaces <b>eth0-r</b> và <b>eth0-g</b> thuộc hai namespaces tương ứng <b>red</b> và <b>green</b>.
<br>
Xin cấp IP cho <b>eth0-r</b> và kiểm tra địa chỉ IP trong namespace red.
<pre>
    <code>
ip netns exec red dhclient eth0-r # xin cap dia chi IP
ip netns exec red ip a

# ket qua
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
19: eth0-r: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether ae:43:1f:2e:ef:f8 brd ff:ff:ff:ff:ff:ff
    inet 10.50.50.11/24 brd 10.50.50.255 scope global eth0-r
       valid_lft forever preferred_lft forever
    inet6 fe80::ac43:1fff:fe2e:eff8/64 scope link
       valid_lft forever preferred_lft forever
    </code>
</pre>
Xin cấp IP cho <b>eth0-g</b>
<pre>
    <code>
ip netns exec green dhclient eth0-g
ip netns exec green ip a

# ket qua    
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
21: eth0-g: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 06:66:b1:76:75:5f brd ff:ff:ff:ff:ff:ff
    inet 10.50.50.62/24 brd 10.50.50.255 scope global eth0-g
       valid_lft forever preferred_lft forever
    inet6 fe80::466:b1ff:fe76:755f/64 scope link
       valid_lft forever preferred_lft forever   
    </code>
</pre>
    </li>
</ul>
<h2><a name="ref">3. Tham khảo</a></h2>
<div>  
[1] - <a href="http://blog.scottlowe.org/2013/09/04/introducing-linux-network-namespaces/">http://blog.scottlowe.org/2013/09/04/introducing-linux-network-namespaces/</a>
<br>
[2] - <a href="http://www.opencloudblog.com/?p=42">http://www.opencloudblog.com/?p=42</a>
<br>
[3] - <a href="https://www.youtube.com/watch?v=_WgUwUf1d34">https://www.youtube.com/watch?v=_WgUwUf1d34</a>
</div>
