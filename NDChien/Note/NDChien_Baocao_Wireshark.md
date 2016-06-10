#Tool Wireshark
###Mục Lục:

[1 Giới thiệu](#1)

[2 Các tính năng nâng cao](#2)

- [2.1 Name Resolution](#2.1)

- [2.2 Protocol Dissection](#2.2)

- [2.3 Following TCP Streams](#2.3)

- [2.4 Cửa sổ thống kê phân cấp giao thức](#2.4)

- [2.5 Xem các Endpoints](#2.5)

- [2.6 Cửa số đồ thị IO](#2.6)

[3 Hướng dẫn sử dụng](#3)

<a name="1"></a>
###1 Giới thiệu

**Wireshark** là một công cụ kiểm tra, theo dõi và phân tích thông tin mạng
Các tính năng cơ bản của wireshark
- Có cửa sổ giao diện rất dễ sử dụng.
- Phần mềm hoàn toàn miễn phí và mã nguồn mở.
- Hỗ trợ hầu hết các hệ điều hành hiện nay.
- Hỗ trợ hầu hết các giao thức hiện nay, kể cả những giao thức đặc biệt như apple talk hay bit torrent.

Giao diện

<img src=http://i.imgur.com/ZNrzMEd.png>

- Danh sách các gói tin: hiển thị tất cả các gói tin đã bắt được, kèm theo thông tin vắn tắt của mỗi gói tin.
- Các phần của gói tin đang chọn sẽ hiển thị các giao thức, các trường của mỗi giao thức. Các trường được tổ chức theo cấu trúc cây, 
- Nội dung của gói tin dưới dạng hệ số16 sẽ được hiển thị tại phần “Nội dung dạng hex của gói tin”.
có thể mở rộng hoặc thu gọn cấu trúc cây để tiện quan sát.

<a name="2"></a>
###2 Các tính năng nâng cao

<a name="2.1"></a>
####2.1 Name Resolution: phân giải và chuyển đổi địa chỉ, hỗ trợ việc ghi nhớ.

Các kiểu công cụ phân giải tên trong Wireshark

	- `MAC Name Resolution`: phân giải địa chỉ MAC tầng 2 sang địa chỉ IP tầng 3.
	- `Network Name Resolution`: chuyển đổi địa chỉ tầng 3 sang một tên DNS dễ đọc như là MarketingPC1
	- `Transport Name Resolution`: chuyển đổi một cổng sang một tên dịch vụ tương ứng với nó.
	
<a name="2.2"></a>	
####2.2 Protocol Dissection

Một protocol dissector cho phép Wireshark phân chia một giao thức thành một số thành phần để phân tích.
Wireshark sử dụng đồng thời vài dissector để phiên dịch mỗi gói tin. 
Nó quyết định dissector nào được sử dụng bằng cách sử dụng phân tích lôgic đã được cài đặt sẵn và thực hiện việc dự đoán.

<a name="2.3"></a>
####2.3 Following TCP Streams
Một trong những tính năng hữu ích nhất của Wireshark là khả năng xem các dòng TCP như là ở tầng ứng dụng. 
Tính năng này cho phép phối hợp tất cả các thông tin liên quan đến các gói tin và chỉ cho bạn dữ liệu mà các gói tin này hàm chứa giống như là người dùng cuối nhìn thấy trong ứng dụng.
Để sử dụng tính năng này, click chuột phải vào 1 gói packet, chọn Follow TCP Stream

<img src=http://i.imgur.com/rc4BocF.png>

<a name="2.4"></a>
####2.4 Cửa sổ thống kê phân cấp giao thức
Khi bắt được một file có kích thước lớn, chúng ta cần biết được phân bố các giao thức trong file đó, bao nhiêu phần trăm là TCP, bao nhiêu phần trăm là IP và DHCP là bao nhiêu phần trăm,... Thay vì phải đếm từng gói tin để thu được kết quả, chúng ta có thể sử dụng cửa sổ thống kê phân cấp giao thức của Wireshark.
Để sử dụng tính năng này, bạn chọn menu Statistics > Protocol Hierarchy

<img src=http://i.imgur.com/8CySIDe.png>

<a name="2.5"></a>
####2.5 Xem các Endpoints
Một Endpoint là chỗ mà kết nối kết thúc trên một giao thức cụ thể. Ví dụ, có hai endpoint trong kết nối TCP/IP: các địa chỉ IP của các hệ thống gửi và nhận dữ liệu, 192.168.1.5 và 192.168.0.8.
Để sử dụng tính năng này, bạn chọn menu Statistics > Endpoint List và chọn một giao thức để hiển thị.

<img src=http://i.imgur.com/WlNpgqj.png>

<a name="2.6"></a>
####2.6 Cửa số đồ thị IO
Cách tốt nhất để hình dung hướng giải quyết là xem chúng dưới dạng hình ảnh. Cửa sổ đồ thị IO của Wireshark cho phép bạn vẽ đồ thị lưu lượng dữ liệu trên mạng.
Để sử dụng tính năng này, bạn chọn menu Statistics > IO Graph

<img src=http://i.imgur.com/Jqxz2KR.png>

<a name="3"></a>
###3 Hướng dẫn sử dụng

Để bắt được gói tin, Wireshark phải được cài đặt trên máy tính có kết nối mạng(LAN, mạng ảo, Internet…) đang hoạt động và Wireshark phải chạy trước, trước khi quá trình trao đổi dữ liệu diễn ra.
Để bắt một gói tin với wireshark. Tại màn hình chính, chọn menu Capture > Interface hoặc nhấn tổ hợp phím Ctrl + I.

<img src=http://i.imgur.com/nqUoxcx.png>

Tham khảo:

[1]- http://www.conmaz.net/kien-thuc/phan-mem-wireshark.html

[2]- http://luanvan.co/luan-van/luan-van-phan-tich-goi-tin-voi-wireshark-45508/\

[3]- http://ksec.info/threads/wireshark-bat-va-phan-tich-goi-tin.575/