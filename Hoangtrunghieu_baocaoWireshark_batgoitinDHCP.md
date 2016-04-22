#Báo cáo tim hiểu cài đặt wireshark

##Mục lục

[I.Giới thiệu](#gtws)

- [1.Giới thiệu](#gt)

- [2.Các tiện ích, đặc điểm của phần mềm Wireshark](#tienich)

- [3.Giao diện](#giaodien)

- [4.Tính năng nâng cao](#tinhnang)

[II.Thực hành bắt phân tích gói tin bằng WireShark](#goitin)

- [1.Bắt gói tin](#bat)

- [2.Phân tích gói tin](#phantich)

<a name="gtws"></a>
##I.Giới thiệu Wireshark
<ul>
<a name="gt"></a>

###1.Giới thiệu 

Wireshark là một công cụ kiểm tra, theo dõi và phân tích thông tin mạng được phát triển bởi Gerald Combs. 
Phiên bản đầu tiên của Wireshark mang tên Ethereal được phát hành năm 1988. 
Đến nay, WireShark vượt trội về khả năng hỗ trợ các giao thức (khoảng 850 loại), từ những loại phổ biến như TCP, IP đến những loại đặc biệt như là AppleTalk và Bit Torrent. 
<a name="tienich"></a>

###2.Các tiện ích, đặc điểm của phần mềm Wireshark 
<ul>
<li>Giao diện đẹp thân thiện, dễ dùng.</li>

<li> Là phần mềm miễn phí </li>

<li> Cộng đồng người dùng tốt, năng động </li>

<li> Hỗ trợ mọi hệ điều hành</li>

<li> Capture với thông tin chi tiết</li>

<li>Có thể mở và lưu trữ dữ liệu</li>

<li>Có thể import, export những packet đến từ nhiều chương trình capture</li>

<li>Lọc, tìm gói tin theo nhiều tiêu chuẩn</li>
</ul>
<a name="giaodien"></a>

###3.Giao diện WireShark
<ul>
<img src=https://farm8.staticflickr.com/7579/16011145562_eae3b825fc_o.png>
<li>Các Tùy chỉnh nằm ở phía trên của cửa sổ. 
Mối quan tâm của chúng ta hiện nay là các tập tin và Capture.
 Các menu File cho phép bạn lưu dữ liệu gói tin bị bắt hoặc mở một tập tin có chứa các gói dữ liệu bị bắt từ trước, và thoát khỏi ứng dụng Wireshark. 
 Menu Capture cho phép bạn bắt đầu bắt gói tin.</li>
 <li>Cửa sổ danh sách gói tin hiển thị một bản tóm tắt một dòng cho mỗi gói tin
bị bắt, tại thời điểm mà các gói tin bị bắt, nguồn và địa chỉ đích của gói tin, các loại giao thức, và thông tin giao thức cụ thể có trong các gói tin. 
Danh sách này có thể được sắp xếp theo tùy chỉnh của mỗi loại bằng cách nhấp vào một tên cột. 
Các loại trường giao thức liệt kê các giao thức cấp cao nhất mà gửi hoặc nhận được gói tin này.</li>
<li>Cửa sổ chi tiết gói tin cung cấp chi tiết về các gói lựa chọn. 
Những chi tiết này bao gồm thông tin về các khung Ethernet (giả sử các gói đã được gửi/nhận trên một cổng Ethernet) và IP gói tin. 
Số lượng Ethernet và IP lớp chi tiết hiển thị có thể được mở rộng hoặc giảm thiểu bằng cách nhấp vào biểu tượng cộng hoặc trừ bên trái của khung Ethernet hoặc IP trong cửa sổ chi tiết gói tin. 
Nếu gói dữ liệu đã được thực hiện trên TCP hoặc UDP, chi tiết về TCP hoặc UDP cũng sẽ được hiển thị, tương tự mà có thể mở rộng hoặc thu nhỏ. 
Cuối cùng, chi tiết về các giao thức cấp cao nhất mà gửi hoặc nhận được gói tin này cũng được cung cấp.</li>
<li>Cửa sổ nội dung gói tin: hiển thị toàn bộ nội dung của khung hình chụp,
trong cả hai định dạng mã ASCII và định dạng mã Hex.</li>
<li>Phía trên cùng của giao diện người dùng đồ họa Wireshark, là màn hình hiển thị kỹ thuật lọc gói tin, mà trong đó một tên giao thức hoặc các thông tin khác có thể được nhập vào đặt để lọc các thông tin hiển thị trong cửa sổ (và do đó các gói tiêu đề và gói nội dung cửa sổ).</li>
</ul>
<a name="tinhnang"></a>

###4.Tính năng nâng cao
<ul>
<li>Name Resolution</li>
<ul>
<li>Phân giải địa chỉ để file dữ liệu dễ đọc</li>
<li>3 công cụ phân giải<li>
<ul>
<li>MAC Name Resolution: phân giải địa chỉ MAC tầng 2 sang IP tầng 3, nếu lỗi chuyển 3 byte đầu của dịa chỉ MAC sang tên hãng sản xuất được IEEE đặc ra</li>
<li>Network Name Resolution: chuyển đổi địa chỉ tầng 3 sang một bên DNS dễ đọc</li>
<li>Transport Name Resolution:chuyển đổi một cổng sang một tên dịch vụ tương ứng</li>
</ul>
</ul>
<li>Protocol Dissection: một protocol dissector cho phép WireShark phân chia giao thức thành một số thành phần để phân tích.ICMP protocol dissector phân chia, định dạng dữ bắt đươcnhiw là một gói ICMP</li>
<li>Following TCP Streams:phối hợp tất cả các thông tin liên quan gói tin và chỉ ra dữ liệu gói tin chứa giống như người dùng cuối thấy trong ứng dụng, sắp xếp dữ liệu, giải mã một phiên instant messages</li>
<li>Cửa sổ thống kê phân cấp giao thức:Khi bắt được một file kích thước lớn ta cần biết phân bố giao thức file đó, thay vì đếm từng fiel ta dùng cửa sổ thông kê phân cấp giao thức</li>
<li>Xem các Endpoints:Endpoint là chỗ kết nối kết thúc trên giao thức cụ thể, chỉ ra mỗi thống kê hữu ích cho mỗi Endpoint gồm địa chỉ từng máy , số lượng gói tin, dung lượng truyền nhận mỗi máy</li>
<li>Cửa sổ đồ thị IO:vẽ đồ thị lưu lượng dữ liệu</li>
</ul>
</ul>
<a name="goitin"></a>

##II.Thực hành bắt phân tích gói tin bằng WireShark
<ul>
<a name="bat"></a>

###1.Bắt gói tin
<ul>
<img src=http://i.imgur.com/LsAkS3x.png>
- Mô hình mạng
- Khởi động 2 máy ảo và cài đặt wireshark trên máy ảo win 7
- Trên máy ảo UbuntuServer gõ lệnh sudo dhclient.
- Máy ảo win7 khởi động wireshark với quyền admin, trong wireshark chọn Local Network Connection 
<img src=http://i.imgur.com/Dqv4pbc.png>
- Trên bộ lọc chọn bootp.
</ul>

<a name="phantich"></a>
###2.Phân tích gói tin DHCP
<ul>
<li>DHCP Discovery</li>
<img src=http://imgur.com/ZdWGK4D.png>
<ul>
<li>1.source mac(client) des mac(servers)</li>
<li>2.source ip (client) = 0.0.0.0 do lúc này client chưa có ip, des ip servers =255.255.255.255 do đây là bản tin broadcast.</li>
<li>3.source port=68(client) và des port=67(server)</li>
<li>4.Loại gói tin:DHCP discovery</li>
<li>5.IP được client yêu cầu cấp phát</li>
<li>6.Hostname của client</li></li>
</ul>
<li>DHCP offer</li>
<img src=http://imgur.com/bWCElmE.png>
<ul>
<li>1.source mac(server) des mac(client).</li>
<li>2.source ip (server) và des ip(client).</li>
<li>3.source port=67(server) des port=68(client).</li>
<li>4.ip client trong gói tin header</li>
<li>5.Loại gói tin:DHCP offer</li>
<li>6.Định danh dhcp server:chính là ip của server</li>
<li>7.Subnet mask cấp cho client</li>
<li>8.default gateway cấp cho client</li>
<li>9.Tên miền</li>
</ul>
<li>DHCP Request</li>
<img src=http://imgur.com/8pUL04S.png>
<li>DHCP ACK</li>
<img src=http://imgur.com/8pUL04S.png>
</ul>
</ul>
</ul>
