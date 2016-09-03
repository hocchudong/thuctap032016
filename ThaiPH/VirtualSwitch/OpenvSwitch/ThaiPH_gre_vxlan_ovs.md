# Lab cấu hình GRE, VXLAN sử dụng OpenvSwitch
# Mục lục
<h3><a href="#gre">1. GRE</a></h3>
<ul>
    <li><a href="#gtopo">1.1. Topology</a></li>
    <li><a href="#gcfg">1.2. Cấu hình</a></li>
    <li><a href="#gw">1.3. Phân tích trên wireshark</a></li>
</ul>
<h3><a href="#vxlan">2. VXLAN</a></h3>
<ul>
    <li><a href="#vxtopo">2.1. Topology</a></li>
    <li><a href="#vxcfg">2.2. Cấu hình</a></li>
    <li><a href="#vxw">2.3. Phân tích trên wireshark</a></li>
</ul>
<h3><a href="#ref">3. Tham khảo</a></h3>

---

<h2><a name="gre">1. GRE</a></h2>
<ul>
    <li><h3><a name="gtopo">1.1. Topology</a></h3>
<br><br>
    <img src="http://i.imgur.com/vAuSNqm.png">
    <br><br>
    Yêu cầu 2 host:
    <ul>
        <li>Chạy ubuntu desktop 14.04</li>
        <li>Cài sẵn KVM, virt-manager, OpenvSwitch</li>
    </ul>
    </li>

    <li><h3><a name="gcfg">1.2. Cấu hình</a></h3>
    <div>
    <i>
        <b>Chú ý: </b>
        <ul>
            <li>HOST 0: eth1 - 10.10.10.105/24</li>
            <li>HOST 1: eth1 - 10.10.10.106/24</li>
        </ul>
    </i>

        <h4>Trên HOST 0: </h4>
        <div>
            Cấu hình hai bridge <b>br0</b> - kết nối với các VM, và tạo kết nối tunnel sử dụng GRE tunnel interface và <b>br1</b> - tunnel endpoint kết nối với card eth1. Thực chất không cần sử dụng một tunnel endpoint tách biệt như vậy. Tuy nhiên trong thực tế, việc này cho phép tách biệt quản lý lưu lượng của hypervisor và quản lý lưu lượng GRE, cho phép sử dụng mạng quản lý bên ngoài.
<pre>
    <code>
# cau hinh br1 lam tunnel endpoint
sudo ovs-vsctl add-br br1
sudo ovs-vsctl add-port br1 eth1
sudo ifconfig eth1 0
sudo ifconfig br1 10.10.10.105/24

# cau hinh br0 và gre tunnel interface
sudo ovs-vsctl add-br br0
sudo ifconfig br0 10.1.1.1/24
sudo ovs-vsctl add-port br0 gre0 -- set interface gre0 type=gre options:remote_ip=10.10.10.106
    </code>
</pre> 
        </div>

        <h4>Trên HOST 1: </h4>
        <div>
            Cấu hình tương tự:
<pre>
    <code>
sudo ovs-vsctl add-br br1
sudo ovs-vsctl add-port br1 eth1
sudo ifconfig eth1 0
sudo ifconfig br1 10.10.10.106/24

sudo ovs-vsctl add-br br0
sudo ifconfig br0 10.1.1.2/24
sudo ovs-vsctl add-port br0 gre0 -- set interface gre0 type=gre options:remote_ip=10.10.10.105
    </code>
</pre>
        </div>

        <h4>Cấu hình chung trên hai host: </h4>
        <div>
            Tạo một libvirt network tương ứng với bridge <b>br0</b> để kết nối các máy ảo vào. Cấu hình file <code>vi ovs-gre.xml</code> định nghĩa ovs-gre network như sau:
<pre>
    <code>
&lt;network&gt;
  &lt;name&gt;ovs-gre&lt;/name&gt;
  &lt;forward mode='bridge'/&gt;
  &lt;bridge name='br0'/&gt;
  &lt;virtualport type='openvswitch'/&gt;
&lt;/network&gt;
    </code>
</pre>
            Lưu lại file và áp dụng cấu hình tạo libvirt network mới:
<pre>
    <code>
virsh net-define ovs-gre.xml
virsh net-start ovs-gre
virsh net-autostart ovs-gre
    </code>
</pre>
        </div>

        <h4>Kiểm tra kết nối</h4>
        <div>
            Trên HOST 0 tạo máy ảo <code>cirros0</code>, trên HOST 1 tạo náy ảo <code>cirros 1</code> và cấu hình địa chỉ tĩnh cho các máy này (dải 10.1.1.0/24). Tiến hành ping thử giữa hai máy và sử dụng wireshark trên host lắng nghe các bản tin này trên interface <b>eth1</b>. Kết quả ping thành công như sau:
            <br><br>
            <img src="http://i.imgur.com/b75By0d.png">
            <br><br>
        </div>

    </div>
    </li>

    <li><h3><a name="gw">1.3. Phân tích trên wireshark</a></h3>
    Phân tích một gói tin ICMP bắt được trên interface eth1:
    <br><br>
    <img src="http://i.imgur.com/QX3YGbD.png">
    <br><br>
    Có thể thấy rằng layer 2 frame (chứa thông tin ICMP/IP giữa hai host <code>10.1.1.20</code> và <code>10.1.1.21</code>) được đóng gói hoàn toàn trong bản tin GRE/IP của các địa chỉ ngoài <code>10.10.10.105</code> và <code>10.10.10.106</code>.   
    </li>
</ul>
<h2><a name="vxlan">2. VXLAN</a></h2>
<ul>
    <li><h3><a name="vxtopo">2.1. Topology</a></h3>
    Vẫn sử dụng topology như trên nhưng thay thế bridge <b>br0</b> dành cho kết nối GRE bằng bridge <b>br-vxl</b> cho kết nối VXLAN, thay GRE port <b>gre0</b> bằng VXLAN port <b>vxl0</b> tương ứng. Cấu hình chi tiết như bên dưới.
    </li>
    <li><h3><a name="vxcfg">2.2. Cấu hình</a></h3>
    Cấu hình tương tự như với GRE, tiến hành tạo thêm 1 bridge <b>br-vxl</b> - kết nối với các VM, và tạo kết nối tunnel sử dụng VXLAN tunnel interface.
    <h4>Trên HOST 0</h4>
    <div>
        Cấu hình bridge <b>br-vxl</b> cho các VM sử dụng dải mạng <code>172.16.1.0/24</code>. Tạo thêm 1 VXLAN port - <b>vxl0</b> để tạo đường hầm kết nối theo giao thức VXLAN:
<pre>
    <code>
ovs-vsctl add-br br-vxl
ifconfig br-vxl 172.16.1.20/24
ovs-vsctl add-port br-vxl vxl0 -- set interface vxl0 type=vxlan options:remote_ip=10.10.10.106
    </code>
</pre>
    </div>

    <h4>Trên HOST 1</h4>
    <div>
       Cấu hình tương tự HOST 0;
<pre>
    <code>
ovs-vsctl add-br br-vxl
ifconfig br-vxl 172.16.1.21/24
ovs-vsctl add-port br-vxl vxl0 -- set interface vxl0 type=vxlan options:remote_ip=10.10.10.105
    </code>
</pre>
    </div>

    <h4>Cấu hình chung trên hai host</h4>
    <div>
        Tạo libvirt network tương ứng với bridge <b>br-vxl</b> để các máy ảo kết nối vào: <code>vi ovs-vxlan.xml</code>:
<pre>
    <code>
&lt;network&gt;
  &lt;name&gt;ovs-vxl&lt;/name&gt;
  &lt;forward mode='bridge'/&gt;
  &lt;bridge name='br-vxl'/&gt;
  &lt;virtualport type='openvswitch'/&gt;
&lt;/network&gt;
    </code>
</pre>
        Lưu lại file cấu hình. Áp dụng cấu hình tạo network mới:
<pre>
    <code>
virsh net-define ovs-vxlan.xml
virsh net-start ovs-vxl
virsh net-autostart ovs-vxl
    </code>
</pre>
    </div>

        <h4>Kiểm tra kết nối</h4>
        <div>
            Vẫn sử dụng hai máy ảo cirros như bài lab với GRE, tuy nhiên lựa chọn network là <b>ovs-vxl</b> vừa mới cấu hình. Sau đó đặt địa chỉ tĩnh cho các máy này trong dải <b>172.16.1.0/24</b>. Tiến hành ping thử giữa hai máy và sử dụng wireshark trên host lắng nghe các bản tin này trên interface <b>eth1</b>. Kết quả ping thành công như sau:
            <br><br>
            <img src="http://i.imgur.com/LKAT6QE.png">
            <br><br>
        </div>


    </li>
    <li><h3><a name="vxw">2.3. Phân tích trên wireshark</a></h3>
    Phân tích một gói tin ICMP bắt được trên interface eth1:
    <br><br>
    <img src="http://i.imgur.com/yzQmGi9.png">
    <br><br>
    Ở trong bản tin ICMP đem phân tích ở trên, có thể thấy xuất hiện VXLAN ID với số hiệu - VXLAN Network Identifier (VNI) = 0.
    </li>
</ul>
<h2><a name="ref">3. Tham khảo</a></h2>
<div>
    [1] - <a href="http://costiser.ro/2016/07/07/overlay-tunneling-with-openvswitch-gre-vxlan-geneve-greoipsec/#.V8f_pKJquPW">http://costiser.ro/2016/07/07/overlay-tunneling-with-openvswitch-gre-vxlan-geneve-greoipsec/#.V8f_pKJquPW</a>
    <br>
    [2] - <a href="http://blog.scottlowe.org/2013/05/07/using-gre-tunnels-with-open-vswitch/">http://blog.scottlowe.org/2013/05/07/using-gre-tunnels-with-open-vswitch/</a>
</div>