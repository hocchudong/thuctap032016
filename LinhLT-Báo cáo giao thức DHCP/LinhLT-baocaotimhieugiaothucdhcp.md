#Báo cáo tìm hiểu giao thức DHCP

#Mục lục

* [1. Khái niệm DHCP](#khai_niem)

* [2. Các thuật ngữ trong DHCP](#thuat_ngu)

* [3. Gói tin DHCP](#goi_tin)

* [4. Các thông điệp DHCP](#thong_diep)

* [5. Cách hoạt động DHCP](#hoat_dong)

* [6. Tài liệu tham khảo](#tai_lieu_tham_khao)


<a name="khai_niem"></a>
#1. Khái niệm DHCP (Dynamic Host Configuration Protocol)
* Đây là giao thức hoạt động ở lớp Application trong mô hình TCP/IP.
* Là giao thức cấu hình tự động địa chỉ IP
* Hiện nay DHCP có 2 version: cho IPv4 và IPv6
* DHCP sử dụng port 67,68 và dùng giao thức UDP.
* Được xác định trên mô hình client-server
	* DHCP Server cấp địa chỉ mạng, phân phối thông số cấu hình tương ứng xuống cho client
    * ”Client”: chỉ các host yêu cầu các địa chỉ IP từ DHCP Server
* DHCP hỗ trợ 3 cơ chế cấp địa chỉ IP
    * Cấp tự động: DHCP gán 1 địa chỉ IP thường trực → 1 Client
    * Cấp động: DHCP gán địa chỉ IP cho 1 khoảng thời gian hữu hạn nào đó
    * Cấp thủ công: 1 địa chỉ IP được gán bời người quản trị. DHCP chỉ để đưa địa chỉ này đến Client

=>Cơ chế cấp động là cơ chế duy nhất được sử dụng để cấp lại địa chỉ mà không còn được sử dụng nữa trên client cho 1 máy client khác

<a name="thuat_ngu"></a>
#2. Các thuật ngữ trong DHCP:
* DHCP Server: máy quản lý việc cấu hình và cấp phát địa chỉ IP cho Client
* DHCP Client: máy trạm nhận thông tin cấu hình IP từ DHCP Server
* Scope: phạm vi liên tiếp của các địa chỉ IP có thể cho một mạng.
* Exclusion Scope: là dải địa chỉ nằm trong Scope không được cấp phát động cho Clients.
* Reservation: Địa chỉ đặt trước dành riêng cho máy tính hoặc thiết bị chạy các dịch vụ (tùy chọn này thường được thiết lập để cấp phát địa chỉ cho các Server, Printer,…..)
* Scope Options: các thông số được cấu hình thêm khi cấp phát IP động cho Clients như DNS Server(006), Router(003)
* DHCP Replay Agent: DHCP Replay Agent là một máy tính hoặc một Router được cấu hình để lắng nghe và chuyển tiếp các gói tin giữa DHCP Client và DHCP Server từ subnet này sang subnet khác.

<a name="goi_tin"></a>
#3. Gói tin DHCP.
![](http://www.tcpipguide.com/free/diagrams/dhcpformat.png)

| Tên Field | Dung Lượng | Mô tả |
|:---------:|:----------:|:-----:|
|Opcode | 8 bits | Thể hiện loại gói tin DHCP.Value 1:các gói tin request, Value 2: các gói tin reply.|
|Hardware type | 8 bits | Quy định cụ thể loại hardware. Value 1: Ethernet (10 Mb), Value 6: IEEE 802 ...|
|Hardware length | 8 bits | Quy định cụ thể độ dài của địa chỉ hardware|
|Hop counts | 8 bits | Dùng cho relay agents|
|Transaction Identifier | 32 bits | Được tạo bởi client, dùng để liên kết giữa request và replies của client và server.|
|Number of seconds | 16 bits | Quy định số giây kể từ khi client bắt đầu thuê hoặc xin cấp lại IP|
|Flags | 16 bits | B, broadcast: 1 bits = 1 nếu client không biết được ip trong khi đang gửi yêu cầu.|
|Client IP address | 32 bits | Client sẽ đặt IP của mình trong trường này nếu và chỉ nếu nó đang có IP hay đang xin cấp lại IP, không thì mặc định = 0|
|Your IP address | 32 bits | IP được cấp bởi server để đăng kí cho client|
|Server IP address | 32 bits | Địa chỉ ip server|
|Gateway IP address | 32 bits | Sử dụng trong relay agent|
|Client hardware address | 16 bytes | Địa chỉ lớp 2 của client, dùng để định danh|
|Server host name | 64 bytes | Khi server gửi gói tin offer hay ack thì sẽ đặt tên của nó vào trường này, nó có thể là nickname hoặc tên miền dns|
|Boot filename | 128 bytes | Sử dụng bời client để yêu cầu loại tập tin khởi động cụ thể trong gói tin discover.Sử dụng bởi server để chỉ rõ toàn bộ đường dẫn, tên file của file khởi động trong gói tin offer|
---------------

<a name="thong_diep"></a>
#4. Các thông điệp DHCP:
* DHCP Discover: Thời gian đầu tiên một máy tính DHCP Client nỗ lực để gia nhập mạng, nó yêu cầu thông tin địa chỉ IP từ DHCP Server bởi việc broadcast một gói DHCP Discover. Địa chỉ IP nguồn trong gói là 0.0.0.0 bởi vì client chưa có địa chỉ IP.

* DHCP Offer: Mỗi DHCP server nhận được gói DHCP Discover từ client đáp ứng với gói DHCP Offer chứa địa chỉ IP không thuê bao và thông tin định cấu hình TCP/IP bổ sung(thêm vào), chẳng hạn như subnet mask và gateway mặc định. Nhiều hơn một DHCP server có thể đáp ứng với gói DHCP Offer. Client sẽ chấp nhận gói DHCP Offer đầu tiên nó nhận được.

* DHCP Request: Khi DHCP client nhận được một gói DHCP Offer, nó đáp ứng lại bằng việc broadcast gói DHCP Request mà chứa yêu cầu địa chỉ IP, và thể hiện sự chấp nhận của địa chỉ IP được yêu cầu.

* DHCP Acknowledge : DHCP server được chọn lựa chấp nhận DHCP Request từ Client cho địa chỉ IP bởi việc gửi một gói DHCP Acknowledge. Tại thời điểm này, Server cũng định hướng bất cứ các tham số định cấu hình tuỳ chọn. Sự chấp nhận trên của DHCP Acknowledge, Client có thể tham gia trên mạng TCP/IP và hoàn thành hệ thống khởi động.

* DHCP Nak: Nếu địa chỉ IP không thể được sữ dụng bởi client bởi vì nó không còn giá trị nữa hoặc được sử dụng hiện tại bởi một máy tính khác, DHCP Server đáp ứng với gói DHCP Nak, và Client phải bắt đầu tiến trình thuê bao lại. Bất cứ khi nào DHCP Server nhận được yêu cầu từ một địa chỉ IP mà không có giá trị theo các Scope mà nó được định cấu hình với, nó gửi thông điệp DHCP Nak đối với Client.

* DHCP Decline : Nếu DHCP Client quyết định tham số thông tin được đề nghị nào không có giá trị, nó gửi gói DHCP Decline đến các Server và Client phải bắt đầu tiến trình thuê bao lại.

* DHCP Release: Một DHCP Client gửi một gói DHCP Release đến một server để giải phóng địa chỉ IP và xoá bất cứ thuê bao nào đang tồn tại.

<a name="hoat_dong"></a>
#5. Cách hoạt động DHCP
![](http://ccieblog.co.uk/wp-content/uploads/2012/10/DHCP-Message-Exchange.png)
* Bước 1:
	* DHCP Client gửi broadcast thông điệp discover message để tìm một DHCP Server nhằm xin IP
	* Gói tin DHCP này được bọc trong một gói UDP với source port là 68 và destination port là 67. Gói UDP đến lượt nó được đóng gói vào một gói IP với source IP là 0.0.0.0 và destination IP là 255.255.255.255.
* Bước 2:
    * DHCP Server nhận được thông điệp này sẽ gửi lại thông điệp offer message cho Client
    * Thông điệp Offer ghi ra mọi thông số server cấp xuống cho client (MAC của client, địa chỉ ip client, subnetmask, địa chỉ ip server, thời gian cho thuê đến client.)
    * Gói tin OFFER này được bọc trong một gói UDP với source port là 67 và destination port là 68. Gói UDP đến lượt nó được đóng gói vào một gói IP với source IP là địa chỉ IP của server và destination IP là 255.255.255.255.
* Bước 3:
	* Client sẽ chọn 1 trong các địa chỉ IP, sau đó gửi lại thông điệp request message tương ứng với DHCP server đó.
	* Gói REQUEST này sẽ được đóng vào một gói UDP với source port là 68 và destination port là 67. Gói UDP sẽ được truyền tải trong một gói IP với source IP là 0.0.0.0 và destination IP là 255.255.255.255.
* Bước 4:
	* Server sẽ hoàn tất bằng cách gửi thông điệp ACK cho client. Ngoài ra còn có gateway mặc định, địa chỉ dns server.
	* DHCP ACK được đóng vào gói UDP với source port là 67 và destination port là 68, được truyền tải trong gói IP có source IP là IP của server và destination IP là 255.255.255.255.
	* Đến đây, client chính thức có cấu hình IP và có thể sử dụng địa chỉ IP được cấp phát để trao đổi dữ liệu. Mỗi cấu hình IP được cấp phát sẽ chỉ có thời hạn trong một khoảng thời gian nhất định, sau khoảng thời gian này, client phải yêu cầu server cấp phát gia hạn lại cấu hình IP của mình. Trong những lần sau, các thông điệp DHCP được gửi unicast thay vì broadcast như lần cấp phát đầu tiên.

**(Tất cả thông điệp đều là broadcast message)**

<a name="tai_lieu_tham_khao"></a>
#6. Tài liệu tham khảo
* https://github.com/kieulam141/DHCP
* http://vdo.vn/cong-nghe-thong-tin/cac-khai-niem-co-ban-ve-dhcp.html
* http://www.ntps.edu.vn/blog/190-ip-services-bai-so-15-dhcp
* http://www.slideshare.net/phanleson/dhcp-4573853