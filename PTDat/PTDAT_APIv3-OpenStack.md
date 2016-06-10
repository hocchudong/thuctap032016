#APIv3-OpenStack.

****

##Giới Thiệu.

- Khái niệm: Một giao diện lập trình ứng dụng (tiếng anh Application Programming Interface hay API) là một giao diện mà một hệ thống máy tính hay ứng dụng cung cấp để cho phép các yêu cầu dịch vụ có thể được tạo ra từ các chương trình máy tính khác, và hoặc cho phép dữ liệu có thể được trao đổi qua lại giữa chúng. Cũng giống như bàn phím là một thiết bị giao tiếp giữa người dùng và máy tính.

##API trong OpenStack.

- Sử dụng API của Openstack có thể tạo máy ảo, tạo image và các hoạt động khác trong Openstack.

- Để gửi các yêu cầu đến API, ta có thể sử dụng các cách thức sau:
 <ul>
 <li>cURL: là một công cụ dòng lệnh mà cho phép bạn gửi các yêu cầu và nhận phản hồi theo http.</li>
 <li>Openstack command-line clients: Mỗi một project của Openstack cung cấp một command-line client mà cho phép bạn truy xuất vào API một cách dễ dàng.</li>
 <li>REST clients: Cả Mozilla và Google đều cung cấp giao diện đồ họa dựa trên trình duyệt cho REST.</li>
 <li>Openstack Python Software Development Kit (SDK): Sử dụng SDK để viết một script tự động Python mà tạo và quản lý tài nguyên trong cloud Openstack. SDK triển khai Python liên kết với Openstack API, nó cho phép bạn thực hiện các nhiệm vụ tự động trong python bởi gọi đến các objects python hơn là gọi đến REST trực tiếp. Tất cả các tools được triển khai bởi sử dung Python SDK.</li>
 </ul>

##Sử dụng Advanced RESTClient Chrome tác động đến API.

###Cài đặt ứng dụng.

- Vào web store của chrome, tìm kiếm và cài đặt ứng dụng Advanced RESTclient cho trình duyệt.

![rest](http://i.imgur.com/wA371m1.png)

- Giao diện của ứng dụng:

![giaodien](http://i.imgur.com/FefnK5L.png)

##Cách sử dụng APIv3.

- Để sử dụng APIv3 chúng ta vào http://developer.openstack.org/api-ref-identity-v3.html để xem chi tiết.
- Bây giờ chúng ta bắt đầu với việc lấy token với APIv3. (Ở trang http://developer.openstack.org/api-ref-identity-v3.html có 3 phần auth/token tuy nhiên chúng ta chọn cái thứ 3). Ở đây chúng ta để ý thêm xem nó sử dụng giao thức gì để thực hiện. Như trong hình thì `/v3/auth/tokens` sử dụng giao thức `POST`.

![scr9](http://i.imgur.com/mC4eior.png)

- Tiếp theo `detail` nó ra và lấy đoạn code.

![scr3](http://i.imgur.com/FTwT4nw.png)

- Ở đây có 2 chỗ cần lưu ý. Đó là 2 cái `id` này. Chúng ta cần thay thế những `id` này thành `id` của OpenStack mà chúng ta cài đặt.

![scr4](http://i.imgur.com/lPzDE33.png)

- Dùng 2 lệnh `openstack user list` để lấy `id` của user admin, và `openstack project list` để lấy `id` của project admin. Sau đó chúng ta thay thế vào đoạn code đã coppy.
- Bật tools Advanced RESTClient Chrome và làm theo các bước như hình vẽ.

![scr5](http://i.imgur.com/rZMyqqH.png)

 <ul>
 <li>1. Điền địa chỉ của controller và enpoint của Keystone cùng vớ đường dẫn APIv3. </li>
 <li>2. Chọn phương thức mà chúng ta sử dụng.</li>
 <li>3. chọn content-type. Để có thể gửi file bằng phương thức HTTP thì các file phải được định dạng dưới dạng JSON.</li>
 <li>4. thay thế `id` mặc định bằng `id` của user admin.</li>
 <li>5. Thay thế `id` project mặc định bằng `id` của project admin.</li>
 </ul>

- Sau đó chúng ta gửi để nhận lại token từ Keystone.
- Nếu thành công chúng ta sẽ nhận được một bản tin như sau :

![scr6](http://i.imgur.com/37KhhgZ.png)

- Ở đây chúng ta chú ý đến 2 trường ở phần Header đó là `X-Subject-Token` và `Vary`. 2 trường này dùng để sử dụng xác thực khi chúng ta thực hiện các tác động vào trong OpenStack.
- Ví dụ ở đây chúng ta lấy ra các list user của OpenStack.

![scr10](http://i.imgur.com/My3XZrQ.png)

- Chúng ta sẽ thực hiện lấy danh sách user bằng phương thức `GET`
 với các bước thực hiện như sau : 

![scr7](http://i.imgur.com/wXO5lQO.png)

- Nếu thành công kết quả chúng ta thu được sẽ là : 

![scr8](http://i.imgur.com/JR19Vfc.png)

- Đây là sơ lược về cách dùng APIv3 trong OPenStack. Bài viết được tham khảo tại các 
- 
#NGUỒN :

- http://developer.openstack.org/api-ref-identity-v3.html
- https://github.com/hocchudong/API-Openstack