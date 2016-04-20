#Tìm hiểu WireShark và bắt, phân tích gói tin DHCP bằng WireShark
----
#Mục Lục
* [1. Tìm hiểu WireShark] (#1)
  * [1.1 Giới thiệu] (#1.1)
  * [1.2 Giao diện tổng quan của WireShark] (#1.2)
  * [1.3 Một số tính năng nâng cao của WireShark] (#1.3)
* [2. Bắt gói tin DHCP] (#2)
  * [2.1 Khởi động WireShark.] (#2,1)
  * [2.2 Giải phóng và cấp phát IP mới.] (#2.2)
  * [2.3 Lọc các gói tin DHCP.] (#2.3)
  * [2.4 Phân tích các gói tin DHCP.] (#2.4)
    * [2.4.1 Phân tích gói tin DHCP Discover] (#2.4.1)
    * [2.4.2 Phân tích gói tin DHCP Offer] (#2.4.2)
    * [2.4.3 Phân tích gói tin DHCP Request] (#2.4.3)
    * [2.4.4 Phân tích gói tin DHCP Ack] (#2.4.4)

----
<a name="1"></a>
##1. Tìm hiểu WireShark.
<a name="1.1"></a>
###1.1 Giới thiệu :
* Wireshark là một công cụ kiểm tra, theo dõi và phân tích thông tin mạng được phát triển bởi Gerald Combs.
* Các tiện ích của phần mềm:
  * Thân thiện với người dùng: Giao diện của Wireshark là một trong những giao diện phần mềm phân tích gói dễ dùng nhất. Wireshark là 
  ứng dụng đồ hoạ với hệ thống menu rât rõ ràng và được bố trí dễ hiểu.
  * Giá rẻ: Wireshark là một sản phẩm miễn phí. Bạn có thể tải về và sử dụng Wireshark cho bất kỳ mục đích nào, kể cả với mục đích 
  thương mại.
  * Hỗ trợ: Cộng đồng của Wireshark là một trong những cộng đồng tốt và năng động nhất của các dự án mã nguồn mở.
  * Hệ điều hành hỗ trợ Wireshark: Wireshark hỗ trợ hầu hết các loại hệ điều hành hiện nay.

<a name="1.2"></a>  
###1.2 Giao diện tổng quan của WireShark.
![] (http://i.imgur.com/7gEZalN.png)
* Giao diện Wireshark có năm thành phần chính:
  * Các Tùy chỉnh nằm ở phía trên của cửa sổ. Mối quan tâm của chúng ta hiện nay là các tập tin và Capture. Các menu File cho phép bạn 
  lưu dữ liệu gói tin bị bắt hoặc mở một tập tin có chứa các gói dữ liệu bị bắt từ trước, và thoát khỏi ứng dụng Wireshark. Menu Capture
  cho phép bạn bắt đầu bắt gói tin.
  * Cửa sổ danh sách gói tin hiển thị một bản tóm tắt một dòng cho mỗi gói tin bị bắt, tại thời điểm mà các gói tin bị bắt, nguồn và địa
  chỉ đích của gói tin, các loại giao thức, và thông tin giao thức cụ thể có trong các gói tin. Danh sách này có thể được sắp xếp theo 
  tùy chỉnh của mỗi loại bằng cách nhấp vào một tên cột. Các loại trường giao thức liệt kê các giao thức cấp cao nhất mà gửi hoặc nhận 
  được gói tin này.
  * Cửa sổ chi tiết gói tin cung cấp chi tiết về các gói lựa chọn. Những chi tiết này bao gồm thông tin về các khung Ethernet (giả sử 
  các gói đã được gửi/nhận trên một cổng Ethernet) và IP gói tin. Số lượng Ethernet và IP lớp chi tiết hiển thị có thể được mở rộng 
  hoặc giảm thiểu bằng cách nhấp vào biểu tượng cộng hoặc trừ bên trái của khung Ethernet hoặc IP trong cửa sổ chi tiết gói tin. Nếu 
  gói dữ liệu đã được thực hiện trên TCP hoặc UDP, chi tiết về TCP hoặc UDP cũng sẽ được hiển thị, tương tự mà có thể mở rộng hoặc thu 
  nhỏ. Cuối cùng, chi tiết về các giao thức cấp cao nhất mà gửi hoặc nhận được gói tin này cũng được cung cấp.
  * Cửa sổ nội dung gói tin: hiển thị toàn bộ nội dung của khung hình chụp,trong cả hai định dạng mã ASCII và định dạng mã Hex.
  * Phía trên cùng của giao diện người dùng đồ họa Wireshark, là màn hình hiển thị kỹ thuật lọc gói tin, mà trong đó một tên giao thức 
  hoặc các thông tin khác có thể được nhập vào đặt để lọc các thông tin hiển thị trong cửa sổ (và do đó các gói tiêu đề và gói nội dung 
  cửa sổ).

<a name="1.3"></a>
###1.3 Một số tính năng của WireShark:
* **Name Resolution**: phân giải và chuyển đổi địa chỉ, hỗ trợ việc ghi nhớ.
  * Dữ liệu truyền trong mạng thông qua một vài hệ thống địa chỉ, các địa chỉ này thường dài và khó nhớ (Ví dụ: MAC). Phân giải điạ chỉ là quá trình mà một giao thức sử dụng để chuyển đổi một địa chỉ loại này thành một địa chỉ loại khác đơn giản hơn.
  	* Các kiểu công cụ phân giải tên trong Wireshark: có 3 loại
  		* MAC Name Resolution: phân giải địa chỉ MAC tầng 2 sang địa chỉ IP tầng 3.
      	* Network Name Resolution: chuyển đổi địa chỉ tầng 3 sang một tên DNS dễ đọc như là MarketingPC1.
    	* Transport Name Resolution: chuyển đổi một cổng sang một tên dịch vụ tương ứng với nó, ví dụ: cổng 80 là http.
* **Protocol dissector**: cho phép Wireshark phân chia một giao thức thành một số thành phần để phân tích
  * Một protocol dissector cho phép Wireshark phân chia một giao thức thành một số thành phần để phân tích.
	* Wireshark sử dụng đồng thời vài dissector để phiên dịch mỗi gói tin.
	* Nó quyết định dissector nào được sử dụng bằng cách sử dụng phân tích lôgic đã được cài đặt sẵn và thực hiện việc dự đoán.
* **Following TCP Streams**: một trong những tính năng hữu ích nhất của Wireshark là khả năng xem các dòng TCP như là ở tầng ứng dụng
  * Một trong những tính năng hữu ích nhất của Wireshark là khả năng xem các dòng TCP như là ở tầng ứng dụng.
	* Tính năng này cho phép bạn phối hợp tất cả các thông tin liên quan đến các gói tin và chỉ cho bạn dữ liệu mà các gói tin này hàm chứa giống như là người dùng cuối nhìn thấy trong ứng dụng.
	* Để sử dụng tính năng này, bạn click chuột phải vào 1 gói packet, chọn Follow TCP Stream
* **Cửa sổ thống kê phân cấp giao thức**
  * Khi bắt được một file có kích thước lớn, chúng ta cần biết được phân bố các giao thức trong file đó, bao nhiêu phần trăm là TCP, bao nhiêu phần trăm là IP và DHCP là bao nhiêu phần trăm,... Thay vì phải đếm từng gói tin để thu được kết quả, chúng ta có thể sử dụng cửa sổ thống kê phân cấp giao thức của Wireshark.
	* Để sử dụng tính năng này, bạn chọn menu Statistics > Protocol Hierarchy
* **Xem các Endpoints**
  * Một Endpoint là chỗ mà kết nối kết thúc trên một giao thức cụ thể. Ví dụ, có hai endpoint trong kết nối TCP/IP: các địa chỉ IP của các hệ thống gửi và nhận dữ liệu, 192.168.1.5 và 192.168.0.8.
	* Để sử dụng tính năng này, bạn chọn menu Statistics > Endpoint List và chọn một giao thức để hiển thị.
* **Cửa sổ đồ thị IO**
  * Cách tốt nhất để hình dung hướng giải quyết là xem chúng dưới dạng hình ảnh. Cửa sổ đồ thị IO của Wireshark cho phép bạn vẽ đồ thị lưu lượng dữ liệu trên mạng.
	* Để sử dụng tính năng này, bạn chọn menu Statistics > IO Graph
	
----
<a name="2"></a>
##2. Dùng WireShark để bắt gói tin.
<a name="2.1"></a>
###2.1 Khởi động WireShark.
* Sau khi khởi động xong ta chọn card mạng muốn bắt gói tin DHCP.
 ![](http://i.imgur.com/CD40bya.png)

<a name="2.2"></a> 
###2.2 Giải phóng và cấp phát IP mới.
* Giải phóng IP.
![](http://i.imgur.com/Q1apZLj.png)
* Cấp phát IP mới.
![](http://i.imgur.com/O4h7hVg.png)

<a name="2.3"></a>
###2.3 Lọc các gói tin DHCP.
* Ta lọc các gói tin DHCP bằng cách gõ **bootp** vào filter.
![](http://i.imgur.com/0x5nZqm.png)
![](http://i.imgur.com/NOK3EQR.png)

<a name="2.4"></a>
###2.4 Phân tích các gói tin DHCP.
<a name="2.4.1"></a>
####2.4.1 Phân tích gói tin DHCP Discovery.
![](http://i.imgur.com/IJhNqBr.png)

Đây là gói tin broadcast gửi từ client đến các servers.
- 1.source mac(client) des mac(servers).
- 2.source ip (client) = 0.0.0.0 do lúc này client chưa có ip, des ip servers =255.255.255.255 do đây là bản tin broadcast.
- 3.source port=68(client) và des port=67(server)

`DHCP header`

- 4.Loại gói tin:DHCP discovery
- 5.IP được client yêu cầu cấp phát
- 6.Hostname của client

<a name="2.4.2"></a>
####2.4.2 Phân tích gói tin DHCP offer.
![](http://i.imgur.com/k10ZDQX.png)
![](http://i.imgur.com/aBxlT6u.png)

Đây là gói tin unicast gửi từ server đến client
- 1.source mac(server) des mac(client).
- 2.source ip (server) và des ip(client).
- 3.source port=67(server) des port=68(client).

`DHCP header`

- 4.ip client trong gói tin header
- 5.Loại gói tin:DHCP offer
- 6.Định danh dhcp server:chính là ip của server
- 7.Thời gian cho client thuê
- 8.Subnet mask cấp cho client
- 9.default gateway cấp cho client
- 10.DNS cấp cho client

<a name="2.4.3"></a>
####2.4.3 Phân tích gói tin DHCP Request.
![](http://i.imgur.com/J68yqbC.png)
* Đây cũng là gói tin broadcast gửi từ client đến các servers.Nó có thêm trường Client Fully Qualified Domain Name trong dhcp header

<a name="2.4.4"></a>
####2.4.4 Phân tích gói tin DHCP Ack.
![](http://i.imgur.com/pYTdBAU.png)
* Đây cũng là gói tin unicast gửi từ server đến client để xác nhận lại các thông tin đã cấp cho client

----
# Tài liệu tham khảo
1. http://antoanthongtin.ictu.edu.vn/dieutraso/286-wireshark-phan-mem-khong-the-thieu-cho-nguoi-lam-bao-mat.html
2. https://github.com/kieulam141/DHCP/edit/master/Capture_wireshark.md
