# Cài đặt OpenStack Mitaka 
# Mục lục
<h4><a href="#preparing">1. Chuẩn bị</a></h4>
<ul style="list-style: none">
<li><a href="#topo">1.1. Cấu hình cho VMware</a></li>
<li><a href="#info">1.2. Mô hình cài đặt</a></li>
<li><a href="#tools">1.3. Công cụ</a></li>
</ul>
<h4><a href="#result">2. Demo kết quả cài đặt</a></h4>
<ul style="list-style: none">
<li><a href="#demo">2.1. Hình ảnh demo OpenStack Mitaka</a></li>
<li><a href="#cloud">2.2. Topology cơ bản</a>
</li>
</ul>
<h4><a href="#ref">3. Tài liệu tham khảo</a></h4>

---

<h3><a name="preparing">1. Chuẩn bị</a></h3>
<ul style="list-style: none">
<li><h4><a name="topo">1.1. Cấu hình cho VMware</a></h4>
Hệ thống lab thực hiện trên VMware, trước hết cần có một số cấu hình như sau:
<ul>
<li>Tạo thêm dải mạng host-only trên VMware. Trong bài lab này là VMnet2: 10.10.10.0/24
</li>
<li>Chỉnh sửa lại dải địa chỉ NAT thành: 172.16.69.0/24
<br><br>
<img src="http://i.imgur.com/sARNoeS.png"/>
</li>
</ul>
</li>
<li><h4><a name="info">1.2. Mô hình cài đặt</a></h4>
Mô hình cài đặt ở đây là mô hình gồm 2 node: 1 node controller và 1 node compute. Cả hai đều cài đặt Ubuntu server 14.04. Thông tin chi tiết cấu hình cho 2 máy như sau:
<ul>
<li><b>Node Controller: </b>
<ul>
<li>Memory: 2.5 GB</li>
<li>CPU: 1 CPU - 2 cores</li>
<li>Storage: 60 GB</li>
<li>Network - 2 card mạng: eth0 (chế độ Host-only thuộc dải VMnet 2), eth1 (chế độ NAT) </li>
<li>OS: Ubuntu server 14.04</li>
</ul>
<br>
<img src="http://i.imgur.com/jOPhGX3.png"/>
<br>
<br>
</li>

<li><b>Node Compute:</b>
<ul>
<li>Memory: 1.5GB - 2GB</li>
<li>CPU: 1 CPU - 2 cores</li>
<li>Storage: 60 GB</li>
<li>Network - 2 card mạng: eth0 (chế độ Host-only thuộc dải VMnet 2), eth1 (chế độ NAT) </li>
<li>OS: Ubuntu server 14.04</li>
</ul>
<br>
<img src="http://i.imgur.com/BpwnMjP.png"/>
<br><br>
<b>Network layout:</b>
<br><br>
<img src="http://i.imgur.com/1BomODP.png"/>
<br><br>
</li>

</ul>
</li>
<li><h4><a name="tools">1.3. Công cụ</a></h4>
Các công cụ sử dụng trong bài lab:
<ul>
<li>VMware Workstation 12 (tùy chọn: virtualbox, ESX, Xen)</li>
<li>Cài đặt ssh client (Super Putty hoặc Mobaxterm)</li>
</ul>
</li>
</ul>
<h3><a name="#result">2. Demo kết quả cài đặt</a></h3>
<ul style="list-style: none">
<li><h4><a name="demo">2.1. Hình ảnh demo OpenStack Mitaka</a></h4>
<img src="http://i.imgur.com/zH3Eiix.png"/>
</li>
<li><h4><a name="cloud">2.2. Topology cơ bản</a></h4>
<ul>
<li>Tạo External network (provider) với subnet: 172.16.69.0/24 . IP Range: 172.16.69.183 - 172.16.69.193</li>
<li>Tạo Internal network (selfservice) với subnet: 192.168.10.0/24. IP Range: 192.168.10.10 - 192.168.10.20</li>
<li>Tạo router Radmin kết nối giữa External Network và Internal Network</li>
<li>Tạo một máy ảo cirros kết nối vào Internal network.</li>
</ul>
Hình ảnh demo có thể xem ở mục trên.
</li>
</ul>
<h3><a name="ref">3. Tài liệu tham khảo</a></h3>
<ul>
<li>Link hướng dẫn cài đặt (tiếng Việt): <a href="https://github.com/congto/OpenStack-Mitaka-Scripts/blob/master/DOCS-OPS-Mitaka/Caidat-OpenStack-Mitaka.md">Cài đặt OpenStack Mitaka tiếng Việt</a></li>
<li>Link hướng dẫn cài từ trang chủ: <a href="http://docs.openstack.org/mitaka/install-guide-ubuntu/">Cài đặt OpenStack Mitaka trên ubuntu 14.04 theo tài liệu trang chủ</a></li>
</ul>

