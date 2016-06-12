#Chương 1 - Các chủ đề căn bản trong Keystone

#Mục lục
<h4><a href="#concepts">1. Các khái niệm trong Keystone</a></h4>
<ul>
<li><a href="#11">1.1. Project</a></li>
<li><a href="#12">1.2. Domain</a></li>
<li><a href="#13">1.3. Users và User Groups (Actor)</a></li>
<li><a href="#14">1.4. Roles</a></li>
<li><a href="#15">1.5. Assignment</a></li>
<li><a href="#16">1.6. Targets</a></li>
<li><a href="#17">1.7. Token</a></li>
<li><a href="#18">1.8. Catalog</a></li>
</ul>

<h4><a href="#id">2. Identity</a></h4>
<ul>
<li><a href="#21">2.1. SQL</a></li>
<li><a href="#22">2..2. LDAP</a></li>
<li><a href="#23">2.3. Multiple Backends</a></li>
<li><a href="#24">2.4. Identity Providers</a></li>
<li><a href="#25">2.5. Các use cases sử dụng Identity Backends</a></li>
</ul>

<h4><a href="#auth">3. Authentication</a></h4>
<ul>
<li><a href="#passwd">3.1. Password</a></li>
<li><a href="#token">3.2. Token</a></li>
</ul>
<h4><a href="#authoz">4. Access Management and Authorization</a></h4>
<h4><a href="#backend">5. Backends và Services</a></h4>
<h4><a href="#faq">6. FAQs</a></h4>

---

<h3><a name="concepts">1. Các khái niệm trong Keystone</a></h3>
<ul>
<li><b><a name="11">1.1. Project</a></b>
<ul>
<li>Khái niệm chỉ sự gom gộp, cô lập các nguồn tài nguyên (server, images, etc.)</li>
<li>Các project tự mình không có các user, các user và group muốn truy cập tài nguyên trong project phải được gán role để quy định tài nguyên được phép truy cập trong project (khái niệm role assignment)</li>
</ul>
</li>
<li><b><a name="12">1.2. Domain</a></b>
<ul>
<li>Cô lập khung nhìn về tập các project và user (cũng như user group) đối với mỗi tổ chức riêng biệt, tránh việc user có khung nhìn toàn cục gây ra xung đột không mong muốn về user name giữa các tổ chức khác nhau trong cùng một hệ thống cloud.</li>
<li>Domain là tập hợp bao gồm các user, group, project</li>
<li>Phân chia tài nguyên vào các "kho chứa" để sử dụng độc lập với mỗi tổ chức</li>
<li>Mỗi domain có thể coi là sự phân chia về mặt logic giữa các tổ chức, doanh nghiệp trên cloud</li>
</ul>
</li>
<li><b><a name="13">1.3. Users và User Groups (Actor)</a></b>
<ul>
<li>User: thực thể được phép truy cập vào tài nguyên cloud đã đươck cô lập bởi domain và project</li>
<li>Group: tập hợp các user</li>
<li>User và user group được phép "common across domain", nghĩa là trên các domain khác nhau, tên user và user group của các domain này có thể giống nhau. Tuy nhiên mỗi user và user group đều có một định danh duy nhất (UUID)</li>
<li>Role: các role gán cho user và user group trên các domain và project có giới hạn toàn cục (global scoped) chứ không phải giới hạn domain (trong bản Liberty, các phiên bản trong tương lai có thể khác)
<br><br>
<img src="http://i.imgur.com/jKJEFDh.png"/>
</li>
</ul>
</li>
<li><b><a name="14">1.4. Roles</a></b>
<div>
Khái niệm gắn liên với Authorization (ủy quyền), giới hạn các thao tác vận hành hệ thống và nguồn tài nguyên mà user được phép. 
<b>Role được gán cho user và nó được gán cho user đó trên một project cụ thể. ("assigned to" user, "assigned on" project)</b>
</div>
</li>
<li><b><a name="15">1.5. Assignment</a></b>
<div>Khái niệm "role assignment" thể hiện sự kết nối giữa một actor(user và user group) với một actor(domain, project) và một role. Role assignment được cấp phát và thu hồi, và có thể được kế thừa giữa các user và group trên project của domains. (do role có giới hạn toàn cục - global scoped)</div>
</li>
<li><b><a name="16">1.6. Targets</a></b>
<div>Khái niệm chỉ project hoặc domain, nơi mà role được gán cho người dùng trên đó (assigned on).</div>
</li>
<li><b><a name="17">1.7. Token</a></b>
<div>Có thể coi là chìa khóa để truy cập tài nguyên trên cloud. Token được sử dụng để xác thực tài khoản người dùng và ủy quyền cho người dùng khi truy cập tài nguyên (thực hiện các API call). 
<br>
Token bao gồm:
<ul>
<li>ID: định danh duy nhất của token trên cloud</li>
<li>payload: là dữ liệu về người dùng (user được truy cập trên project nào, danh mục các dịch vụ sẵn sàng để truy cập cùng với endpoints truy cập các dịch vụ đó), thời gian khởi tạo, thời gian hết hạn, etc.</li>
</ul>
</div>
</li>
<li><b><a name="18">1.8. Catalog</a></b>
Là danh mục các dịch vụ để người dùng tìm kiếm và truy cập. Catalog chỉ ra các endpoints truy cập dịch vụ, loại dịch vụ mà người dùng truy cập cùng với tên tương ứng, etc. Từ đó người dùng có thể request khởi tạo VM và lưu trữ object.
</li>
</ul>

<h3><a name="id">2. Identity</a></h3>
<ul>
<li><b><a name="21">2.1. SQL</a></b>
<div>
Tùy chọn để lưu trữ các actor (user và group), hỗ trợ các hệ quản trị cơ sở dữ liệu như: MySQL, PostgreSQL, DB2, etc. Việc thiết lập sử dụng SQL nằm trong file cấu hình keystone.conf. 
<br>
Ưu điểm:
<ul>
<li>Dễ dàng cài đặt</li>
<li>Quản lý các user và group thông qua OpenStack APIs</li>
</ul>
Nhược điểm:
<ul>
<li>Keystone không thể thiết lập trở thành Identity Provider hỗ trợ xác thực tập trung khi sử dụng SQL</li>
<li>Hỗ trợ cả mật khẩu yếu (không luân chuyển password để xác thực được, không khôi phục được password)</li>
<li>Hầu hết doanh nghiệp đều có một LDAP server để lưu thông tin nhân viên</li>
<li>Identity silo</li>
</ul>
</div>
</li>
<li><b><a name="22">2..2. LDAP</a></b>
<div>
<ul>
<li>LDAP là tùy chọn khác để thu thập và lưu trữ actor. Keystone truy cập LDAP giống như nhiều ứng dụng khác sử dụng LDAP (System Login, Email, Web Apps, etc.). </li>
<li>Thiết lập cho Keystone kết nối với LDAP trong file keystone.conf. </li>
<li>LDAP thiết lập cho Keystone liệu có quyền "write" dữ liệu vào LDAP hay chỉ có quyền "read"</li>
<li>Trường hợp lý tưởng là LDAP chỉ thực hiện thao tác read, nghĩa là hỗ trợ tìm kiếm user, group và thực hiện xác thực</li>
<li>
Ưu điểm:
<ul>
<li>Không cần duy trì bản sao của các tài khoản người dùng</li>
<li>Keystone không cấu hình LDAP để trở thành identity provider</li>
</ul>
</li>
<li>
Nhược điểm:
<ul>
<li>Các service accounts (nova, glance, swift, etc.) vẫn cần lưu trữ ở đâu đó, bởi LDAP admin không muốn những account này lưu trữ trong LDAP</li>
<li>Keystone vẫn có thể "thấy" được mật khẩu người dùng, bởi mật khẩu nằm trong yêu cầu xác thực. Keystone đơn giản chỉ chuyển tiếp những yêu cầu này đi. Tuy nhiên trường hợp lý tưởng nhất vẫn là Keystone không được "thấy" password nữa.</li>
</ul>
</li>
</ul>
</div>
</li>
<li><b><a name="23">2.3. Multiple Backends</a></b>
<div>
<ul>
<li>Hỗ trợ từ bản Juno với Identity API version 3. </li>
<li>Triển khai các backend riêng  biệt cho mỗi domain Keystone. Trong đó "default" domain sử dụng SQL backend để lưu trữ các service account. (tài khoản tương ứng với các dịch vụ khác trong OpenStack tương tác với Keystone). LDAP backends có thể hosted trên domain riêng biệt của họ. Thông thường LDAP của quản trị hệ thống cloud OpenStack khác với LDAP của từng công ty. Do đó trên mỗi domain của công ty riêng biệt thường triển khai quản lý thông tin nhân viên của họ.
<br><br>
<img src="http://i.imgur.com/DfUFPVIg.png" />
</li>
<li>Ưu điểm:
<ul>
<li>Hỗ trợ đa hệ thống LDAPs cho nhiều tài khoản user, còn SQL lưu trữ service accounts, LDAP lưu thông tin </li>
<li>Tận dụng lợi thế của LDAP</li>
</ul>
</li>
<li>Nhược điểm:
<ul>
<li>Cài đặt sử dụng phức tạp hơn  SQL</li>
<li>Xác thực các tài khoản người dùng trong phạm vị domain</li>
</ul>
</li>
</ul>
</div>
</li>
<li><b><a name="24">2.4. Identity Providers</a></b>
<div>
<ul>
<li>User lưu trong Keystone, được xem như các tài khoản không bền vững (ephemeral)</li>
<li>Các federated user sẽ có các thuộc tính map với role của group</li>
<li>Đứng về góc nhìn của Keystone, các identity provider là tài nguyên lưu trữ danh tính, có thể là hệ thống backend như (LDAP, AD, MongoDB) hoặc các tài khoản mạng xã hội như (Google, Facebook, Twitter). Thông qua hệ thống Identity Manager trên mỗi domain, các thuộc tính của người dùng sẽ được đưa về các định danh federated có định dạng tiêu chuẩn như SAML, OpenID Connect.  </li>
<li>Ưu điểm
<ul>
<li>Tận dụng hạ tầng và phần mềm có sẵn để xác thực người dùng và thu thập thông tin người dùng</li>
<li>Tách biệt Keystone và vấn đề xử lý thông tin định danh</li>
<li>Mở cửa cho mục đích liên kết giữa các hệ thống cloud, hybrid cloud.</li>
<li>Keystone không còn "thấy" được user password nữa</li>
<li>Identity provider hoàn toàn thực hiện việc xác thực </li>
</ul>
</li>
<li>
Nhược điểm: cài đặt các identity source rất phức tạp.
</li>
</ul>
</div>
</li>

<li><b><a name="25">2.5. Các use cases sử dụng Identity Backends</a></b>
<table style="border: 1px solid #EEE">
<tr>
<td>Identity Source</td>
<td>User cases</td>
</tr>

<tr>
<td>SQL</td>
<td>
<ul>
<li>Sử dụng trong môi trường kiểm thử và phát triển với OpenStack</li>
<li>Lượng người dùng nhỏ</li>
<li>Dùng với các tài khoản đặc biệt (service user - nova, glance, etc.)</li>
</ul>
</td>
</tr>

<tr>
<td>LDAP</td>
<td>
<ul>
<li>Sử dụng trong môi trường doanh nghiệp</li>
<li>Sử dụng chỉ LDAP nếu có khả năng tạo service account trong LDAP</li>
</ul>
</td>
</tr>

<tr>
<td>Multiple Backends</td>
<td>
<ul>
<li>Hướng tiếp cận thích hợp với hầu hết doanh nghiệp</li>
<li>Sử dụng trong trường hợp LDAP không cho phép lưu service account</li>
</ul>
</td>
</tr>

<tr>
<td>Identity Provider</td>
<td>
<ul>
<li>Muốn sử dụng mô hình Federated Identity</li>
<li>Sử dụng nếu các Identity provider đã có sẵn</li>
<li>Keystone không được phép truy cập LDAP</li>
<li>Không có LDAP identity </li>
<li>Sử dụng nếu tương tác với LDAP được chuyển tới nền tảng cơ bản và Web server</li>
</ul>
</td>
</tr>
</table>
</li>
</ul>

<h3><a name="auth">3. Authentication</a></h3>
<ul>
<li><b><a name="passwd">3.1. Password</a></b>
<div>
<ul>
<li>Là một trong những cách phổ biến xác thực người dùng và dịch vụ.</li>
<li>Được gửi thông qua POST request tới Keystone. Request sẽ có payload dạng như sau
<br><br>
<img src="http://i.imgur.com/yabcww8.png"/>
</li>
<li>Trong payload của request chứa đủ thông tin để xác định user có tồn tại hay không, xác thực người dùng nếu tồn tại, thu thập danh mục các dịch vụ dựa trên quyền hạn của user trên một phạm vi (project)</li>
<li>Trong "user" section phải xác định thông tin domain của người dùng (domain name hoặc ID), trừ khi cung cấp ID định danh của người dùng. Bởi lẽ trên các domain khác nhau có thể cho phép tên người dùng giống nhau.</li>
<li>"scope" section là tùy chọn nhưng thường sử dụng để giúp người dùng thu thập danh mục các dịch vụ. Section này xác định project nào người dùng được làm việc. Nếu người dùng không được gán role trên project thì request sẽ bị từ chối. Section này cũng mang đủ thông tin để tìm ra nó, bao gồm cả thông tin về domain, bởi tên project cũng có thể trùng nhau giữa các domain khác nhau. Trừ khi cung cấp project ID, khi đó không cần thông tin domain nữa.
<br><br>
<img src="http://i.imgur.com/W3M1cOH.png"/>
<br><br>
Hình trên mô tả request người dùng khi cung cấp username, password, project scope cho Keystone. Keystone sẽ xác thực người dùng và trả lại cho người dùng một token sử dụng để xác thực khi request yêu cầu cấp phát tài nguyên từ các dịch vụ OpenStack khác.
</li>
</ul>
</div>
</li>
<li><b><a name="token">3.2. Token</a></b>
<div>
Tương tự như trên, user có thể xin cấp phát token mới bằng cách cung cấp token đang sử dụng. Keystone sẽ trả lại token mới với cùng phạm vị (domain, project) va roles với token ban đầu.
<br><br>
<img src="http://i.imgur.com/KMd2TU1.png"/>
<br><br>
Việc xin cấp lại token có nhiều mục đích, ngoài việc refresh lại token mới bị hết hạn còn có thể là thay đổi từ một unscoped token sang scoped token.
</div>
</li>
</ul>
<h3><a name="authoz">4. Access Management and Authorization</a></h3>
<div>
<ul>
<li>Keystone quản lý truy cập và ủy quyền cho người dùng được phép sử dụng APIs nào </li>
<li>Keystone tạo ra RBAC (Role-based access control) policy thực thi trên mỗi public API endpoints. Các policy này lưu trữ trên file hoặc đĩa. Thông thường lưu trong file có tên "policy.json". </li>
<li>File policy.json thiết lập target và rules. Một file policy có cấu trúc điển hình như sau:
<br><br>
<img src="http://i.imgur.com/gtJeOEo.png"/>
<br><br>
<ul>
<li>Phần đầu file policy thiết lập các target với role cụ thể</li>
<li>Rule: cấu trúc "identity:protected controller" dùng để quản lý các APIs.</li>
<li>Full 1:1 mapping giữa rule và các APIs thể hiện như sau:
<table>
<tr>
<td>Policy Target</td>
<td>API</td>
</tr>

<tr>
<td>identity:list_projects</td>
<td>GET /v3/projects</td>
</tr>

<tr>
<td>identity:create_project</td>
<td>POST /v3/projects</td>
</tr>

<tr>
<td>identity:delete_project</td>
<td>DELETE /v3/projects/{project_id}</td>
</tr>

<tr>
<td>identity:list_user_projects</td>
<td>GET /v3/users/{user_id}/projects</td>
</tr>
</table>
</li>
</ul>
</li>
</ul>
</div>

<h3><a name="backend">5. Backends và Services</a></h3>
<div>
Các dịch vụ Keystone cung cấp và hệ thống backend hỗ trợ triển khai các dịch vụ đó thể hiện trong hình sau.
<br><br>
<img src="http://i.imgur.com/d7UDtcq.png"/>
<br><br>
</div>

<h3><a name="faq">6. FAQs</a></h3>
<div>
Một số chú ý và câu hỏi thường gặp với keystone
<ul>
<li>Domain vs Region: 
<ul>
<li>Domain tách biệt về mặt tài nguyên giữa các chủ sở hữu của các project và identity source (LDAP, SQL)</li>
<li>Region đại diện bởi vị trí địa lý như: US-West, USS-East</li>
</ul>
</li>
<li>Mỗi người dùng chỉ nằm trong một domain, tên user có thể trùng nhau giữa các project khác nhau. Tuy nhiên mỗi user có một định danh UUID duy nhất</li>
<li>Khái niệm scope nhắc tới domain và project. 
<ul>
<li>Unscoped token: là token trả về khi đã xác thực danh tính user nhưng chưa chỉ định rõ project và domain. Token loại này dùng để truy vấn xác định xem project nào mà người dùng được phép truy cập.</li>
<li>Scoped token: xác thực với 1 project và domain cụ thể. Token này mang theo cả thông tin về role dùng để xác định các thao tác vận hành hệ thống được phép thực hiện.</li>
</ul>
</li>
</ul>
</div>