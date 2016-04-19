#Tìm hiểu giao thức DHCP
#Mục Lục
* [1. Khái niệm] (#1)
* [

----
## 1.Khái niệm.
* **Dynamic Host Configuration Protocol (DHCP - giao thức cấu hình động máy chủ)** là một giao thức cấu hình tự động địa chỉ IP. Máy tính 
được cấu hình một cách tự động vì thế sẽ giảm việc can thiệp vào hệ thống mạng. Nó cung cấp một database trung tâm để theo dõi tất cả các 
máy tính trong hệ thống mạng, điều này làm tránh việc trùng địa chỉ IP giữa 2 máy khác nhau.
* Nếu không có DHCP, các máy có thể cấu hình IP thủ công. Ngoài ra DHCP còn cung cấp thông tin cấu hình khác, cụ thể như DNS.
* Hiện nay DHCP có 2 version: cho IPv4 và IPv6.
* Mô hình DHCP cơ bản:

![] (http://vdo.vn/wp-content/uploads/2013/03/model_dhcp_server.png)
----
## 2. Các thuật ngữ cơ bản trong DHCP.
* **DHCP Server**: máy quản lý việc cấu hình và cấp phát địa chỉ IP cho Client
* **DHCP Client**: máy trạm nhận thông tin cấu hình IP từ DHCP Server
* **Scope**: phạm vi liên tiếp của các địa chỉ IP có thể cho một mạng.
* **Exclusion Scope**: là dải địa chỉ nằm trong Scope không được cấp phát động cho Clients.
* **Reservation**: Địa chỉ đặt trước dành riêng cho máy tính hoặc thiết bị chạy các dịch vụ (tùy chọn này thường được thiết lập để cấp phát địa chỉ cho các Server, Printer,…..)
* **Scope Options**: các thông số được cấu hình thêm khi cấp phát IP động cho Clients như DNS Server(006), Router(003)  ![] 

----
##3. Các thông điệp DHCP:
* **DHCP Discover**: Thời gian đầu tiên một máy tính DHCP Client nỗ lực để gia nhập mạng, nó yêu cầu thông tin địa chỉ IP từ DHCP Server bởi việc broadcast một gói DHCP Discover. Địa chỉ IP nguồn trong gói là 0.0.0.0 bởi vì client chưa có địa chỉ IP.
* **DHCP Offer**: Mỗi DHCP server nhận được gói DHCP Discover từ client đáp ứng với gói DHCP Offer chứa địa chỉ IP không thuê bao và thông tin định cấu hình TCP/IP bổ sung(thêm vào), chẳng hạn như subnet mask và gateway mặc định. Nhiều hơn một DHCP server có thể đáp ứng với gói DHCP Offer. Client sẽ chấp nhận gói DHCP Offer đầu tiên nó nhận được.
* **DHCP Request**: Khi DHCP client nhận được một gói DHCP Offer, nó đáp ứng lại bằng việc broadcast gói DHCP Request mà chứa yêu cầu địa chỉ IP, và thể hiện sự chấp nhận của địa chỉ IP được yêu cầu.
* **DHCP Acknowledge** : DHCP server được chọn lựa chấp nhận DHCP Request từ Client cho địa chỉ IP bởi việc gửi một gói DHCP Acknowledge. Tại thời điểm này, Server cũng định hướng bất cứ các tham số định cấu hình tuỳ chọn. Sự chấp nhận trên của DHCP Acknowledge, Client có thể tham gia trên mạng TCP/IP và hoàn thành hệ thống khởi động.
* **DHCP Nak**: Nếu địa chỉ IP không thể được sữ dụng bởi client bởi vì nó không còn giá trị nữa hoặc được sử dụng hiện tại bởi một máy tính khác, DHCP Server đáp ứng với gói DHCP Nak, và Client phải bắt đầu tiến trình thuê bao lại. Bất cứ khi nào DHCP Server nhận được yêu cầu từ một địa chỉ IP mà không có giá trị theo các Scope mà nó được định cấu hình với, nó gửi thông điệp DHCP Nak đối với Client.
* **DHCP Decline** : Nếu DHCP Client quyết định tham số thông tin được đề nghị nào không có giá trị, nó gửi gói DHCP Decline đến các Server và Client phải bắt đầu tiến trình thuê bao lại.
* **DHCP Release**: Một DHCP Client gửi một gói DHCP Release đến một server để giải phóng địa chỉ IP và xoá bất cứ thuê bao nào đang tồn tại.

----
##4.Quá trình của DHCP.

![] (http://vdo.vn/wp-content/uploads/2013/03/sodo_dhcp_server.png)

* Các bước lần lượt là:
  * B1: Máy trạm khởi động với “địa chỉ IP rỗng” cho phép liên lạc với DHCP Servers bằng giao thức TCP/IP. Nó broadcast một thông điệp DHCP Discover chứa địa chỉ MAC và tên máy tính để tìm DHCP Server .
  * B2: Nhiều DHCP Server có thể nhận thông điệp và chuẩn bị địa chỉ IP cho máy trạm. Nếu máy chủ có cấu hình hợp lệ cho máy trạm, nó gửi thông điệp “DHCP Offer” chứa địa chỉ MAC của khách, địa chỉ IP “Offer”, mặt nạ mạng con (subnet mask), địa chỉ IP của máy chủ và thời gian cho thuê đến Client. Địa chỉ “offer” được đánh dấu là “reserve” (để dành).
  * B3: Khi Client nhận thông điệp DHCP Offer và chấp nhận một trong các địa chỉ IP, Client sẽ gửi thông điệp DHCP Request để yêu cầu IP phù hợp cho DHCP Server thích hợp.
  * B4: Cuối cùng, DHCP Server khẳng định lại với Client bằng thông điệp DHCP Acknowledge.
  
----


