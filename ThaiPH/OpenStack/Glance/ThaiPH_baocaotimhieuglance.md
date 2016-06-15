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
<ul>
<li><a href="#image_details">8.1. Liệt kê và lấy thông tin về các images</a></li>
<li><a href="#image_store">8.2. Cấu hình hệ thống lưu trữ backend cho các images</a></li>
<li><a href="#image_log">8.3. Cấu hình file log của glance</a></li>
</ul>
<h4><a href="#image_api">9. Thao tác với glance bằng API</a></h4>
<ul>
<li><a href="#cli">9.1. Gửi yêu cầu tới API sử dụng OpenStack command line client</a></li>
<li><a href="#cURL">9.2. Gửi yêu cầu tới API sử dụng cURL</a></li>
<li><a href="#rest">9.3. Gửi yêu cầu tới API sử dụng REST client trên trình duyệt</a></li>
</ul>
<h4><a href="#cache">10. Glance image cache</a></h4>
<h4><a href="#ref">11. Tham khảo</a></h4>
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
<li><b>glance-api: </b>tiếp nhận lời gọi API để tìm kiếm, thu thập và lưu trữ image</li>
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
<img src="http://docs.openstack.org/developer/glance/_images/architecture.png"/>
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
<img src="http://docs.openstack.org/developer/glance/_images/image_status_transition.png"/>
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
<li><b>pending_delete: </b>
Tương tự như trạng thái <b>deleted</b>, tuy nhiên Glance chưa gỡ bỏ dữ liệu của image ngay. Một image khi đã rơi vào trạng thái này sẽ không có khả năng khôi phục.
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

<h3><a name="image_log">8.3. Cấu hình file log của glance</a></h3>
<div>
Mặc định Glance có hai file nhật ký lưu trong thư mục <code>/var/log/glance/</code>:
<ul>
<li><code>glance-api.log</code>: ghi lại lịch sử truy cập api server</li>
<li><code>glance-registry.log
</code>: ghi lại lịch sử liên quan tới registry server</li>
</ul>
Kiểm tra thử 2 file log:
<pre>
<code>
controller@controller:/var/log/glance$ ls
glance-api.log  glance-registry.log
</code>
</pre>
Để thay đổi file log mặc định, thực hiện chỉnh sửa cấu hình trong file <code>/etc/glance/glance-api.conf</code>. Thực hiện chỉnh sửa các tham số <code>log_file</code> và <code>log_dir</code>.  Giả sử ta thay đổi lại file log như sau:
<pre>
<code>
[DEFAULT]
log_file = /var/log/glance/glance_log_custom.log 
</code>
</pre>
Lưu lại file cấu hình, thực hiện khởi động lại glance-api server:
<pre>
<code>
root@controller:/etc/glance# sudo glance-control api start glance-api.conf
Starting glance-api with /etc/glance/glance-api.conf
</code>
</pre>
Kiểm tra thử trong thư mục chứa các file log của glance, ta sẽ thấy có file log mới xuất hiện: <code>glance_log_custom.log</code>
<pre>
<code>
root@controller:/etc/glance# ls /var/log/glance/
glance-api.log  glance_log_custom.log  glance-registry.log

</code>
</pre>
</div>
Ngoài ra, tham số <code>log_dir</code> sẽ thiết lập thưc mục lưu trữ các file log, nếu không thiết lập giá trị này, thì file log sẽ được lưu trong đường dẫn tuyệt đối chỉ ra bởi tham số <code>log_file</code>
</div>

<h2><a name="image_api">9. Thao tác với glance bằng API</a></h2>
<div>
<h3><a name="cli">9.1. Gửi yêu cầu tới API sử dụng OpenStack command line client</a></h3>
<div>
<ul>
<li><h4>a. Upload(create) một image lên thư mục lưu trữ glance</h4>
<pre>
<code>
root@controller:~/img-list# ls
cirros-0.3.4-x86_64-disk.img  Fedora-Cloud-Base-23-20151030.x86_64.qcow2
root@controller:~/img-list# openstack image create "fedora" \
> --file Fedora-Cloud-Base-23-20151030.x86_64.qcow2 \
> --disk-format qcow2 --container-format bare \
> --public
+------------------+------------------------------------------------------+
| Field            | Value                                                |
+------------------+------------------------------------------------------+
| checksum         | 38d62e2e1909c89f72ba4d5f5c0005d5                     |
| container_format | bare                                                 |
| created_at       | 2016-06-11T12:24:32Z                                 |
| disk_format      | qcow2                                                |
| file             | /v2/images/0bd9c9c6-211e-4998-8dfc-a54a14a42ca9/file |
| id               | 0bd9c9c6-211e-4998-8dfc-a54a14a42ca9                 |
| min_disk         | 0                                                    |
| min_ram          | 0                                                    |
| name             | fedora                                               |
| owner            | 5274cf4a29534f68bb3305333aef3606                     |
| protected        | False                                                |
| schema           | /v2/schemas/image                                    |
| size             | 234363392                                            |
| status           | active                                               |
| tags             |                                                      |
| updated_at       | 2016-06-11T12:24:47Z                                 |
| virtual_size     | None                                                 |
| visibility       | public                                               |
+------------------+------------------------------------------------------+
</code>
</pre>
</li>

<li><h4>b. Liệt kê danh sách các image đã upload</h4>
<pre>
<code>
root@controller:~/img-list# openstack image list
+--------------------------------------+--------+--------+
| ID                                   | Name   | Status |
+--------------------------------------+--------+--------+
| 0bd9c9c6-211e-4998-8dfc-a54a14a42ca9 | fedora | active |
| ce64b039-6e40-4f13-b44e-5813c62dc082 | cirros | active |
+--------------------------------------+--------+--------+
</code>
</pre>
</li>

<li><h4>c. Xem thông tin image</h4>
<pre>
<code>
root@controller:~/img-list# openstack image show fedora
+------------------+------------------------------------------------------+
| Field            | Value                                                |
+------------------+------------------------------------------------------+
| checksum         | 38d62e2e1909c89f72ba4d5f5c0005d5                     |
| container_format | bare                                                 |
| created_at       | 2016-06-11T12:24:32Z                                 |
| disk_format      | qcow2                                                |
| file             | /v2/images/0bd9c9c6-211e-4998-8dfc-a54a14a42ca9/file |
| id               | 0bd9c9c6-211e-4998-8dfc-a54a14a42ca9                 |
| min_disk         | 0                                                    |
| min_ram          | 0                                                    |
| name             | fedora                                               |
| owner            | 5274cf4a29534f68bb3305333aef3606                     |
| protected        | False                                                |
| schema           | /v2/schemas/image                                    |
| size             | 234363392                                            |
| status           | active                                               |
| tags             |                                                      |
| updated_at       | 2016-06-11T12:24:47Z                                 |
| virtual_size     | None                                                 |
| visibility       | public                                               |
+------------------+------------------------------------------------------+

</code>
</pre>
</li>

<li><h4>d. Xóa một image</h4>
Ví dụ ở đây xóa image fedora (xóa theo tên hoặc id của image), kiểm tra lai danh sách các image sau khi xóa:
<pre>
<code>
root@controller:~/img-list# openstack image delete fedora
root@controller:~/img-list# openstack image list
+--------------------------------------+--------+--------+
| ID                                   | Name   | Status |
+--------------------------------------+--------+--------+
| ce64b039-6e40-4f13-b44e-5813c62dc082 | cirros | active |
+--------------------------------------+--------+--------+
</code>
</pre>
</li>

<li><h4>e. Phân quyền truy cập public hay private cho image</h4>
Để thực hiện phân quyền truy cập cho image là "public" hay "private", sử dụng command <code>set</code>. Ví dụ, hiện tại image fedora đang có thuộc tính " visibility       | public  ", nghĩa là được truy cập public. Thiết lập lại quyền truy cập của image này sang private như sau:
<pre>
<code>
root@controller:~/img-list# openstack image set --private fedora
root@controller:~/img-list# openstack image show fedora
+------------------+------------------------------------------------------+
| Field            | Value                                                |
+------------------+------------------------------------------------------+
| checksum         | 38d62e2e1909c89f72ba4d5f5c0005d5                     |
| container_format | bare                                                 |
| created_at       | 2016-06-11T12:40:28Z                                 |
| disk_format      | qcow2                                                |
| file             | /v2/images/ec62a8ee-6ab0-4118-9029-a81ca92b8d43/file |
| id               | ec62a8ee-6ab0-4118-9029-a81ca92b8d43                 |
| min_disk         | 0                                                    |
| min_ram          | 0                                                    |
| name             | fedora                                               |
| owner            | 5274cf4a29534f68bb3305333aef3606                     |
| protected        | False                                                |
| schema           | /v2/schemas/image                                    |
| size             | 234363392                                            |
| status           | active                                               |
| tags             |                                                      |
| updated_at       | 2016-06-11T12:48:32Z                                 |
| virtual_size     | None                                                 |
| visibility       | private                                              |
+------------------+------------------------------------------------------+
</code>
</pre>
Như vậy sau khi thực hiện lệnh <code>set</code>, quyền truy cập của image fedora đã chuyển sang private. Lệnh <code>openstack image set</code> có thể sử dụng để thay đổi bất kì thuộc tính nào của image.
</li>
</ul>
</div>

<h3><a name="cURL">9.2. Gửi yêu cầu tới API sử dụng cURL</a></h3>
<div>
<ul>
<li><h4>a. Xin cấp phát token</h4>
<pre>
<code>
root@controller:~# curl -i \
   http://10.10.10.132:5000/v3/auth/tokens \
   -X POST \
   -H "Content-Type: application/json" \
   -d '
 { "auth": {
     "identity": {
       "methods": ["password"],
       "password": {
         "user": {
           "id": "ab8d4b68012b4d67b9445de9108c3945",
           "password": "Welcome123"
         }
       }
     },
     "scope": {
       "project": {
         "id": "2cf5f2f7d9754c2abb0059501c031ef9"
       }
     }
   }
 }' 
HTTP/1.1 201 Created
Date: Sat, 11 Jun 2016 14:36:54 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Subject-Token: gAAAAABXXCIGD14rLiR-fjcCXhwp4krp7DpsIJhPKYedtRgpRtQBQTcK_XpTBvjh7KrsEog4rzsrHEpk_zi-dQ72796X3JaaY3V2sAE1osGFZ-aHosOcqhu0EgJTUnfQsCOCIJzwReTrQH6MY76xXtitvZxioTzy2ZCa-AkMTV9pUlMV-863TMA
Vary: X-Auth-Token
X-Distribution: Ubuntu
x-openstack-request-id: req-0a38574a-f421-4316-9b43-94fd43996e61
Content-Length: 2839
Content-Type: application/json

{"token": {"methods": ["password"], "roles": [{"id": "44ef633a6e984d2badb4fdbb6103f060", "name": "admin"}], "expires_at": "2016-06-11T15:36:54.540327Z", "project": {"domain": {"id": "34fb0c49dd1440d69c89d1418af9c857", "name": "default"}, "id": "2cf5f2f7d9754c2abb0059501c031ef9", "name": "service"}, "catalog": [{"endpoints": [{"region_id": "RegionOne", "url": "http://controller:8774/v2.1/2cf5f2f7d9754c2abb0059501c031ef9", "region": "RegionOne", "interface": "admin", "id": "3132ada4c76b49a3a2c4f75a0054fc88"}, {"region_id": "RegionOne", "url": "http://controller:8774/v2.1/2cf5f2f7d9754c2abb0059501c031ef9", "region": "RegionOne", "interface": "public", "id": "bf4d2f86b99e429a98ff0f01953c85d6"}, {"region_id": "RegionOne", "url": "http://controller:8774/v2.1/2cf5f2f7d9754c2abb0059501c031ef9", "region": "RegionOne", "interface": "internal", "id": "fb671db7f0b646e583f92abf17bc2bc4"}], "type": "compute", "id": "02640b079181463f895f4517fa543535", "name": "nova"}, {"endpoints": [{"region_id": "RegionOne", "url": "http://controller:9292", "region": "RegionOne", "interface": "admin", "id": "8bcb202f5f8240dbb446f0e3ed582dfa"}, {"region_id": "RegionOne", "url": "http://controller:9292", "region": "RegionOne", "interface": "public", "id": "e7b18522287e4b638d76ff985133328c"}, {"region_id": "RegionOne", "url": "http://controller:9292", "region": "RegionOne", "interface": "internal", "id": "f25fac4b28e84598a8e9308d82183c9f"}], "type": "image", "id": "35322d214f6a443b902976e4f696400c", "name": "glance"}, {"endpoints": [{"region_id": "RegionOne", "url": "http://controller:5000/v3", "region": "RegionOne", "interface": "internal", "id": "3d3eb84648ae4ed9adc854ca74a9f066"}, {"region_id": "RegionOne", "url": "http://controller:5000/v3", "region": "RegionOne", "interface": "public", "id": "75f684ee85334928bd39cd0cc5ecc9b2"}, {"region_id": "RegionOne", "url": "http://controller:35357/v3", "region": "RegionOne", "interface": "admin", "id": "fdd31508be4e455a92ac3d2993a834ed"}], "type": "identity", "id": "3bfd9a2f671c4643bb125eb413b4c6be", "name": "keystone"}, {"endpoints": [{"region_id": "RegionOne", "url": "http://controller:9696", "region": "RegionOne", "interface": "admin", "id": "29d0d44fbcd441ef88fe2b6d414d373f"}, {"region_id": "RegionOne", "url": "http://controller:9696", "region": "RegionOne", "interface": "internal", "id": "3b7a64010336434abb0a1ce4c621c25a"}, {"region_id": "RegionOne", "url": "http://controller:9696", "region": "RegionOne", "interface": "public", "id": "6e5342da57d74da49830deb6aee08a3d"}], "type": "network", "id": "eab2ce36306845469ddfb448fcaebb86", "name": "neutron"}], "user": {"domain": {"id": "34fb0c49dd1440d69c89d1418af9c857", "name": "default"}, "id": "ab8d4b68012b4d67b9445de9108c3945", "name": "nova"}, "audit_ids": ["RrmxD2O1QP6p5SQS60YwEw"], "issued_at": "2016-06-11T14:36:54.000000Z"}}
</code>
</pre>
Sau khi thành công, ta được cấp phát một token sử dụng để xác thực và ủy quyền khi thực hiện các cURL command tác động tới API. Ở đây ta nhận được token: <code>gAAAAABXXCIGD14rLiR-fjcCXhwp4krp7DpsIJhPKYedtRgpRtQBQTcK_XpTBvjh7KrsEog4rzsrHEpk_zi-dQ72796X3JaaY3V2sAE1osGFZ-aHosOcqhu0EgJTUnfQsCOCIJzwReTrQH6MY76xXtitvZxioTzy2ZCa-AkMTV9pUlMV-863TMA</code>
<br>
Ngoài token, để thực hiện các cURL command, ta cần phải có danh sách endpoint của các dịch vụ bằng việc thực hiện lệnh sau:
<pre>
<code>
root@controller:~/img-list# openstack endpoint list
+----------------------------------+-----------+--------------+--------------+---------+-----------+-------------------------------------------+
| ID                               | Region    | Service Name | Service Type | Enabled | Interface | URL                                       |
+----------------------------------+-----------+--------------+--------------+---------+-----------+-------------------------------------------+
| 29d0d44fbcd441ef88fe2b6d414d373f | RegionOne | neutron      | network      | True    | admin     | http://controller:9696                    |
| 3132ada4c76b49a3a2c4f75a0054fc88 | RegionOne | nova         | compute      | True    | admin     | http://controller:8774/v2.1/%(tenant_id)s |
| 3b7a64010336434abb0a1ce4c621c25a | RegionOne | neutron      | network      | True    | internal  | http://controller:9696                    |
| 3d3eb84648ae4ed9adc854ca74a9f066 | RegionOne | keystone     | identity     | True    | internal  | http://controller:5000/v3                 |
| 6e5342da57d74da49830deb6aee08a3d | RegionOne | neutron      | network      | True    | public    | http://controller:9696                    |
| 75f684ee85334928bd39cd0cc5ecc9b2 | RegionOne | keystone     | identity     | True    | public    | http://controller:5000/v3                 |
| 8bcb202f5f8240dbb446f0e3ed582dfa | RegionOne | glance       | image        | True    | admin     | http://controller:9292                    |
| bf4d2f86b99e429a98ff0f01953c85d6 | RegionOne | nova         | compute      | True    | public    | http://controller:8774/v2.1/%(tenant_id)s |
| e7b18522287e4b638d76ff985133328c | RegionOne | glance       | image        | True    | public    | http://controller:9292                    |
| f25fac4b28e84598a8e9308d82183c9f | RegionOne | glance       | image        | True    | internal  | http://controller:9292                    |
| fb671db7f0b646e583f92abf17bc2bc4 | RegionOne | nova         | compute      | True    | internal  | http://controller:8774/v2.1/%(tenant_id)s |
| fdd31508be4e455a92ac3d2993a834ed | RegionOne | keystone     | identity     | True    | admin     | http://controller:35357/v3                |
+----------------------------------+-----------+--------------+--------------+---------+-----------+-------------------------------------------+
</code>
</pre>
Ở đây, ta chỉ lấy endpoint của dịch vụ <code>glance</code>. Thực hiện thiết lập biến môi trường cho endpoint của dịch vụ glance và token (để tiện sử dụng cho các cURL command):
<pre>
<code>
export OS_AUTH_TOKEN=gAAAAABXXCIGD14rLiR-fjcCXhwp4krp7DpsIJhPKYedtRgpRtQBQTcK_XpTBvjh7KrsEog4rzsrHEpk_zi-dQ72796X3JaaY3V2sAE1osGFZ-aHosOcqhu0EgJTUnfQsCOCIJzwReTrQH6MY76xXtitvZxioTzy2ZCa-AkMTV9pUlMV-863TMA
export OS_IMAGE_URL=http://controller:9292 
</code>
</pre>
</li>
<li><h4>b. cURL command liệt kê danh sách các image</h4>
<pre>
<code>
curl -s \
  $OS_IMAGE_URL/v2/images \
  -X GET \
  -H "X-Auth-Token: $OS_AUTH_TOKEN" \
  
{"images": [{"status": "active", "name": "fedora", "tags": [], "container_format": "bare", "created_at": "2016-06-11T12:40:28Z", "size": 234363392, "disk_format": "qcow2", "updated_at": "2016-06-11T12:48:32Z", "visibility": "private", "self": "/v2/images/ec62a8ee-6ab0-4118-9029-a81ca92b8d43", "min_disk": 0, "protected": false, "id": "ec62a8ee-6ab0-4118-9029-a81ca92b8d43", "file": "/v2/images/ec62a8ee-6ab0-4118-9029-a81ca92b8d43/file", "checksum": "38d62e2e1909c89f72ba4d5f5c0005d5", "owner": "5274cf4a29534f68bb3305333aef3606", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}, {"status": "active", "name": "cirros", "tags": [], "container_format": "bare", "created_at": "2016-04-21T08:59:42Z", "size": 13287936, "disk_format": "qcow2", "updated_at": "2016-04-21T08:59:42Z", "visibility": "public", "self": "/v2/images/ce64b039-6e40-4f13-b44e-5813c62dc082", "min_disk": 0, "protected": false, "id": "ce64b039-6e40-4f13-b44e-5813c62dc082", "file": "/v2/images/ce64b039-6e40-4f13-b44e-5813c62dc082/file", "checksum": "ee1eca47dc88f4879d8a229cc70a07c6", "owner": "5274cf4a29534f68bb3305333aef3606", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}], "schema": "/v2/schemas/images", "first": "/v2/images"}
</code>
</pre>
</li>
<li><h4>c. cURL command hiển thị thông tin của một image</h4>
Ví dụ ở đây lấy thông tin của image fedora, sử dụng id của image fedora lấy được từ lệnh liệt kê các image ở mục b.
<pre>
<code>
curl -s \
   $OS_IMAGE_URL/v2/images/ec62a8ee-6ab0-4118-9029-a81ca92b8d43 \
   -X GET \
   -H "X-Auth-Token: $OS_AUTH_TOKEN" \
   
{"status": "active", "name": "fedora", "tags": [], "container_format": "bare", "created_at": "2016-06-11T12:40:28Z", "size": 234363392, "disk_format": "qcow2", "updated_at": "2016-06-11T12:48:32Z", "visibility": "private", "self": "/v2/images/ec62a8ee-6ab0-4118-9029-a81ca92b8d43", "min_disk": 0, "protected": false, "id": "ec62a8ee-6ab0-4118-9029-a81ca92b8d43", "file": "/v2/images/ec62a8ee-6ab0-4118-9029-a81ca92b8d43/file", "checksum": "38d62e2e1909c89f72ba4d5f5c0005d5", "owner": "5274cf4a29534f68bb3305333aef3606", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}
</code>
</pre>
</li>
<li><h4>d. cURL command tạo image mới (chưa có dữ liệu)</h4>
Giả sử ở đây tạo mới image có tên "cirros-test" (chưa có dữ liệu)
<pre>
<code>
curl -i -X POST -H "X-Auth-Token: $OS_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"name": "cirros-test", "tags": ["cirros"]}' \
    $OS_IMAGE_URL/v2/images

HTTP/1.1 201 Created
Content-Length: 559
Content-Type: application/json; charset=UTF-8
Location: http://10.10.10.132:9292/v2/images/bb9b711d-0e48-42f4-9ee3-45548f5309bf
X-Openstack-Request-Id: req-e10e4203-6bcf-416b-9db5-44bcf27af55d
Date: Sat, 11 Jun 2016 15:19:35 GMT

{"status": "queued", "name": "cirros-test", "tags": ["cirros"], "container_format": null, "created_at": "2016-06-11T15:19:34Z", "size": null, "disk_format": null, "updated_at": "2016-06-11T15:19:34Z", "visibility": "private", "self": "/v2/images/bb9b711d-0e48-42f4-9ee3-45548f5309bf", "min_disk": 0, "protected": false, "id": "bb9b711d-0e48-42f4-9ee3-45548f5309bf", "file": "/v2/images/bb9b711d-0e48-42f4-9ee3-45548f5309bf/file", "checksum": null, "owner": "2cf5f2f7d9754c2abb0059501c031ef9", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}
</code>
</pre>
</li>
<li><h4>e. cURL command cập nhật các thuộc tính của image</h4>
Ở đây ta sẽ cập nhật 2 thuộc tính quan trọng để tạo image mới là: <code>disk_format</code> và <code>container_format</code>
<pre>
<code>
curl -i -X PATCH -H "X-Auth-Token: $OS_AUTH_TOKEN" \
-H "Content-Type: application/openstack-images-v2.1-json-patch" \
-d '[{"op": "add", "path": "/disk_format", "value": "qcow2"}, {"op": "add", "path": "/container_format", "value": "bare"}]' \
$OS_IMAGE_URL/v2/images/bb9b711d-0e48-42f4-9ee3-45548f5309bf

HTTP/1.1 200 OK
Content-Length: 564
Content-Type: application/json; charset=UTF-8
X-Openstack-Request-Id: req-417345a8-7b1a-41d0-8bb8-df13046b66c7
Date: Sat, 11 Jun 2016 15:53:42 GMT

{"status": "queued", "name": "cirros-test", "tags": ["cirros"], "container_format": "bare", "created_at": "2016-06-11T15:19:34Z", "size": null, "disk_format": "qcow2", "updated_at": "2016-06-11T15:53:42Z", "visibility": "private", "self": "/v2/images/bb9b711d-0e48-42f4-9ee3-45548f5309bf", "min_disk": 0, "protected": false, "id": "bb9b711d-0e48-42f4-9ee3-45548f5309bf", "file": "/v2/images/bb9b711d-0e48-42f4-9ee3-45548f5309bf/file", "checksum": null, "owner": "2cf5f2f7d9754c2abb0059501c031ef9", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}
</code>
</pre>
Lúc này image vẫn chưa được khởi tạo hoàn toàn và đang trong trạng thái "queued":
<pre>
<code>
root@controller:~/img-list# openstack image list
+--------------------------------------+-------------+--------+
| ID                                   | Name        | Status |
+--------------------------------------+-------------+--------+
| bb9b711d-0e48-42f4-9ee3-45548f5309bf | cirros-test | queued |
| ec62a8ee-6ab0-4118-9029-a81ca92b8d43 | fedora      | active |
| ce64b039-6e40-4f13-b44e-5813c62dc082 | cirros      | active |
+--------------------------------------+-------------+--------+
</code>
</pre>
</li>
<li><h4>f. cURL command upload dữ liệu nhị phân của image lên (tải lên dữ liệu cho image đã khởi tạo)</h4>
Sau khi thiết lập hai thuộc tính <code>disk_format</code> và <code>container_format</code>, tiến hành upload dữ liệu image lên để hoàn thành quá trình tạo image:
<pre>
<code>
curl -i -X PUT -H "X-Auth-Token: $OS_AUTH_TOKEN" \
	-H "Content-Type: application/octet-stream" \
	-d @/root/img-list/cirros-0.3.4-x86_64-disk.img \
	$OS_IMAGE_URL/v2/images/bb9b711d-0e48-42f4-9ee3-45548f5309bf/file

HTTP/1.1 100 Continue

HTTP/1.1 204 No Content
Content-Type: text/html; charset=UTF-8
Content-Length: 0
X-Openstack-Request-Id: req-4f88e148-5dd5-4e21-a08d-af0537b7e8b8
Date: Sat, 11 Jun 2016 15:55:36 GMT
</code>
</pre>
Tiến hành kiểm tra lại trạng thái của image cirros-test vừa mới khởi tạo, ta sẽ thấy image này ở trạng thái "active", nghĩa là sẵn sàng để sử dụng:
<pre>
<code>
root@controller:~/img-list# openstack image list
+--------------------------------------+-------------+--------+
| ID                                   | Name        | Status |
+--------------------------------------+-------------+--------+
| bb9b711d-0e48-42f4-9ee3-45548f5309bf | cirros-test | active |
| ec62a8ee-6ab0-4118-9029-a81ca92b8d43 | fedora      | active |
| ce64b039-6e40-4f13-b44e-5813c62dc082 | cirros      | active |
+--------------------------------------+-------------+--------+
</code>
</pre>
</li>
<li><h4>g. cURL command xóa image</h4>
Tiến hành xóa image cirros-test
<pre>
<code>
curl -i -X DELETE -H "X-Auth-Token: $OS_AUTH_TOKEN" \
     $OS_IMAGE_URL/v2/images/bb9b711d-0e48-42f4-9ee3-45548f5309bf

HTTP/1.1 204 No Content
Content-Type: text/html; charset=UTF-8
Content-Length: 0
X-Openstack-Request-Id: req-1e756ecb-e954-4c8b-b96b-0f3f3afb63ff
Date: Sat, 11 Jun 2016 15:57:54 GMT
</code>
</pre>
Kiểm tra lại danh sách các image, ta thấy image cirros đã bị loại bỏ:
<pre>
<code>
root@controller:~/img-list# openstack image list
+--------------------------------------+--------+--------+
| ID                                   | Name   | Status |
+--------------------------------------+--------+--------+
| ec62a8ee-6ab0-4118-9029-a81ca92b8d43 | fedora | active |
| ce64b039-6e40-4f13-b44e-5813c62dc082 | cirros | active |
+--------------------------------------+--------+--------+
</code>
</pre>
</li>
</ul>
</div>

<h3><a name="rest">9.3. Gửi yêu cầu tới API sử dụng REST client trên trình duyệt</a></h3>
<div>
<ul>
<li><h4>a. Cài đặt extention REST client trên trình duyệt</h4>
Hai trình duyệt phổ thông là Firefox là Chrome đều cung cấp addon (extention) REST client. Demo dưới đây sử dụng extention Advanced REST client trên trình duyệt Chrome
<br><br>
<img src="http://i.imgur.com/T669fOK.png"/>
<br><br>
</li>
<li><h4>b. Lấy Token</h4>
Sử dụng api <code>/v3/auth/tokens</code>, gửi thông điệp <code>POST</code> tới api với header và payload phù hợp. Ví dụ ở đây xin cấp phát token ở phạm vị project (project scoped), do đó ta phải chỉ rõ <b>user id</b> và <b>project id</b> của project mà trên đó user được gán roles. 
<br><br>
<img src="http://i.imgur.com/eH4OClR.png"/>
<br><br>
Nếu thành công, bản tin phản hồi trở về với mã 200 OK như hình dưới, trả lại cho ta một token với role tương ứng. Chú ý lưu lại token này để thực hiện các yêu cầu khác, tương tự như khi ta sử dụng cURL.
<br><br>
<img src="http://i.imgur.com/1mXEyVK.png"/>
<br><br>
</li>
<li><h4>c. Gửi yêu cầu liệt kê danh sách các image</h4>
Sử dụng token nhận được gửi yêu cầu lấy danh sách các image tới API <code>/v2/images</code>, sử dụng token vừa nhận được ở trên chèn vào header của bản tin request.
<br><br>
<img src="http://i.imgur.com/uGnYina.png"/>
<br><br>
Nếu thành công ta sẽ nhận được bản tin phản hồi với danh sách các images.
<br><br>
<img src="http://i.imgur.com/A5E1ikc.png"/>
<br><br>
</li>
<li><h4>d. Lấy thông tin về image</h4>
Tương tự như khi sử dụng cURL, ta lấy id của image nào đó trong danh sách các image trả về để làm tham số cho request lấy thông tin image đó tới api <b>/v2/images/image_id</b>.  Như mọi request khác, ta phải đưa token vào header để xác thực và ủy quyền. Giả sử ở đây ta lấy thông tin của image <b>fedora</b> với id tương ứng.
<br><br>
<img src="http://i.imgur.com/6BUhcrT.png" />
<br></br>
Nếu request thành công, ta sẽ nhận được thông tin phản hồi với thông tin chi tiết của image fedora như sau.
<br><br>
<img src="http://i.imgur.com/U3LfTe8.png" />
<br></br>
</li>
</ul>
Các thao tác khác hoàn toàn tương tự như khi sử dụng cURL command, chú ý các tham số trên URI, header, payload, phương thức gửi request. 
</div>
<i><b>Chú ý:</b> Để biết thông tin chi tiết về cách sử dụng và tương tác với các API liên quan tới glance cũng như các dịch vụ khác, tham khảo <a href="http://developer.openstack.org/api-ref-image-v2.html" target="_blank">tại đây.</a></i>
</div>

<h2><a name="cache">10. Glance image cache</a></h2>
<div>
<ul>
<li>Việc kích hoạt Glance cache thường được khuyên khi sử dụng hệ thống lưu trữ mặc định là <code>file</code>, tuy nhiên nếu sử dụng Ceph RBD backend sẽ có một số khác biệt.</li>
<li>Kích hoạt glance cache dẫn tới việc tạo ra cached của image đó trong thư mục <code>/var/lib/glance/image-cache</code> mỗi lần boot máy ảo lên. Giả sửa ta có một máy ảo với kích thước VM image là cỡ 50GB, nếu như mỗi lần boot mà lại tạo cached như vây, hệ thống lưu trữ sẽ sớm bị cạn kiệt, trừ khi ta mount thư mục <code>/var</code> vào một ổ lưu trữ lớn.</li>
<li>Cache sẽ được kích hoạt khi có image đưa vào thư mục <code>/var/lib/nova/instances/_base</code>, điều này xảy ra trong một số trường hợp như sau:
<ul>
<li>Sử dụng OpenStack phiên bản Juno nhưng sử dụng container format là QCOW2</li>
<li>Sử dụng OpenStack phiên bản trước Juno mà không áp dụng bản vá hỗ trợ COW clones.</li>
</ul>
Như vậy nghĩa là người dùng chỉ sử dụng RAW images và COW cloens trong Nova thì sẽ không bị ảnh hưởng, bởi lẽ chẳng có image nào đưa vào thư mục <code>/var/lib/nova/instances/_base</code> cả. Mọi việc diễn ra ở cấp độ của Ceph (thực hiện snapshot image và clone image)
</li>
<li>Để kích hoạt hay tắt glance cache, tiến hành cấu hình trong file <code>/etc/glance/glance-api.conf</code>. Để kích hoạt cached, tìm tới dòng sau và cấu hình:
<pre>
<code>
[paste_deploy]
flavor = keystone+cachemanagement
</code>
</pre>
Tắt glance cache:
<pre>
<code>
[paste_deploy]
flavor = keystone
</code>
</pre>
Sau đó khởi động lại glance để áp dụng các thay đổi:
<pre>
<code>
sudo glance-control all restart
</code>
</pre>
</li>
</ul>
</div>

<h2><a name="ref">11. Tham khảo</a></h2>
<div>
[1] - <a href="http://docs.openstack.org/developer/glance/architecture.html">http://docs.openstack.org/developer/glance/architecture.html</a>
<br>
[2] - <a href="http://www.sparkmycloud.com/blog/openstack-glance">http://www.sparkmycloud.com/blog/openstack-glance</a>
<br>
[3] - <a href="http://docs.openstack.org/user-guide/common/cli_manage_images.html">http://docs.openstack.org/user-guide/common/cli_manage_images.html</a>
<br>
[4] - <a href="http://docs.openstack.org/developer/glance/configuring.html#configuring-logging-in-glance">http://docs.openstack.org/developer/glance/configuring.html#configuring-logging-in-glance</a>
<br>
[5] - <a href="http://docs.openstack.org/cli-reference/openstack.html">http://docs.openstack.org/cli-reference/openstack.html</a>
<br>
[6] - <a href="http://docs.openstack.org/user-guide/cli_manage_images_curl.html">http://docs.openstack.org/user-guide/cli_manage_images_curl.html</a>
<br>
[7] - <a href="http://developer.openstack.org/api-ref-image-v2.html">http://developer.openstack.org/api-ref-image-v2.html</a>
<br>
[8] - <a href="https://www.sebastien-han.fr/blog/2014/11/03/openstack-glance-disable-cache-management-while-using-ceph-rbd/">https://www.sebastien-han.fr/blog/2014/11/03/openstack-glance-disable-cache-management-while-using-ceph-rbd/</a>
</div>

