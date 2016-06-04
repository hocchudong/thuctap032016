#Báo cáo tìm hiểu project glance

##Mục lục

##1.Tổng quan

- Glance là một dịch vụ trong openstack dùng để khám phá, đăng ký, khôi phục lại đĩa và image máy chủ

- Dùng RESTful API để truy vấn VM image và khôi phục lại image thực tế

- Lưu trữ image đa dạng từ định dạng lưu trữ, nơi lưu trữ

- Các image lưu trữ như nguyên mẫu để chạy thực thể mới

- Glance có thể hoạt động độc lập

- Có thể tạo snapshot để khôi phục dữ liệu VM

##2.Khái niệm

- Glance-api:chấp nhận lời gọi API	để khám phá, phục hồi và lưu trữ

- Glance-registry:lưu trữ,xử lý, lấy dữ liệu cho image.

- database: lưu trữ dữ liệu image thường là MySQL hoặc SQlite

- storage repository:tích hợp thành phần bên ngoài như Amazon S3 và HTTP cho image

- image cache:mặc định là bị vô hiệu hóa,nhưng có thể hoạt động bằng việc cấu hình bỏi API máy chủ,lưu trữ sao chép của image để phục vụ nhiều API máy chủ cùng lúc

- File system:mặc định lưu trữ đĩa ảo trong hệ thống lưu trữ 

- Object Storage:dịch vụ cấp cao lưu trữ đối tượng

- Block storage:dịch vụ cấp cao lưu trữ khối dữ liệu

- VMWare:ESX/ESXi hoặc vCenter Server

- S3:dịch vụ Amazone S#

- HTTP: Glance đọc đĩa ảo trên internet qua HTTP,kho dữ liệu này ở dạng chỉ được đọc

- RADOS Block Device (RBD):	lưu trữ images trong cụm cơ sở dữ liệu Ceph bởi giao diện Ceph’s RBD

- Sheepdog:hệ thông phân phối lưu trữ cho QEMU/KVM

- GridFS:lưu trữ bỏi MongoDB

- Glance-api.conf: Tập tin cấu hình cho dịch vụ image API.

- Glance-scrubber.conf:tiện ích xóa hoàn toàn các images bị xóa.Có thể triển khai nhiều glance-scrubber có thể chạy nhưng chỉ có 1 cái chạy trong file scrubber.conf file 

##3.Kiến trúc

- Client:ứng dựng sử dụng Glance

- REST API:đưa ra chức năng Glance

- Database Abstraction Layer (DAL) :ứng dụng đồ họa thông nhất giao tiếp Glance và cơ sở dữ liệu

- Glance Domain Controller:phần mềm trung gian thực hiện chức năng Glance:ủy quyền,thông báo,chính sách,kết nối cơ sở dữ liệu

- Glance store:thực hiện tương tác Glance với các kho dữ liệu bên ngoài

- Registry layer:tổ chức liên lạc an toàn giữa các tên miền với DAL bằng dử dụng dịch vụ riêng biệt

<img src=http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing11.png>



- Mô tả:
<ul>
<li>Là kiến trúc client-server có RESTful API thông qua đó gửi yêu cầu đến máy chủ và thực hiện</li>
<li>Yêu cầu từ client chấp nhận qua RESTful API và đợi xác thực</li>
<li>Glance Domain Controller quản lý tất cả hoạt động nội bộ mà chia thành nhiều lớp,mỗi lớp thực hiện công việc riêng của mình</li>
<li>Glance store là lớp giao tiếp giữa Glance với hệ lưu trữ bên ngoài cung cấp giao diện thống nhất để truy cập Glance dùng SQlite</li>

##4.Định dạng lưu trữ

- Định dạng đĩa

|Định dạng|Mô tả|
|Raw|đĩa không cấu trúc|
|VHD|Định dạng phổ biến nhất hỗ trợ bởi nhiều công nghệ ảo hóa từ OpenStack trừ KVM
|VMDK|định dạng phổ biến bởi VMWare|
|qcow2|định dạng QEMU, định dạng gốc choKVM và QEMU hỗ trọ nhiều phép tính nâng cao|
|VDI|Định dạng đĩa cảu Virtual Box|
|ISO|Định dạng nén của đĩa quang học|
|AMI,ARI,AKI|Định dạng của Amazone|	

- Định dạng Containers

|Định dạng|Mô tả|
|bare|không có container hay metadata trong đĩa|
|ovf|định dạng ovf|
|aki,ari,ami|Định dạng đĩa của Amazone|
|ova|là file tar ova lưu trữ|
|docker|là file dạng docker được lưu trữ|

##5.Trạng thái

- Mô tả: chỉ ra trạng thái đĩa khi tải lên.Đầu tiên đĩa sẽ đưa vào hàng đợi để xác thực,trạng thái saving là chưa tải lên xong, sau khi hoàn thành sẽ sang tràng thái actie,nếu thất bại nó bị kill hay bị xoá, ta có thể dùng lênh để điều khiển bằng dòng lệnh

<img src=http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing1.jpg>

- queues:dịch vụ định danh đĩa để giũ đĩa nếu không có đĩa nào thì kích thước =01/Untitled-drawing1

- saving:biểu thị đĩa định dạng raw đang được tải lên

- active:biểu thị dữ liệu đĩa có đủ trên Glance khi đã tải lên hoặc kích thước đặt về 0

- deactived:biểu thị không phải quản trị thì không truy cập tới dữ liệu đĩa 

- killed:biểu thị tải lên bị lỗi đĩa không đọc được

- deleted:vẫn giữ thông tin về đĩa nhưng không có sẵn để dùng, đĩa trong trạng thái này sẽ tự động xóa bỏ sau vài ngày

- Deactivating and Reactivating:người dùng có thể ngưng hoạt động,khỏi dộng lại hoặc xóa nó nếu nó nguy hiểm,khi cập nhật đĩa người dùng muốn ẩn với mọi người khi cập nhật xong thì người dùng có thể boot vào máy ảo


