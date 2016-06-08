#OpenStack Glance
#Mục lục
<h4><a href="#intro">1. Giới thiệu OpenStack Glance</a></h4>
<h4><a href="#component">2. Các thành phần của Glance</a></h4>
<h4><a href="#arch">3. Kiến trúc của Glance</a></h4>
<h4><a href="#formats">4. Các định dạng lưu trữ image của glance</a></h4>
<h4><a href="#flow">5. Luồng trạng thái của Glance</a></h4>
<h4><a href="#conf">6. Các file cấu hình của glance</a></h4>
<h4><a href="#img">7. Image và Instance</a></h4>
<h4><a href="#manage_image">8. Quản lý các images</a></h4>
<h4><a href="#ref">9. Tham khảo</a></h4>
---

<h2><a name="intro">1. Giới thiệu OpenStack Glance</a></h2>
<div>
<ul>
<li>Là Image services bao gồm việc tìm kiếm, đăng ký, thu thập các images của các máy ảo. Glance cung cấp RESTful API cho phép truy vấn metadata của image máy ảo cũng như thu thập image thực sự</li>
<li>Images của máy ảo thông qua Glance có thể lưu trữ ở nhiều vị trí khác nhau từ hệ thống file thông thường cho tới hệ thống object-storage như OpenStack Swift.</li>
<li>Trong Glance, các images được lưu trữ giống như các template. Các Template này sử dụng để vận hành máy ảo mới. Glance là giải pháp để quản lý các ảnh đĩa trên cloud. Nó cũng có thể lấy bản snapshots từ các máy ảo đang chạy để thực hiện dự phòng cho các VM và trạng thái các máy ảo đó.</li>
</ul>
</div>

<h2><a name="component">2. Các thành phần của Glance</a></h2>
<div>
Glance bao gồm các thành phần sau:
<ul>
<li><b>glance-api: </b>tiếp nhận lời gọi API để tìm kiems, thu thập và lưu trữ image</li>
<li><b>glance-registry: </b>thực hiện tác vụ lưu trữ, xử lý và thu thập metadata của images</li>
<li><b>database: </b>cơ sở dữ liệu lưu trữ metadata của image</li>
<li><b>storage repository: </b>được tích hợp với nhiều thành phần khác trong OpenStack như hệ thống file thông thường, Amazon và HTTP phục vụ cho chức năng lưu trữ images</li>
</ul>
<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing2.png"/><br><br>
Glance tiếp nhận các API request yêu cầu images từ người dùng cuối hoặc các nova component và costheer lưu trữ các file images trong hệ thống object storage Swift hoặc các storage repos khác. Glance hỗ trợ các hệ thống backend lưu trữ  sau:
<ul>
<li><b>File system</b>
<div>Glance lưu trữ images của các máy ảo trong hệ thống tệp tin thông thường theo mặc định, hỗ trợ đọc ghi các image files dễ dàng vào hệ thống tệp tin</div>
</li>
<li><b>Object Storage</b>
<div>Là hệ thống lưu trữ do OpenStack Swift cung cấp - dịch vụ lưu trữ có tính sẵn sàng cao , lưu trữ các image dưới dạng các object.</div>
</li>
<li><b>BlockStorage</b>Hệ thống lưu trữ có tính sẵn sàng cao do OpenStack Cinder cung cấp, lưu trữ các image dưới dạng khối</li>
<li><b>VMWare</b></li>
<li><b>Amazon S3</b></li>
<li><b>HTTP</b>
<div>Glance có thể đọc các images của các máy ảo sẵn sàng trên Internet thông qua HTTP. Hệ thống lưu trữ này chỉ cho phép đọc.</div>
</li>
<li><b>RADOS Block Device(RBD)</b>
<div>Lưu trữ các images trong cụm lưu trữ Ceph sử dụng giao diện RBD của Ceph</div>
</li>
<li><b>Sheepdog</b>
<div>Hệ thống lưu trữ phân tán dành cho QEMU/KVM</div>
</li>
<li><b>GridFS</b>
Lưu trữ các image sử dụng MongoDB
</li>
</ul>
</div>
<h2><a name="arch">3. Kiến trúc của Glance</a></h2>
<div>
<div>
Glance có kiến trúc client-server và cung cấp REST API thông qua đó yêu cầu tới server được thực hiện. Yêu cầu từ client được tiếp nhận thông qua REST API và đợi sự xác thực của Keystone. Keystone Domain controller quản lý tất cả các tác vụ vận hành bên trong. Các tác vụ này chia thành các lớp, mỗi lớp triển khai nhiệm vụ vụ riêng của chúng.
</div>
<div>Glance store driver là lớp giao tiếp giữa glane và các hệ thống backend bên ngoài hoặc hệ thống tệp tin cục bộ, cung cấp giao diện chung để truy cập. Glance sử dụng SQL Database làm điểm truy cập cho các thành phần khác trong hệ thống.</div>
<div>Kiến trúc Glance bao gồm các thành phần sau:
<ul>
<li><b>Client: </b>ứng dụng sử dụng Glance server</li>
<li><b>REST API: </b>gửi yêu cầu tới Glance thông qua REST</li>
<li><b>Database Abstraction Layer (DAL): </b>là một API thống nhất việc giao tiếp giữa Glance và databases</li>
<li><b>Glance Domain Controller: </b>là middleware triển khai các chức năng chính của Glance: ủy quyền, thông báo, các chính sách, kết nối cơ sở dữ liệu</li>
<li><b>Glance Store: </b>tổ chức việc tương tác giữa Glance và các hệ thống lưu trữ dữ liệu</li>
<li><b>Registry Layer: </b>lớp tùy chọn tổ chức việc giao tiếp một cách bảo mật giữa domain và DAL nhờ việc sử dụng một dịch vụ riêng biệt</li>
</ul>
<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing11.png"/>
</div>
</div>

<h2><a name="formats">4. Các định dạng lưu trữ image của glance</a></h2>
<div>
<h3>Disk Formats</h3>
Là định dạng của các disk image
<table>
<tr>
<td>Disk Format</td>
<td>Notes</td>
</tr>

<tr>
<td>Raw</td>
<td>Định dạng đĩa phi cấu trúc</td>
</tr>

<tr>
<td>VHD</td>
<td>Định dạng chung hỗ trợ bởi nhiều công nghệ ảo hóa trong OpenStack, ngoại trừ KVM</td>
</tr>

<tr>
<td>VMDK</td>
<td>Định dạng hỗ trợ bởi VMWare</td>
</tr>

<tr>
<td>qcow2</td>
<td>Định dạng đĩa QEMU, định dạng mặc định hỗ trợ bởi KVM vfa QEMU, hỗ trợ các chức năng nâng cao</td>
</tr>

<tr>
<td>VDI</td>
<td>Định dạng ảnh đĩa ảo hỗ trợ bởi VirtualBox</td>
</tr>

<tr>
<td>ISO</td>
<td>Định dạng lưu trữ cho đĩa quang</td>
</tr>

<tr>
<td>AMI, ARI, AKI</td>
<td>Định dạng ảnh Amazon machine, ramdisk, kernel</td>
</tr>
</table>

<h3>Container Formats</h3>
Container Formats mô tả định dạng files và chứa các thông tin metadata về máy ảo thực sự. Các định dạng container hỗ trợ bởi Glance
<table>
<tr>
<td>Container Formats</td>
<td>Notes</td>
</tr>

<tr>
<td>bare</td>
<td>Định dạng xác định không có container hoặc meradate đóng gói cho image</td>
</tr>

<tr>
<td>ovf</td>
<td>Định dạng container OVF</td>
</tr>

<tr>
<td>aki</td>
<td>Xác định lưu trữ trong Glance là Amazon kernel image</td>
</tr>

<tr>
<td>ari</td>
<td>Xác định lưu trữ trong Glance là Amazon ramdisk image </td>
</tr>

<tr>
<td>ami</td>
<td>Xác định lưu trữ trong Glance là Amazon machine image</td>
</tr>

<tr>
<td>ova</td>
<td>Xác định lưu trữ trong Glance là file lưu trữ OVA</td>
</tr>

<tr>
<td>docker</td>
<td>Xác định lưu trữ trong Glance và file lưu trữ Docker</td>
</tr>
</table>
</div>

<h2><a name="flow">5. Luồng trạng thái của Glance</a></h2>
<div>
Luồng trạng thái của Glance cho biết trạng thái của image trong quá trình tải lên. Khi tạo một image, bước đầu tiên là queing, image được đưa vào hàng đợi trong một khoảng thời gian ngắn, được  bảo vệ và sẵn sàng để tải lên. Sau khi queuing image chuyển sang trạng thái Saving nghĩa là quá trình tải lên chưa hoàn thành. Một khi image được tải lên hoàn toàn,  trạng thái image chuyển sang Active. Khi quá trình tải lên thất bại nó sẽ chuyển sang trạng thái bị hủy hoặc bị xóa. Ta có thể deactive và reactive các image đã upload thành công bằng cách sử dụng command.
<br>
Luồng trạng thái của flow được mô tả theo hình sau:
<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing1.jpg"/>
<br><br>
Các trạng thái của image:
<ul>
<li><b>queued</b>
<div>Định danh của image được bảo vệ trong Glance registry. Không có dữ liệu nào của image được tải lên Glance và kích thước của image không được thiết lập rõ ràng sẽ được thiết lập về zero khi khởi tạo.</div>
</li>
<li><b>saving</b>
<div>Trạng thái này biểu thị rằng dữ liệu thô của image đang upload lên Glance. Khi image được đăng ký với lời gọi POST /images và có một header đại diện x-image-meta-location, image đó sẽ không bao giờ được đưa và trạng thái "saving" (bởi vì dữ liệu của image đã có sẵn ở một nơi nào đó)</div>
</li>
<li><b>active</b>
<div>Biểu thị rằng một image đã sẵn sàng tỏng Glance. Trạng thái này được thiết lập khi dữ liệu của image được tải lên hoàn toàn.</div>
</li>
<li><b>deactivated</b>
<div>Trạng thái biểu thị việc không được phép truy cập vào dữ liệu của image với tài khoản không phải admin. Khi image ở trạng thái này, ta không thể tải xuống cũng như export hay clone image.</div>
</li>
<li><b>killed</b>
<div>Trạng thái biểu thị rằng có vấn đề xảy ra trong quá trình tải dữ liệu của image lên và image đó không thể đọc được</div>
</li>
<li><b>deleted</b>
<div>Trạng thái này biểu thị việc Glance vẫn giữ thông tin về image nhưng nó không còn sẵn sàng để sử dụng nữa. Image ở trạng thái này sẽ tự động bị gỡ bỏ vào ngày hôm sau.</div>
</li>
</ul>
</div>

<h2><a name="conf">6. Các file cấu hình của glance</a></h2>
<div>
Các tệp cấu hình của glance nằm trong thư mục <b><code>/etc/glance</code></b>. Có tất cả 7 tệp cấu hình như sau:
<ul>
<li><b>glance-api.conf:</b>
File cấu hình cho API của image service.
</li>
<li><b>glance-registry.conf: </b>
File cấu hình cho glance image registry - nơi lưu trữ metadata về các images.
</li>

<li><b>glance-api-paste.ini: </b>Cấu hình cho các API middleware pipeline của Image service</li>

<li><b>glance-manage.conf: </b>Là tệp cấu hình ghi chép tùy chỉnh. Các tùy chọn thiết lập trong tệp <b><code>glance-manage.conf</code></b> sẽ ghi đè lên các section cùng tên thiết lập trong các tệp <b><code>glance-registry.conf</code></b> và <b><code>glance-api.conf</code></b>. Tương tự như vậy, các tùy chọn thiết lập trong tệp <b><code>glance-api.conf</code></b> sẽ ghi đè lên các tùy chọn thiết lập trong tệp <b><code>glance-registry.conf</code></b></li>

<li><b>glance-registry-paste.ini: </b>Tệp cấu hình middle pipeline cho các registry của Image service.</li>

<li><b>glance-scrubber.conf: </b>
Tiện ích sử dụng để dọn sạch các images đã ở trạng thái "deleted".  Nhiều glance-scrubber có thể chạy trong triển khai, tuy nhiên chỉ có một scrubber được thiết lập để "dọn dẹp" cấu hình trong file "scrubber.conf". Clean-up scrubber này kết hợp với các scrubber khác  bằng cách duy trì một hàng đợi chính của các images cần được loại bỏ.  Tệp glance-scrubber.conf cũng đặc tả cấu hình các giá trị quan trọng như khoảng thời gian giữa các lần chạy, thời gian chờ của các images trước khi bị xóa. Glance-scrubber có thể chạy theo định kỳ hoặc có thể chạy như một daemon trong khoảng thời gian dài.
</li>
<li><b>policy.json: </b> File tùy chọn được thêm vào để điều khiển truy cập áp dụng với image service. Trong file này ta có thể định nghĩa các roles và policies. Nó là tính năng bảo mật trong OpenStack Glance.</li>
</ul>
</div>
<h2><a name="img">7. Image và Instance</a></h2>
<div>
Như đã đề cập, disk images được lưu trữ giống như các template. Image service kiểm soát việc lưu trữ và quản lý của các images. Instance là một máy ảo riêng biệt chạy trên compute node, compute node quản lý các instances. User có thể vận hành bao nhiêu máy ảo tùy ý với cùng một image. Mỗi máy ảo đã được vận hành được tạo nên bởi một bản sao của image gốc, bởi vậy bất kỳ chỉnh sửa nào trên instance cũng không ảnh hưởng tới image gốc. Ta có thể tạo bản snapshot của các máy ảo đang chạy nhằm mục đích dự phòng hoặc vận hành một máy ảo khác.
<br>
Khi ta vận hành một máy ảo, ta cần phải chỉ ra flavor của máy ảo đó. Flavor đại diện cho tài nguyên ảo hóa cung cấp cho máy ảo, định nghĩa số lượng CPU ảo, tổng dung lượng RAM cấp cho máy ảo và kích thước  ổ đĩa không bền vững cấp cho máy ảo. OpenStack cung cấp một số flavors đã định nghĩa sẵn, ta có thể tạo và chỉnh sửa các flavors theo ý mình. 
<br>
Sơ đồ dưới đây chỉ ra trạng thái của hệ thống trước khi vận hành máy ảo. Trong đó image store chỉ số lượng các images đã được định nghĩa trước, compute node chứa các vcpu có sẵn, tài nguyên bộ nhớ và tài nguyên đĩa cục bộ, cinder-volume chứa số lượng volumes đã định nghĩa trước đó.
<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing2.jpg"/>
<br><br>
Trước khi vận hành 1 máy ảo, ta phải chọn một image, flavor và các thuộc tính tùy chọn.  Lựa chọn flavor nào cung cấp root volume, có nhãn là vda và một ổ lưu trữ tùy chọn được đánh nhãn vdb (ephemeral - không bền vững, và cinder-volumen được map với ổ đĩa ảo thứ ba, có thể gọi tên là vdc
<img src="http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/new.jpg"/><br><br>
Theo mô tả trên hình, image gốc được copy vào ổ lưu trữ cục bộ từ image store. Ổ vda là ổ đầu tiên mà máy ảo truy cập. Ổ vdb là ổ tạm thời (không bền vững - ephemeral) và rỗng, được tạo nên cùng với máy ảo, nó sẽ bị xóa khi ngắt hoạt động của máy ảo. Ổ vdc kết nối với cinder-volume sử dụng giao thức iSCSI. Sau khi compute node dự phòng vCPU và tài nguyên bộ nhớ, máy ảo sẽ boot từ root volume là vda. Máy ảo chạy và thay đổi dữ liệu trên các ổ đĩa. Nếu volume store được đặt trên hệ thống mạng khác, tùy chọn "my_block_storage_ip" phải được dặc tả chính xác trong tệp cấu hình storage node chỉ ra lưu lượng image đi tới compute node. 
<br>
Khi máy ảo bị xóa, ephemeral storage (khối lưu trữ không bền vững) bị xóa; tài nguyên vCPU và bộ nhớ được giải phóng. Image không bị thay đổi sau tiến trình này.
</div>

<h2><a name="manage_image">8. Quản lý các images</a></h2>
<div>
<h3><a name="image_details">8.1. Liệt kê và lấy thông tin về các images</a></h3>
<ul>
<li>Để liệt kê danh sách các images sử dụng lệnh <b><code>glance image-list</code></b> 
<pre>
root@controller:~# glance image-list
+--------------------------------------+--------+
| ID                                   | Name   |
+--------------------------------------+--------+
| ce64b039-6e40-4f13-b44e-5813c62dc082 | cirros |
+--------------------------------------+--------+
</pre>
</li>
<li>Hiển thị chi tiết thông tin của 1 image sử dụng lệnh: <b><code>glance image-show image_id</code></b>
<pre>
root@controller:~# glance image-show ce64b039-6e40-4f13-b44e-5813c62dc082
+------------------+--------------------------------------+
| Property         | Value                                |
+------------------+--------------------------------------+
| checksum         | ee1eca47dc88f4879d8a229cc70a07c6     |
| container_format | bare                                 |
| created_at       | 2016-04-21T08:59:42Z                 |
| disk_format      | qcow2                                |
| id               | ce64b039-6e40-4f13-b44e-5813c62dc082 |
| min_disk         | 0                                    |
| min_ram          | 0                                    |
| name             | cirros                               |
| owner            | 5274cf4a29534f68bb3305333aef3606     |
| protected        | False                                |
| size             | 13287936                             |
| status           | active                               |
| tags             | []                                   |
| updated_at       | 2016-04-21T08:59:42Z                 |
| virtual_size     | None                                 |
| visibility       | public                               |
+------------------+--------------------------------------+
</pre>
</li>
</ul>

<h3><a name="image_store">8.2. Cấu hình hệ thống lưu trữ backend cho các images</a></h3>
<div>
Để cấu hình hệ thống backend lưu trữ các images trong glance, tiến hành chỉnh sửa section <b><code>[glance_store]</code></b> trong file <b><code>/etc/glance/glance-api.conf</code></b>
<pre>
<code>
[glance_store]
stores = file,http
default_store = file
filesystem_store_datadir = /var/lib/glance/images/
</code>
</pre>
</div>
Ví dụ như trong cấu hình trên, ta cho phép hai hệ thống backend lưu trữ image là <b>file</b> và <b>http</b>, trong đó sử dụng hệ thống backend lưu trữ mặc định là <b>file</b>. Cấu hình thư mục lưu trữ các file images khi tải lên glance bằng biến <b><code>filesystem_store_datadir</code></b>. Ví dụ ở đây ta cấu hình lưu trong thư mục <b><code>/var/lib/glance/images/</code></b>. Kiểm tra thử thư mục lưu trữ image:
<pre>
<code>
root@controller:~# ls -l /var/lib/glance/images
total 12980
-rw-r----- 1 glance glance 13287936 Apr 21 15:59 ce64b039-6e40-4f13-b44e-5813c62dc082
</code>
</pre>
Như vậy ở đây có một image lưu trữ với kích thước cỡ 13MB. Thông tin về nơi lưu trữ image có thể truy vấn trực tiếp trong bảng <b>image_locations</b> của database <b>glance</b>
<pre>
<code>
MariaDB [glance]> select id, image_id, status, value from image_locations;
+----+--------------------------------------+--------+--------------------------------------------------------------------+
| id | image_id                             | status | value                                                              |
+----+--------------------------------------+--------+--------------------------------------------------------------------+
|  1 | ce64b039-6e40-4f13-b44e-5813c62dc082 | active | file:///var/lib/glance/images/ce64b039-6e40-4f13-b44e-5813c62dc082 |
+----+--------------------------------------+--------+--------------------------------------------------------------------+
1 row in set (0.00 sec)

</code>
</pre>
</div>

<h2><a name="ref">9. Tham khảo</a></h2>
<div>
<a href="http://www.sparkmycloud.com/blog/openstack-glance">http://www.sparkmycloud.com/blog/openstack-glance</a>
</div>

