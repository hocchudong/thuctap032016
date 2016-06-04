#Keystone - Giới thiệu chung
#Mục lục
<h4><a href="#keystone">1. Keystone là gì?</a></h4>
<h4><a href="#architecture">2. Kiến trúc Keystone</a></h4>
<h4><a href="#flow">3. Keystone workflow</a></h4>
<h4><a href="#usr">4. Keystone User Management</a></h4>
<h4><a href="#serv">5. Keystone Service Management</a></h4>

---

<h3><a name="keystone">1. Keystone là gì?</a></h3>
<div>
Keystone là OpenStack project cung cấp các dịch vụ Identity, Token, Catalog, Policy cho các project khác trong OpenStack. Nó triển khai Identity API của OpenStack.
</div>
<div>Hai tính năng chính của Keystone:
<ul>
<li>User Management: keystone xác thực tài khoản người dùng và chỉ định xem người dùng có quyền được làm gì.</li>
<li>Service Catalog: Cung cấp một danh mục các dịch vụ sẵn sàng cùng với các API endpoints để truy cập các dịch vụ đó.</li>
</ul>
</div>

<h3><a name="architecture">2. Kiến trúc Keystone</a></h3>
<div>
Keystone cung cấp các dịch vụ chính như sau:
<ul>
<li>Identity: các Identity service cung cấp dịch vụ xác thực các thông tin chứng thực người dùng gửi tới, cung cấp dữ liệu về Users, Projects, Roles cũng như các metadata khác.</li>
<li>Token: xác nhận và quản lý các Tokens sử dụng cho việc xác thực các yêu cầu sau khi thông tin của các user/project đã được xác thực. </li>
<li>Catalog: cung cấp endpoints của các dịch vụ sử dụng cho việc tìm kiếm và truy cập các dịch vụ.</li>
<li>Policy: cung cấp cơ chế ủy quyền rule-based</li>
<li>Resource</li>
<li>Assignment</li>
</ul>
<img src="http://i.imgur.com/wB4KyCi.png"/>
<div>Mỗi dịch vụ lại được cấu hình để sử dụng một backend cho phép keystone lưu trữ thông tin Identity như thông tin credentials, token, etc. Việc quy định mỗi dịch vụ sử dụng hệ thống backend nào được cấu hình trong file keystone.conf. (có thể tham khảo hình vẽ trên). Một số hệ thống backend điển hình:
<ul>
<li>KVS Backend(hiện tại không còn sử dụng): là giao diện backend đơn giản hỗ trợ tìm kiếm theo khóa chính</li>
<li>SQL Backend: cung cấp hệ thống backend bền vững để lưu trữ thông tin</li>
<li>PAM Backend: Hệ thống backend mở rộng cung cấp quan hệ 1-1 giữa user và tenants(sử dụng trong các phiên bản cũ như Gzilly ).</li>
<li>LDAP Backend: LDAP là hệ thống lưu trữ các user và project trong các subtree tách biệt nhau.</li>
<li>Multiple Backend: sử dụng kết hợp nhiều hệ thống Backend, trong đó SQL lưu trữ các service account (tài khoản của các dịch vụ như: nova glance, etc.), còn LDAP sử dụng lưu trữ thông tin người dùng, etc.</li>
</ul>
</div>
Keystone trong hệ thống OpenStack:
<img src="https://camo.githubusercontent.com/c02dcfac61b8789b5b4193d1122ee6e39a33944b/687474703a2f2f646f63732e6f70656e737461636b2e6f72672f61646d696e2d67756964652f5f696d616765732f6f70656e737461636b5f6b696c6f5f636f6e6365707475616c5f617263682e706e67"/>
</div>

<h3><a name="flow">3. Keystone workflow</a></h3>
<div>
<img src="http://i.imgur.com/VaHYH48.png"/>
<br>

</div>

<h3><a name="usr">4. Keystone User Management</a></h3>
<div>
Keystone quản lý các user, project(tenants),  roles, chịu trách nhiệm xác thực và ấn định quyền truy cập các tài nguyên trong hệ thống. Có ba khái niệm chính trong tính năng User Management:
<ul>
<li>User: là tải khoản của người sử dụng dịch vụ, bao gồm một số thông tin như: username, password, email</li>
<li>Project(tenant): khái niệm liên quan tới việc gộp, cô lập các nguồn tài nguyên. Tự các project không hề có user. Người dùng được gán roles đối với mỗi project, quy định quyền truy cập tài nguyên trong project.</li>
<li>Roles: chỉ định các thao tác vận hành hệ thống được phép thực hiện, tài nguyên mà người dùng được phép sử dụng.</li>
</ul>
</div>

<h3><a name="serv">5. Keystone Service Management</a></h3>
<div>
Keystone cũng cung cấp danh mục các dịch vụ cùng với các API endpoints để truy cập các dịch vụ đó. Có hai khái niệm chính trong tính năng "service management":
<ul>
<li>Services: các dịch vụ khác trong OpenStack sẽ có tài khoản tương ứng (thường có có tên tài khoản trùng code name của dịch vụ như nova, glance, etc.). Các tài khoản này thuộc domain đặc biệt tên là service.</li>
<li>Endpoints: điểm đầu mối để truy cập các dịch vụ, thể hiện bằng URL để truy cập các dịch vụ đó.</li>
</ul>
</div>
