#OpenStack Glance
OpenStack Glance là một dịch vụ image, cung cấp khám phá, đăng ký và lấy cho disk và server images. Glance là trung tâm kho chứa các images virtual. Glance có RESTful API cho phép truy vấn VM image metadata cũng như thu hồi các images. VM images có sẵn thông qua glance có thể được lưu trữ từ nhiều địa điểm từ hệ thống tập tin đơn giản đến Object Storage System (Switf).

Trong glance, images được lưu dưới dạng các template, được sử dụng để tạo một máy ảo mới. Glance được thiết kế là một dịch vụ độc lập cần thiết cho các disk images ảo, đặt thành các tổ chức. Glance cung cấp giải pháp end-to end cho quản lý image disk của cloud. Nó có thể take snapshots từ những máy ảo đang chạy để sao lưu.

##1. Các thành phần trong Glance.

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing2.png)

- **Glance-API:** Nơi đồng ý các API calls để phát hiện, thu hồi và lưu trữ images.
- **Glance-Registry:** Nơi lưu trữ, xử lý và lấy các thông tin metadata cho images.
- **database:** Lưu trữ các metadata.
- **Storage repository:** Tích hợp với các thành phần bên ngoài khác như hệ thống file thường, Amazon S3 và HTTP cho images.

Glance đồng ý các API request images từ người dùng cuối hoặc các thành phần của NOVA và có thể lưu các file vào Object storage service (swift), hoặc các storage repository khác.

Dịch vụ image hỗ trợ các back end để lưu trữ:

- **File system:** Mặc định, các file images của virtual machine được lưu vào hệ thống file. Đây là giải pháp đơn giản.
- **Object Storage:** The OpenStack highly available service for storing objects.
- **Block storage:** The OpenStack highly available service for storing blocks.
- **Vmware:** ESX/ESXi or vCenter Server target system.
- **S3:** The Amazon S3 service.
- **HTTP**: Openstack image có thể đọc images của máy ảo trên internet thông qua giao thức http. Cách này chỉ có thể đọc.
- **RADOS Block Device (RBD):** Stores images inside of a Ceph storage cluster using Ceph’s RBD interface.
- **Sheepdog:** Hệ thống phân phối lưu trữ cho QEMU/KVM.
- **GridFS:** Lưu trũ images bằng cách sử dụng MongoDB.


##2. Kiến trúc của Glance.
Glance có kiến trúc client-server và cung cấp REST API để request đến server. Request từ client sẽ được đồng ý thông qua REST API và đợi Keystone xác nhận. Glance Domain controller quản lý tất cả hoạt động nội bộ, được chia thành các lớp, mỗi lớp thực hiện các nhiệm vụ riêng.

Glance store là nơi giao tiếp giữa các lớp glance và storage backend bên ngoài hoặc local file system và cung cấp interface thống nhất để truy cập. Glance sử dụng SQL để truy cập cho mỗi thành phần trong hệ thống. 

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing11.png)


Kiến trúc của Glance bao gồm nhiều thành phần:

- **Client:** Bất kỳ một ứng dụng được sử dụng Glance server.
- **REST API:** Các chức năng Glance được phơi bày thông qua REST.
- **Database Abstraction Layer (DAL):** Là một interface cho lập trình ứng dụng. Dùng để thống nhất các thông tin liên lạc giữa Glance và databases.
- **Glance Domain Controller:** Thực hiện các chức năng chính của Glance: authorization, notifications, policies, database connections.
- **Glance Store:** Tương tác giữa Glance và các data stores khác nhau.
- **Registry Layer:** Là lớp tùy chọn, tổ chức các thông tin liên lạc giữa domain và DAL bằng cách sử dụng một dịch vụ riêng biệt.

##3. Glance Formats:
Khi chúng ta uploading một file image đến glance, chúng ta cần xác định formats của Virtual machine images. Glance hỗ trợ nhiều định dạng như Disk format và Container Formats. Virtual disk tương tự như ổ đĩa máy thật, chỉ cô động trong một tập tin. Ảo hóa khác nhau hỗ trợ các disk formats khác nhau.

**Disk format:** Disk format của images máy ảo là định dạng của tập tin image cơ bản. Các nhà cung cấp thiết bị ảo có định dạng khác nhau để đưa ra những thông tin chứa trong một hình ảnh đĩa của máy ảo. Sau đây là các định dạng được hỗ trợ bởi Glance.

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing6.png)


**Container Formats:** Glance cũng hỗ trợ các khái niệm về container format, trong đó mô tả các định dạng tập tin và có chứa metadata để bổ sung vào máy ảo. Lưu ý rằng chuỗi định dạng container hiện không được sử dụng bởi Glance hoặc các thành phần OpenStack khác, vì vậy để an toàn chỉ cần xác định `bare` như là định dạng container nếu bạn không chắc chắc. Sau đây là các container format được hỗ trợ trong Glance.

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing8.png)


Chú ý, Container Formats hiện không được sử dụng bởi Glance hoặc các thành phần khác của OpenStack. Vì vậy, `bare` được cho là định dạng container. Khi chúng ta tải lên một image trong glane, bare có nghĩa là không contrainer.

##4. Glance Status Flow
Glance status flow hiển thị status của image khi chúng ta uploading. Khi chúng ta tạo một image, bước đầu tiên là xếp hàng, image sẽ nằm trong hàng đợi trong một thời gian ngắn để định danh, dành cho image và sẵn sàng upload. Sau khi xếp hạng, image đi đến status `Saving` có nghĩa là không được tải lên hoàn toàn. Một khi image được tải lên hoàn toàn thì status `Active`. Khi uploading thất bại, nó sẽ đi vào trạng thái `killed` hoặc `delete`. Chúng ta có thể tắt và kích hoạt lại các image được tải lên bằng cách sử dụng dòng lệnh.
Ta có sơ đồ dưới: 
![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing1.jpg)


- **queued:** Việc nhận dạng hình ảnh được dành cho Glance registry. Không có dữ liệu image nào được tải lên Gance và kích thước image không được set 0 khi tạo.
- **saving:** Biểu thị dữ liệu raw của images khi bắt đầu được upload lên glance. Khi image được đăng ký với lệnh call to POST /images và header hiện tại là `x-image-meta-location`, image đó sẽ không bao giờ được trong tình trạng `saving` (như dữ liệu image đã có sẵn ở một vị trí khác). 

- **active:** Biểu thị image có sẵn trong Glance. Điều này xảy ra khi image data được tải lên, hoặc kích thước hình ảnh được thiết về 0 khi tạo.

- **deactivated:** Biểu thị truy cập đến image data không được phép với bất kỳ user nào không phải là admin. Nghiêm cấm các hoạt động như image export và image cloning có thể yêu cầu image data.

- **killed:** Biểu thị rằng một lỗi xảy ra trong quá trình tải image lên, và image này không đọc được.

- **delete:** Glance giữ lại các thông tin về image, nhưng nó không còn sẵn để sử dụng. Một image trong state sẽ được gỡ bỏ tự động vào một ngày sau đó.
- **Deactivating and Reactivating an image:** Chúng ta có thể deactive tạm thời 1 image. Sau đó có thể active lại hoặc loại bỏ nó. 

##5. Glance Configuration Files
- **Glance-api.conf:** File cấu hình api.
- **Glance-registry.conf:** File cấu hình registry, là nơi lưu trữ metadata của images.
- **Glance-scrubber.conf:** Utility used to clean up images that have been deleted. Nhiều glance-scrubber có thể chạy trên một deployment. Tuy nhiên, chỉ có một hành động clean-up scrubber trong glance-scrubber.conf. Clean-up scrubber phối hợp với các glance scrubbers khác bằng cách duy trì một hàng đợi những image cần được hủy bỏ. Nó cũng quy định cụ thể các mục cấu hình quan trọng như thời gian giữa các lần chạy, chiều dài thời gian của hình ảnh  có thể được cấp phát trước khi họ xóa cũng như các lựa chọn kết nối registry. Nó có thể chạy như một công việc định kỳ hoặc long-running daemon.

- **policy.json:** Bổ sung kiểm soát truy cập cho image service. Chúng ta có thể xác định vai trò, chính sách, bảo mật trong glance.

##6. Image and Instance
Như đã nói ở trên, Disk images được lưu trữ dưới dạng các tamplate. Dịch vụ Image điều khiển lưu trữ và quản lý các images. Instance là các máy ảo độc lập mà chạy trên compute node, compute node quản lý các instance. Người dùng có thể khởi động bất kỳ số lượng các instance từ các image giống nhau.Mỗi instance được lauched được thực hiện bằng cách sao chép base image, bất kỳ sửa đổi về instance không ảnh hưởng đến base image. Chúng ta có thể take snapshot instance đang chạy và có thể được sử dụng để khởi động các instance khác.

Khi chúng ta khởi động một instance, chúng ta cần phải xác định flavor, là đại diện cho tài nguyên ảo. Flavors xác định cpu, ram có sẵn, kích thước ổ đĩa. OpenStack dung cấp các flavor được xác định trước, và chúng ta có thể tạo và sửa các flavors theo ý mình.

Sơ đồ dưới đây cho biết tình trạng hệ thống trước khi launching một instance. Các image store, có số lượng image được xác định trước, compute nod chứa vcpu sẵn, bộ nhớ và tài nguyên đĩa địa phương và cinder-volume chứa số lượng contains number được xác định trước.

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing2.jpg)



Trước khi launching chọn một image, flavor và bất kỳ thuộc tính tùy chọn.flavor được lựa chọn cung cấp một root volume, dán nhãn là VDA và lưu trữ tạm thời bổ sung được dán nhãn là VDB và cinder-volume là ánh xạ tới ảo đĩa thứ ba và gọi nó là VDC.

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/new.jpg)


Trong hình này, các image base được sao chép vào local disk từ các image store. VDA là đĩa đầu tiên mà các instances truy cập, các instance bắt đầu nhanh hơn nếu kích thước của image là nhỏ hơn như ít dữ liệu cần phải được sao chép trên mạng. VDB là một đĩa trống tạm thời được tạo ra dùng với instance, nó sẽ được xóa khi dụ chấm dứt.

VDC kết nối với cinder-volume sử dụng iSCSI. Sau khi compute node quy định các vCPU và tài nguyên bộ nhớ, các instance khởi động lên từ khối lượng gốc vda. Instance chạy và thay đổi dữ liệu trên các đĩa. Nếu volume store nằm trên một mạng riêng biệt, tùy chọn `my_block_storage_ip` quy định trong tập tin cấu hình storage node chỉ đạo lưu lượng dữ liệu image với các compute node.

Khi instance được xóa bỏ, the state is reclaimed with the exception of the persistent volume. Việc lưu trữ tạm thời bị purged; bộ nhớ và tài nguyên vCPU được giải phóng. Những image vẫn không thay đổi trong suốt quá trình này.

##7. Tài liệu tham khảo
[http://www.sparkmycloud.com/blog/openstack-glance/](http://www.sparkmycloud.com/blog/openstack-glance/)
[http://docs.openstack.org/developer/glance/formats.html](http://docs.openstack.org/developer/glance/formats.html)




