#Project Glance

##Mục lục:
###[1.Tổng quan chung về Project Glance] (#1)
	- [1.1. Khái niệm](#1.1)
	- [1.2. Công dụng](#1.2)
	
###[2.Glance Components](#2)

###[3.Glance Architecture](#3)
	- [3.1.Các khái niệm AuthN/AuthZ] (3.1#)
	- [3.2.Khái niệm SSO] (#3.2)

###[4. Glance Formats](#4)

###[5. Luồng trạng thái của Glance] (#5)

###[6. File cấu hình của image] (#6)


<a name="1"></a>
###1.Tổng quan chung về Project Glance:

<a name="1.1"></a>
####1.1. Khái niệm:
Glance là 1 Project trong Openstack, được sinh ra để cung cấp dịch vụ khai báo, lưu trữ và quản lý các Virtual Machine image. Hỗ trợ các định dạng khác nhau của hypervisor như: vmdk, iso, ami...

<a name="1.2"></a>
####1.2. Công dụng:
	- Để lưu trữ các image, chuyển phát image tới Nova để bắt đầu instance, snapshot từ các instance đang chạy có thể được lưu trữ vì vậy máy ảo đó có thể được backup.
	- Glance có các RESTful APT cho phép truy vấn các image metadata cũng như thu hồi các image hiện có.
	- Các image đã có sẵn trong Glancen có thể được lưu trữ trong các nơi từ 1 file hệ thống đơn giản cho tói object storage
	
<a name ="2"></a>
###2. Glance Components:
Glance có các thành phần như sau:
		- **Glance API**: Cho phép các API có thể tìm kiếm, nhận và lưu trữ các Virtual Machine image.
		- **Glance registry**: Lưu trữ và nhận thông tin về các image.
		- **Glance database**: Là nơi lưu trữ các image metadata.
		- **Storage repository**: Là thành phần tích hợp với các hệ thống lưu trữ bên ngoài khác như file systems, Amazon S3 và HTTP.
<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing2.png">
Glance chấp nhận các yêu cầu API cho các images từ người dùng cuối (end-users) hoặc các thành phần Nova và có thể lưu trữ bằng dịch vụ Object storage, swift hoặc các dịch vụ lưu trữ khác.


	- **File system**: Mặc định lưu trữ các VM images trong file system. Back-end này đơn giản là ghi lại file image vào file system
	- **Object Storage*: Các dịnh vụ Openstack có tính sẵn sàng cao để lưu trữ hướng đối tượng
	- **Block Storage**: Các dịch vụ Openstack có tính sẵn sàng cao để lưu trữ khối
	- **VMware**: ESX/ESXi or vCenter Server target system
	- **S3**: Amazon S3 service
	- **HTTP*: Openstack image service có thể đọc được virtual machine image có sẵn trên internet thông qua giao thức HTTP. Tuy nhiên, lưu trữ này chỉ có thể đọc được.
	- **RADOS Block Device (RBD)**: Lưu trữ image bên trong 1 cụm lưu trữ Ceph sử dụng Ceph’s RBD interface.
	- **Sheepdog**: 1 hệ thống lưu trữ phân phối cho QEMU/KVM
	- **GridFS**: Lưu trữ các images sử dụng MongoDB

<a name ="3"></a>	
###3. Glance Architecture:
Glance có một kiến trúc client-server và cung cấp các REST API để thông qua đó yêu cầu server thực hiện. Yêu cầu từ máy client được chấp nhận thông qua REST API và chờ cho Keystone chứng thực. Glance domain controller quản lý tất cả các hoạt động nội bộ, nó được chia là các layer và mỗi layer có 1 nhiệm vụ riêng.Glance store là tầng giao tiếp giữa Glance và extenal storage back-end hoặc local file system và cung cấp 1 giao diện thống nhất để chấp thuận. Glance sử dụng SQL central database để có thể truy cập vào tất cả các thành phần trong hệ thống 

<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing11.png">

Glance gồm có 1 sô thành phần như:

	- **Client**: Bất kì ứng dụng nào sử dụng Glance server.
	- **REST API**: exposes Glance functionality via REST
	- **Database Abstraction Layer (DAL)**: Là 1 giao diện ứng dụng trong đo hợp nhất các Glance và database
	- **Glance Domain Controller**: Thực hiện các chức năng chính của Glance như: authorization, notifications, policies, database connections.
	- **Glance Store**: Tạo ra sự tương tác giữa Glance và các data stores khác
	- **Registry Layer**: Tùy chọn layer tạo ra thông tin liên lạc an toàn giữa Domain và DAL bằng cách sử dụng 1 dịch vụ riêng biệt.


<a name="3.1"></a>
####3.1. Khái niệm cơ bản về AuthN/AuthZ:
**AuthN**

	- Xác thực người dùng
	- Giao tiếp với danh tính người dùng, có 1 số lượng lớn các hệ thống để kiểm soát mức độ nhận dạng và quản lý người dùng
	- Làm giảm tải số lượng thông tin người dùng cung cấp thông qua SSO

**AuthZ**

	- Trả lời câu hỏi liên quan đến những thiết lập khác nhau, những gì người dùng hay hệ thống được phép truy cập
	- 1 nền tảng AuthZ có thể xác định 1 người dùng là 1 developer, sau đó nó sẽ cấo phép của mình để đẩy mã nguồn lên git, những không được sửa đổi các phần mềm triển khai hoặc môi trường sản xuất


<a name="3.2"></a>
####3.2.SSO (Single sign on)
- Chỉ được triển khai khi hệ thống đã xác thực và phân quyền, có nhiệm vụ cung cấp cho người dùng quyền truy cập vào các tài nguyên trong phạm vi cho phép với 1 lần đăng nhập (xác thực)
- Access control:
<ul>
<li>Authentication: Định danh người dùng</li>
<li>Authorization: Là quá trình kiểm chứng người dùng có quyền hạn gì</li>
</ul>
- SSO được sử dụng dưới các định dạng:
<ul>
<li>Single domain: Khi xác thực thành công vào domain.com, người dùng đồng thời được xác thực vào các sub-domain</li>
<li>Multi domain: Khi xác thực thành công vào abc.com thì người dùng cũng đồng thời được xác thực vào xyz.com</li>
<li>Application vs Third-party product:Ví dụ SSO giữa IBM và Websphere Application server</li>
</ul>
<a name="4"></a>
###4.Glance Formats:

- Khi ta thêm 1 image vào Glance, cần xác định được các định dạng disk formats hay container format của image.
- Container format được coi là phần hồn của image và disk được coi là phần xác, bởi vì khi ta gọi 1 image, hệ thống sẽ đọc container format trước để biết thông tin của image(hệ điều hành, định dạng, nơi lưu trữ), khi nó đọc xong và xác định được thông tin của image thì nó mới gọi tiếp đến disk format. Việc này làm giảm thừoi gian xử lý bởi Container format nhẹ hơn disk format rất nhiều nên có thể đọc nhanh hơn.
-**Disk format**

|Định dạng|Mô tả|
|---------|-----|
|Raw|đĩa không cấu trúc|
|VHD|Định dạng phổ biến nhất hỗ trợ bởi nhiều công nghệ ảo hóa từ OpenStack trừ KVM
|VMDK|định dạng phổ biến bởi VMWare|
|qcow2|định dạng QEMU, định dạng gốc choKVM và QEMU hỗ trọ nhiều phép tính nâng cao|
|VDI|Định dạng đĩa cảu Virtual Box|
|ISO|Định dạng nén của đĩa quang học|
|AMI,ARI,AKI|Định dạng của Amazone|	

-*Container format*
|Định dạng|Mô tả|
|---------|-----|
|bare|không có container hay metadata trong đĩa|
|ovf|định dạng ovf|
|aki,ari,ami|Định dạng đĩa của Amazone|
|ova|là file tar ova lưu trữ|
|docker|là file dạng docker được lưu trữ|

<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/snapshot5.png">

<a name="5"></a>
###5. Luồng trạng thái của Glance:
Luồng trạng thái của Glance cho biết trạng thái của image trong quá trình tải lên. Khi tạo một image, bước đầu tiên là queing, image được đưa vào hàng đợi trong một khoảng thời gian ngắn, được bảo vệ và sẵn sàng để tải lên. Sau khi queuing image chuyển sang trạng thái Saving nghĩa là quá trình tải lên chưa hoàn thành. Một khi image được tải lên hoàn toàn, trạng thái image chuyển sang Active. Khi quá trình tải lên thất bại nó sẽ chuyển sang trạng thái bị hủy hoặc bị xóa. Ta có thể deactive và reactive các image đã upload thành công bằng cách sử dụng command. 
<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing1.jpg">

-**queued**: Định danh của image được lưu giữ trong Glance registry. Không có dữ liệu nào của image được tải lên Glance và kích thước của image không được thiết lập rõ ràng sẽ được thiết lập về zero khi khởi tạo.
-**saving**: Trạng thái này biểu thị rằng dữ liệu thô của image đang upload lên Glance. Khi image được đăng ký với lời gọi POST /images và có một header đại diện x-image-meta-location, image đó sẽ không bao giờ được đưa và trạng thái "saving" (bởi vì dữ liệu của image đã có sẵn ở một nơi nào đó)
-**active**: Biểu thị trạng thái sẵn sàng của 1 image trong Glance. Trạng thái này được thiết lập khi dữ liệu của image được tải lên đầy đủ.
-**deactivated**: Trạng thái biểu thị việc không được phép truy cập vào dữ liệu của image với tài khoản không phải admin. Khi image ở trạng thái này, ta không thể tải xuống cũng như export hay clone image.
-**killed**: Trạng thái biểu thị rằng có vấn đề xảy ra trong quá trình tải dữ liệu của image lên và image đó không thể đọc được
-**deleted**: Trạng thái này biểu thị việc Glance vẫn giữ thông tin về image nhưng nó không còn sẵn sàng để sử dụng nữa. Image ở trạng thái này sẽ tự động bị gỡ bỏ vào ngày hôm sau.

<a name="6"></a>
###6. File cấu hình của image:





	

	








