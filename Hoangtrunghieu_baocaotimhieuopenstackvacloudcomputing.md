#Báo cáo tìm hiểu Cloud Computing và Open Stack
##Mục lục
[I.Tổng quan về ảo hóa](#aohoa)

- [1.Khái niệm](#khainiem)

- [2.So sánh trước và sau ảo hóa](#sosanh)

- [3.Ưu điểm công nghệ ảo hóa](#uudiem)

- [4.Phân loại công nghệ ảo hóa](#phanloai)

- [5.Hường tiếp cận công nghệ ảo hóa](#huong)

[II.Cloud Computing](#cloud)

- [1.Định nghĩa](#dn)

- [2.5 Yếu tố](#yeuto)

- [3.4 mô hình](#mohinh)

- [4.3 dịch vụ](#dichvu)

[III.OpenStack](#stack)

- [1.Khái niệm](#knstack)

- [2.Đặc điểm](#dacdiem)

- [3.Kiến trúc](#kientruc)

- [4.Vai trò từng project](#project)

<a name="aohoa"></a>
###I.Ảo hóa(Virtualization)
<a name="khainiem"></a>
####1.Khái niệm
- `Virtualization`(Ảo hóa) ra đời những năm 196x đề cập đến hành động phiên bảo `Virtual`(Ảo)của một cái gì đó 
bao gồm cả các máy tính ảo với nền tảng phần cứng, hệ ddieuf hành, thiết bị lưu trữ hoặc cả một tập tài nguyên về mạng máy tính,.. nhưng không bị hạn chế
(nguồn wiki)
<a name="sosanh"></a>
#####2.So sánh trước sau ảo hóa
|Trước ảo hóa|Sau ảo hóa|
|------------|----------|
|- Một hệ điều hành trên 1 máy|- Phần cứng độc lập với hệ điều hành và phần mềm|
|- Phần mềm và phần cứng gắn chặt nhăt|- Các máy ảo có thể được cung ứng từ mọi hệ thống|
|- Hạ tầng không linh hoạt, tốn kém,dễ xảy ra xung đột khi chạy nhiều ứng dụng trên cùng máy ảo|- Có thể quản lý hệ điều hành va ứng dụng như một đơn vị duy nhất biowr vì chúng được đóng gói vào một máy ảo|
<a name="uudiem"></a>
#####3.Ưu điểm của `Virtualization`
<ul>
<li>Giảm thiểu chi phí bảo dưỡng</li>
<li>Tương thích với nhiều ứng dụng và hệ điều hành đòng thời</li>
<li>Tập trung cho kiểm soát và quản trị/li>
<li>Dễ dàng sao lưu và khôi phục</li>
<li>Khai thác nhiều hơn nữa về công suất hoạt động của phần cứng</li>
<li>Live Migration-"Chuyển đổi máy ảo kể cả khi đang hoạt đông"</li>
<li>Nâng cao độ sẵn sàng cho hệ thông</li>
</ul>

<a name="phanloai"></a>
#####4.Phân loại công nghệ ảo hóa
- Full `Virtualization`:
<ul>
<li>Open source:KVM, VirtualBox, KQEMU</li>
<li>Commercial:VMware,MS Hyper-VMware</li>
</ul>
- Para `Virtualization`: Xen,VMWare
- OS-Level `Virtualization`: OpenVc, Linux-VServer, Docker

<a name="huong"></a>
#####5.Hướng tiếp cận ảo hóa
- Host Architecture:
<ul>
<li>Được cài đặt và chạy như một ứng dụng</li>
<li>Dự vào một hệ điều hành của máy vật lý đẻ quanr lý tài nguyên và hỗ trợ thiết bị</li>
</ul>
- Bare-Metal(Hypervisor) Architecture
<li>Ảo hóa từ lõi-trong kernel</li>
<li>Cài đặt trực tiếp lên phần cứng</li>
</ul>

<a name="cloud"></a>
####II.Cloud Computing
<a name="dn"></a>
#####1.Định nghĩa
>Cloud computing is a model for enabling ubiquitous
, convenient, on-demand network access to a shared pool of 
configurable computing resources (e.g., networks, servers, storage, 
applications, and services) that can be rapidly provisioned and 
released with minimal management effort or service provider interaction. 
This cloud model is composed of five essential characteristics, three 
service models, and four deployment models.<The NIST Definition of Cloud Computing>

>Điện toán đám may là mô hình phổ biến,thuân tiện, cho phép người dùng chủ động kết nối tới một số lượng 
tài nguyên máy tính(mạng,máy chủ,bộ nhớ,ứng dụng và dịch vụ)có thể được cung cấp nhanh chóng với sự kiểm soát nhỏ nhất
hay sự tương tác với nhà cung cấp. Mô hình đám mây là sự hợp thành của 5 yếu tố,3 mô hình dịch vụ, 4 mô hình triển khai.
<a name="yeuto"></a>
#####2. 5 yếu tố 
<ul>
<li>On-demand self-service(tự phục vụ theo yêu cầu): người sử dụng có thể đơn phương chủ động khởi tạo, tạm dừng dịch vụ,.. </li>
<li>Broad network access(mạng lưới kết nối rộng lớn): người dùng có thể truy cập trên mọi nền tảng thiết bị, hạ tầng mạng và khu vực địa lý</li>
<li>Resource pooling(tổng hợp tài nguyên):gộp tài nguyên vật lý sau đó phân bỏ tự động cho người dùng</li>
<li>Rapid elasticcity(đàn hồi nhanh):Cấp phát thu hồi tài nguyên nhanh chóng, cân bằng tỉ lệ tài nguyên ra, vào với yêu cầu </li>
<li>Mearsured service(Tính toán dịch vụ):đo lường kiểm soát thời gian sử dụng, tính toán chi phí, mức độ sử dụng</li>
</ul>
<a name="mohinh"></a>
#####3. 4 mô hình:
<ul>
<img src=http://imgur.com/VRExyoz.png>
<li>Private Cloud:hạ tầng cung cấp độc quyền cho một tổ chức bao gồm nhiều người dùng(doanh nhân,..) có thể sở hữu, quản lý,vận hành bởi tổ chức, bên thứ 3 hoặc kết hợp của 2 yếu tố trên
Được cung cấp cho nội bộ tổ chức, ít nhu cầu bảo mật và tính pháp lý hơn Public Cloud</li>
<img src=http://imgur.com/Na6vAYg.png>
<li>Community Cloud:hạ tầng được cung cấp độc quyền sử dụng bởi một tổ chức người dùng  có chung mối quan tâm(nhiệm vụ,bảo mật,..)có thể sở hữu, quản lý, vận hành bởi 1 hoặc nhiều tổ chức trong cộng đồng,.. kể cả khi có hoặc không có quyền
.Dịch vụ cung cấp cho khách hàng qua internet</li>
<img src=http://imgur.com/5hEgahf.png>
<li>Public Cloud: hạ tầng cung cấp mở cho mọi người,sở hữu quản lý vận hành bởi doanh nghiệp,học viện,...và nó tồn tại bởi nhà các nhà cung cấp dịch vụ</li>
<img src=http://imgur.com/Na6vAYg.png>
<li>Hybrid Cloud:là sự kết hợp hạ tầng của nhiều hạ tầng điện toán đám mây( private,community,public) mà vẫn duy trì các đặc tính riêng biệt nhưng được giới hạn bởi một công nghệ tiêu chuẩn có thể cho phép dữ liệu và ứng dụng di chuyển </li>
</ul>
<a name="dichvu"></a>
#####4. 3 mô hình dịch vụ:
<ul>
<li>Sofware as a Service(SaaS): Khả năng cung cấp cho người tiêu dùng là sử dụng các ứng dụng của nhà cung cấp chạy trên một cơ sở hạ tầng điện toán đám mây.Ứng dụng được truy cập qua các thiết bị khác nhau qua một client nhỏ như trình duyệt,...
Người dùng không quản lý hay điều khiển hạ tầng bao gồm mạng, máy chủ,, hệ điều hành,.. với những ngoại lệ mà người dùng có thể chỉnh sửa thiết lập </li>
<li>Platform as a Service(PaaS):Cung cấp cho khách triển khai hạ tầng điện toán đám mây được tạo ra hoặc mua ứng dụng ,thư viện, công cụ cung cấp bởi  nhà cung cấp. Người sử dụng không quản lý ,điều khiển hạ tầng nhưng có thể điều khiển ứng dụng và chỉnh sửa thiết lập cho ứng dụng lưu trữ môi trường</li>
<li>Infasture as a Service(IaaS): Cung cấp cho người dùng khả năng xử lý , lư trữ,mạng, và các thao tác với tài nguyên máy tính ,nơi mà người dùng có thể triển khai và chạy phần mềm tùy ý, bao gồm cả hệ điều hành và ứng dụng. người dùng không quản lý, điều khiển hạ tầng điện toán nhưng điều khienr hệ điều hành, bộ nhớ, triển khai phần mềm trong giới hạn cho phép </li>

<li> 3 mô hình dịch vụ từ các góc nhìn:</li>
<ul>
<li>Từ người quản trị</li>
<img src=http://imgur.com/frDPtOO.png>
<li> Từ phí người dùng</li>
<img src=http://imgur.com/y2VGKgq.png>
</ul>
<li> Uu và nhược điểm:</li>
<img src=http://imgur.com/Cwr3b21.png>
</ul>

<a name="stack"></a>
####III.OpenStack
<a name="knstack"></a>
#####1.Khái niệm

Là nền tảng mã nguồn mở sử dụng để xây dựng mô hình private và public cloud.
<a name="dacdiem"></a>
#####2.Đặc điểm

- Thiết kế theo module

- "Mở" về thiêt kế, công động, phát triển, mã nguồn

- 6 tháng lại ra phiên bản mới

- 99.99% là mã python 2.x

- Tên đánh theo A,B,.. tối đa 10 kí tự là danh từ

- Tên- mã dự án: Computer-Nova, Network_NEUTRON
<a name="kientruc"></a>
#####3.Kiến trúc

- Mức ý niệm
<img src=http://imgur.com/EUv4t70.png>

- Mức logic
<img src=http://imgur.com/E24U4uy.png>

<img src=http://imgur.com/T6c4JP8.png>

- Kiến thiết theo từng module

-Có thể lựa chọn module để triển khai

-Có thể tích hợp khác với từng project

-Các dịch vụ mở rộng theo chiều ngang

-Các project đều có APIs mở
<a name="project"></a>
######4. Vai trò từng project

- OpenStack Dashboard - Horizon
<ul>
<li>Cung cấp giao diện cho người dùng - tương tác OpenStack</li>
<li>Tương tác APIs của dịch vụ</li>
<li>Không đủ chức năng điều khiển OpenStack</li>
</ul>
<img src=http://imgur.com/eLR10I3.png>

- OpenStack Identity - Keystone
<ul>
<li>Dịch vụ xác thực và ủy quyền trong OpenStack</li>
<li>Quản lý, tạo, sửa,...tài khoản ,nhòm người dùng </li>
<li>Hỗ trợ kết hợp với LDAP,PAM,SQL</li>
</ul>
<img src=http://imgur.com/MR55Ef1.png>

- OpenStack Compute - Nova
<ul>
<li>Lập lịch cho máy ảo. Tạo sửa máy ảo</li>
<li>Trước có nova network, nova volume nhưng giờ đã bỏ</li>
<li>Quản lý vòng đời máy ảo từ lúc tạo ra đến lúc xóa đi</li>
<li>Tương tác EC2(dịch vụ cung cấp máy ảo) của AWS</li>
<li>Hỗ trợ nhiều Hypervisor:KM,VMWare,...</li>
<li>Hỗ trọ nhiều backend storage:iSCSl,SAN,...</li>
</ul>
<img src=http://imgur.com/LtdhQAG.png>

- OpenStack Image Service - Glance
<ul>
<li>Lưu trữ, truy vấn các disk image</li>
<li>Hỗ trợ các Hypervisor</li>
<li>Làm việc các Storage backend:Swift, Filesystem,..</li>
</ul>
<img src=http://imgur.com/LtdhQAG.png>

- OpenStack Object Storage - Swift
<ul>
<li>Đọc ghi đối tương(file) qua HTTP</li>
<li>Tương tự dịch vụ S3(Simple Storage Service) của AWS(dịch vụ luwu trữ file)</li>
<li>Dữ liệu có khả năng tạo bản sao</li>
<li>Theo kiểu phân tán, có khả năng chống chịu lỗi và nhất quán</li>
<li>Có thể triển khai độc lập về lưu trữ(swiftstack.com)</li>
</ul>
<img src=http://imgur.com/eiydVL9.png>

- OpenStack Network - Neutron
<ul>
<li>Từng có tên là Quantum</li>
<li>Cung caaos dịch vụ mạng trong OpenStack</li>
<li>Thay thế nova-network hướng tới SDN trong OpenStack</li>
<li>Có nhiều dịch vụ cao cấp:FWaaS,LBaaS,VPNaaS</li>
<li>Có cơ chế Plugin để làm việc với các hãng và giải pháp về network khác</li>
</ul>
<img src=http://imgur.com/wucci1k.png>

- OpenStack Block Storage - Cinder
<ul>
<li>Thay thế nova-volume,cấp các "block storage" gắn vào máy ảo</li>
<li>Cung cấp volume gắn vào máy ảo</li>
<li>Khởi tạo các máy từ Volume</li>
<li>Có plugin để kết nồi với Storage các hãng</li>
<li>Có thể sao lưu mở rộng volume</li>
</ul>
<img src=http://imgur.com/PFtyjgY.png>

- OpenStack Block Orchestration - Heat
<ul>
<li>Thuật ngữ "Orchestration"</li>
<li>Dùng để triển khai các ứng dụng dựa vào template được dựng sẵn</li>
<li>tự động tính toán sử dụng tài nguyên</li> 
<li>là tab "stack" trong Horizon</li>
</ul>
<img src=http://imgur.com/W4Nhtif.png>

- OpenStack Block Telemetry - Ceilometer
<ul>
<li>Đáp ứng tính anwng "pay as you go" của cloud computing</li>
<li>Thống kê tài nguyên người dùng sử dụng</li>
<li>Giám sát mức đọ sử dụng tài nguyên trong OpenStack</li>
<li>Mục tiêu: đo lường để tính xhi phí</li>
<li>Tích hợp trong Horizon với quyền admib</li>
</ul>
<img src=http://imgur.com/VWGks8E.png>

- OpenStack Database Service - Trove
<ul>
<li>Dịch vụ cung cấp về cơ sở dữ liệu có mặt trong OpenStack Icehouse</li>
<li>Cung cấp Database không cần thông qua người quản trị</li>
<li>Tự động backup đảm ảo an toàn</li>
<li>Hỗ trợ SQL và NoSQL</li>
</ul>
