# Tìm hiểu wireshark và phân tích giao thức DHCP với wireshark
# Mục lục
<h4><a href="#wireshark">1. Tìm hiểu wireshark</a></h4>
<ul style="list-style: none">
<li><a href="#intro">1.1. Giới thiệu</a></li>
<li><a href="#feature">1.2. Các tính năng của wireshark</a></li>
<li><a href="#basic">1.3. Các tính năng nâng cao</a></li>
</ul>
<h4><a href="#dhcp">2. Phân tích giao thức DHCP với wireshark</a></h4>
<ul style="list-style: none">
<li><a href="#lab">2.1. Chuẩn bị lab DHCP</a></li>
<li><a href="#analysis">2.2. Phân tích giao thức DHCP</a>
<ul style="list-style: none">
<li><a href="#filter">2.2.1. Lọc gói DHCP</a></li>
<li><a href="#discover">2.2.2. Gói tin DHCPDiscover</a></li>
<li><a href="#offer">2.2.3. Gói tin DHCPOffer</a></li>
<li><a href="#request">2.2.4. Gói tin DHCPRequest</a></li>
<li><a href="#ack">2.2.5. Gói tin DHCPACK</a></li>
</ul>
</li>
</ul>
<h4><a href="#ref">3. Tài liệu tham khảo</a></h4>

---

<h3><a name="wireshark"></a>1. Tìm hiểu wireshark</h3>
<ul style="list-style: none">
<li><h4><a name="intro">1.1. Giới thiệu</a></h4>
<ul>
<li>Phần mềm phân tích gói tin miễn phí và mã nguồn mở.</li>
<li>Sử dụng nhằm mục đích khắc phục lỗi mạng, phân tích hệ thống mạng, phát triển các giao thức và cũng được sử dụng trong giảng dạy.</li>
<li>Là một phần mềm đa nền tảng, hỗ trợ hầu hết các hệ điều hành hiện tại: GNU/Linux, OS X, BSD, Windows, etc. Với các hệ điều hành không hỗ trợ GUI, wireshark có phiên bản terminal-based là TShark.</li>
<li>WireShark vượt trội về khả năng hỗ trợ các giao thức (khoảng 2000 loại trong phiên bản 2.0.2), từ những loại phổ biến như TCP, IP đến những loại đặc biệt như là AppleTalk và Bit Torrent</li>
</ul>
</li>
<li><h4><a name="feature">1.2. Các tính năng của wireshark</a></h4>
<ul>
<li>Bắt các gói tin theo thời gian thực trên các NIC</li>
<li>Mở các file captured của các công cụ bắt gói tin khác như tcpdump/WinDump</li>
<li>Import các packet từ file text chứa mã hex của dữ liệu các packet</li>
<li>Hiển thị dữ liệu với các thông tin chi tiết của các giao thức</li>
<li>Lưu lại các bản tin các bắt được</li>
<li>Export các packet đã bắt được từ file capture</li>
<li>Lọc các gói theo patern</li>
<li>Tìm kiếm các gói tin và tô màu cho các packet đã lọc</li>
<li>etc.</li>
</ul>
</li>
<li><h4><a name="advfeature">1.3. Các tính năng nâng cao</a>

</h4>
<h4>Name Resolution</h4>
<ul>
<li>Dữ liệu truyên trong mạng thông qua một số hệ thống địa chỉ và thường là khó nhớ. (như địa chỉ MAC). Phân giải địa chỉ (Name resolution) là quá trình chuyển đổi địa chỉ loại này sang địa chỉ loại khác dễ hiểu hơn</li>
<li>Các kiểu công cụ phân giải tên trong Wireshark:
<ul>
<li>MAC Name Resolution: phân giải địa chỉ MAC sang địa chỉ IP. Nếu lỗi Wireshark chuyển 3 byte đầu tiên của địa chỉ MAC sang tên hãng sản xuất được IEEE đặc tả. Ví dụ: khi lab trên VMware ta có địa chỉ Vmware_0b:4e:75</li>
<li>Network Name Resolution: chuyển đổi địa chỉ tầng 3 sang một tên DNS để dễ nhớ</li>
<li>Transport Name Resolution: chuyển đổi một cổng sang tên một dịch vụ tương ứng. Ví dụ: cổng 80 là http, cổng 22 là ssh</li>
</ul>
</li>
</ul>
<h4>Protocol Dissection</h4>
<ul>
<li>Một protocol disector cho phép Wireshark phân chia một giao thức thành một số thành phần để phân tích</li>
<li>Một desector cho một giao thức phải tích hợp trong Wireshark để hỗ trợ phân tích giao thức đó</li>
<li>Wireshark quyết định việc lựa chọn dissector nào được sử dụng bằng cách phân tích logic đã được cài đặt sẵn và dự đoán.</li>
</ul>
<h4>Following TCP Streams</h4>
<p>Wireshark xem các dòng TCP như ở tầng ứng dụng, cho phép phối hợp các thông tin liên quan tới các gói tin, chỉ cung cấp dữ liệu mà các gói tin hàm chứa giống như người dùng cuối. Tính năng này sắp xếp dữ liệu để xem một cách đơn giản.</p>
<h4>Cửa sổ thống kê phân cấp giao thức</h4>
Khi bắt được một file có kích thước lớn, chúng ta cần biết được phân bố các giao thức trong file đó, ví dụ như bao nhiêu phần trăm TCP, bao nhiêu phần trăm IP, etc. . Thay vì phải đếm từng gói tin để thu được kết quả, chúng ta có thể sử dụng cửa sổ thống kê phân cấp giao thức để kiểm thử mạng.
<br><br>
<img src="http://i.imgur.com/nV1ClTH.png"/>
<br>
<h4>Xem các Endpoints</h4>
<p>Một Endpoint là chỗ mà kết nối kết thúc trên một giao thức cụ thể. Việc xem các endpoint cho phép khoanh vùng vấn đề chỉ còn lại là các endpoint cụ thể trong mạng. Hộp thoại endpoints thống kê các thông tin hữu ích như địa chỉ của từng máy, số lượng gói tin và dung lượng đã được truyền nhận của từng máy.</p>
<br>
<img src="http://i.imgur.com/vGpE0St.png"/>
<br>
<h4>Cửa số đồ thị IO</h4>
<ul>
<li>Cửa sổ đồ thị IO của Wireshark cho phép bạn vẽ đồ thị lưu lượng dữ liệu trên mạng.</li>
<li>Cho phép tìm kiếm các đột biến hoặc những thời điểm không có dữ liệu truyền của các giao thức cụ thể </li>
<li>Cho phép vẽ đồng thời 5 đường trên cùng một đồ thị cho từng giao thức, giúp dễ dàng hơn để thấy sự khác nhau của các đồ thị.</li> 
<br><br>
<img src="http://i.imgur.com/Xcfj46I.png"/>
<br>
</ul>
</li>
</ul>
<h3><a name="dhcp"></a>2. Phân tích giao thức DHCP với wireshark</h3>
<ul style="list-style: none">
<li><h4><a name="lab">2.1. Chuẩn bị lab DHCP</a></h4>
<p>Sử dụng lab DHCP trong bài báo cáo <a href="https://github.com/hocchudong/Thuc-tap-thang-03-2016/blob/master/ThaiPH_baocaotimhieudhcp.md#wireshark">Tìm hiểu giao thức DHCP.</a></p>
<div><i>Chú ý: </i>Ở bài lab trên sử dụng DHCP server cài trên ubuntu 14.04. Các gói bắt và phân tích DHCP dưới đây sử dụng client là CentOS 7. Dưới đây là hình ảnh địa chỉ của CentOS client được cấp phát bởi DHCP server.
<br><br>
<img src="http://i.imgur.com/csb7oSX.png"/>
<br>
</div>
</li>
<li><h4><a name="analysis">2.2. Phân tích giao thức DHCP</a></h4>
<ul style="list-style: none">
<li><h4><a name="filter">2.2.1. Lọc gói DHCP</a></h4>
<ul>
<li>Do bài lab với DHCP cấp IP cho các máy trong dải VMnet2 nên ta sẽ bắt các gói tin trên VMware Network Adapter VMnet2.
<br><br>
<img src="http://i.imgur.com/RkuKOa8.png"/>
<br><br></li>
<li>Lọc gói DHCP, gõ: <code>bootp</code>
<br><br>
<img src="http://i.imgur.com/1f7VJ5k.png"/>
<br>
</li>
</ul>
</li>
<li><h4><a name="discover">2.2.2. Gói tin DHCPDiscover</a></h4>
Bản tin broadcast từ máy client gửi cho DHCP server yêu cầu cấp địa chỉ IP trong lần đầu tham gia mạng. 
<ul>
<li>IP nguồn: 0.0.0.0. IP đích: 255.255.255.255</li>
</ul>
<br><br>
<img src="http://i.imgur.com/axZmj8n.png"/>
<br><br>
</li>
<li><h4><a name="offer">2.2.3. Gói tin DHCPOffer</a></h4>
DHCP server gửi bản tin offer đề nghị cấp địa chỉ 10.10.10.152 cho client, kèm theo các thông tin về subnet mask, domain name, thời gian cho thuê IP, etc.
<br><br>
<img src="http://i.imgur.com/3W9Kvyi.png"/>
</li>
<li><h4><a name="request">2.2.4. Gói tin DHCPRequest</a></h4>
Bản tin DHCP client gửi cho DHCP server chấp nhận địa chỉ IP được cấp từ bản tin offer trên
<br><br>
<img src="http://i.imgur.com/JXPU9XC.png"/>
<br><br>
</li>
<li><h4><a name="ack">2.2.5. Gói tin DHCPACK</a></h4>
Server xác nhận các thông tin từ bản tin DHCPRequest và gửi trả lại phía client các thông tin cấu hình IP, kết thúc quá trình cấp phát địa chỉ IP.
<br><br>
<img src="http://i.imgur.com/VyhGvZl.png"/>
<br><br>
</li>
</ul>
</li>
</ul>
<h3><a name="ref">3. Tài liệu tham khảo</a></h3>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wireshark">https://en.wikipedia.org/wiki/Wireshark</a></li>
<li><a href="https://www.wireshark.org/download/docs/user-guide-a4.pdf">
https://www.wireshark.org/download/docs/user-guide-a4.pdf
</a></li>
</ul>




