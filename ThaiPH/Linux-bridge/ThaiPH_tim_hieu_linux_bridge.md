# Tìm hiểu Linux bridge
# Mục lục

<h3><a href="#intro">1. Giới thiệu Linux bridge</a></h3>
<ul>
<li><a href="#arch">1.1. Kiến trúc</a></li>
<li><a href="#component">1.2. Các thành phần</a></li>
<li><a href="#func">1.3. Các chức năng</a></li>
</ul>
<h3><a href="#labs">2. Lab tính năng Linux bridge</a></h3>
<ul>
<li><a href="#topo">2.1. Topology</a></li>
<li><a href="#config">2.2. Cài đặt và cấu hình</a></li>
</ul>
<h3><a href="#ref">3. Tham khảo</a></h3>

---

<h2><a name="intro">1. Giới thiệu Linux bridge</a></h2>
<ul>
<li><h3><a name="arch">1.1. Kiến trúc</a></h3>
<div>
Linux bridge là một soft-switch, một trong ba công nghệ cung cấp switch ảo trong hệ thống Linux (bên cạnh macvlan và OpenvSwitch), giải quyết vấn đề ảo hóa network bên trong các máy vật lý.
<br>
Bản chất, linux bridge sẽ tạo ra các switch layer 2 kết nối các máy ảo (VM) để các VM đó giao tiếp được với nhau và có thể kết nối được ra mạng ngoài. Linux bridge thường sử dụng kết hợp với hệ thống ảo hóa KVM-QEMU.
</div>
</li>

<li><h3><a name="component">1.2. Các thành phần</a></h3>
<div>
<img src="http://i.imgur.com/GKs6wWF.png"/><br><br>
Kiến trúc linux bridge minh họa như hình vẽ trên. Một số khái niệm liên quan tới linux bridge:
<ul>
<li><b>Port</b>: tương đương với port của switch thật</li>
<li><b>Bridge</b>: tương đương với switch layer 2</li>
<li><b>Tap</b>: hay <b>tap interface</b> có thể hiểu là giao diện mạng để các VM kết nối với bridge cho linux bridge tạo ra</li>
<li><b>fd</b>: forward data - chuyển tiếp dữ liệu từ máy ảo tới bridge</li>
</ul>
</div>
</li>

<li><h3><a name="func">1.3. Các tính năng</a></h3>
<ul>
<li><b>STP</b>: Spanning Tree Protocol - giao thức chống loop gói tin trong mạng</li>
<li><b>VLAN</b>: chia switch (do linux bridge tạo ra) thành các mạng LAN ảo, cô lập traffic giữa các VM trên các VLAN khác nhau của cùng một switch.</li>
<li><b>FDB</b>: chuyển tiếp các gói tin theo database để nâng cao hiệu năng switch</li>
</ul>
</li>
</ul>
<h2><a name="labs">2. Lab tính năng Linux bridge</a></h2>
<ul>
<li><h3><a name="topo">2.1. Topology</a></h3>
<img src="http://i.imgur.com/zswlIDa.jpg"/>
<br><br>
<div>
<ul>
<li>Một máy tính với 2 card eth1, eth2 (có thể sử dụng máy ảo), cài ubuntu 14.04.</li>
<li><b>Trường hợp 1</b>: Tạo một switch ảo và gán interface eth1 vào switch đó, tạo một máy ảo bên trong máy host, gắn vào tab interface của switch và kiểm tra địa chỉ được cấp phát. (Có thể tạo 2 VM trong host cùng gắn vào tab interface của switch, ping kiểm tra kết nối).</li>
<li><b>Trường hợp 2</b>: Gắn cả 2 card mạng eth1, eth2 của host vào switch ảo, set priority cho hai port ứng với 2 card. Kiểm tra xem máy ảo (gắn vào tab interface của switch ảo) nhận ip cùng dải với card mạng vật lý nào.</li>
</ul>
</div>

</li>
<li><h3><a name="config">2.2. Cài đặt và cấu hình</a></h3>
<ul>
<li><b>Trường hợp 1: </b>
<ul>
<li><b>Bước 1</b>: Tạo switch ảo br1. Nếu đã tồn tại có thể xóa switch này đi và tạo lại:
<pre>
<code>
brctl delbr br1 # xóa đi nếu đã tồn tại
brctl addbr br1 # tạo mới
</code>
</pre>
</li>
<li><b>Bước 2</b>: Gán port eth1 vào swith br1
<pre>
<code>
brctl addif br1 eth1
brctl stp br1 on # enable tính năng STP nếu cần
</code>
</pre>
</li>
<li><b>Bước 3</b>: Khi tạo một switch mới <b>br1</b>, trên máy host sẽ xuất hiện thêm 1 NIC ảo trùng tên switch đó (br1). Ta có thể cấu hình xin cấp phát IP cho NIC này sử dụng command hoặc cấu hình trong file <b>/etc/network/interfaces</b> để giữ cấu hình cho switch ảo sau khi khởi động lại:
<pre>
<code>
dhclient br1
</code>
</pre>
Nếu trước đó trong file <b>/etc/network/interfaces</b> đã cấu hình cho NIC eth1, ta phải comment lại cấu hình đó hoặc xóa cấu hình đó đi và thay bằng các dòng cấu hình sau:
<pre>
<code>
/etc/network/interfaces
auto br1
iface br1 inet dhcp
bridge_ports eth1
bridge_stp on
bridge_fd 0
bridge_maxwait 0
</code>
</pre>
</li>
<li><b>Bước 4</b>: Khởi động lại các card mạng và kiểm tra lại cấu hình bridge:
<pre>
<code>
ifdown -a && ifup -a # khởi động lại tất cả các NIC
brctl show # kiểm tra cấu hình switch ảo
</code>
</pre>
Kết quả kiểm tra cấu hình sẽ tương tự như sau:
<pre>
<code>
bridge name	bridge id		STP enabled	interfaces
br0		8000.000c29586f24	yes		eth0
br1		8000.000c29586f2e	yes		eth1
lxcbr0		8000.000000000000	no		
virbr0		8000.000000000000	yes
</code>
</pre>
Kết quả cấu hình thành công gắn NIC eth1 vào switch ảo br1 sẽ hiển thị như đoạn mã trên.
</li>
<li><b>Bước 5:</b> Để kiểm tra, ta có thể tạo một máy ảo và tạo một NIC kết nối với switch <b>br1</b>.</li>
</ul>
</li>

<li><b>Trường hợp 2</b>: Gắn 2 NIC eth1 và eth2 vào cùng switch <b>br1</b>. Do trước đó NIC eth1 đã gán vào br1, giờ ta sẽ tiến hành gán tiếp NIC eth2, đồng thời thiết lập mức độ ưu tiên của các port tương ứng với các NIC đã gán vào switch br1.
<pre>
<code>
brctl addif br1 eth2 # gán NIC eth2 vào sw br1
# Thiết lập mức ưu tiên cho các port
brctl setportprio br1 eth1 1
brctl setportprio br1 eth2 2
</code>
</pre>
Theo lý thuyết, port nào có độ ưu tiên cao hơn thì các VM khi gắn vào tab interface của switch ảo sẽ nhận IP cùng dải với NIC của máy host đã gán vào switch ảo đó. Theo như cấu hình trên, port tương ứng với NIC eth2 có độ ưu tiên cao hơn. Như vậy VM sẽ nhận IP cùng dải với eth2.
<br>
Trong bài lab này, card <b>eth1</b> thuộc dải mạng <b>10.10.10.0/24</b> và card <b>eth2</b> thuộc dải mạng <b>10.10.2.0/24</b>. Như vậy VM sẽ nhận IP thuộc dải <b>10.10.2.0/24</b>. Minh họa:
<br><br>
<img src="http://i.imgur.com/CjGhbFS.png"/>
<br><br>
<img src="http://i.imgur.com/gWcAeq1.png"/>
<br><br>
</li>
</ul>
</li>

</ul>
<h2><a name="ref">3. Tham khảo</a></h2>
<div>
[1] - <a href="http://www.innervoice.in/blogs/2013/12/02/linux-bridge-virtual-networking/">http://www.innervoice.in/blogs/2013/12/02/linux-bridge-virtual-networking/</a>
<br>
[2] - <a href="https://github.com/hocchudong/Linux-bridge">https://github.com/hocchudong/Linux-bridge</a>
</div>
