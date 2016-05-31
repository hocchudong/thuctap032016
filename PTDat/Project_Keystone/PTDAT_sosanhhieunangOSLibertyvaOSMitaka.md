###Keystone token Performance: Liberty với Mitaka.

- Một số cải tiến đã được thực hiện trong Keystone Mitaka, bao gồm bộ nhớ đệm và danh mục. Nó tạo ra các thẻ nhanh hơn theo đánh giá của các nhà phát triển Keystone.
- Chúng ta cùng xem qua thử nghiệm của MATT FISCHER.
 
####

- Thử nghiệm cho chạy 3 node Keystone cluster trên các máy ảo đang chạy trên OpenStack CLoud. Các node được frontend bởi một VM khác chạy haproxy. Keystone được sử dụng thuật toán cân bằng tải roud-robin. Yêu cầu các token từ máy ảo thứ 3 thông qua các VIP được cung cấp bởi haproxy. Các Keystone node có 2 VCPU và 4G RAM>
- Keystone đang chạy bên trong một container docker, chạy uwsgi. uwsgi có 2 đề tĩnh : 
 <ul>
 <li>The Mitaka code is based on stable/mitaka from March 22, 2016.</li>
 <li>The Liberty code is based on stable/liberty from March 16, 2016.</li>
 </ul>

- Keystone được cấu hình sử dụng thẻ Fernet và mysql phụ trợ.
 
**Thiết lập thử nghiệm**

- MATT làm 20 điểm chuẩn chạy đối với mỗi thiết lập, trì hoãn 120 giây giữa mỗi lần chạy. Mục tiêu ở đây là  để thậm chí ra thay đổi hiệu suất dựa trên thực tế rằng đây là những máy ảo đang chạy trong một đám mây. Các bài kiểm tra chạy như sau:
 <ul>
 <li>Create 200 tokens serially</li>
 <li>Validate 200 tokens serially</li>
 <li>Create 1000 tokens concurrently (20 at once)</li>
 <li>Validate 500 tokens concurrently (20 at once)</li>
 </ul>

- Có một cái gì đó không ổn trong hoạt động của thẻ Mitaka Fernet và có sự xuống cấp nghiêm trọng ở đây.
- Các biểu đồ sẽ cho ta thấy kết quả của cuộc thử nghiệm. Mỗi biểu đồ dưới đây cho thấy có bao nhiêu yêu cầu mỗi giây có thể được xử lý, và xác nhận đồng thời là liên quan đến nhiều nhất bởi vì đây là mô hình chuẩn của những gì một đám mây đang làm. Hàng chục cuộc gọi API được thực hiện cùng một lúc đến hàng chục dịch vụ và mỗi một người muốn xác nhận một token.

![scr1](http://i.imgur.com/TtHWSlo.png)

- Vì vậy, bạn có thể thấy rằng xác nhận đồng thời là chậm hơn nhiều. Chúng ta hãy cũng so sánh với memcache được kích hoạt:

![scr2](http://i.imgur.com/Ns7rPPv.png)

![scr3](http://i.imgur.com/AMU8p99.png)

- Thông qua memcache (hiển thị bằng số liệu thống kê lệnh) ở Mitaka là ghấp 3-4 lần những gì ở Liberty. Có lẽ Keystone là bộ nhớ đệm quá nhiều hoặc quá thường xuyên.