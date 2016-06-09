#OpenStack Glance
##Mục lục:

[1 Giới thiệu](#1)

[2 Các thành phần](#2)

[3 Back-end](#3)

[4 Glance Configuration Files](#4)

[5 Glance Architecture](#5)

[6 Glance image Status](#6)

[7 Glance Task](#7)

[8 Disk and Container Formats](#8)

[9 Common Image Properties](#9)

[10 Image and instance](#10)

[11 Image cache](#11)


=====================================

<a name="1"></a>
###1 Giới thiệu

<li>OpenStack Glance là một image service. Cung cấp khả năng tìm kiếm, đăng ký và lấy virtual machine image.</li>
<li>Glance có RESTful API cho phép truy vấn VM image metadata.</li>
<li>VM image  được tạo bởi Glance và chứa trong các backends.</li>
<li>Các image được chứa giống như các mẫu và được dùng cho việc tạo các instances mới.</li>
<li>Glance được thiết kế như một dịch vụ độc lập với kích thước lớn để có thể cài đặt các virtual disk images.</li>
<li>Có thể tạo Snapshot từ các instance đang chạy để back up VM và các trạng thái của nó.</li>
</ul>

<img src=http://i.imgur.com/1RDL2Mp.jpg>

<a name="2"></a>
###2 Các thành phần

<img src=http://i.imgur.com/nD6AclU.jpg>

<li>**Glance-api**: Chấp nhận các yêu cầu API.</li>
<li>**Glace-registry**: Nơi lưu trữ, xử lý, lấy các thông tin metadata cho images.</li>
<li>**Glance-database**: Nơi chứa image metadata.</li>
<li>**Storage repository**: Kết nối các thành phần bên ngoài OpenStack như File systems, Amazon S3 và HTTP để chứa các images.</li>
</ul>

<a name="3"></a>
###3 Back-end

<li>**File System**: Hệ thống mặc định chứa các virtual machine images trong file system back-end.
<li>**Object Storage**: Dịch vụ có sẵn để lưu trữ object.</li>
<li>**Block Storage**: Dịch vụ có sẵn để lưu trữ block.</li>
<li>**VMware**: ESX/ESXi hoặc vCenter Server.</li>
<li>**S3**: Dịch vụ Amazon S3.</li>
<li>**HTTP**: Dịch vụ image có thể đọc các virtual machine images trên internet thông qua HTTP. (Read only).</li>
<li>**RADOS Block Device (RBD)**: Chứa các image sau các nhóm lưu trữ Ceph sử dụng giao diện Ceph’s RBD.</li>
<li>**Sheepdog**: Một hệ thống lưu trữ cho QEMU/KVM.</li>
<li>**GridFS**: Lưu trữ image sử dụng MongoDB.</li>
</ul>

Ví dụ: 

<img src=http://i.imgur.com/IbOgWhG.jpg>

<a name="4"></a>
###4 Glance Configuration Files

Thư mục chưa file cấu hình glance `/etc/glance`

<li> **metadefs:** This directory contains predefined namespaces for Glance Metadata Definitions Catalog. Files from this directory can be loaded into the database using `db_load_metadefs` command for glance-manage. Similarly you can unload the definitions using `db_unload_metadefs` command.</li>
<li> **Glance-api.conf:** File cấu hình api.</li>
<li> **Glance-registry.conf:** File cấu hình registry, là nơi lưu trữ metadata của images.</li>
<li> **Glance-scrubber.conf:** Utility used to clean up images that have been deleted. Nhiều glance-scrubber có thể chạy trên một deployment. Tuy nhiên, chỉ có một hành động clean-up scrubber trong glance-scrubber.conf. Clean-up scrubber phối hợp với các glance scrubbers khác bằng cách duy trì một hàng đợi những image cần được hủy bỏ. Nó cũng quy định cụ thể các mục cấu hình quan trọng như thời gian giữa các lần chạy, chiều dài thời gian của hình ảnh  có thể được cấp phát trước khi họ xóa cũng như các lựa chọn kết nối registry. Nó có thể chạy như một công việc định kỳ hoặc long-running daemon.</li>
<li> **glance-api-paste.ini:** </li>
<li> **glance-registry-paste.ini:**</li>
<li> **glance-cache.conf:**     </li>
<li> **glance-manage.conf:**   </li>   
<li> **schema-image.json:**</li>
<li> **policy.json:** Bổ sung kiểm soát truy cập cho image service. Chúng ta có thể xác định vai trò, chính sách, bảo mật trong glance.</li>
</ul>

<a name="5"></a>
###5 Glance Architecture

<img src=http://i.imgur.com/gnct7jK.jpg>

Components:

<li>**A client**: Các application truy cập Glance.</li>
<li>**REST API**: 
<li>**Database Abstraction Layer (DAL)**: Một giao diện ứng dụng cho phép truyền thông giữa Glance và database.</li>
<li>**Glance Domain Controller**: Thực hiện các chức năng ủy quyền, thông báo, chính sách, kết nối dữ liệu.</li>
<li>**Glance Store**: Dùng để tương tác giữa Glance và các data store khác.</li>
<li>**Registry Layer**: Dùng để bảo vệ khi giao tiếp giữa Domain và DAL.</li>
</ul>

<a name="6"></a>
###6 Glance image Status

<img src=http://i.imgur.com/XKxHZon.jpg>

Status:

<li>**Queued**: Danh tính của image được định nghĩa trong Glance-registry. Dữ liệu của image ko được update lên Glance, không có kích thước rõ ràng.</li>
<li>**Saving**: Dữ liệu dạng thô đang được tải lên. Khi image đã được đăng ký với 1 lời gọi POST /image và có một nhãn x-image-meta-location thì image đó sẽ ko được cho vào trạng thái Saving.</li>
<li>**Active**: Thể hiện một image đã có sẵn trên Glance.</li>
<li>**Deactivated**: Thể hiện quyền truy cấp dữ liệu image không được gán cho người dùng ko phải admin. Cấm downloads, export, clone các image.</li>
<li>**Killed**: Thể hiện quá trình tải lên gặp lỗi, các image ko thể đọc được.</li>
<li>**Deleted**: Khi image không được dùng trong một khoảng thời gian hoặc lỗi thì nó sẽ được xóa.</li>
<li>**Pending delete**: Giống như Deleted nhưng image chưa xóa bỏ các image data và nó không thể khôi phục.</li>
</ul>

<a name="7"></a>
###7 Glance Task

Task được thêm vào để hỗ trợ Glance. Nó là một yêu cầu Glance cung cấp cataloging, storage, delivery of virtual machine images. Khi Nova yêu cầu image để khởi động instance thì Task upload image lên Glance cho Nova. Nó dùng Glance để cung cấp dữ liệu cho các lời gọi API đã được xác định khi Nova khởi tạo.

**Task Entities**

Task Entities được biểu diển bởi một cấu trúc dữ liệu JSON đã mã hóa và được định nghĩa bởi sơ đồ JSON trong `/v2/schemas/task`.
Task Entities có ID để xác định nó là duy nhất trong các endpoint mà nó thuộc về. ID được dùng như token trong yêu cầu URLs để tương tác với task cụ thể.
Ngoài các đặc tính như created_at, self, type, status, updated_at, etc. Task còn có các đặc tính:

<ul>
<li>Input: Được xác định là một JSON blod. Nó là thông tin cho các yêu cầu của người dùng.</li>
<li>Result: Được xác định là một JSON blod. Nội dung sẽ đc ghi lại bởi Deployer. Result sẽ ko có giá trị sau khi task kết thúc và nó sẽ là Null khi failure.</li>
<li>Message: Sẽ là Null khi task failure.</li>
</ul>

JSON: etc/schema-image.json

**Task status**

<li>**Pending**: Chưa có tiến trình nào trên task.</li>
<li>**Processing**: Các Task đã được chọn, được chạy bằng cách sử dụng các backend Glance logic cho task.</li>
<li>**Success**: Task đã thành công.</li>
</ul>

<a name="8"></a>
###8 Disk and Container Formats

Danh sách định dạng disk và container được hỗ trợ:

Disk format: 

| Định dạng | Mô tả |
|:----------------:|:--------:|
| raw | Định dạng có cấu trúc |
| vhd | disk của máy ảo VMware, Xen... |
| vmdk | Hỗ trợ bởi nhiều máy ảo phổ biến |
| vdi | Hỗ trợ bởi VirtualBox,QEMU |
| iso | Định dạng lưu trữ dữ liệu của đĩa quang học |
| cow2 | Hỗ trợ bởi QEMU |
| aki | Amazon kernel image |
| ari | Amazon ramdisk image |
| ami | Amazon machine image |

Container format: dùng để xem virtual machine image như một định dạng tập tin, nó có thể chứa siêu dữ liệu về máy ảo thực tế.

| Định dạng | Mô tả |
|:----------------:|:--------:|
| bare | Không lưu trữ hoặc đóng gói siêu dữ liệu |
| ovf | Định dạng OVF |
| aki | Amazon kernel image |
| ari | Amazon ramdisk image |
| ami | Amazon machine image |
| ova | tập lưu trữ OVA tar |

<a name="9"></a>
###9 Common Image Properties

Khi thêm các image thì ta có thể chỉ định thêm các đặc tính có thể hữu ích cho người dùng.

<li>**Architecture**
	Kiến trúc được định nghĩa tại http://docs.openstack.org/cli-reference/glance.html#image-service-property-keys .</li>
<li>**Instance_uuid**: Metadata được dùng để ghi lại instance mà image gắn tới.</li>
<li>**Kernel_id**: ID của image nên được dùng như kernel khi khởi động AMI-style image.</li>
<li>**Ramdisk_id**: ID của image nên được dùng như ramdisk.</li>
<li>**Os_distro**: http://docs.openstack.org/cli-reference/glance.html#image-service-property-keys </li>
<li>**Os_version**: Phiên bản hệ điều hành.</li>
</ul>

<a name="10"></a>
###10 Image and instance

Các image được lưu trữ như các template. Image service điểu khiển việc lưu trữ và quản lý các image. 
Instance là các máy ảo độc lập chạy trên các compute note. Người dùng có thể khởi động nhiều instance từ cùng image. Các sửa đổi trên instance ko ảnh hưởng tới image. Chúng ta có thể snapshot các instance đang chạy và dùng nó cho các instance khác.

Khi tạo instance chúng ta cấn xác định các Flavors. Chúng là các tài nguyên ảo. Flavors được xác định là số lượng CPU ảo, số RAM có sẵn, kích thước các disk. 

Mô hình hệ thống ban đầu 

<img src=http://i.imgur.com/dlzOpZz.jpg>

Trước khi khởi động thì instance chọn một image, Flavors và các thuộc tính tùy chọn. Flavors được cung cấp một root volume có nhãn là VDA, lưu trữ tạm thời bổ sung là VDB và cinder-volume được ánh xạ là VDC.

<img src=http://i.imgur.com/Ad2m54h.jpg>

<a name="11"></a>
###11 Image cache

OpenStack Glance Image Cache: Glance API server có thể cấu hình để có một local image cache. Một image cache chứa các bản copy của image. Về cơ bản thì cho phép nhiều API server chứa các file image giống nhau, dẫn tới khả năng mở rộng các endpoint cung cấp image. Mặc định tính năng bị disabled. 

###12 Chú ý

Thư mục chứa các image **/var/lib/glance/images**

File log:  /var/log/glance

- **glance-api.log**: Image service API server
- **glance-registry.log**: Image service Registry server

Phần cấu hình backend trong file `glance-api.conf`
```sh
[glance_store]
default_store = file
stores = file,http
filesystem_store_datadir = /var/lib/glance/images/
```

Tham Khảo:

[1]- http://www.sparkmycloud.com/blog/openstack-glance/

[2]- http://www.slideshare.net/openstackstl/openstack-glance-48463490

[3]- http://docs.openstack.org/developer/glance/



























