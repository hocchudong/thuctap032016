# Cấu hình bonding với Linux bridge
# Mục lục

<h3><a href="#concept">1. Khái niệm bonding</a></h3>
<ul>
<li><a href="#basic">1.1. Khái niệm</a></li>
<li><a href="#mode">1.2. Các bonding mode</a></li>
</ul>
<h3><a href="#topo">2. Topology</a></h3>
<h3><a href="#config">3. Cấu hình</a></h3>
<ul>
<li><a href="#requirement">3.1. Cài đặt các gói cần thiết</a></li>
<li><a href="#kernel">3.2. Kernel module</a></li>
<li><a href="#cfg">3.1. Cấu hình bonding network</a></li>
</ul>
<h3><a href="#ref">4. Tham khảo</a></h3>

---

<h2><a name="concept">1. Khái niệm bonding</a></h2>
<ul>
<li><h3><a name="basic">1.1. Khái niệm</a></h3>
Bonding hay còn gọi là port forwarding hoặc link aggregation là việc kết hợp nhiều NIC thành một NIC logic duy nhất nhằm cân bằng tải, tăng thông lượng, khả năng chịu lỗi, etc. của hệ thống.
</li>
<li><h3><a name="mode">1.2. Các bonding mode</a></h3>
Có 7 bonding modes:
<ul>
<li><b>Mode 0 - balance-rr</b>: Áp dụng cơ chế Round-robin cung cấp khả năng cân bằng tải và chịu lỗi</li>
<li><b>Mode 1 - active-backup</b>: Áp dụng cơ chế Active-backup. Tại một thời điểm chỉ có 1 slave interface active, các slave khác sẽ active khi nào slave đang active bị lỗi. Địa chỉ MAC của đường bond sẽ thấy từ bên ngoài chỉ trên một port để tránh gây khó hiểu cho switch. Mode này cung cấp khả năng chịu lỗi</li>
<li><b>Mode 2 - balance-xor</b>: Áp dụng phép XOR: thực hiện XOR MAC nguồn và MAC đích, rồi thực hiện modulo với số slave. Mode này cung cấp khả năng cân bằng tải và chịu lỗi</li>
<li><b>Mode 3 - broadcast</b>: Gửi tin trên tất cả các slave interfaces. Mode này cung cấp khả năng chịu lỗi.</li>
<li><b>Mode 4 - 802.3ad</b>: IEEE 802.3ad. Mode này sẽ tạo một nhóm tập hợp các intefaces chia sẻ chung tốc độ và thiết lập duplex (hai chiều). Yêu cầu để sử dụng mode này là có Ethtool trên các drivers gốc để đạt được tốc độ và cấu hình hai chiều trên mỗi slave, đồng thời các switch sẽ phải cấu hình hỗ trợ chuẩn IEEE 802.3ad.</li>
<li><b>Mode 5 - balance-tlb</b>: Cân bằng tải thích ứng với quá trình truyền tin: lưu lượng ra ngoài phân tán dựa trên tải hiện tại trên mỗi slave (tính toán liên quan tới tốc độ). Lưu lượng tới nhận bởi slave active hiện tại, nếu slave này bị lỗi khi nhận gói tin, các slave khác sẽ thay thế, MAC address của đường bond sẽ chuyển sang một trong các slave còn lại.</li>
<li><b>Mode 6 - balance-alb</b>: Cân bằng tài thích ứng: bao gồm cả cân bằng tải truyền (balance-tlb) và cân bằng tải nhận (rlb - receive load balancing) đối với lưu lượng IPv4. Cân bằng tải nhận đạt được nhờ kết hợp với ARP. Bondin driver sẽ chặn các bản tin phản hồi ARP gửi bởi hệ thống cụ bộ trên đường ra và ghi đè địa chỉ MAC nguồn bằng địa chỉ MAC của một trong các slaves trên đường bond.</li>
</ul>
</li>

</ul>
<h2><a name="topo">2. Topology</a></h2>
<div>Chuẩn bị máy cài ubuntu 14.04 với 2 card mạng <b>eth0</b> và <b>eth1</b> thuộc dải: <b>172.16.69.0/24</b></div>
<h2><a name="config">3. Cấu hình</a></h2>
<ul>
<li><h3><a name="requirement">3.1. Cài đặt các gói cần thiết</a></h3>
Cài gói ifenslave để attach và detach các NIC slave vào đường bond:
<pre>
<code>
apt-get install ifenslave
</code>
</pre>
</li>
<li><h3><a name="kernel">3.2. Kernel module</a></h3>
Nạp module bonding vào nhân hệ điều hành:
<pre>
<code>
echo bonding >> /etc/modules
modprobe bonding
</code>
</pre>
Kiểm tra thư mục cấu hình bonding:
<pre>
<code>
ls -l /proc/net/bonding
</code>
</pre>
</li>
<li><h3><a name="cfg">3.1. Cấu hình bonding network</a></h3>
Mở file:
<pre>
<code>
vim /etc/network/interfaces
</code>
</pre>
Cấu hình bond0 kết hợp hai interfaces eth0 và eth1 như sau (cơ chế Round-robin - Mode 0 - balance-rr):
<pre>
<code>
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet manual
    bond-master bond0

auto eth1
iface eth1 inet manual
    bond-master bond0

auto bond0
iface bond0 inet static
    # For jumbo frames, change mtu to 9000
    mtu 1500
    address 172.16.69.1
    netmask 255.255.255.0
    network 172.16.69.0
    broadcast 172.16.69.255
    gateway 172.16.69.1
    bond-miimon 100 # Specifies the MII link monitoring frequency in milliseconds. This determines how often the link state of each slave is inspected for link failures.
    bond-downdelay 200 # Specifies the time, in milliseconds, to wait before disabling a slave after a link failure has been detected.
    bond-updelay 200 # Specifies the time, in milliseconds, to wait before enabling a slave after a link recovery has been detected.
    bond-mode 0
    bond-slaves none # we already defined the interfaces above with bond-master
</code>
</pre>
Khởi động lại các card mạng để áp dụng thay đổi:
<pre>
<code>ifdown -a && ifup -a</code>
</pre>
</li>

</ul>
<h2><a name="ref">4. Tham khảo</a></h2>
<div>
[1] - <a href="https://www.kernel.org/doc/Documentation/networking/bonding.txt">https://www.kernel.org/doc/Documentation/networking/bonding.txt</a>
<br>
[2] - <a href="https://raymii.org/s/tutorials/NIC_Bonding_on_Ubuntu_12.04.html">https://www.kernel.org/doc/Documentation/networking/bonding.txt</a>
</div>
