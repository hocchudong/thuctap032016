# Tìm hiểu tcpdump
# Mục lục
<h4><a href="#wireshark">1. Giới thiệu tcpdump</a></h4>
<h4><a href="#dhcp">2. Một số lệnh cơ bản của tcpdump</a></h4>
<h4><a href="#ref">3. Tài liệu tham khảo</a></h4>

---

<h4><a name="wireshark">1. Giới thiệu tcpdump</a></h4>
<div>
TCPDUMP là một chương trình phân tích gói tin cho phép theo dõi băng thông mạng thông qua việc lưu trữ dữ liệu (gói tin – packet) truyền tải trên mạng có thể "bắt được" (capture) vào file để phục vụ công việc phân tích sâu hơn về sau này.  Lệnh tcpdump này có sẵn ở hầu hết các hệ điều hành Linux/Unix.
</div>
Một số tính năng của tcpdump:
<ul>
<li>Nhìn thấy được các bản tin dump trên terminal</li>
<li>Bắt các bản tin và lưu vào định dạng PCAP (có thể đọc được bởi Wireshark)</li>
<li>Tạo được các bộ lọc Filter để bắt các bản tin cần thiết, ví dụ: http, ftp, ssh, etc.</li>
<li>Có thể nhìn được trực tiếp các bản tin điều khiển hệ thống Linux sử dụng wireshark</li>
<li>Có thể nhìn được trực tiếp các bản tin điều khiển hệ thống Linux sử dụng wireshark</li>
<li>Tham khảo thêm các options trên <a href="http://www.tcpdump.org/tcpdump_man.html">tcpdump man page</a></li>
</ul>

<h4><a name="dhcp">2. Một số lệnh cơ bản của tcpdump</a></h4>
<ul>
<li>2.1. Bắt gói tin từ một giao diện ethernet cụ thể thông qua tcpdump -i
<div>Nếu thực thi lệnh tcpdump không có tùy chọn, nó sẽ bắt tất cả các gói tin lưu thông qua card mạng. tùy chọn -i cho phép lọc một interface cụ thể. Ví dụ lọc để bắt các gói qua interface eno16777736 :
<br><br>
<img src="http://i.imgur.com/fTaa1qT.png"/>
<br><br>
</div>
</li>
<li>2.2. Chỉ bắt số lượng N gói tin thông qua lệnh tcpdump -c
<div>Khi thực thi lệnh tcpdump, nó sẽ thực hiện chừng nào chưa hủy lệnh (Ctrl+C). Sử dụng tùy chọn -c để giới hạn số lượng gói tin sẽ bắt. 
<br><br>
<img src="http://i.imgur.com/yPtEEWZ.png"/>
<br><br>
</div>
</li>
<li>2.3. Hiển thị các gói tin được bắt trong hệ ASCII thông qua tcpdump -A
<br><br>
<img src="http://i.imgur.com/TnGwuuM.png"/>
<br><br>
</li>
<li>2.4. Hiển thị các gói tin được bắt dưới dạng HEX và ASCII thông qua tcpdump -XX
<br><br>
<img src="http://i.imgur.com/EFVvYy4.png"/>
<br><br>
</li>
<li>2.5. Bắt gói tin và ghi vào một file thông qua tcpdump -w
<div>Việc lưu lại file "captured" có thể dùng để sử dụng phân tích sau, hoặc có thể mở bằng các phần mềm phân tích mạng khác như wireshark (định dạng thường gặp là *.pcap). Ví dụ:
<br><br>
<img src="http://i.imgur.com/NvXsr7u.png"/>
<br><br>
</div>
</li>
<li>2.6. Đọc các gói tin từ một file thông qua tcpdump -r
<div>tcpdump cho phép mở file "captured" trước đó hoặc mở file "captured" của các công cụ phân tích mạng khác như wireshark. Ví dụ ở đây mở file dhcp.pcapng do wireshark bắt được:
<br><br>
<img src="http://i.imgur.com/SRvV9bA.png"/>
<br><br>
</div>
</li>
<li>2.7. Bắt các gói tin với địa chỉ IP thông qua tcpdump -n
<br><br>
<img src="http://i.imgur.com/YQfNhFu.png"/>
<br><br>
</li>
<li>2.8. Bắt các gói tin với các dấu thời gian thông quan tcpdump -tttt
<br><br>
<img src="http://i.imgur.com/rE7PuZd.png"/>
<br><br>
</li>
<li>2.9. Đọc các gói tin lớn hơn N byte -> chỉ cho phép đọc các gói tin lớn hơn N bytes:
<code>tcpdump -w g_512.pcap greater 512</code>
</li>
<li>2.10. Chỉ nhận những gói tin trong với một kiểu giao thức cụ thể. Ví dụ giao thức tcp:
<br><br>
<img src="http://i.imgur.com/IQtInxA.png"/>
<br><br>
</li>
<li>2.11. Đọc các gói tin nhỏ hơn N byte: <code> tcpdump -w l_512.pcap  less 512</code>
</li>
<li>2.12.Nhận các gói tin trên một cổng cụ thể thông qua tcpdump port
<br><br>
<img src="http://i.imgur.com/mO5VHGG.png"/>
<br><br>
</li>
<li>2.13. Bắt các gói tin trên địa chỉ IP và cổng đích
<br><br>
<img src="http://i.imgur.com/tRGrST4.png"/>
<br><br>
</li>
<li>2.14. Bắt các gói tin kết nối TCP giữa hai host<br>
<code>tcpdump -w dump1.pcap -i eth0 dst eno16777736 and port 22</code>
<br>
</li>
<li>2.15. Bộ lọc gói tin tcpdump – Bắt tất cả các gói tin ngoại trừ arp 
<br><br>
<img src="http://i.imgur.com/8XaQyw2.png"/>
<br><br>
</li>
</ul>

<h4><a name="ref">3. Tài liệu tham khảo</a></h4>
<ul>
<li><a href="http://securitydaily.net/phan-tich-goi-tin-15-lenh-tcpdump-duoc-su-dung-trong-thuc-te/">http://securitydaily.net/phan-tich-goi-tin-15-lenh-tcpdump-duoc-su-dung-trong-thuc-te/</a></li>
<li><a href="http://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/">http://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool</a></li>
</ul>
