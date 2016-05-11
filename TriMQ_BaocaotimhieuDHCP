#Tìm hiểu về giao thức DHCP

##Mục lục:

####[1.Khái niệm](#khainiem)
####[2.Mô hình hoạt động của DHCP](#tacdung)
####[3.Các loại bản tin DHCP](#bantin)
<li>[DHCP discover](#discover)</li>
<li>[DHCP offer](#offer)</li>
<li>[DHCP request](#request)</li>
<li>[DHCP ACK/Nack](#ack)</li>
<li>[DHCP decline](#decline)</li>
<li>[DHCP release](#release)</li>

####[4.DHCP header](#header)
####[5.Cách thức hoạt động](#hoatdong)

<a name="khainiem"></a>
####1.Khái niệm:
Giao thức DHCP (Dynamic host configuration protocol) là 1 giao thức cấu hình tự động địa chỉ IP cho cả IPv4 và IPv6. Nằm ở tầng Application của mô hình TCP/IP. Sử dụng port 67, 68 và UDP.

 <a name="tacdung"></a>
####2.Mô hình hoạt động của DHCP:
#####Mô hình client-server:
<ul>
	<li>DHCP server: cấp tự động địa chỉ IP cho máy client.</li>
	<li>DHCP client: Yêu cầu server cấp phát địa chỉ IP.</li>
</ul>
#####Các cơ chế cấp:
<ul>
	<li>Cấp tự động: Gán 1 địa chỉ IP thường trực cho client.</li>
	<li>Cấp động: Gán địa chỉ IP trong 1 khoảng thời gian hữu hạn.</li>
	<li>Cấp thủ công: Địa chỉ IP sẽ được gán bởi người quản trị, chỉ đưa địa chỉ này đến máy client.</li>
</ul>

<a name="bantin"></a>
####3.Các loại bản tin DHCP:

<a name="discover"></a>
<li>**DHCP discover**: Khi 1 client muốn gia nhập mạng, nó sẽ broadcast 1 gói tin dhcp discover tới dhcp server để yêu cầu cấp thông tin địa chỉ ip. Ip nguồn trong gói là 0.0.0.0.</li>
<li>**DHCP offer**: Unicast từ DHCP server sau khi nhận được gói Discover của client. Gói tin bao gồm thông tin IP đề nghị cấp cho client như: IP address, Subnet Mask, Gateway...Có thể sẽ có nhiều DHCP server cùng gửi gói tin này, Client sẽ nhận và xử lý gói Offer đến trước.</li>
<li>**DHCP request**: Broadcast từ client khi nhận được gói DHCP Offer. Nội dung gói tin: xác nhận thông tin IP sẽ nhận từ server để cho các server khác không gửi gói tin offer cho clien đấy nữa.</li>
<li>**DHCP ACK/Nack**:</li>
<ul>
	<li>DHCP Ack: Unicast bởi DHCP server đến DHCP client xác nhận thông tin từ gói DHCP Request. Tất cả thông tin cấu hình IP sẽ được gửi đến cho client và kết thúc quá trình cấp phát IP.</li>
	<li>DHCP Nack: Unicast từ server, khi server từ chối gói DHCP Request.</li>
</ul>	
<li>**DHCP decline**: Broadcast từ client nếu client từ chối IP đã được cấp.</li>
<li>**DHCP release**: Được gửi bởi DHCP client khi client bỏ địa chỉ IP và hủy thời gian sử dụng còn lại. Đây là gói tin unicast gửi trực tiếp đến DHCP server cung cấp IP đó.</li>

<a name="header"></a>
####4.DHCP header:

<img src="http://www.technologyuk.net/the_internet/internet/images/bootp_message_format.gif">

**A description of the BOOTP message fields is given below:**
<ul>
	<li>Opcode (8 bits): Thể hiện loại gói tin DHCP.Value 1:các gói tin request, Value 2: các gói tin reply.</li>
	<li>Hardware type (8 bits): Quy định cụ thể loại hardware. Value 1: Ethernet (10 Mb), Value 6: IEEE 802 ...</li>
	<li>Hardware length (8 bits): 	Quy định cụ thể độ dài của địa chỉ hardware.</li>
	<li>Hop counts	(8 bits): Dùng cho relay agents</li>
	<li>Transaction Identifier	(32 bits): Được tạo bởi client, dùng để liên kết giữa request và replies của client và server.</li>
	<li>Number of seconds	(16 bits): Quy định số giây kể từ khi client bắt đầu thuê hoặc xin cấp lại IP</li>
	<li>Flags (16 bits	): B, broadcast: 1 bits = 1 nếu client không biết được ip trong khi đang gửi yêu cầu.</li>
	<li>Client IP address	(32 bits): Client sẽ đặt IP của mình trong trường này nếu và chỉ nếu nó đang có IP hay đang xin cấp lại IP, không thì mặc định = 0</li>
	<li>Your IP address	(32 bits): IP được cấp bởi server để đăng kí cho client</li>
	<li>Server IP address	(32 bits): Địa chỉ ip server</li>
	<li>Gateway IP address	(32 bits): Sử dụng trong relay agent</li>
	<li>Client hardware address (16 bytes): Địa chỉ lớp 2 của client, dùng để định danh</li>
	<li>Server host name	(64 bytes): Khi server gửi gói tin offer hay ack thì sẽ đặt tên của nó vào trường này, nó có thể là nickname hoặc tên miền dns</li>
	<li>Boot filename	(128 bytes): Sử dụng bời client để yêu cầu loại tập tin khởi động cụ thể trong gói tin discover.Sử dụng bởi server để chỉ rõ toàn bộ đường dẫn, tên file của file khởi động trong gói tin offer</li>
</ul>	
<a name="hoatdong"></a>
####5.Cách thức hoạt động:

<img src="http://tecadmin.net/wp-content/uploads/2013/03/dhcp.png">

Để nhận được IP từ DHCP server, DHCP client phải khởi tạo giao tiếp với server với 1 loạt gói tin liên tiếp nhau. Quá trình này diễn ra qua 4 bước chính:
<ul>
<li>Bước 1: DHCP Client gửi broadcast thông điệp discover message để tìm một DHCP Server nhằm xin IP.</li>
<li>Bước 2: DHCP Server nhận được thông điệp này sẽ gửi lại thông điệp offer message cho Client.</li>
<li>Bước 3: Client sẽ chọn 1 trong các địa chỉ IP, sau đó gửi lại thông điệp request message tương ứng với DHCP server đó.</li>
<li>Bước 4: Server sẽ hoàn tất bằng cách gửi thông điệp ACK cho client. Ngoài ra còn có gateway mặc định, địa chỉ dns server.</li>
</ul>



