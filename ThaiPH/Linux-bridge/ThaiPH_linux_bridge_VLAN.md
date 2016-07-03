# VLAN với Linux bridge
# Mục lục

<h3><a href="#topo">1. Topology</a></h3>
<h3><a href="#installation">2. Cài đặt và cấu hình</a></h3>
<ul>
<li><a href="#check">2.1. Kiểm tra hệ thống</a></li>
<li><a href="#pakages">2.2. Cài các gói phần mềm cần thiết</a></li>
<li><a href="#config">2.3. Cấu hình hệ thống để sử dụng VLAN</a></li>
<li><a href="#configvl">2.4. Cấu hình các VM và kiểm tra hoạt động của VLAN</a></li>
</ul>
<h3><a href="#ref">4. Tham khảo</a></h3>

---

<h2><a name="topo">1. Topology</a></h2>
<div>
<img src="http://i.imgur.com/AReMadw.jpg"/><br><br>
<ul>
<li>Máy host cài ubuntu 14.04, có một card mạng (eth2)</li>
<li>Cấu hình 2 VLAN subinterfaces 101 và 102 trên card mạng (eth2) của máy host</li>
<li>Cấu hình 2 switch (do linux bridge tạo ra) và gán 2 VLAN subinterfaces ở trên tương ứng vào 2 bridge này</li>
<li>Cài đặt một số VM và gắn card mạng của các VM này vào các tap interfaces của 2 switch ảo trên để kiểm tra kết nối</li>
</ul>
</div>

<h2><a name="installation">2. Cài đặt và cấu hình</a></h2>
<ul>
<li><h3><a name="check">2.1. Kiểm tra hệ thống</a></h3>
Kiểm tra xem hệ thống có hỗ trợ ảo hóa không bằng cách sử dụng lệnh:
<pre>
<code>
egrep '(vmx|svm)' /proc/cpuinfo
</code>
</pre>
Nếu có kết quả trả về nghĩa là hệ thống có thể hỗ trợ ảo hóa. Nếu không, cần phải cấu hình lại máy để cho phép hỗ trợ ảo hóa VT-X hoặc AMD-V. Nếu sử dụng host là máy vật lý phải chỉnh sửa trong BIOS. Còn nếu sử dụng host là máy ảo, ví dụ ở đây sử dụng VMWare, chỉnh sửa lại cấu hình như sau:
<br><br>
<img src="http://i.imgur.com/uTDgFxO.png"/>
</li>
<li><h3><a name="pakages">2.2. Cài các gói phần mềm cần thiết</a></h3>
Cài đặt các gói sau để hỗ trợ vlan, KVM, bridge networking:
<pre>
<code>
apt-get install vlan ubuntu-virt-server python-vm-builder kvm-ipxe bridge-utils libguestfs-tools
</code>
</pre>
</li>
<li><h3><a name="config">2.3. Cấu hình hệ thống để sử dụng VLAN</a></h3>
<ul>
<li>Cấu hình 2 VLAN subinterfaces trên card eth2 và up 2 interfaces này lên:
<pre>
<code>
vconfig add eth2 101
vconfig add eth2 102
ifconfig eth2.101 up
ifconfig eth2.102 up
</code>
</pre>
Nếu tạo thành công kết quả trả về sẽ tương tự như sau:
<pre>
<code>
Added VLAN with VID == 101 to IF -:eth2:-
Added VLAN with VID == 102 to IF -:eth2:-
</code>
</pre>
Hoặc cũng có thể kiểm tra 2 vlan đã tạo như sau:
<pre>
<code>
cat /proc/net/vlan/config
</code>
</pre>
Kết quả trả về sẽ tương tự như sau:
<pre>
<code>
VLAN Dev name	 | VLAN ID
Name-Type: VLAN_NAME_TYPE_RAW_PLUS_VID_NO_PAD
eth2.101       | 101  | eth2
eth2.102       | 102  | eth2
</code>
</pre>
</li>
<li>Tạo hai switch ảo và gán 2 VLAN subinterfaces trên vào hai switch tương ứng này:
<pre>
<code>
brctl addbr br-vl101
brctl addbr br-vl102
brctl addif br-vl101 eth2.101
brctl addif br-vl102 eth2.102
</code>
</pre>
Kiểm tra việc gán interfaces đã thành công chưa sử dụng lệnh:
<pre>
<code>
brctl show
</code>
</pre>
Kết quả trả về thành công sẽ tương tự như sau:
<pre>
<code>
bridge name	bridge id		STP enabled	interfaces
br-vl101	8000.000c29586f38	yes		    eth2.101
br-vl102	8000.000c29586f38	yes		    eth2.102
br0		 8000.000c29586f24	yes		    eth0
lxcbr0	  8000.000000000000	no
</code>
</pre>
</li>
<li>Lưu giữ lại cấu hình này để tránh bị mất khi khởi động lại bằng cách chỉnh sửa trong file <b>/etc/network/interfaces</b>:
<pre>
# config vlan 101
auto eth2.101
iface eth2.101 inet manual
vlan-raw-device eth2

auto br-vl101
iface br-vl101 inet static
address 10.0.2.141/24
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
address 10.0.2.152/24
bridge_ports eth2.102
bridge_stp on
bridge_fd 9
bridge_maxwait 0
up /sbin/ifconfig $IFACE up || /bin/true
</pre>
Khởi động lại các interfaces để áp dụng thay đổi:
<pre>
<code>ifdown -a && ifup -a</code>
</pre>
</li>
</ul>
</li>

<li><h3><a name="configvl">2.4. Cấu hình các VM và kiểm tra hoạt động của VLAN</a></h3>
<div>
Trong kịch bản của bài lab này, có 3 VM với cấu hình như sau:
<ul>
<li><b>kvm0</b>: thuộc vlan 102, được gán vào switch <b>br-vl102 </b>. Cấu hình IP tĩnh cho máy này với IP: <b>10.0.2.147/24</b>
<br><br>
<img src="http://i.imgur.com/XBWFFcF.png"/>
<br><br>
</li>
<li><b>kvm1</b> và <b>vm1</b>: thuộc vlan 101, được gán vào switch <b>br-vl101</b>. Cấu hình IP tĩnh cho 2 máy:
<ul>
<li><b>kvm1</b>: 10.0.2.145/24</li>
<li><b>vm1</b>: 10.0.2.140/24</li>
</ul>
<br><br>
<img src="http://i.imgur.com/PJPH2UT.png"/>
<br><br>
<img src="http://i.imgur.com/GZELzyp.png"/>
<br><br>
</li>
</ul>
Tiến hành ping giữa các máy kiểm tra kết nối:
<ul>
<li>Ping giữa máy khác vlan: máy kvm0 (vlan 102) và máy kvm1 (vlan 101). Kết quả hai máy không truyền thông được với nhau:
<br><br>
<img src="http://i.imgur.com/LL9y187.png"/>
<br><br>
</li>
<li>Ping giữa hai máy cùng vlan 101 - kvm1 và vm1. Kết quả hai máy truyền thông được với nhau:
<br><br>
<img src="http://i.imgur.com/RuleRxg.png"/>
<br><br>
</li>
</ul>
</div>
</li>

</ul>
<h2><a name="ref">4. Tham khảo</a></h2>
<div>
[1] - <a href="https://raymii.org/s/tutorials/KVM_with_bonding_and_VLAN_tagging_setup_on_Ubuntu_12.04.html#Set_up_network_bridge_for_VLAN">KVM - VLAN - Bonding</a>
<br>
[2] - <a href="https://raymii.org/s/tutorials/NIC_Bonding_on_Ubuntu_12.04.html">KVM - VLAN tagging Ubuntu 12.04</a>
<br>
[3] - <a href="https://dnaeon.github.io/linux-bonding-vlans-bridges-and-kvm/">https://dnaeon.github.io/linux-bonding-vlans-bridges-and-kvm/</a>
<br>
[4] - <a href="https://wiki.debian.org/NetworkConfiguration">https://wiki.debian.org/NetworkConfiguration</a>
</div>
