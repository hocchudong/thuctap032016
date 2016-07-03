#Project Glance

##Mục lục:
###[1.Tổng quan chung về Project Glance] (#1)
- [1.1. Khái niệm](#1.1)
- [1.2. Công dụng](#1.2)
	
###[2.Glance Components](#2)

###[3.Glance Architecture](#3)
- [3.1.Các khái niệm AuthN/AuthZ](3.1#)
- [3.2.Khái niệm SSO](#3.2)

###[4. Glance Formats](#4)

###[5. Luồng trạng thái của Glance] (#5)

###[6. File cấu hình của image] (#6)
- [6.1. Thư lục lưu trữ image](#luutruimage)
- [6.2. Thư mực lưu file cấu hình image](#cauhinhimage)


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
<ul>
<li><b>Glance API</b>: Cho phép các API có thể tìm kiếm, nhận và lưu trữ các Virtual Machine image.</li>
<li><b>Glance registry</b>: Lưu trữ và nhận thông tin về các image.</li>
<li><b>Glance database</b> Là nơi lưu trữ các image metadata.</li>
<li><b>Storage repository</b>: Là thành phần tích hợp với các hệ thống lưu trữ bên ngoài khác như file systems, Amazon S3 và HTTP.</li>
</ul>
<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing2.png">
Glance chấp nhận các yêu cầu API cho các images từ người dùng cuối (end-users) hoặc các thành phần Nova và có thể lưu trữ bằng dịch vụ Object storage, swift hoặc các dịch vụ lưu trữ khác.
<ul>
<li><b>File system</b>: Mặc định lưu trữ các VM images trong file system. Back-end này đơn giản là ghi lại file image vào file system</li>
<li><b>Object Storage</b>: Các dịnh vụ Openstack có tính sẵn sàng cao để lưu trữ hướng đối tượng</li>
<li><b>Block Storage</b>: Các dịch vụ Openstack có tính sẵn sàng cao để lưu trữ khối</li>
<li><b>VMware</b>: ESX/ESXi or vCenter Server target system</li>
<li><b>S3</b>: Amazon S3 service</li>
<li><b>HTTP</b>: Openstack image service có thể đọc được virtual machine image có sẵn trên internet thông qua giao thức HTTP. Tuy nhiên, lưu trữ này chỉ có thể đọc được.</li>
<li><b>RADOS Block Device (RBD)</b>: Lưu trữ image bên trong 1 cụm lưu trữ Ceph sử dụng Ceph’s RBD interface.
Sheepdog: 1 hệ thống lưu trữ phân phối cho QEMU/KVM</li>
<li><b>GridFS</b>: Lưu trữ các images sử dụng MongoDB</li>
</ul>
<a name ="3"></a>	
###3. Glance Architecture:
Glance có một kiến trúc client-server và cung cấp các REST API để thông qua đó yêu cầu server thực hiện. Yêu cầu từ máy client được chấp nhận thông qua REST API và chờ cho Keystone chứng thực. Glance domain controller quản lý tất cả các hoạt động nội bộ, nó được chia là các layer và mỗi layer có 1 nhiệm vụ riêng.Glance store là tầng giao tiếp giữa Glance và extenal storage back-end hoặc local file system và cung cấp 1 giao diện thống nhất để chấp thuận. Glance sử dụng SQL central database để có thể truy cập vào tất cả các thành phần trong hệ thống 

<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing11.png">

Glance gồm có 1 sô thành phần như:
<ul>
<li><b>Client</b>: Bất kì ứng dụng nào sử dụng Glance server.</li>
<li><b>REST API</b>: exposes Glance functionality via REST</li>
<li><b>Database Abstraction Layer (DAL)</b>: Là 1 giao diện ứng dụng trong đo hợp nhất các Glance và database</li>
<li><b>Glance Domain Controller</b>: Thực hiện các chức năng chính của Glance như: authorization, notifications, policies, database connections.</li>
<li><b>Glance Store</b>: Tạo ra sự tương tác giữa Glance và các data stores khác</li>
<li><b>Registry Layer</b>: Tùy chọn layer tạo ra thông tin liên lạc an toàn giữa Domain và DAL bằng cách sử dụng 1 dịch vụ riêng biệt.</li>
</ul>


<a name="3.1"></a>
####3.1. Khái niệm cơ bản về AuthN/AuthZ:
-AuthN
<ul>
<li>Xác thực người dùng</li>
<li>Giao tiếp với danh tính người dùng, có 1 số lượng lớn các hệ thống để kiểm soát mức độ nhận dạng và quản lý người dùng</li>
<li>Làm giảm tải số lượng thông tin người dùng cung cấp thông qua SSO</li>
</ul>
-AuthZ
<ul>
<li>Trả lời câu hỏi liên quan đến những thiết lập khác nhau, những gì người dùng hay hệ thống được phép truy cập</li>
<li>1 nền tảng AuthZ có thể xác định 1 người dùng là 1 developer, sau đó nó sẽ cấo phép của mình để đẩy mã nguồn lên git, những không được sửa đổi các phần mềm triển khai hoặc môi trường sản xuất</li>
</ul>

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

######Disk format

|Định dạng|Mô tả|
|---------|-----|
|Raw|đĩa không cấu trúc|
|VHD|Định dạng phổ biến nhất hỗ trợ bởi nhiều công nghệ ảo hóa từ OpenStack trừ KVM|
|VMDK|định dạng phổ biến bởi VMWare|
|qcow2|định dạng QEMU, định dạng gốc choKVM và QEMU hỗ trọ nhiều phép tính nâng cao|
|VDI|Định dạng đĩa cảu Virtual Box|
|ISO|Định dạng nén của đĩa quang học|
|AMI,ARI,AKI|Định dạng của Amazone|	

######Container format
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
<ul>
<li><b>queued</b>: Định danh của image được lưu giữ trong Glance registry. Không có dữ liệu nào của image được tải lên Glance và kích thước của image không được thiết lập rõ ràng sẽ được thiết lập về zero khi khởi tạo.</li>
<li><b>saving</b>: Trạng thái này biểu thị rằng dữ liệu thô của image đang upload lên Glance. Khi image được đăng ký với lời gọi POST /images và có một header đại diện x-image-meta-location, image đó sẽ không bao giờ được đưa và trạng thái "saving" (bởi vì dữ liệu của image đã có sẵn ở một nơi nào đó)</li>
<li><b>active</b>: Biểu thị trạng thái sẵn sàng của 1 image trong Glance. Trạng thái này được thiết lập khi dữ liệu của image được tải lên đầy đủ.</li>
<li><b>deactivated</b>: Trạng thái biểu thị việc không được phép truy cập vào dữ liệu của image với tài khoản không phải admin. Khi image ở trạng thái này, ta không thể tải xuống cũng như export hay clone image.</li>
<li><b>killed</b>: Trạng thái biểu thị rằng có vấn đề xảy ra trong quá trình tải dữ liệu của image lên và image đó không thể đọc được</li>
<li><b>deleted</b>: Trạng thái này biểu thị việc Glance vẫn giữ thông tin về image nhưng nó không còn sẵn sàng để sử dụng nữa. Image ở trạng thái này sẽ tự động bị gỡ bỏ vào ngày hôm sau.</li>
</ul>
<a name="6"></a>

###6. File cấu hình của image:
Những thư mục chứa file cấu hình của Image service
<a name="luutruimage"></a>
####6.1. Thư mục lưu trữ image

`var/lib/glance/image`
- Đoạn file cấu hình thư mục lưu trữ image trong `glance-api.conf`

```sh
[glance_store]
default_store = file
stores = file,http
filesystem_store_datadir = /var/lib/glance/images/
```
<a name="cauhinhimage"></a>
####6.2. Thư mục chứa file cấu hình của Glance

`etc/glance`

-Các thư mục file cấu hình của Glance:
<ul>
<li><b>Glance-api.conf</b>: File cấu hình cho dịch vụ API image.</li>
<li><b>Glance-registry.conf</b>: Tập tin cấu hình cho glance image registry, chứa các metadata về images</li>
<li><b>Glance-scrubber.conf</b>: Tiện ích dùng để xóa sạch các image đã được xóa. Nhiều cái scrubber-glance có thể chạy trên 1 deployment</li>
<li><b>policy.json</b>: Kiểm soát các truy cập vào image service. Tại đây chúng ta có thể xác định được vai trò, chính sách, đó là các tính năng bảo mật trong Openstack Glance</li>
</ul>


<a name=image></a>
####7. Image and Instance:
Như đã nói trước đó, các disk image được lưu trữ như là 1 template. Image service kiểm soát và quản lý các images.Instance là 1 cái máy ảo riêng biệt chạy trên node compute và node compute cũng quản lý các instances. Người dùng có thể chạy bất kì số lượng instances nào với cùng image. Mỗi lần khởi động instances được tạo bởi bản copy dựa vào image. Vậy nên bất ì thay đổi nào trên instances đều không bị ảnh hưởng đến image cơ bản. Chúng ta có thể thực hiện 1 snapshot của instances đang chạy và có thể khởi động các instances khác.
Khi chúng ta chạy 1 instances ta cần phải xác định được flavor của nó, đó là đại điện cho tài nguyên ảo. Flavor xác định có bao nhiêu CPUs ảo mà instances có, số lượng RAM sẵn có của nó, kích cỡ của ổ đĩa. Openstack cung cấp các flavor đã được xác định trước, chúng ta có thể khởi tạo và chỉnh sửa các flavor.
Sơ đồ dưới đây cho biết tình trạng hệ thống trước khi launching một instance. Các image store, có số lượng image được xác định trước, compute nod chứa vcpu sẵn, bộ nhớ và tài nguyên đĩa địa phương và cinder-volume chứa số lượng contains number được xác định trước.

<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing2.jpg">

Trước khi khởi chạy 1 instance đã được chọn image, flavor hay bất kì thuộc tính nào khác. Lựa chọn flavor cũng cấp 1 root volume, dán nhãn là VDA và lưu trữ tạm thời bổ sung được dán nhãn là VDB và cinder-volume là ánh xạ tới ảo đĩa thứ ba và gọi nó là VDC.

<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/new.jpg">

Trong hình này, các image base được sao chép vào local disk từ các image store. VDA là đĩa đầu tiên mà các instances truy cập, các instance bắt đầu nhanh hơn nếu kích thước của image là nhỏ hơn như ít dữ liệu cần phải được sao chép trên mạng. VDB là một đĩa trống tạm thời được tạo ra dùng với instance, nó sẽ được xóa khi dụ chấm dứt.
Vdc kết nôi tới cinder-volume sử dụng iSCSI. Sau khi compute node quy định vCPU và tài nguyên về bộ nhớ, instance được boot từ volume vda. Instance chạy và thay đổi dữ liệu trên ổ đĩa. Nếu volume store nằm trên 1 mạng riêng biệt, tùy chọn my_block_storage_ip được xác định trong storage node tập tin file cấu hình image lưu thông qua compute node.
Khi 1 cái instance bị xóa. Trạng thái này được phá bỏ kể cả với trường hợp ngoại lệ là volume khó bị xóa. Ephemeral storage bị xóa đi; bộ nhớ, vCPU và các tài nguyên đã được sử dụng nhưng image remain vẫn không thay đổi trong suốt quá trình này.











	

	








