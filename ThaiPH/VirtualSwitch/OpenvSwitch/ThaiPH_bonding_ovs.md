# Bonding với OpenvSwitch
# Mục lục

<h3><a href="#ovsbond">1. Bonding trong OpenvSwitch</a></h3>
<ul>
<li><a href="#brief">1.1. Sơ lược về bonding trong OpenvSwitch</a></li>
<li><a href="#atb">1.2. Bond mode - active-backup</a></li>
<li><a href="#slb">1.3. Bond mode - balance-slb</a></li>
<li><a href="#tcp">1.4. Bond mode - balance-tcp</a></li>
</ul>
<h3><a href="#topo">2. Topology</a></h3>
<h3><a href="#config">3. Cấu hình</a></h3>
<ul>
<li><a href="#basic">3.1. Cấu hình bonding với 2 card của máy ảo</a></li>
<li><a href="#lacp">3.2. LACP với OpenvSwitch</a></li>
</ul>
<h3><a href="#ref">4. Tham khảo</a></h3>

---

<h2><a name="ovsbond">1. Bonding trong OpenvSwitch</a></h2>
<ul>
<li><h3><a name="brief">1.1. Sơ lược về bonding trong OpenvSwitch</a></h3></li>
<div>
Bonding cho phép hai hay nhiều interface (còn gọi là "slave" khi thực hiện cấu hình bonding) để chia sẻ lưu lượng mạng. Ở góc nhìn mức cao, các interface được liên kết với nhau thành một port logic duy nhất nhưng chúng có băng hông tổng cộng của nhiều thiết bị. Ví dụ: 2 card mạng
vật lý 1Gbps khi được bond với nhau được xem như một card với tốc độ 2Gpbs. Cấu hình bond mang tới khả năng dự phòng, bond port sẽ không bị down chừng nào vẫn còn slave đang "sống".
<br>

Trong OpenvSwitch, một bond interface là sự kết hợp của hai hoặc nhiều hơn hai slave. Cấu hình lỗi xảy ra khi một bond chỉ có 1 slave, port đó vẫn là port thông thường, không thể thực hiện bất kỳ tính năng nào của bonding.
<br>

Có nhiều chế độ thực hiện bonding tuy nhiên openvswitch chỉ triển khai ba chế độ: <b>active-backup</b>, <b>balance-slb</b>, <b>blance-tcp</b> . Trong đó chế độ balance-slb (source load balancing) là phức tạp nhất. SLB bonding chia lưu lượng giữa các slave dựa trên địa chỉ MAC nguồn Ethernet. Cấu hình slb bonding chỉ hữu dụng trong trường hợp lưu lượng qua đường bond mà có nhiều địa chỉ Ethernet nguồn, ví dụ như lưu lượng mạng đi từ nhiều máy ảo được ghép lại thông qua đường bond.
</div>
<li><h3><a name="atb">1.2. Bond mode - active-backup</a></h3>
Active-backup là chế độ bond đơn giản nhất, dễ dàng cho phép các kết nối tới nhiều switches mà không cần cấu hình thêm cho switch. Nhược điểm chế độ này là lưu lượng từ tất cả các VMs chỉ đi qua một liên kết active duy nhất trên đường bond. Mọi link dự phòng khác trên đường bond không được sử dụng. Giả sử hệ thống với Ethernet adapters tốc độ 10Gbps, thông lượng tối đa cho tất cả các VM sẽ bị giới hạn trong 10Gbps.
<br><br>
<img src="https://eapch37923.i.lithium.com/t5/image/serverpage/image-id/772i377649A697233636/image-size/original?v=v2&px=-1"/>
<br><br>
</li>
<li><h3><a name="slb">1.3. Bond mode - balance-slb</a></h3>
Lưu lượng từ MAC nguồn đã băm có thể được chuyển tới liên kết ít active hơn để cân bằng hơn trong việc sử dụng các liên kết thành viên trong đường bond. Mỗi card mạng của máy ảo sử dụng duy nhất một slave interface trong đường bond, tuy nhiên lưu lượng từ nhiều máy ảo (xử lý với nhiều địa chỉ MAC nguồn) được phân tán
trên các interface thành viên của đường bond tùy theo thuật toán băm. Kết quả là, nếu như một node với 2 interfaces tốc độ 10Gbps, tổng thông lượng mà các VMs có thể sử dụng sẽ tăng lên 20Gbps, trong khi thông lượng mỗi VM tối đa sử dụng được là 10Gbps.
<br><br>
<img src="https://eapch37923.i.lithium.com/t5/image/serverpage/image-id/773i0E0B11323B2697EF/image-size/original?v=v2&px=-1"/>
<br><br>
</li>
<li><h3><a name="tcp">1.4. Bond mode - balance-tcp</a></h3>
Để có thể tận dụng được hoàn toàn lợi thế về băng thông được cung cấp khi sử dụng nhiều liên kết tới các switch từ các máy ảo đơn lẻ, OVS buộc phải cấu hình sử dụng LACP và balance-tcp. Tuy nhiên, trong cấu hình này, LACP và balance-tcp yêu cầu phải cấu hình về switch bởi vì nếu cấu hình không đúng, kết nối mạng có thể bị gián đoạn. Với LACP, nhiều liên kết tách biệt trên các switch vật lý được đối xử như một liên kết layer-2 duy nhất. Lưu lượng có thể bị chia ra giữa nhiều liên kết trong mô hình active-active dựa trên thuật toán băm lưu lượng (traffic-hashing).
<br>
Lưu lượng có thể được cân bằng giữa các thành viên của liên kết bond mà không liên quan gì tới bảng MAC trên switch, bởi vì các uplink được đối xử như một liên kết layer-2 duy nhất. Cấu hình balance-tcp kết hợp LACP được khuyên dùng vì nhiều luồng dữ liệu từ Layer-4 (transport) từ một VM có thể sử dụng được băng thông tổng cộng của tất cả các uplink (các liên kết thành viên của bond). Do đó nếu như nếu một máy có 2 card 10Gbps khi cấu hình bonding chế độ balance-tcp kết hợp với LACP, các TCP streams từ một máy ảo trên đó có thể sử dụng băng thông tối đa là 20Gbps thay vì chỉ là 10Gbps khi cấu hình balance-slb.
<br><br>
<img src="https://eapch37923.i.lithium.com/t5/image/serverpage/image-id/774iAA103D96E3C9D67D/image-size/original?v=v2&px=-1"/>
<br><br>
</li>
</ul>
<h2><a name="topo">2. Topology</a></h2>
<div>
<ul>
<li>Chuẩn bị một máy ảo ubuntu 14.04 server, có cài openvswitch và các module hỗ trợ ảo hóa kvm.</li>
<li>Cấu hình 2 card mạng chế độ host-only cùng dải(trong bài lab sử dụng dải 10.10.10.0/24)</li>
</ul>
2 mô hình được sử dụng trong bài viết:
<ul>
<li>Bonding với 2 card eth1 và eth2 của máy ảo</li>
<li>Kiểm tra tính năng link Aggregation và LACP với Open vSwitch theo mô hình sau:
<ul>
<li>Dùng OVS tạo hai switch ảo br0 và br1 và tạo 2 port trên mỗi switch</li>
<li>Tiến hành nối các port giữa hai switch thành 2 đường dự phòng hỗ trợ nhau như hình minh họa. Tiến hành bond 2 port trên mỗi switch. Để kiểm tra tính dự phòng, tạo 2 máy ảo, mỗi máy ảo cắm vào 1 switch ảo như trên. Tiến hành ping giữa hai máy, kiểm tra kết nối khi ta ngắt một trong hai đường kết nối.</li>
</ul>

<br><br>
<img src="https://qiita-image-store.s3.amazonaws.com/0/43114/4a30c4f1-3255-0902-163f-70748a2892e0.jpeg"/>
<br><br>
</li>
</ul>

</div>
<h2><a name="config">3. Cấu hình</a></h2>
<ul>
<li><h3><a name="basic">3.1. Cấu hình bonding với 2 card của máy ảo</a></h3>

<div>
<h4>Tạo switch ảo</h4>
<div>
<pre>
<code>
ovs-vsctl add-br ovsbond
</code>
</pre>
</div>

<h4>Tạo bond interface với hai slave là <b>eth1</b> và <b>eth2</b></h4>
<div>
<pre>
<code>
 ovs-vsctl add-bond ovsbond bond12 eth1 eth2 bond_mode=balance-slb other_config:bond-detect-mode=miimon other_config:bond-miimon-interval=100 other_config:bond_updelay=100 other_config:lacp-time=fast
</code>
</pre>

<br>
Kiểm tra lại cấu hình bond:
<pre>
<code>
ovs-appctl bond/show bond12 #su dung bond interface la bond12
</code>
</pre>
Kết quả sẽ tương tự như sau:
<pre>
<code>
---- bond12 ----
bond_mode: balance-slb
bond-hash-basis: 0
updelay: 0 ms
downdelay: 0 ms
next rebalance: 6638 ms
lacp_status: off

slave eth1: enabled
        active slave
        may_enable: true

slave eth2: enabled
        may_enable: true

</code>
</pre>
</div>

<h4>Cấu hình chuyển qua các mode bonding khác</h4>
<div>
<pre>
<code>
ovs-vsctl set port bond12 bond_mode=balance-slb # voi che do balance-slb
ovs-vsctl set port bond12 bond_mode=balance-tcp # voi che do balance-tcp
</code>
</pre>

</div>

<h4>Cấu hình bằng cách sửa file: <code>vi /etc/network/interfaces</code></h4>
<div>
Chú ý khi dùng cách này ta chỉ tạo rước bridge ovsbond, mọi cấu hình khác  đều thực hiện trong file <code>/etc/network/interfaces</code> để tránh bị xung đột với cấu hình bằng lệnh. Nội dung file chỉnh sửa lại như sau:
<pre>
<code>
auto eth1
iface eth1 inet manual

auto eth2
iface eth2 inet manual

allow-ovsbond bond12
iface bond12 inet manual
        ovs_type OVSBond
        ovs_bridge ovsbond
        ovs_bonds eth1 eth2
        ovs_options bond_mode=active-backup #balance-slb or balance-tcp

auto ovsbond
iface ovsbond inet static
        address 10.10.10.167/24
        ovs_type OVSBridge
        ovs_ports bond12
 balance-tcp
</code>
</pre>
Lưu lại file, khởi động lại toàn bộ các card mạng. Kiểm tra lại cấu hình.

</div>



</div>
</li>
<li><h3><a name="lacp">3.2. LACP với OpenvSwitch</a></h3>
Trước hết, ta thực hiện cấu hình 2 switch ảo br0 và br1 với các port internal kết nối giữa 2 switch như topology.
<h4>Tạo 2 bridge br0 và br1</h4>
<div>
<pre>
<code>
ovs-vsctl add-br br0
ovs-vsctl add-br br1
</code>
</pre>
</div>

<h4>Tạo các bond interface trên các bridge br0 và br1, kích hoạt sẵn giao thức lacp</h4>
<div>
<pre>
<code>
ovs-vsctl add-bond br0 bond0 e00 e01 lacp=active
ovs-vsctl add-bond br1 bond1 e10 e11 lacp=active
</code>
</pre>
</div>

<h4>Tạo các liên kết internal giữa hai bridge (hai liên kết e00-e10 và e01-e11)</h4>
<div>
<pre>
<code>
ovs-vsctl set interface e00 type=patch options:peer=e10
ovs-vsctl set interface e10 type=patch options:peer=e00
ovs-vsctl set interface e11 type=patch options:peer=e01
ovs-vsctl set interface e01 type=patch options:peer=e11
</code>
</pre>
</div>

<h4>Kiểm tra lại cấu hình bonding</h4>
<div>
<pre>
<code>
# cau hinh bond0
root@ubuntu:~# ovs-appctl bond/show bond0
---- bond0 ----
bond_mode: active-backup
bond-hash-basis: 0
updelay: 0 ms
downdelay: 0 ms
lacp_status: negotiated

slave e00: enabled
	active slave
	may_enable: true

slave e01: enabled
	may_enable: true

# cau hinh bond1
root@ubuntu:~# ovs-appctl bond/show bond1
---- bond1 ----
bond_mode: active-backup
bond-hash-basis: 0
updelay: 0 ms
downdelay: 0 ms
lacp_status: negotiated

slave e10: enabled
        may_enable: true

slave e11: enabled
        active slave
        may_enable: true

</code>
</pre>
</div>

<h4>Tạo các máy ảo gắn vào 2 bridge br0 và br1</h4>
<div>
Trong mô hình này, sử dụng 2 máy ảo:
<ul>
<li><b>kvm-th0:</b> Gán interface vào bridge <b>br0</b>, thiết lập địa chỉ IP tĩnh: 10.10.10.160/24</li>
<li><b>kvm-th1:</b> Gán interface vào bridge <b>br1</b>, thiết lập địa chỉ IP tĩnh: 10.10.10.163/24</li>
</ul>
Ban đầu ta thực hiện ping giữa hai máy ảo này, kết quả ping bình thường
<br><br>
<img src="http://i.imgur.com/mpPq1ng.png"/>
<br><br>
Tiếp đó, vẫn giữ trạng thái ping giữa hai máy ảo, đòng thời chỉnh sửa cấu hình sai, mục đích là cố ý gây ra sự cố trên đường link internal đang active. Hiện tại giả sử đang sử dụng liên kết active e00-e10. Ta cấu hình peer e00 nối với interface br1 trên bridge br1(chú ý interface br1 được tạo ra mặc định sau khi tạo bridge br1, hai khái niệm này khác nhau).
<pre>
<code>
ovs-vsctl set interface e00 type=patch options:peer=br1
</code>
</pre>
Trong khoảng thời gian ngắn sau khi thực hiện cấu hình ngắt kết nối e00-e10, hiện tượng mất kết nối giữa hai máy xảy ra (Destination host unreachable). Tuy nhiên, do cấu hình bonding active-backup kết hợp với lacp, liên kết e01-e11 được kích hoạt thay thế cho kết nối đã mất, cho phép thiết lập lại kết nối giữa hai máy ảo.
<br><br>
<img src="http://i.imgur.com/ujB16yt.png"/>
<br><br>
</div>

</li>
</ul>



<h2><a name="ref">4. Tham khảo</a></h2>
<div>
[1] - <a href="https://github.com/openvswitch/ovs/blob/master/vswitchd/INTERNALS">https://github.com/openvswitch/ovs/blob/master/vswitchd/INTERNALS</a>
<br>
[2] - <a href="http://blog.scottlowe.org/2012/10/19/link-aggregation-and-lacp-with-open-vswitch/">http://blog.scottlowe.org/2012/10/19/link-aggregation-and-lacp-with-open-vswitch/</a>
<br>
[3] - <a href="http://ryoogata.github.io/2015/02/20/openvswitch/">http://ryoogata.github.io/2015/02/20/openvswitch/</a>

<br>
[4] - <a href="http://qiita.com/STomohiko/items/ebbc2654e10bc62aed0d">http://qiita.com/STomohiko/items/ebbc2654e10bc62aed0d</a>
<br>
[5] - <a href="http://brezular.com/2011/12/04/openvswitch-playing-with-bonding-on-openvswitch/">http://brezular.com/2011/12/04/openvswitch-playing-with-bonding-on-openvswitch/</a>
<br>
[6] - <a href="https://www.youtube.com/watch?v=gziYnsvsCdQ">https://www.youtube.com/watch?v=gziYnsvsCdQ</a>
<br>
[7] - <a href="https://next.nutanix.com/t5/Nutanix-Connect-Blog/Network-Load-Balancing-with-Acropolis-Hypervisor/ba-p/6463">https://next.nutanix.com/t5/Nutanix-Connect-Blog/Network-Load-Balancing-with-Acropolis-Hypervisor/ba-p/6463</a>

</div>
