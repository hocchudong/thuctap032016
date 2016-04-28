#Báo cáo OpenStack
##Mục Lục

##Tổng quan OpenStack
- 1.Khái niệm
OpenStack là một nền tảng điện toán đám mây mã nguồn mở tạo nên bởi nhiều dịch vụ và mỗi dich vụ thực hiện một chức năng nhưng chúng có mối liên hệ với nhau.

- 2.Dịch vụ

<ul>
|Dịch vụ|Tên Project|Mô tả|
|-------|-----------|-----|
|Dashboard|Horizon|Tạo 1 giao diện trên web để sử dụng|
|Compute|Nova|Quản lý vòng đời máy ảo trên môi trường OpenStack bao gồm tạo, lập lịch, hủy máy ảo theo yêu cầu|
|Networking|Neutron|Cung cấp dịch mạng cho các dịch vụ khác OpenStack, cung cấp APIs để người dùng tạo ra và đưa vào dịch vụ và hỗ trợ nhiều loại mạng và công nghệ|
<li>Storage</li>
|Object Storage|Swift|Lưu trữ và lấy các đối tượng dữ liệu qua một RESTful,API gốc HTTP,tạo bản sao,theo kiểu phân tán, có khả năng chống chịu lỗi,có thể triển khai thành dịch vu độc lập|
|Block Storage|Cinder|Cung cấp các khối dữ liệu để chạy máy ảo.Cung cấp volume,khởi tạo máy từ volume,có plugin để kết nố,có thể sao lưu, mở rộng volume|
<li>Shared services</li>
|Identity service|Keystone|Cung cấp sự xác nhận và dịc vụ xác nhận OpenStack. Cung cấp danh sách endpoints cho OpenStack|
|Imange Service|Glance|Lưu trữ và nhận image đĩa của máy ảo.Compute sử dụng khi cung cấp thực thể|
|Telemetry|Ceilometer||Giám sát và tính toán để tính tiền,và thông kê|
<li>Dịch vụ cấp cao</li>
|Orchestratiom|Heat|Điều phối tài nguyên và ứng dụng bằng sử dụng HOT,triển khai dựa vào templates dựng sẵn,tự động tính toán tài nguyên, là stack tab Horizon|
|Database Service|Trove|Dịch vụ cơ sở dữ liệu, cung cấp database,tự backup đảm bảo an toàn|
</ul>
