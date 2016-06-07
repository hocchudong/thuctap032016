#Báo cáo về OpenStack Glane.

****

#Mục lục.
 <ul>
 <li>[Glane là gì?] (#glane)</li>
 <li>[Glane component] (#component)</li>
 <li>[Glane architecture] (#architecture)</li>
 <li>[Glane format] (#format)
  <ul>
  <li>[Disk format] (#diskformat)</li>
  <li>[Container format] (#containerformat)</li>
  </ul>
 </li>
 <li>[Glane Status Flow] (#flow)</li>
 <li>[Glane configuration file] (#config)</li>
 <li>[Image and Instance] (#so1)</li>
 </ul>

<a name="glane"></a>
##OpenStack Glane là gì?
- OpenStack Glane là một image service bao gồm : discovering, registering, retrieving cho cho disk và các server image. OpenStack Glane có một trung tâm lưu trữ cho các vitual image. OpenStack Glane có RESTful API cho phép truy vấn vào VM image metadata của actual image. VM image được tạo thông qua Glane có thể được lưu tại các store khác nhau từ file system, đến object storage cũng như OpenStack Swift project.
- Trong Glane, image là kho các template sử dụng để chạy các instance mới. Glane được thiết kế như một service duy nhất cho nhiều tổ chức lớn cần tạo các vitual disk image.

<a name="component"></a>
##Glane component.

- Glane có các thành phần sau : 
 <ul>
 <li>Glane-api : Chấp nhận các API call cho image discovery, retrieval and storage.</li>
 <li>Glane-registry : Đó là các store, process, và retrie metadata information cho các image.</li>
 <li>database : Là nơi lưu trữ image metadata.</li>
 <li>storage repository : Đó là thành phần thêm vào cho đủ nằm ngoài các thành phần OpenStack giống như file system, Amazon s3, and HTTP cho các image storage.</li>
 </ul>

![scr1](http://i.imgur.com/No2Ylyo.png)

- Glane API yêu cầu image từ end-users hoặc NOVA component và có thể lưu trữ trong object storage swift hoặc các kho lưu trữ khác.
- Image service hỗ trợ một số back-end store như sau: 
 <ul>
 <li>File system : OpenStack Image service mặc lưu trữ các vitual machine image trong file system back-end. Thông thường back-end write các image file tới local file system.</li>
 <li>Object storage : OpenStack service có tính sẵn sàng cao cho việc lưu trữ các object.</li>
 <li>Block Storage : OpenStack service có tính sẵn sàng cao cho việc lưu trữ các block.</li>
 <li>VMware : ESX/ESXi hoặc vCenter server mục tiêu hướng đến hệ thống.</li>
 <li><S3 : The Amazon S3 service.</li>
 <li>HTTP : OpenStack Image Service có thể đọc các vitual machine service có sẵn trên internet sử dụng giao thức HTTP. This store read only.</li>
 <li>RADOS Block Device (RBD) : Kho image bên trong một cluster lưu trữ Celp sử dụng Celp interface.</li>
 <li>Sheepdog : Một hệ thống phân phối lưu trữ cho QEMU/KVM.</li>
 <li>GridFS : Lưu trữ image sử dụng mongoDB.</li>
 </ul>

<a name="architecture"></a>
##Glane Architecture.

- Glane có một kiến trúc client-server và cung cấp RESTful API thông qua đó request từ server được thực hiện. Request từ client được chấp nhận thông qua API và chờ Keystone xác thực. Glane domain là bộ điều khiển quản lý tất cả các hoạt động nội bộ, được chia thành các layer mỗi layer thực hiện nhiệm vụ riêng của mình.
- Glane store là lớp giao tiếp giữa glane và và storage back end ở ngoài glane hoặc local filesystem và nó cung cấp giao diện thống nhất để truy cập. Glane sử dụng SQL central Database để truy cập cho tất cả các thành phần trong hệ thống.
- Một số chú ý trong Glane architecture.
 <ul>
 <li>Ckient : Bất kỳ Application nào sử dụng Glane server đều là client.</li>
 <li>RESTAPI : Có thể gọi chức năng của Glane thông qua REST.</li>
 <li>Database Abstraction Layer (DAL) : Một giao diên lập trình ứng dụng , trong đó hợp nhất các thông tin liên lạc giữa Glane và DB.</li>
 <li>Glane store : Tương tác giữa Glane và những backed khác.</li>
 <li>Registry Layer : Tùy chọn tổ chức một lớp trao đổi thông tin an toàn giữa các miền và các DAL bằng cách sử dụng một dịch vụ riêng biệt.</li>
 </ul>

![scr](http://i.imgur.com/GwZ52jD.png)

<a name="format"></a>
##Glane Format.

- Khi upload một image lên Glane chúng ta cần xác định rõ các định dạng của Vitual machine images. Glane hỗ trợ nhiều kiểu định dạng như Disk format và Contianer format. Vitual Disk tương tự như server'boot driver chỉ cô đọng trong một tập tin.

<a name="diskformat"></a>
###Disk format.

- Disk format của một vitual machine image là định dạng cơ bản của file image disk cơ bản. Các định dạng được hỗ trợ bởi OpenStack Glane.

![scr2](http://i.imgur.com/pZXIyv3.png)

<a name="containerformat"></a>
###Container format.

- OpenStack cũng hỗ trợ những concept về Container. Trong đó lưu trữ định dạng tập tin có chứa metadata bổ sung cho vitual machine thực tế. Có thể hiểu Container format như sau. 

EX : Để kiểm tra được một Image nào đó có phải chúng ta cần hay không người ta phải chạy cả một cái Image đó mới có thể kiểm tra được , tuy nhiên chúng ta có thể dựa vào Container format để kiểm tra làm cho chúng ta không cần phải mất công chạy cả cái Image đó để kiểm tra bởi vì cái COntainer format chứa công thông tin về (tên hệ điều hành, định dạng, nơi lưu trữ,....).

![scr](http://i.imgur.com/hyEzNiC.png)

- Những định dạng Container format mà OpenStack hỗ trợ : 

![scr](http://i.imgur.com/P2bu1qw.png)

- Chú ý rằng Container Format Không được sử dụng bởi Glane hoặc các thành phần khác của OpenStack. Vì vậy "bare" được cho là container format trong khi chúng ta tải lên một image trong Glane. Bare nghĩa là nằm ngoài container.
 
<a name="flow"></a>
##Glane Status Flow.

- Glane Status Flow cho chúng ta thấy tình trạng của Image trong khi chúng ta tải lên. Khi chúng ta khởi tại một image, bước đầu tiên là queuing. Image sẽ được sắp xếp vào một hàng đợi trong một thời gian ngắn để định danh (hàng đợi này dành cho image) và sẵn sàng được upload. Sau khi kết thúc thời gian queuing thì image sẽ được upload đến "Saving" , tuy nhiên ở đây không phải image nào cũng được tải lên hoàn toàn. Những Image nào được tải lên hoàn toàn sẽ trong trạng thái "Active". Khi upload không thành công nó sẽ đến trạng thái "killed" hoặc "deleted" . Chúng ta có thể tắt và tái kích hoạt một Image đang "Active" hoàn toàn bằng một lệnh. 
- Chi tiết về Glane Status Flow :

![scr](http://i.imgur.com/Jt2uyvo.png)

- Các trạng thái trong Glane Status Flow :
 <ul>
 <li>queued : Việc nhận diện một Image đã được dành cho một image trong registry glane . Các dữ liệu image nào được tải lên glane mà kích thước image không được rõ ràng sẽ thiết lập để không được tạo.</li>
 <li>Saving : Biểu thị rằng dữ liệu thô của image đang được tải lên Glane. Khi một iamge đăng ký với một call đến POST/image và có một x-image-meta-location vị trí tiêu đề hiện tại, image đó sẽ không bao giờ được trong tình trạng tiết kiệm (như dữ liệu Image đã có sẵn ở vị trí khác).</li>
 <li>Active : Biểu thị một image đó là hoàn toàn có sẵn trong Glane. Điều này xảy ra khi các dữ liệu image được tải lên hoặc kích thước image được rõ ràng để thiết lập được tạo.</li>
 <li>Deactiveted : Biểu thị rằng quyền truy cập vào Image không được phép truy cập từ bất kỳ ai cả admin-user.</li>
 <li>killed : Biểu thị một lỗi xảy ra trong quá trình truyền tải dữ liệu của một image, và image là không thể đọc được.</li>
 <li>deleted : Trong Glane đã giữ lại các thông tin về image, nhưng không còn có sẵn để sử dụng. Một image trong trạng thái này sẽ được gỡ bỏ tự động vào một ngày sau đó.</li>
 </ul>

<a name="config"></a>
##Glane configuration files.

- Glane-api.conf : Cấu hình file cho image service API.
- Glane-registry.conf : Cấu hình file cho glane image registry đó là kho metadata về images.
- Glane-scrubber.conf : Tiện ích sử dụng để làm sạch image đã bị xóa. Multiple glane-scrubber có thể sử dụng chạy một triển khai duy nhất, nhưng chỉ có một lần có thể hành động clean-up scrubber trong scrubber.conf file. 
- Policy.json : Bổ sung truy cập kiểm soát áp dụng cho các image service. Trong này, chúng tra có thể xác định vai trò, chính sách, làm tăng tính bảo mật trong Glane OpenStack.

<a name="so1"></a>
##Image and Instance.

- Khi hình ảnh được lưu trữ như các template. Image service điều khiểu lưu trữ và quản lý image. Instance là những máy ảo độc lập chạu trên các compute node, compute node quản lý các instance. Người dùng có thể khởi động với số lượng bất kỳ các máy ảo cùng image. Mỗi lần thực hiện chạy một máy ảo được thực hiện bằn cách sao chép từ base image, bất kỳ sửa đổi nào trên instance không ảnh hưởng đển các base image. CHúng ta có thể snaphost một instance đang chạy và có thể chạy chúng như một instance khác.
- Khi chạy một instance chúng ta cần xác định các flavor. Đó là đại diện cho tài nguyên ảo. Flavor định xác định bao nhiêu CPU ảo cho một Instance cần có và số lượng RAM sẵn có cho nó, và kích thước của nó trong bộ nhớ tạm của mình. OpenStack cung cấp một thiết lập flavor được xác định từ trước, chúng ta có thể chỉnh sửa các flavor riêng của chúng ta. Sơ đồ dưới đây cho biết tình trạng của hệ thống trước khi lauching an instance. Các image store có số lượng image được xác định trước, compute node chứa CPU có sẵn, bộ nhớ và tài nguyên local disk và cinder-volume chứa số lượng đã được xác định từ trước . 

![scr](http://i.imgur.com/JjCsq5h.png)

- Trước khi chạy một instance chọn một image, flavor và bất kỳ thuôc tính tùy chọn nào . CHọn flavor cung cấp một root volume, dán nhãn là "vda" và một bổ sung vào bộ nhớ tạm thời dán nhãn là "vdb" và cinder-volume được ánh xạ tới ổ đĩa thứ 3 gọi là "vdc".

![scr](http://i.imgur.com/1n7W1ZA.png)

- VDA : Các image được sao chép vào các local disk. VDA là disk đầu tiên mà các instance được truy cập.
- VDB : là một disk tạm có các sản phẩm tạo ra cùng với instance sẽ bị xóa khi kết thức instance.
- VDC : kết nối với cinder-volume sử dụng iSCSI. Sau khi compute node quy định vCPU và tài nguyên bộ nhớ. Các instance boots up từ root volume VDA. Instance chạy và thay đổi dữ liệu trên disk . Nếu volume store nằm trên một mạng riêng biệt , tùy chọn my_block_storage_ip trong tập tin cấu hình storage node sẽ chỉ đạo giao tiếp với compute node.

#Source :
http://www.sparkmycloud.com/blog/openstack-glance/