# VLAN với OpenvSwitch
# Mục lục
<ul>
<li><h3><a href="#topo">1. Topology</a></h3></li>
<li><h3><a href="#config">2. Cài đặt và cấu hình VLAN</a></h3>
<ul>
<li><h4><a href="#required">2.1. Cài các gói phụ thuộc và phần mềm cần thiết</a></h4></li>
<li><h4><a href="#cfg">2.2. Cấu hình VLAN</a></h4></li>
</ul>
</li>
<li><h3><a href="#ref">3. Tham khảo</a></h3></li>
</ul>

---

<ul>
<li><h2><a name="topo">1. Topology</a></h2>
<img src="http://i.imgur.com/3O5ci4L.jpg"/>
<br><br>
Chuẩn bị:
<ul>
<li>Máy vật lý: cài ubuntu 14.04, kvm, openvswitch. Có thể tham khảo cách cài openvswitch <a href="#">tại đây</a></li>
<li>Sử dụng OpenvSwitch tạo 2 switch ảo br-ex, br-ex1 kết nối với nhau bằng một đường trunk, thiết lập các vlan tag 100 và 200</li>
<li>Tạo 4 máy ảo gán vào các vlan tương ứng với các tab interface của 2 switch ảo trên:
<ul>
<li><b>kvm-th0</b> và <b>kvm-th1</b>: gán vào switch <b>br-ex</b></li>
<li><b>kvm-u0</b> và <b>kvm-u1</b>: gàn vào switch <b>br-ex1</b></li>
<li>Gán các máy ảo vào các vlan: <b>kvm-th0</b> và <b>kvm-u0</b> gán vào vlan 100, <b>kvm-th1</b> và <b>kvm-u1</b> gán vào vlan 200.</li>

</ul>
</li>

<li>Tiến hành ping giữa các máy ảo kiểm tra hoạt động của vlan.</li>
</ul>
</li>

<li><h2><a name="config">2. Cài đặt và cấu hình VLAN</a></h2>
<ul>
<li><h3><a name="required">2.1. Cài các gói phụ thuộc và phần mềm cần thiết</a></h3>
Chuẩn bị cài đặt các gói phần mềm phụ thuộc sau:
<ul>
<li><b>KVM:</b> tham khảo cách cài trên ubuntu 14.04 theo hướng dẫn của <a href="https://www.howtoforge.com/tutorial/kvm-on-ubuntu-14.04/">howtoforge</a>.</li>
<li><b>OpenvSwitch:</b> tham khảo cách cài <a href="#">tại đây</a>.</li>
</ul>
</li>

<li><h3><a name="cfg">2.2. Cấu hình VLAN</a></h3>
<h4>Tạo các switch ảo và cấu hình vlan tag</h4>
<ul>
<li>a. Tạo switch ảo:
<pre>
<code>
ovs-vsctl add-br br-ex
ovs-vsctl add-br br-ex1
</code>
</pre>
</li>
<li>b. Tạo các tap interface và gắn vlan tag (các máy ảo được coi như các access port trên các vlan):
<pre>
<code>
# tab interfaces on br-ex
ovs-vsctl add-port br-ex tap0 tag=100
ovs-vsctl add-port br-ex tap1 tag=200
# tab interfaces on br-ex1
ovs-vsctl add-port br-ex1 tap2 tag=100
ovs-vsctl add-port br-ex1 tap3 tag=200
</code>
</pre>
</li>
<li>c. Tạo các trunk port trên các switch ảo và tạo đường trunk kết nối hai switch:
<pre>
<code>
# create trunk ports on switches
ovs-vsctl add-port br-ex trk
ovs-vsctl add-port br-ex1 trk1
# combine 2 switches
ovs-vsctl set interface trk type=patch options:peer=trk1
ovs-vsctl set interface trk1 type=patch options:peer=trk
</code>
</pre>
</li>
<li>d. Kiểm tra lại cấu hình các switch:
<pre>
<code>
ovs-vsctl show
</code>
</pre>
Kết quả sẽ tương tự như sau:
<pre>
<code>
Bridge "br-ex1"
    Port "br-ex1"
        Interface "br-ex1"
            type: internal
    Port "trk1"
        Interface "trk1"
            type: patch
            options: {peer=trk}
    Port "tap2"
        tag: 100
        Interface "tap2"
    Port "tap3"
        tag: 200
        Interface "tap3"
Bridge br-ex
    Port br-ex
        Interface br-ex
            type: internal
    Port "tap1"
        tag: 200
        Interface "tap1"
    Port "eth1"
        Interface "eth1"
    Port "tap0"
        tag: 100
        Interface "tap0"
    Port trk
        Interface trk
            type: patch
            options: {peer="trk1"}
ovs_version: "2.0.2"
</code>
</pre>
</li>
</ul>
</li>

</ul>

<h4>Tạo network cho các máy ảo kết hợp OpenvSwitch với libvirt</h4>
Để khai báo network mới với libvirt, ta tạo một file định dạng <i>*.xml</i> và sử dụng công cụ <b>virsh</b> (thường cài đặt cùng với kvm-qemu) để áp dụng cấu hình trong file đó.
Ở đây, ta khai báo 2 file xml cấu hình 2 network tương ứng với hai switch ảo ở trên:
<ul>
<li>Cấu hình network tương ứng br-ex: <code>vi ovs-vlan.xml</code>
<pre>
<code>
&lt;network&gt;
  &lt;name&gt;ovs-network&lt;/name&gt;
  &lt;forward mode='bridge'/&gt;
  &lt;bridge name='br-ex'/&gt;
  &lt;virtualport type='openvswitch'/&gt;
  &lt;portgroup name='vlan-00' default='yes'&gt;
  &lt;/portgroup&gt;
  &lt;portgroup name='vlan-100'&gt;
    &lt;vlan&gt;
      &lt;tag id='100'/&gt;
    &lt;/vlan&gt;
  &lt;/portgroup&gt;
  &lt;portgroup name='vlan-200'&gt;
    &lt;vlan&gt;
      &lt;tag id='200'/&gt;
    &lt;/vlan&gt;
  &lt;/portgroup&gt;
  &lt;portgroup name='vlan-all'&gt;
    &lt;vlan trunk='yes'&gt;
      &lt;tag id='100'/&gt;
      &lt;tag id='200'/&gt;
    &lt;/vlan&gt;
  &lt;/portgroup&gt;
&lt;/network&gt;
</code>
</pre>

</li>

<li>Cấu hình network tương ứng với br-ex1: <code>vi ovs-vlan_br-ex1.xml</code>
<pre>
<code>
&lt;network&gt;
  &lt;name&gt;ovs-network-1&lt;/name&gt;
  &lt;forward mode='bridge'/&gt;
  &lt;bridge name='br-ex1'/&gt;
  &lt;virtualport type='openvswitch'/&gt;
  &lt;portgroup name='vlan-00' default='yes'&gt;
  &lt;/portgroup&gt;
  &lt;portgroup name='vlan-100'&gt;
    &lt;vlan&gt;
      &lt;tag id='100'/&gt;
    &lt;/vlan&gt;
  &lt;/portgroup&gt;
  &lt;portgroup name='vlan-200'&gt;
    &lt;vlan&gt;
      &lt;tag id='200'/&gt;
    &lt;/vlan&gt;
  &lt;/portgroup&gt;
  &lt;portgroup name='vlan-all'&gt;
    &lt;vlan trunk='yes'&gt;
      &lt;tag id='100'/&gt;
      &lt;tag id='200'/&gt;
    &lt;/vlan&gt;
  &lt;/portgroup&gt;
&lt;/network&gt;
</code>
</pre>

</li>

<li>Áp dụng cấu hình network mới:

<pre>
<code>
# define new networks
virsh net-define ovs-vlan.xml
virsh net-define ovs-vlan_br-ex1.xml

# start new networks
virsh net-start ovs-network
virsh net-start ovs-network-1

# auto start networks when turning on
virsh net-autostart ovs-network
virsh net-autostart ovs-network-1
</code>
</pre>


</li>
</ul>
<h4>Tạo các máy ảo và thiết lập network cho các máy ảo</h4>
Tạo 4 máy ảo và thực hiện cấu hình network cho 4 máy ảo sử dụng công cụ <b>virsh</b>. Ví dụ ở đây ta cấu hình network cho máy ảo kvm-th0 theo topo. Cấu hình các máy ảo thiết lập trong 1 file <i>*.xml</i> nằm trong thư mục <code>/etc/libvirt/qemu/</code>. Để chỉnh sửa cấu hình một máy ảo, ta sử dụng lệnh:
<pre>
<code>
# virsh edit vm_name
virsh edit kvm-th0
</code>
</pre>
 Thiết lập cho máy ảo này thuộc vlan-100 và gán vào switch br-ex (tương ứng với ovs-network). Ta chỉnh sửa section <interface> như sau:
<pre>
<code>
&lt;interface type='network'&gt;
  &lt;mac address='52:54:00:10:aa:1c'/&gt;
  &lt;source network='ovs-network' portgroup='vlan-100'/&gt;
  &lt;model type='virtio'/&gt;
  &lt;address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/&gt;
&lt;/interface&gt;
</code>
</pre>
Tiến hành cấu hình tương tự cho các máy ảo khác theo đúng topology.

<h4>Kiểm tra kết nối các máy tính trên các vlan</h4>
<div>
<ul>
<li>Cấu hình ip tĩnh cho các máy ảo như topology.</li>
<li>Tiến hành ping giữa các máy trong cùng vlan: kvm-th0 với kvm-u0(vlan-100), kvm-th1 với kvm-u1 (vlan-200). Kết quả ping thành công.
</li>
<li>Tiến hành ping giữa các máy khác vlan: kvm-th0 với kvm-th1 hoặc kvm-u1 (cũng có thể kiểm tra ping kvm-u0 với kvm-th1 hoặc kvm-u1). Kết quả ping không thành công.</li>
<li>Demo:
<ul>
<li>ping giữa hai máy cùng vlan <b>vlan-100</b> là kvm-th0 và kvm-u0
<br><br>
<img src="http://i.imgur.com/m4WcRQd.png"/>
<br><br>
</li>
<li>ping giữa hai máy khác vlan kvm-th0 và kvm-u1
<br><br>
<img src="http://i.imgur.com/r61hw9x.png"/>
<br><br>
</li>
</ul>
</li>
</ul>
</div>
</li>

<li><h2><a name="ref">3. Tham khảo</a></h2>
[1] - <a href="http://openvswitch.org/support/config-cookbooks/vlan-configuration-cookbook/">http://openvswitch.org/support/config-cookbooks/vlan-configuration-cookbook/</a>
<br>
[2] - <a href="http://blog.scottlowe.org/2012/11/07/using-vlans-with-ovs-and-libvirt/">http://blog.scottlowe.org/2012/11/07/using-vlans-with-ovs-and-libvirt/</a>
<br>
[3] - <a href="http://blog.scottlowe.org/2013/05/28/vlan-trunking-to-guest-domains-with-open-vswitch/">http://blog.scottlowe.org/2013/05/28/vlan-trunking-to-guest-domains-with-open-vswitch/</a>
</li>
</ul>
