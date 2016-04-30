#Báo cáo OpenStack
##Mục Lục

##I.Tổng quan OpenStack
- 1.Khái niệm
OpenStack là một nền tảng điện toán đám mây mã nguồn mở tạo nên bởi nhiều dịch vụ và mỗi dich vụ thực hiện một chức năng nhưng chúng có mối liên hệ với nhau.

- 2.Dịch vụ

|Dịch vụ|Tên Project|Mô tả|
|-------|-----------|-----|
|Dashboard|Horizon|Tạo 1 giao diện trên web để sử dụng|
|Compute|Nova|Quản lý vòng đời máy ảo trên môi trường OpenStack bao gồm tạo, lập lịch, hủy máy ảo theo yêu cầu|
|Networking|Neutron|Cung cấp dịch mạng cho các dịch vụ khác OpenStack, cung cấp APIs để người dùng tạo ra và đưa vào dịch vụ và hỗ trợ nhiều loại mạng và công nghệ|
|Object Storage|Swift|Lưu trữ và lấy các đối tượng dữ liệu qua một RESTful,API gốc HTTP,tạo bản sao,theo kiểu phân tán, có khả năng chống chịu lỗi,có thể triển khai thành dịch vu độc lập|
|Block Storage|Cinder|Cung cấp các khối dữ liệu để chạy máy ảo.Cung cấp volume,khởi tạo máy từ volume,có plugin để kết nố,có thể sao lưu, mở rộng volume|
|Identity service|Keystone|Cung cấp sự xác nhận và dịc vụ xác nhận OpenStack. Cung cấp danh sách endpoints cho OpenStack|
|Imange Service|Glance|Lưu trữ và nhận image đĩa của máy ảo.Compute sử dụng khi cung cấp thực thể|
|Telemetry|Ceilometer||Giám sát và tính toán để tính tiền,và thông kê|
|Orchestratiom|Heat|Điều phối tài nguyên và ứng dụng bằng sử dụng HOT,triển khai dựa vào templates dựng sẵn,tự động tính toán tài nguyên, là stack tab Horizon|
|Database Service|Trove|Dịch vụ cơ sở dữ liệu, cung cấp database,tự backup đảm bảo an toàn|

- 3.Sơ đồ các projects
<ul>
<li>Sơ đồ quan hệ các projects</li>
<img src=https://dague.net/wp-content/uploads/2014/08/screenshot_185.png>
<li>Sơ đồ lớp cảu OpenStack</li>
<img src=https://dague.net/wp-content/uploads/2014/08/screenshot_184.png>
<li>Sơ đồ projects OpenStack theo Node</li>
<img src=http://docs.openstack.org/icehouse/install-guide/install/apt-debian/content/figures/1/figures/installguide_arch-neutron.png>
</ul>

##II.Keystone - Dịch vụ xác thực
- Định nghĩa: 
<ul>
<li>là dịch vụ theo dõi người dùng và quyền truy cập</li>
<li>Cung cấp danh sách endpoints vơi APTs endpoints</li>
</ul>
- Bản chất: cung cấp chức năng xác thực và ủy quyền cho môi trường khác nhau của OpenStack. Người dùng cung cấp ủy nhiệm cho Keystone và dựa vào kết quả xác thực chỉ định quyền hạn thông qua thẻ tới người dùng
Quyền hạn chỉ định rõ quyền hoặc đặc quyền thực hiện các công việc trong OpenStack.
- Người dùng: cá nhân,dịch vụ(Nova,Cinder,...),endpoints

Dự án,nhóm tổ chức được gộp lại thành tenant.

Keystone chỉ định quyền hạn tới người dùng. người dùng có nhiều quyền hạn trong các tenant khác nhau.

- Sơ đồ hoạt động Keystone
<img src=https://senecacd.files.wordpress.com/2012/11/identity-diagram.png>
 
 - Dịch vụ Keystone
 <ul>
 <li>Identity</li>
 <ul>
 <li>Dịch vụ nhận dạng cung cấp xác nhận dữ liệu về người dùng,nhóm, tên miền, vai trò hay bất kì dữ liệu liên quan.</li>
 <li>Trong mọi trường hợp dữ liệu được quản lý bởi dịch vụ,cho phép dịch vụ quản lý tất cả CRUD kết hợp với dữ liệu</li>
 <li>Mặt khác, dữ liệu được kéo lên theo mức độ khác nhau bởi dịch vụ phụ trợ có thẩm quyền</li>
 </ul>
 <li>Token: Dịch vụ  quản lý xác nhận mã thông báo dùng cho chứng thực yêu cầu mỗi khi thông tin người dùng đã được xác minh </li>
<li>Catalog: Tạo các endpoints và quản lý </li>
<li>Policy:dịch vụ ủy quyền cung cấp cơ chế ủy quyền và quản lý no</li>
<ul>
<li>Key Value Store: là giao diện tra cứu các khóa </li>
<li>Memcached:cung cấp bộ nhớ đệm</li>
<li>SQL:lưu trữ dữ liệu</li>
<li>LDAP:kết nối thông qua LDPA tới các thư mục ở cơ sở dữ liệu</li>
</ul>
</ul>

##III.Nova-Dịch vụ tính toán

- Nova là modun quản lý máy ảo trong hạ tầng OpenStack bằng cách trở thành tầng ảo có giao diện hỗ trợ ảo hóa

- Hỗ tr công nghệ ảo hóa như KVM,ESXi,Hyper-V

- Chia làm 3 nhóm
<ul>
<li> Nhóm A: Trình điều khiển hỗ trợ đầy đủ. Đảm bảo thử nghiệm :</li>
<ul>
<li>Kiểm tra, thử nghiệm cổng vào</li>
<li>Trình điều khiển có: libvirt (qemu/KVM trên x86)</li>
</ul>
<li> Nhóm B</li>
<ul>
<li>Kiểm tra cổng vào</li>
<li>Kiểm tra chức năng hệ thông mà cổng không xác nhận nhưng gợi ý  kết quả trong gerit</li>
<li>Trình điều khiển:Hyper-V,Vmware,XenServer6.2</li>
</ul>
<li>Nhóm C</li>
<ul>
<li>Trình điều khiien thiết lập chế độ tối thiểu và có thể không hoạt động bất cứ lúc nào</li>
<li>Bao gồm:baremetal, docker, Xen via libvirt, LXC via libvirt </li>
</ul>
       

 
