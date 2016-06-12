#Introduction
#Mục lục
<h4><a href="#general">1. Khả năng của Identity, Authentication, Access Management </a></h4>
<h4><a href="#id">2. Identity</a></h4>
<h4><a href="#auth">3. Authentication</a></h4>
<h4><a href="#authoz">4. Access Management (Authorization)</a></h4>
<h4><a href="#benefit">5. Lợi ích chính của Keystone</a></h4>

---

<h3><a name="general">1. Khả năng của Identity, Authentication, Access Management </a></h3>
<div>
Môi trường cloud IaaS cung cấp cho người dùng khả năng truy cập vào các tài nguyên quan trọng như máy ảo, dung lượng lớn khối lưu trữ và object storage cũng như băng thông mạng. Vấn đề của mọi môi trường cloud là vấn đề về bảo mật, kiểm soát truy cập vào các tài nguyên có giá trị. Trong môi trường OpenStack , Keystone service là thành phần quan trọng chịu trách nhiệm cung cấp khả năng truy cập một cách an toàn vào tài nguyên cloud.  Theo khảo sát, 90%-95% người dùng OpenStack báo cáo họ sử dụng Keystone trong hệ thống của mình.<br>
<img src="http://i.imgur.com/BeQdwv6.png"/>
</div>

<h3><a name="id">2. Identity</a></h3>
<div>
Khái niệm Identity chỉ người dùng truy cập vào tài nguyên cloud. Trong Keystone, identity đại diện bởi một user. Trong phạm vi triển khai đơn giản, identity của một user (danh tính người dùng) có thể lưu trữ trong Keystone database. Trong môi trường thương mại, thông thường sẽ sử dụng hệ thống Identity Provider thay thế. Keystone có thể thu thập thông tin người dùng từ các Identity Provider bên ngoài.
</div>

<h3><a name="auth">3. Authentication</a></h3>
<div>
Là tiến trình xác thực danh tính người dùng, bao gồm các thông tin đăng nhập như: username, password. Về cơ bản OpenStack có thể thực hiện mọi bước xác thực. Tuy nhiên những thông tin nhạy cảm như username, password phải được quản lý và bảo vệ. Do đó, Keystone sử dụng hệ thống backend như LDAP hoặc Active Directory.
<br>
Ngoài định danh bằng username và password, việc sử dụng token là giải pháp tốt để thu hẹp khung nhìn về các thông tin nhạy cảm của người dùng, bảo vệ các thông tin đó. Token cũng hạn chế về thời gian tồn tại tránh những trường hợp có khả năng bị đánh cắp.
</div>

<h3><a name="authoz">4. Access Management (Authorization)</a></h3>
<div>
Khái niệm Authorization chỉ tiến trình xác định tài nguyên mà người dùng được phép truy cập. Cloud OpenStack cung cấp cho người dùng khả năng truy cập lượng lớn tài nguyên, do đó cần phải xác định xem user có quyền khởi tạo máy ảo hay không, có quyền được attach hay xóa volume của block storage không, user được phép tạo mạng ảo không, etc. Trong OpenStack, Keystone gán cho user roles truy cập vào các Project và Domains. Các subproject khác như Nova, Cinder, Neutron sẽ kiểm tra Project và Role của user, đánh giá thông tin ủy quyền với policy engine. Policy engine này sẽ kiểm tra thông tin (đặc biệt là Role) để xác định các thao tác vận hành mà người dùng được phép thực hiện.
</div>

<h3><a name="benefit">5. Lợi ích chính của Keystone</a></h3>
<div>
Keystone mang đến nhiều lợi ích cho môi trường OpenStack như:
<li>Thực hiện nhiều tác vụ phức tạp tích hợp với các hệ thống xác thực ngoài, cung cấp chuẩn quản lý truy cập (Access Management) cho tất cả các dịch vụ khác trong OpenStack. như Nova, Glance, Cinder, Neutron, etc. Do đó Keystone cô lập tất cả các dịch vụ khác khỏi vấn đề đòi hỏi hiểu biết về cách tương tác với các identity và authorization providers khác nhau.</li>
<li>Cung cấp một registry các containers (projects) để OpenSAtack phân chia tài nguyên (server, images etc.)</li>
<li>Cung cấp một registry các Domains sử dụng để phân chia không gian các user, group, project, etc. cho các khách hàng.</li>
<li>Cung cấp tập các Roles sử dụng để ủy quyền truy cập giữa Keystone và file policy của mỗi OpenStack services.</li>
<li>Một kho các assignment cho phép nhiều users và groups có thể được gán roles trên các project và domain</li>
<li>Một catalog lưu trữ các OpenStack services, endpoints, regions, cho phép clients tìm kiếm  dịch vụ hoặc endpoints để truy cập các dịch vụ đó.</li>
</div>
