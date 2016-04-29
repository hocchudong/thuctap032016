#Tìm hiểu các Project trong OpenStack
#Mục lục
* [1. Compute (NOVA)](#nova)
    * [1.1. Các chứng năng chính](#nova_chuc_nang)
    * [1.2. Các thành phần chính](#nova_thanh_phan)
    * [1.3. Nova Networking](#nova_networking)
    * [1.4 Users & Projects (Tenants)](#nova_users_projects)
* [2. Object Storage - Swift](#swift)
    * [2.1 Các chức năng chính](swift_chuc_nang)
    * [2.2 Các thành phần chính](swift_thanh_phan)
* [3. Image service - Glance](#glance)
    * [3.1 Chức năng chính](#glance_chuc_nang)
    * [3.2 Thành phần chính](#glance_thanh_phan)
    * [3.3 Hỗ trợ các định dạng](#glance_dinh_dang)
* [4. Identity Service - Keysotne](#identity)
    * [4.1 Các chức năng chính](#identity_chuc_nang)
    * [4.2 Các thành phần chính](#identity_thanh_phan)
* [5 Web based UI Service - Horizon](#horizon)

<a name="nova"></a>
#* [1. Compute (NOVA)](#nova)
* Là phần cơ bản của OpenStack
* Điều khiển, phân phối các tài nguyên hệ thống cho các máy ảo
* Cung cấp cho người dùng khả năng chạy máy ảo, giao diện để quản lý các máy ảo trên nên phàn cứng.
* NOVA sử dụng lại các hypervisor:
	* Hyper-V 2008.
	* KMV.
	* LXC.
	* QEMU.
	* UML.
	* VMWARE ESX/ESXi.
	* XEN.

<a name="nova_chuc_nang"></a>
##1.1. Các chứng năng chính:
* Quản lý tài nguyên ảo hóa: CPU, Memory, Disk, Network Interfaces,...
* Quản lý mạng nội bộ (LAN): Flat, Flat DHCP, VLAN, IPv6,..
* API với nhiều tính năng và xác thực: Quản lý việc users truy cập vào các tài nguyên và ngăn chặn truy cập trái phép qua lại giữa các users.
* Distributed and asynchronous architecture:
* Virtual Machie (VM) image management:
* Live VM management (Instance): Khởi tạo, đóng băng hay xóa instances.
* Floating IP address:
* Security Groups:
* Role Based Access Controll (BRAC)
* Projects &Quotas
* VNC Proxy through web browser
* Adavanced Scheduler:

<a name="nova_thanh_phan"></a>
##1.2. Các thành phần chính
![](http://docs.openstack.org/developer/nova/_images/Novadiagram.png)

| Thành phần | Chức năng |
|:----------:|:----------:|
| Cloud Controller|Quản lý và tương tác với tất cả các thành phần của Nova|
|API Server|Giống như một Web service đầu cuối của Cloud Controller|
|Compute Controller| Cung cấp, quản lý tài nguyên từ các máy ảo.
|Object Store|Cung cấp khả năng lưu trữ,thành phần này đi cùng với Compute Controller|
|Auth Manager| Dịch vụ authentication và authorization|
|Volume Controller|Lưu trữ theo block-level, giống như Amazon EBS|
|Network Controller|Tạo quản lý các kết nối trong virtual network để các server có thể tương tác với nhau và với public network|
|Scheduler|Chọn ra compute controller thích hợp nhất để lưu instance|

<a name="nova_networking"></a>
##1.3. Nova Networking

Có 2 kiểu IP trong Nova:
* Fixed IPs: được gán cho instance khi khởi tạo, không thay đổi được (private IP)
* Floating IPs: được gán thêm cho instance sau khi khởi tạo bởi admin, có thể thay đổi (public IP)

Có 3 kiểu cấu hình cho Fixed IPs:
* Flat mode: các instance được gán địa chỉ theo một bridge interface br100.
* Flat DHCP mode: tương tự như Flat mode nhưng br100 được cấu hình như một DHCP server sẽ gán IP cho các instance
* Vlan DHCP mode: mỗi project sẽ được gán cho một VLAN riêng. 

<a name="nova_users_projects"></a>
##1.4 Users & Projects (Tenants)
|||
|:-----:|:-----:|
| Cloud Administrator (admin)| Global role. Toàn quyền trong hệ thống.|
| IT Security (itsec)| Global role. IT security. Cách ly bất cứ instance nào trong bất kì project nào.|
| Project Manager (projectmanager)| Projec role. Mặc định cho người sở hữu project. Thêm bớt user vào proj, tương tác với các img, chạy instance.|
| Network Administrator (netadmin)| Project role. Cấu hình tường lửa, và các rule cho network, gán public IP cho instance.|
| Developer (developer)| Project role. Mặc định cho user|

<a name="swift"></a>
##2. Object Storage - Swift
* Được thiết kế để cung cấp lưu trữ quy mô lớn dữ liệu có thể được truy cập thông qua các API.
* Nó là hoàn toàn phân phối, lưu trữ nhiều bản sao của từng đối tượng để đạt được tính sẵn sàng cao và khả năng mở rộng.

<a name="swift_chuc_nang"></a>
##2.1 Các chức năng chính
* Lưu trữ và lấy các đối tượng(files)
* Set và sửa metadata trên đối tượng(tags)
* Phiên bản đối tượng
* Phục vụ static web và đối tượng thông qua HTTP

<a name="swift_thanh_phan"></a>
##2.2 Các thành phần chính

![](http://i.imgur.com/aSXoweI.png)

| Thành phần chính | Chức năng |
|:----------------:|:--------:|
|Proxy swift | nhận các request và chứng thực user.|
|Object swift | lưu trữ, quản lý các đối tượng được lưu.|
|Container swift | lưu trữ thông tin và trả về danh sách các object đang được lưu bên Object Store.|
|Account swift | cũng giống như Container swift nhưng nhiệm vụ của nó là quản lý danh sách các Container|
|The Ring | Thành phần này sẽ tạo một ánh xạ giữa tên của các thực thể được lưu trên đĩa cứng và địa chỉ vật lý của nó.|

<a name="glance"></a>
#3. Image service - Glance
* Glance cung cấp các dịch vụ khai báo, lưu trữ, quản lý các virtual machine images. 
* Hỗ trợ nhiều định dạng: raw, vhd, vmdk, vdi, iso, qcow2, aki, ari, ami

<a name="glance_chuc_nang"></a>
##3.1 Chức năng chính
* Lưu trữ public và private images
* Người sử dụng có thể query và liệt kê các image sẵn có để sử dụng
* Chuyển phát image tới Nova để bắt đầu instance
* Snapshot từ các instance đang chạy có thể được lưu trữ vì vậy máy ảo đó có thể được backup

<a name="glance_thanh_phan"></a>
##3.2 Thành phần chính

![](http://i.imgur.com/Spf0dPc.png)


| Thành phần chính | Chức năng |
|:----------------:|:--------:|
|Glance API server | nhận các hàm gọi API |
| Glance Registry server | lưu và cung cấp các thông tin (metadata) về image|
| Image Storage | lưu trữ các file image |

<a name="glance_dinh_dang"></a>
##3.3 Hỗ trợ các định dạng

| Định dạng | Mô tả |
|:----------------:|:--------:|
| raw | This is an unstructured disk image format|
| vhd | This is the VHD disk format, a common disk format used by virtual machine monitors from VMWare, Xen, Microsoft, VirtualBox,...|
| vmdk | Another common disk format supported by many common virtual machine monitors|
|vdi|A disk format supported by VirutalBox virtual machine monitor and the QUEMU emulator|
|iso|An archive format for the data contents of an optical disc|
|qcow2|A disk format supported by the QEMU emulator that can expand dynamically and supports Copy on Write|
|aki| This indicates what is stored in Glance is an Amazon kernel image|
|ari| This indicates what is stored in Glance is an Amazon ramdisk image|
|ami| This indicates what is stored in Glance is an Amazon machine image|

<a name="identity"></a>
#4. Identity Service - Keysotne
Cung cấp khả năng chứng thực, đặt các chính sách phân quyền cho các project.

<a name="identity_chuc_nang"></a>
##4.1 Các chức năng chính:
*  Xác thực user và vấn đề token để truy cập vào các dịch vụ
* Lưu trữ user và người thuê cho  vai trò kiểm soát truy cập (role-based access control (RBAC))
* Cung cấp catalog của dịch vụ trên cloud
* Tạo các chính sách giữa user và dịch vụ

<a name="identity_thanh_phan"></a>
##4.2 Các thành phần chính:

![](http://1.bp.blogspot.com/-BLElS5LHrbI/VFcOwKqN7PI/AAAAAAAAAPw/sOi-hj4GJ-Q/s1600/keystone_backends.png)

| Thành phần | Chức năng |
|:----------:|:----------|
|Identity| Xác thực về chứng chỉ, dữ liệu của Users, Groups, Projects, Domains và Roles.|
|Token| Dịch vụ xác thực và quản lý Tokend dược sử dụng để xác thực yêu cầu của một thông tin người dùng đã được xác minh.|
|Catalog| Cung cấp 1 đăng ký đầu cuối sử dụng để phát hiện đầu cuối.|
|Policy| Chính sách những quy tắc và giao diện quản lý nguyễn quy tắc này.|

<a name="horizon"></a>
##5 Web based UI Service - Horizon
Hozionlà một module ứng dụng web, cung cấp cho người dùng cuối và người quản trị cloud có một giao diện sử dụng các OpenStack services

<a name="horizon_dashboard"></a>
##5.1 OpenStack Dashboard
Cung cấp cho quản trị viên và người dùng giao điện đồ họa để truy cập, cung cấp và tự động hóa các tài nguyên trên đám mây.
* Cho phép quản trị viên và người dùng kiểm soát các tài nguyên compute, storage, networking.
* Cung cấp một cái nhìn tổng thể về kích cỡ, trạng thái đám mây của bạn. Bạn có thể tạo users, tạo projects, phân công users cho projects, thiết lập các giới hạn tài nguyên cho dự án.
* Cung cấp cho người dùng một cổng thông tin tự phục vụ với các tài nguyên giới hạn bởi quản trị viên.

##5.2 Horizon API
API Cho phép chúng ta phát triển những chức năng tốt hơn so với OpenStack Dashborad cung cấp.




