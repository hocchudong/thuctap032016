#Tìm hiểu giao thức DHCP
#Mục lục
<h3><a href="#conceptnbenefit">1. Khái niệm DHCP và vai trò</a></h3>
<ul style="list-style: none">
<li><h4><a href="#concept">1.1. Khái niệm</a></h4></li>
<li><h4><a href="#benefit">1.2. Lợi ích của giao thức DHCP</a></h4></li>
</ul>
<h3><a href="#detail">2. Hoạt động của giao thức DHCP</a></h3>
<ul style="list-style: none">
<li><h4><a href="#process">2.1. Tiến trình hoạt động của DHCP</a></h4></li>
<li><h4><a href="#msg">2.2. Các loại bản tin DHCP</a></h4></li>
<li><h4><a href="#dhcp-header">2.3. Cấu trúc DHCP Header</a></h4></li>
</ul>

<h3><a href="#install">3. Cài đặt DHCP server trên ubuntu 14.04</a></h3>
<ul style="list-style: none">
<li><h4><a href="#prepate">3.1. Chuẩn bị bài lab</a></h4></li>
<li><h4><a href="#config">3.2. Cài đặt và cấu hình DHCP</a></h4></li>
<li><h4><a href="#demo">3.3. Hình ảnh demo IP được cấp phát trên các DHCP client</a></h4></li>
</ul>

<h3><a href="#wireshark">4. Bắt và phân tích các bản tin DHCP trên wireshark</a></h3>
---

<h3><a name="conceptnbenefit">1. Khái niệm DHCP và vai trò</a></h3>
<ul style="list-style: none">
<li><h4><a name="concept">1.1. Khái niệm</a></h4>
<ul>
<li>Giao thức DHCP (Dynamic Host Configuration Protocol) - giao thức hoạt động theo mô hình client/server</li>
<li>Tự động cấp phát địa chỉ IP cho các máy client trong mạng và các thông tin cấu hình liên quan: subnet mask, default gateway, etc.</li>
<li>DHCP cũng cấp phát các thông số cấu hình TCP/IP tới các máy client trong hệ thống</li>
</ul>
</li>
<li><h4><a name="benefit">1.2. Lợi ích của giao thức DHCP</a></h4>
<ul>
<li>Cấu hình địa chỉ IP một cách tin cậy: DHCP giảm thiểu tối đa lỗi cấu hình gây ra bởi việc cấu hình IP thủ công, ví dụ như cấu hình sai topology hay cấu hình IP bị xung đột (hai máy trong mạng cấu hình cùng một địa chỉ IP)</li>
<li>Đơn giản hóa việc quản trị mạng:
<ul>
<li>Cấu hình tập trung và tự động các thông tin TCP/IP cho các máy client</li>
<li>Quản lý và duy trì miền địa chỉ IP cấp phát cho các client, tự động cấp phát nhưng cũng tự động thu hồi địa chỉ IP (khi một máy client rời khỏi mạng)</li>
<li>Chuyển tiếp bản tin DHCP khởi tạo bằng việc sử dụng DHCP relay agent, tránh việc phải cài đặt DHCP trên mỗi subnet</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3><a name="detail">2. Hoạt động của giao thức DHCP</a></h3>
<ul style="list-style: none">
<li><h4><a name="process">2.1. Tiến trình hoạt động của DHCP</a></h4>
<div style="text-align: center"><img src="https://camo.githubusercontent.com/abd7e50ad6a89a5df9ac2cf4e3926afde9dfb4e1/687474703a2f2f692e696d6775722e636f6d2f59367a31476b702e706e67"/></div>
<ul>
<li><b>Bước 1:</b> Khi máy Client khởi động, máy sẽ gửi broadcast gói tin DHCP DISCOVER, yêu cầu một Server phục vụ mình. Gói tin này cũng chứa địa chỉ MAC của client.

Nếu client không liên lạc được với DHCP Server thì sau 4 lần truy vấn không thành công nó sẽ tự động phát sinh ra 1 địa chỉ IP riêng cho chính mình nằm trong dãy 169.254.0.0 đến 169.254.255.255 dùng để liên lạc tạm thời. Và client vẫn duy trì việc phát tín hiệu Broad cast sau mỗi 5 phút để xin cấp IP từ DHCP Server.</li>
<li><b>Bước 2:</b> Các máy Server trên mạng khi nhận được yêu cầu đó. Nếu còn khả năng cung cấp địa chỉ IP, đều gửi lại cho máy Client một gói tin DHCP OFFER, đề nghị cho thuê một địa chỉ IP trong một khoảng thời gian nhất định, kèm theo là một Subnet Mask và địa chỉ của Server. Server sẽ không cấp phát đia chỉ IP vừa đề nghị cho client thuê trông suốt thời gian thương thuyết.</li>
<li><b>Bước 3:</b> Máy Client sẽ lựa chọn một trong những lời đề nghị ( DHCPOFFER) và gửi broadcast lại gói tin DHCPREQUEST và chấp nhận lời đề nghị đó. Điều này cho phép các lời đề nghị không được chấp nhận sẽ được các Server rút lại và dùng để cấp phát cho các Client khác.</li>
<li><b>Bước 4:</b> Máy Server được Client chấp nhận sẽ gửi ngược lại một gói tin DHCP ACK như một lời xác nhận, cho biết địa chỉ IP đó, Subnet Mask đó và thời hạn cho sử dụng đó sẽ chính thức được áp dụng. Ngoài ra server còn gửi kèm những thông tin bổ xung như địa chỉ Gateway mặc định, địa chỉ DNS Server.</li>
</ul>
</li>
<li><h4><a name="msg">2.2. Các loại bản tin DHCP</a></h4></li>
<ul>
<li><h4>DHCPDiscover</h4>
Là bản tin broadcast của client trong lần đầu tiên tham gia vào mạng, bản tin này yêu cầu cấp phát địa chỉ IP từ DHCP server.
</li>
<li><h4>DHCPOffer</h4>
Là bản tin broadcast của DHCP server thông báo rằng đã nhận được bản tin DHCPDiscover và có tập cấu hình một địa chỉ IP để cấp cho client. Bản tin DHCPOffer chứa một địa chỉ IP chưa cấp phát và kèm theo các thông tin cấu hình TCP/IP, cũng như thông tin về subnetmask, default gateway. 
</li>
<li><h4>DHCPRequest</h4>
Bản tin broadcast bởi DHCP client sau khi lựa chọn một bản tin DHCPOffer. Bản tin này chứa địa chỉ IP từ bản tin DHCPOffer đã chọn, xác nhận thông tin IP đã nhận từ server để các DHCP server khác không gửi bản tin Offer cho client đó nữa.
<li><h4>DHCPAck</h4>
Broadcast bởi DHCP server đến DHCP client xác nhận thông tin từ gói DHCP Request. Tất cả thông tin cấu hình IP sẽ được gửi đến cho client và kết thúc quá trình cấp phát IP.
</li>
<li><h4>DHCPNack</h4>
Broadcast bởi DHCP server tới DHCP clientthông báo từ chối bản tin DHCPRequest.
</li>
<li><h4>DHCPDecline</h4>
Broadcast bởi một DHCP client tới một DHCP server, thông báo từ chối IP được cung cấp vì địa chỉ đó đã được sử dụng bởi một máy khác.
</li>
<li><h4>DHCPRelease</h4>
Unicast từ DHCP client tới DHCP cung cấp IP rằng nó bỏ địa chỉ IP và thời gian sử dụng còn lại.
</li>
<li><h4>DHCPInform</h4>
Gửi từ một DHCP client (đã được cấu hình một địa chỉ IP) tới một DHCP server, để hỏi thêm về các tham số cấu hình cục bộ .
</li>
</ul>
<li><h4><a name="dhcp-header">2.3. Cấu trúc DHCP Header</a></h4>
<table style="border: 1px solid #EEE">
<tr>
<th>Trường</th>
<th>Dung lượng</th>
<th>Mô tả</th>
</tr>
<tr>
<td>Opcode</td>
<td>8 bits</td>
<td>Thể hiện loại gói tin DHCP.Value 1:các gói tin request, Value 2: các gói tin reply.</td>
</tr>
<tr>
<td>Hardware type</td>
<td>8 bits</td>
<td>Quy định cụ thể loại hardware. Value 1: Ethernet (10 Mb), Value 6: IEEE 802 ...</td>
</tr>
<tr>
<td>Hardware length</td>
<td>8 bits</td>
<td>Quy định cụ thể độ dài của địa chỉ hardware</td>
</tr>
<tr>
<td>Hop counts</td>
<td>8 bits</td>
<td>Dùng cho relay agents</td>
</tr>
<tr>
<td>Transaction Identifier</td>
<td>32 bits</td>
<td>Được tạo bởi client, dùng để liên kết giữa request và replies của client và server.</td>
</tr>
<tr>
<td>Number of seconds</td>
<td>16 bits</td>
<td>Quy định số giây kể từ khi client bắt đầu thuê hoặc xin cấp lại IP</td>
</tr>
<tr>
<td>Flags</td>
<td>16 bits</td>
<td> 
<img src="https://camo.githubusercontent.com/a797e7d3d729c8a20610548d557885178f5b4a0f/687474703a2f2f692e696d6775722e636f6d2f6f6e3569346d382e706e67"/>
B, broadcast: 1 bits = 1 nếu client không biết được ip trong khi đang gửi yêu cầu.</td>
</tr>
<tr>
<td>Client IP address</td>
<td>32 bits</td>
<td>Client sẽ đặt IP của mình trong trường này nếu và chỉ nếu nó đang có IP hay đang xin cấp lại IP, không thì mặc định = 0</td>
</tr>
<tr>
<td>Your IP address</td>
<td>32 bits</td>
<td>IP được cấp bởi server để đăng kí cho client</td>
</tr>
<tr>
<td>Server IP address</td>
<td>32 bits</td>
<td>Địa chỉ IP của server</td>
</tr>
<tr>
<td>Gateway IP address</td>
<td>32 bits</td>
<td>Sử dụng trong relay agent</td>
</tr>
<tr>
<td>Client hardware address</td>
<td>16 bytes</td>
<td>Địa chỉ lớp 2 của client, dùng để định danh</td>
</tr>
<tr>
<td>Server host name</td>
<td>64 bytes</td>
<td>Khi server gửi gói tin offer hay ack thì sẽ đặt tên của nó vào trường này, nó có thể là nickname hoặc tên miền dns</td>
</tr>
<tr>
<td>Boot filename</td>
<td>128 bytes</td>
<td>Sử dụng bởi client để yêu cầu loại tập tin khởi động cụ thể trong gói tin discover.Sử dụng bởi server để chỉ rõ toàn bộ đường dẫn, tên file của file khởi động trong gói tin offer</td>
</tr>
</table>
</li>
</ul>

<h3><a name="install">3. Cài đặt DHCP server trên ubuntu 14.04</a></h3>
<ul style="list-style: none">
<li><h4><a name="prepate">3.1. Chuẩn bị bài lab</a></h4>
<ul>
<li>Hai máy ảo ubuntu server 14.04 (máy DHCP-Server và máy mininet), một máy ảo Windows XP Pro SP3 (các máy ảo cài đặt trên VMware). Trong đó:
<ul>
<li>DHCP server: máy DHCP-Server</li>
<li>DHCP client: máy mininet và máy XP</li>
</ul>
<br>
<img src="http://i.imgur.com/kPh6qPD.png"/>
</li>
<li>Thiết lập network: mỗi máy ảo thiết lập hai card mạng như sau
<ul>
<li>Một card chế độ bridge</li>
<li>Một card chế độ Host only (trong bài lab này là dải 10.10.10.0/24)</li>
<li>Thiết lập cấu hình ip tĩnh cho card host-only của máy DHCP server với địa chỉ 10.10.10.1
<img src="http://i.imgur.com/PRjuTVt.png" />
</li>
</ul>
<div><i>Chú ý: </i>Hai máy client có thể cấu hình chỉ cần một card chế độ host-only, riêng máy DHCP-server cấu hình 2 card mạng (một card bridge đóng vai trò kết nối mạng để cài đặt DHCP server, card còn lại để cấu hình hệ thống DHCP, chi tiết nói rõ hơn ở phần sau).</div>
</li>
</ul>
</li>
<li><h4><a name="config">3.2. Cài đặt và cấu hình DHCP</a></h4>
Bước này thực hiện trên máy DHCP-Server
<ul>
<li>Bước 1: Update hệ thống: <code>sudo apt-get update</code>
</li>
<li>Bước 2: Cài đặt gói isc-dhcp-server và các gói phụ thuộc: <code>sudo apt-get install isc-dhcp-server -y</code>
</li>
<li>Bước 3: Sau khi cài đặt xong, thực hiện cấu hình gán interface của DHCP server, chỉnh sửa file sau: <code>sudo vi /etc/default/isc-dhcp-server</code>
<br>Ở đây chọn card eth1(địa chỉ 10.10.10.1/24).
<img src="http://i.imgur.com/mzgLaan.png" />
</li>
<li>Bước 4: Cấu hình dải IP cấp cho client. Mở và cấu hình file: <code>sudo vi /etc/dhcp/dhcpd.conf</code>
<div>Tìm tới dòng "slightly" và uncomment, chỉnh sửa lại như sau:<br>
<pre>
<code>
# A slightly different configuration for an internal subnet.
subnet 10.10.10.0 netmask 255.255.255.0 {
  range 10.10.10.150 10.10.10.160;
  option domain-name-servers 8.8.8.8, 8.8.4.4;
#  option domain-name "internal.example.org";
  option routers 10.10.10.1;
  option broadcast-address 10.10.10.255;
  default-lease-time 600;
  max-lease-time 7200;
}
</code>
</pre>
</div>
<img src="http://i.imgur.com/0bFuVsl.png"/>
</li>
<li>Bước 5: Khởi động lại dịch vụ: <code>sudo service isc-dhcp-server restart</code>
<div><i>Chú ý: </i>Sau khi cài đặt và cấu hình xong DHCP server, cần phải tắt DHCP server ảo của VMware đi (do bản chất khi tạo một dải vmnet chế độ host-only có một DHCP ảo cấp IP cho các máy ảo nên ta phải tắt đi để sử dụng DHCP server được cài đặt trên máy ubuntu theo bài lab này)
<img src="http://i.imgur.com/x2x2gfX.png?1"/>
</div>
</li>
</ul>
</li>
<li><h4><a name="demo">3.3. Hình ảnh demo IP được cấp phát trên các DHCP client</a></h4>
Như trong bài lab cấu hình cài đặt ở trên, dải IP cấp cho các client là: 10.10.10.150 - 10.10.10.160. Sau khi khởi động các máy client (mininet và Windows XP), địa chỉ của chúng đã được cấp phát lại theo dải trên. Cụ thể như hình minh họa dưới
<ul>
<li>Máy mininet trước và sau khi khởi động lại địa chỉ thay đổi từ: 10.10.10.137 (do DHCP server ở chế độ Host-only cấp) sang 10.10.10.150 (do DHCP server được cài đặt trên máy DHCP server là ubuntu)
<img src="http://i.imgur.com/VzR3s7F.png"/>
<img src="http://i.imgur.com/ulReZQs.png"/>
</li>
<li>IP của máy Windows XP sau khi khởi động lại và được cấp phát từ DHCP server: 10.10.10.151
<img src="http://i.imgur.com/3JQQIyz.png" />
</li>
</ul>
</li>
</ul>

<h3><a name="wireshark">4. Bắt và phân tích các bản tin DHCP trên wireshark</a></h3>

