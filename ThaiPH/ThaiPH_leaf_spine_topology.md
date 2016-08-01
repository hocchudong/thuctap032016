# Leaf-spine Cumulus Lab
# Mục lục
<h3><a href="#leaf-spine">1. Giới thiệu Leaf-Spine topology</a></h3>
<h3><a href="#topo">2. Mô hình bài lab</a></h3>
<h3><a href="#cfg">3. Cài đặt và cấu hình</a></h3>
<ul>
    <li><a href="#essential">3.1. Các phần mềm cần thiết</a></li>
    <li><a href="#cfgsws">3.2. Cấu hình các switch</a></li>
    <li><a href="#check">3.3. Kiểm tra kết nối giữa các switch</a></li>
</ul>
<h3><a href="#ref">4. Tham khảo</a></h3>

---

<h2><a name="leaf-spine">1. Giới thiệu Leaf-Spine topology</a></h2>
<div>
    <h4>Tại sao phải sử dụng leaf-spine topology?</h4>
    <div>
    Hiện nay, vấn đề nâng cao khả năng truyền dữ liệu lớn với tốc độ tức thời trong hệ thống mạng, thiết kế 3 tầng trong datacenter được thay thế bởi thiết kế <b>Leaf-Spine</b>. Kiến trúc Leaf-Spine thích ứng được với các yêu cầu ngày một thay đổi của các công ty trong ngành công nghiệp BigData với sự phát triển của các datacenter.      .
    </div>

    <h4>Thiết kế mạng truyền thống trong datacenter</h4>
    <div>
      Mô hình truyền thống ba tầng trong datacenter được thiết kế để sử dụng trong hệ thống mạng chung, thường được phân đoạn thành các PODs(Point of Delivery), hạn chế về vị trí của các thiết bị chẳng hạn như các máy chủ ảo. Kiến trúc này bao gồm 3 tầng: các Core Routers, Aggregation (hay Distribution) routers và các Access switches. Các thiết bị này kết nối nội bộ với nhau bằng các đường dự phòng và có thể gây ra loop trong mạng. Do đó trong thiết kế ba tầng này sử dụng giao thức STP để tránh loop. Tuy nhiên, việc làm như vậy sẽ ngắt các tất cả các đường dự phòng trừ các đường chính do giao thức này tạo ra để tránh loop. Các đường dự phòng đó chỉ được kích hoạt và sử dụng khi các đường đang active bị sự cố. Do đó, các đường chính có thể gặp tình trạng quá tải khi lưu lượng dồn qua đó quá nhiều, trong khi các đường dự phòng lại không được sử dụng.
      <br><br>
      <img src="http://humairahmed.com/blog/wp-content/uploads/2013/01/trad-arch-e1358499790910.png">
      <br><br>
    </div>

    <h4>Leaf-Spine Network Topology</h4>
    <div>
        Với cấu hình <b>Leaf-Spine</b>, tất cả các thiết bị nằm chung trong một số segment và có trễ truyền tin có thể dự đoán được. Thiết kế này chỉ gồm hai lớp, <b>Leaf</b> layer và <b>Spine</b> layer. Leaf layer chứa các switch truy nhập nhằm tạo kết nối tới các thiết bị như server, firewall, load balancer, và các router phần rìa. Spine layer được hình thành bởi các switch thực hiện định tuyến và là khung xương sống của mạng, nơi và các Leaf switch kết nối nội bộ với nhau và với các Spine switch. 
        <br>
        Để cho phép khả năng dự đoán được khoảng cách giữa các thiết bị trong thiết kế này, mô hình định tuyến động Layer 3 được sử dụng để kết nối các các lớp. Định tuyến động cho phép tìm ra đường tốt nhất để xác định và thay đổi dựa trên phản hồi trạng thái của mạng. Mô hình Leaf-Spine này tập trung vào lưu lượng "East-West", tức là lưu lượng truyền tải nội bộ trong datacenter và không đi ra hệ thống mạng khác ở bên ngoài. Hướng tiếp cận này giải quyết những hạn chế nội tại của giao thức Spanning Tree với khả năng sử dụng giao thức mạng khác và các phương pháp khác để tạo ra hệ thống mạng linh động.  
        <br><br>
        <img src="https://blog.westmonroepartners.com/wp-content/uploads/2015/02/Leaf-Spine.jpg">
        <br><br>
    </div>

    <h4>Ưu điểm của mô hình <b>Leaf-Spine</b></h4>
    <div>
      Với Leaf-Spine, hệ thống mạng sử dụng định tuyến Layer 3. Tất cả các router được cấu hình sử dụng trong trạng thái active thông qua việc sử dụng giao thức Equal-Cost Multipathing (ECMP). Điều này cho phép tất cả các kết nối được sử dụng cùng một thời điểm trong khi vẫn giữ được tính ổn định cũng như tránh loop trong mạng. Với giao thức chuyển mạch truyền thống Layer 2 như STP trên mô hình 3 tầng, ta phải cấu hình chính xác trên mọi thiết bị, chỉ cần cấu hình không đúng một thiết bị cũng có thể dẫn tới thiết lập đường đi không hiệu quả. 
      <br>
      Ưu điểm khác của mô hình này là dễ dàng trong việc thêm phần cứng mới và tăng dung lượng. Khi một liên kết bị <b>oversubscription</b> (nghĩa là lưu lượng tạo ra tập trung trên một liên kết active gây quá tải), việc tăng dung lượng được đáp ứng dễ dàng. Một Spine switch có thể được thêm vào và uplinks có thể được mở rộng tới mọi Leaf switch, kết quả là băng thông giữa hai lớp tăng lên và giảm thiểu <b>oversubscription</b>. Khi một cổng của thiết bị gặp vấn đề, Leaf switch mới có thể được bổ sung để kết nối nó với mọi spine switch và bổ sung cấu hình mạng vào switch dễ dàng. Khả năng mở rộng dễ dàng cho phép tối ưu hóa tiến trình nâng cấp, mở rộng hệ thống mạng mà không phải quản lý hay gặp trục tặc về các giao thức chuyển mạch Layer 2.
    </div>

</div>
<h2><a name="topo">2. Mô hình bài lab</a></h2>
<div>
    Bài lab tạo ra cấu hình 2-spine/2-leaf bằng việc import các OVA images của Cumulus VX vào 4 máy ảo VirtualBox, mỗi máy ảo này đại diện cho một switch leaf hoặc spine (Cumulus-VX-leaf1, Cumulus-VX-leaf2, Cumulus-VX-spine1, Cumulus-VX-spine2). Các switch này kết nối với nhau theo topology như sau:
    <br><br>
    <img src="https://docs.cumulusnetworks.com/download/attachments/5115521/VX_VirtualBox_topo_noOOB.png?version=1&modificationDate=1436460939000&api=v2">
    <br><br>
    <i><b>Chú ý: </b>Cumulus VX là các máy ảo do Cumulus phát hành, cho phép các nhà quản trị cloud và kỹ sư mạng thực hiện kiểm thử mô hình mạng đã thiết kế: build môi trường sandbox phục vụ học tập các khái niệm của Open Networking, tiền đề của việc vận hành network, các kịch bản và ứng dụng phát triển trong môi trường network của riêng mình. Trong giới hạn bài lab này, Cumulus VX được sử dụng để build các switch.</i>
</div>
<h2><a name="cfg">3. Cài đặt và cấu hình</a></h2>
<ul>
    <li><h3><a name="essential">3.1. Các phần mềm cần thiết</a></h3>
<div>
    <ul>
        <li>Tải và cài đặt <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox.</a></li>
        <li>Đăng ký một <a href="https://cumulusnetworks.com/cumulus-linux/secure/register/">tài khoản Cumulus</a>. Dùng tải khoản này đăng nhập và tải <a href="https://cumulusnetworks.com/cumulus-vx/download/">Cumulus VX OVA image</a>. Chú ý tải image tương ứng với VirtualBox.
        </li>
        <li>Cấu hình sẵn một dải NAT cho VirtualBox như sau:
        <ul>
            <li>Click <i>File -> Preferences</i> hoặc dùng phím tắt <i>Ctrl + G</i> mở hộp thoại cấu hình cho VirtualBox.</li>
            <li>Click vào tab <i>Network -> NAT Networks</i>. Sau đó Click vào biểu tượng dấu <i>+</i> ở bên phải để thêm dải mạng NAT cho VirtualBox như hình bên dưới (sử dụng dải 10.10.10.0/24, đặt tên là VMNAT)
            <br><br>
            <img src="http://i.imgur.com/qOiaU7g.png">
            <br><br>
            </li>
        </ul>
        </li>
        <li>Tiến hành import image OVA này vào 4 máy ảo VirtualBox khác nhau đại diện cho 4 switch. 
        <ul>
            <li><b>Cumulus-VX-leaf1: </b>Click biểu tượng <i>Setting</i> chỉnh lại cấu hình <i>Network</i>. Cấu hình 4 card mạng như sau:
            <ul>
                <li>
                    Trên tab <b>Adapter 1</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>NAT Network</b> và lựa chọn dải <b>VMNAT</b> trong danh sách <b>Name</b>. Click vào mũi tên <b>Advanced</b>, lựa chọn Adapter  Type là <b>Paravirtualized Network (virtio-net)</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 2</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>l1s1</b>, biểu thị kết nối <b>Cumulus-VX-leaf1 VM</b> với <b>Cumulus-VX-spine1 VM</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 3</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>l1s2</b>, biểu thị kết nối <b>Cumulus-VX-leaf1 VM</b> với <b>Cumulus-VX-spine2 VM</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 4</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>leaf1</b>.
                </li>
            </ul>
            <br><br>
            <img src="http://i.imgur.com/fj74kU8.png">
            <br><br>
            </li>

            <li><b>Cumulus-VX-leaf2: </b>Click biểu tượng <i>Setting</i> chỉnh lại cấu hình <i>Network</i>. Cấu hình 4 card mạng như sau:
            <ul>
                <li>
                    Trên tab <b>Adapter 1</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>NAT Network</b> và lựa chọn dải <b>VMNAT</b> trong danh sách <b>Name</b>. Click vào mũi tên <b>Advanced</b>, lựa chọn Adapter  Type là <b>Paravirtualized Network (virtio-net)</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 2</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>l2s1</b>, biểu thị kết nối <b>Cumulus-VX-leaf2 VM</b> với <b>Cumulus-VX-spine1 VM</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 3</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>l2s2</b>, biểu thị kết nối <b>Cumulus-VX-leaf2 VM</b> với <b>Cumulus-VX-spine2 VM</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 4</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>leaf2</b>.
                </li>
            </ul>
            </li>
            <li><b>Cumulus-VX-spine1: </b>Click biểu tượng <i>Setting</i> chỉnh lại cấu hình <i>Network</i>. Cấu hình 4 card mạng như sau:
            <ul>
                <li>
                    Trên tab <b>Adapter 1</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>NAT Network</b> và lựa chọn dải <b>VMNAT</b> trong danh sách <b>Name</b>. Click vào mũi tên <b>Advanced</b>, lựa chọn Adapter  Type là <b>Paravirtualized Network (virtio-net)</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 2</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>l1s1</b>, biểu thị kết nối <b>Cumulus-VX-spine1 VM</b> với <b>Cumulus-VX-leaf1 VM</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 3</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>l2s1</b>, biểu thị kết nối <b>Cumulus-VX-spine1 VM</b> với <b>Cumulus-VX-leaf2 VM</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 4</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>spine1</b>.
                </li>
            </ul>
            </li>
            <li><b>Cumulus-VX-spine2 </b>Click biểu tượng <i>Setting</i> chỉnh lại cấu hình <i>Network</i>. Cấu hình 4 card mạng như sau:
            <ul>
                <li>
                    Trên tab <b>Adapter 1</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>NAT Network</b> và lựa chọn dải <b>VMNAT</b> trong danh sách <b>Name</b>. Click vào mũi tên <b>Advanced</b>, lựa chọn Adapter  Type là <b>Paravirtualized Network (virtio-net)</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 2</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>l1s2</b>, biểu thị kết nối <b>Cumulus-VX-spine2 VM</b> với <b>Cumulus-VX-leaf1 VM</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 3</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>l2s2</b>, biểu thị kết nối <b>Cumulus-VX-spine2 VM</b> với <b>Cumulus-VX-leaf2 VM</b>.
                </li>
                <li>
                    Trên tab <b>Adapter 4</b>, trong danh sách <b>Attached to</b>, lựa chọn <b>Internal Network</b>. Sau đó cứ đổi <b>Name</b> thành <b>spine2</b>.
                </li>
            </ul>
            </li>
        </ul>
        </li>
    </ul>
</div>
    </li>

    <li><h3><a name="cfgsws">3.2. Cấu hình các switch</a></h3>
    Đăng nhập vào các switch (các máy ảo) với:
    <ul>
        <li>Tài khoản: <i>cumulus</i></li>
        <li>Mật khẩu: <i>CumulusLinux!</i></li>
    </ul>
    Trên cả 4 switch, tiến hành chỉnh sửa file <code>/etc/quagga/daemons</code>, tìm và sửa lại các thuộc tính với giá trị như bên dưới:
    <pre>
        <code>
zebra=yes
bgpd=yes
ospfd=yes 
        </code>
    </pre>
    <i><b>Chú ý: </b>Các bước cấu hình sau thực hiện với quyền <b>root</b></i>

    <h4>Cấu hình switch <b>Cumulus-VX-leaf1</b></h4>
    <ul>
        <li>
            Chỉnh sửa file <code>vi /etc/network/interfaces</code> với nội dung như sau:
            <pre>
                <code>
# The loopback network interface
auto lo
  iface lo inet loopback
  address 10.2.1.1/32

# The primary network interface
auto eth0
  iface eth0 inet dhcp

auto swp1
  iface swp1
  address 10.2.1.1/32

auto swp2
  iface swp2
  address 10.2.1.1/32

auto swp3
  iface swp3
  address 10.4.1.1/24
                </code>
            </pre>
        </li>

        <li>
           Chỉnh sửa file <code>vi /etc/quagga/Quagga.conf</code> với nội dung như sau:
           <pre>
               <code>
service integrated-vtysh-config

interface swp1
  ip ospf network point-to-point

interface swp2
  ip ospf network point-to-point

router-id 10.2.1.1

router ospf
  ospf router-id 10.2.1.1
  network 10.2.1.1/32 area 0.0.0.0
  network 10.4.1.0/24 area 0.0.0.0
               </code>
           </pre>
        </li>
    </ul>

    <h4>Cấu hình switch <b>Cumulus-VX-leaf2</b></h4>
    <ul>
        <li>
            Chỉnh sửa file <code>vi /etc/network/interfaces</code> với nội dung như sau:
            <pre>
                <code>
# The loopback network interface
auto lo
  iface lo inet loopback
  address 10.2.1.2/32

# The primary network interface
auto eth0
  iface eth0 inet dhcp

auto swp1
  iface swp1
  address 10.2.1.2/32

auto swp2
  iface swp2
  address 10.2.1.2/32

auto swp3
  iface swp3
  address 10.4.2.1/24
                </code>
            </pre>
        </li>

        <li>
           Chỉnh sửa file <code>vi /etc/quagga/Quagga.conf</code> với nội dung như sau:
           <pre>
               <code>
service integrated-vtysh-config 

interface swp1
  ip ospf network point-to-point

interface swp2
  ip ospf network point-to-point

router-id 10.2.1.2

router ospf
  ospf router-id 10.2.1.2                                                           
  network 10.2.1.2/32 area 0.0.0.0  
  network 10.4.2.0/24 area 0.0.0.0
               </code>
           </pre>
        </li>
    </ul>

    <h4>Cấu hình switch <b>Cumulus-VX-spine1</b></h4>
    <ul>
        <li>
            Chỉnh sửa file <code>vi /etc/network/interfaces</code> với nội dung như sau:
            <pre>
                <code>
# The loopback network interface
auto lo
  iface lo inet loopback
  address 10.2.1.3/32

# The primary network interface
auto eth0
  iface eth0 inet dhcp

auto swp1
  iface swp1
  address 10.2.1.3/32

auto swp2
  iface swp2
  address 10.2.1.3/32

auto swp3
  iface swp3
                </code>
            </pre>
        </li>

        <li>
           Chỉnh sửa file <code>vi /etc/quagga/Quagga.conf</code> với nội dung như sau:
           <pre>
               <code>
service integrated-vtysh-config 

interface swp1
  ip ospf network point-to-point

interface swp2
  ip ospf network point-to-point

router-id 10.2.1.3

router ospf
  ospf router-id 10.2.1.3
  network 10.2.1.3/32 area 0.0.0.0 
               </code>
           </pre>
        </li>
    </ul>

    <h4>Cấu hình switch <b>Cumulus-VX-spine2</b></h4>
    <ul>
        <li>
            Chỉnh sửa file <code>vi /etc/network/interfaces</code> với nội dung như sau:
            <pre>
                <code>
# The loopback network interface
auto lo
  iface lo inet loopback
  address 10.2.1.4/32

# The primary network interface
auto eth0
  iface eth0 inet dhcp

auto swp1
  iface swp1
  address 10.2.1.4/32

auto swp2
  iface swp2
  address 10.2.1.4/32

auto swp3
  iface swp3
                </code>
            </pre>
        </li>

        <li>
           Chỉnh sửa file <code>vi /etc/quagga/Quagga.conf</code> với nội dung như sau:
           <pre>
               <code>
service integrated-vtysh-config 

interface swp1
  ip ospf network point-to-point

interface swp2
  ip ospf network point-to-point

router-id 10.2.1.4

router ospf
  ospf router-id 10.2.1.4
  network 10.2.1.4/32 area 0.0.0.0
               </code>
           </pre>
        </li>
    </ul>
    Sau tất cả các bước trên, tiến hành khởi động lại các dịch vụ <b>Quagga</b> và <b>Networking</b> như sau:
    <pre>
        <code>
systemctl restart networking
systemctl restart quagga.service
        </code>
    </pre>
    </li>

    <li><h3><a name="check">3.3. Kiểm tra kết nối giữa các switch</a></h3>
Trên switch(máy ảo) <b>leaf1</b>, tiến hành ping tới các switch còn lại:
        <ul>
            <li>Ping tới <b>leaf2</b>:
        <pre>
            <code>
PING 10.2.1.2 (10.2.1.2) 56(84) bytes of data.
64 bytes from 10.2.1.2: icmp_seq=1 ttl=63 time=3.52 ms
64 bytes from 10.2.1.2: icmp_seq=2 ttl=63 time=2.35 ms
64 bytes from 10.2.1.2: icmp_seq=3 ttl=63 time=1.93 ms
64 bytes from 10.2.1.2: icmp_seq=4 ttl=63 time=2.01 ms
64 bytes from 10.2.1.2: icmp_seq=5 ttl=63 time=1.97 ms        

--- 10.2.1.2 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4007ms
rtt min/avg/max/mdev = 1.935/2.361/3.523/0.600 ms
            </code>
        </pre>
            </li>
            <li>Ping tới <b>spine1</b>:
        <pre>
            <code>
PING 10.2.1.3 (10.2.1.3) 56(84) bytes of data.
64 bytes from 10.2.1.3: icmp_seq=1 ttl=64 time=1.16 ms
64 bytes from 10.2.1.3: icmp_seq=2 ttl=64 time=1.56 ms
64 bytes from 10.2.1.3: icmp_seq=3 ttl=64 time=0.979 ms
64 bytes from 10.2.1.3: icmp_seq=4 ttl=64 time=1.30 ms
64 bytes from 10.2.1.3: icmp_seq=5 ttl=64 time=0.988 ms        

--- 10.2.1.3 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 0.979/1.199/1.563/0.221 ms
            </code>
        </pre>
            </li>
            <li>Ping tới <b>spine2</b>:
        <pre>
            <code>
PING 10.2.1.4 (10.2.1.4) 56(84) bytes of data.
64 bytes from 10.2.1.4: icmp_seq=1 ttl=64 time=1.27 ms
64 bytes from 10.2.1.4: icmp_seq=2 ttl=64 time=1.29 ms
64 bytes from 10.2.1.4: icmp_seq=3 ttl=64 time=1.34 ms
64 bytes from 10.2.1.4: icmp_seq=4 ttl=64 time=1.14 ms
64 bytes from 10.2.1.4: icmp_seq=5 ttl=64 time=1.26 ms        

--- 10.2.1.4 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4007ms
rtt min/avg/max/mdev = 1.147/1.264/1.346/0.072 ms
            </code>
        </pre>
            </li>

        </ul>

    </li>
</ul>
<h2><a name="ref">4. Tham khảo</a></h2>
<div>
    [1] - <a href="https://docs.cumulusnetworks.com/display/VX/Creating+a+Two-Spine%2C+Two-Leaf+Topology">https://docs.cumulusnetworks.com/display/VX/Creating+a+Two-Spine%2C+Two-Leaf+Topology</a>
    <br>
    [2] - <a href="https://blog.westmonroepartners.com/a-beginners-guide-to-understanding-the-leaf-spine-network-topology/">https://blog.westmonroepartners.com/a-beginners-guide-to-understanding-the-leaf-spine-network-topology/</a>
</div>

