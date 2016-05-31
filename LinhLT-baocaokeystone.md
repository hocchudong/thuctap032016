#Keystone
* Mô hình triển khai nền tảng dịch vụ Cloud cung cấp cho người dùng quyền được truy cập các vào tài nguyên như máy ảo, bộ nhớ, mạng,...
* Tính năng quan trọng của bất kỳ cloud nào là làm cách nào để cung cấp điều khiển truy cập vào các tài nguyên. 
* Trong OpenStack, project keystone chịu trách nhiệm cung cấp điều khiển truy cập vào toàn bộ tài nguyên cloud. 
* Keystone chứng mình nó là một thành phần quan trọng trong cloud.

# Mục lục



<a name="chuc_nang"></a>
#1. Các chức năng cơ bản của Keystone
<a name="identity"></a>
##1.1 Identity:
* Identity xác định ai là người truy cập vào tài nguyên
cloud.
* Trong openstack, idenity thường được dùng
để định danh user.
* idenity có thể lưu user vào Keystone database.
* Trong môi trường thương mại,  Identity thường sử dụng bên thứ ba. 
* Keystone có thể lấy lại thông tin định danh người dùng từ idenity bên thứ ba.

<a name="authentication"></a>
##1.2 Authentication:
* Authentication xử lý việc xác nhận định danh người dùng.
* Trong nhiều trường hợp, authentication là thực hiện xác nhận thông tin đăng nhập user và mật khẩu.
* Lúc Ban đầu, Keystone có khả năng thực hiện tất cả authentication. Điều đó là không được khuyến khích với môi trường doanh nghiệp.
* Trong môi trường doanh nghiệp, password cần được bảo vệ và quản lý.
* Keystone dễ dàng tích hợp với các nền tảng authentication đã tồn tại khác là LDAP, Active Directory.
* Khi người dùng định danh bằng mật khẩu, authentication sẽ tạo ra token cho bước authentication tiếp theo.
* Token sẽ làm giảm tầm nhìn, phơi bày password mà nó cần được giấu đi và bảo vệ càng tốt.
* Token có giới hạn thời gian sống và hết hạn nếu chúng bị đánh cắp.
* OpenStack chủ yếu dựa vào token để authentication và các mục đích khác.
* Keystone là một dịch vụ của OpenStack có thể giải quyết vấn đề trên.
* Hiện tại, Keystone được sử dụng `bearer token`. Có nghĩa là bất cứ ai thu được quyền sở hữu token, dù đúng hay sai đều có khả năng sử dụng token để xác thực và truy cập vào tài nguyên. Kết quả là, việc sử dụng Keystone rất quan trọng trong việc bảo vệ token và các thành phần khác.

<a name="authorization"></a>
##1.3 Authorization
* Một user đã được định danh và token đã được tạo và phân bổ, mọi thứ bắt đầu trở nên thú vị. Bởi vì chúng ta có đủ nền tảng và địa điểm để bắt đầu thực hiện authorization.
* Authorization xử lý xác định những tài nguyên nào user được phép truy cập.
* Trong OpenStack cung cấp cho người dùng quyền truy cập vào tài nguyên rất lớn. Ví dụ, có cần cơ chế mà người dùng được phép tạo 1 máy ảo cụ thể, attach hay delete volume of block storage, được phép tạo mạng ảo,...
* Trong openstack, keystone bản đồ user đến Projects hoặc domain bằng cách liên kết role cho user đối với Projects hay domain đó.
* Một số dịch vụ OpenStack khác như Nova, Cinder, Neutron xem xét project của user và role và đánh giá thông tin sử dụng policy.
* Công cụ chính sách xem xét thông tin (đặc biệt là giá trị role) và quyết định hành động của user được phép thực hiện.


**Keystone chủ yếu tập trung vào idenity, authentication và authorization.**
<a name="loi_ich"></a>
##1.4 Các lợi ích như:
* Xác thực đơn và cấp quyền cho các dịch vụ khác của OpenStack.
* Keystone xử lý các hệ thống xác thực ngoài và cung cấp theo chuẩn cấp quyền cho tất cả các dịch vụ khác của OpenStack: nova, glance, cinder, neutron,... và keystone cô lập tất cả các dịch này.
* Keystone cung cấp project, là những dịch vụ có thể sử dụng tài nguyên riêng.
* Keystone cung cấp domain, được sử dụng để định nghĩa tách rời không gian cho user, groups và project để cho phép tách rời khỏi khách hàng.

* Roles được sử dụng để authorization giữa Keystone vào policy files của mỗi dịch vụ openstack. Phân công user và groups vào project nào, domain nào.
* Lưu trữ catalog cho dịch vụ OpenStack, endpoints, region, cho phép clients khám phá các dịch vụ hoặc endpoints mà họ cần.

<a name="khai_niem"></a>
#2 Các khái nhiệm cơ bản.
<a name="projects"></a>
##2.1 Projects
* Trong keystone, projects là khái niệm trừu tượng, sử dụng bởi các dịch vụ khác trong OpenStack.
* Projects có chứa các tài nguyên.
* Tiền thân của Projects là tenants, thay đổi để trực quan hơn.
* Projects không phải là chủ user nhưng user và group có quyền truy cập vào các project, sử dụng các role.
* Các role trên user và group chỉ ra rằng họ có quyền gì để truy cập vào các tài nguyên trong Projects.

![](http://916c06e9a68d997cd06a-98898f70c8e282fcc0c2dba672540f53.r39.cf1.rackcdn.com/Screen%20Shot%202014-01-08%20at%201.58.09%20PM.png)

* Ví dụ hình trên: 
    * Mỗi user có thể thuộc nhiều projects khác nhau, và có quyền hạn khác nhau.
    * Ví dụ: Users SandraD, có quyền admin ở trong projects Aerospace nhưng trong projects CompSci chỉ có quyền support.


<a name="domain"></a>
##2.2 Domain
* Là khái niệm vừa ra đời ở api v3.
* Không có cơ chế để hạn chế tầm nhìn của project trên các tổ chức khau nhau -> dẫn đến va chạm giữa tên project của các tổ chức khác nhau. username cũng có thể va chạm giữa 2 tổ chức.
* Keystone ra khái nhiệm trừu tượng mới: domain.
* Dùng để cô lập tầm nhìn, tập hợp các project, user cho 1 tổ chức cụ thể.
* 1 domain có thể bao gồm user, group, project....
* Domain cho phép bạn phân chia các nguồn tài nguyên trong cloud vào các tổ chức cụ thể.

![](http://916c06e9a68d997cd06a-98898f70c8e282fcc0c2dba672540f53.r39.cf1.rackcdn.com/Screen%20Shot%202014-01-08%20at%201.04.26%20PM.png)


<a name="users_groups"></a>
##2.3 Users và Groups
* Groups là một nhóm người dùng.
* Có thể được gán trên domain của group hoặc trên project của group đấy.

![](http://916c06e9a68d997cd06a-98898f70c8e282fcc0c2dba672540f53.r39.cf1.rackcdn.com/ss.png)

* Ví dụ:
	* JohnB có vai trò là Sysadmin ở trong group 1, thuộc 2 Projects Biology và Aerospace.
	* LisaD có vai trò là Engineer trong group 2 thuộc Projects Compsci

<a name="roles"></a>
##2.4 Roles
* Chỉ ra vai trò của người dùng trong project hoặc trong domain,...

* Mỗi user có thể có vai trò khác nhau đối với từng project.

![](https://open.ibmcloud.com/documentation/_images/UserManagementWithGroups.gif)

<a name="assignment"></a>
##2.5 Assignment
* Thể hiện sự kết nối giữa một actor(user và user group) với một actor(domain, project) và một role.
* Role assignment được cấp phát và thu hồi, và có thể được kế thừa giữa các user và group trên project của domains. 

<a name="targets"></a>
##2.6 Targets
* Nơi mà role được gán cho user (Project hoặc domain).

<a name="token"></a>
##2.7 Token
* Người dùng muốn sử dụng OpenStack API thì cần phải chứng minh mình là ai, và mình nên đưuọc cho phép trong câu hỏi API.
* Cách mà họ lưu trữ là gửi token đến API call và Keystone phản ứng để sinh ra token.
* Người dùng nhận token và xác thực thành công lần nữa ở Keystone.
* Token mang nó để cấp quyền.
* Token chứa cả ID và payload. ID bảo đảm là duy nhất trên mỗi cloud và payload chứa dữ liệu user. payload có thể chứa những dữ liệu dưới: create, expire, authenticated, project, catalog,....

<a name="catalog"></a>
##2.8 Catalog:
* Nó chứa URLs và endpoints của các dịch vụ trong cloud.
* Với catalog, người dùng và ứng dụng có thể biết ở đâu để gửi yêu cầu tạo máy ảo hoặc storage objects.
* Dịch vụ catalog chia thành danh sách các endpoint, mỗi endpoint chi thành các admin URL, internal URL, public URL.
Ví dụ:

<a name="thanh_phan"></a>
#3. Các thành phân cơ bản trong Keystone
<a name="thanh_phan_identity"></a>
##3.1 Identity
<a name="sql"></a>
###3.1.1 SQL
* Keystone hỗ trợ SQL để lưu trữ thông tin users và groups
* Hỗ trợ các database là: MySQL, PostgreSQL và DB2.
* Keystone sẽ lưu thông tin name, password và chi tiết.
* Cài đặt database phải cấu hình trong file cấu hình keystone.
* Chủ yếu, Keystone là Identity Provider, không phải là tốt nhất cho mọi người và cũng ko phải là tốt nhất cho khách hàng doanh nghiệp. 
* Ưu điểm
	* dễ dàng cài đặt.
	* Quản lý users và groups quả OpenStack APIs.

* nhược điểm:
	* Keystone không nên là Identity Provider.
	* Mật khẩu yếu ( không khôi phục mk, không xoay mật khẩu).
	* Các doang nghiệp thường sử dụng LDAP.
	* Phải ghi nhớ username và password.

<a name="ldap"></a>
###3.1.2 LDAP
* Keystone sẽ truy cập vào LDAP giống như các ứng dụng
khác sử dụng LDAP.
* Cấu hình trong file config của keystone để
sử dụng LDAP.
* LDAP thường được dùng để chỉ đọc, có nghĩa là tìm user và groups (qua search) và authentication (qua bind).
* Nếu sử dụng LDAP chỉ để đọc, keystone sẽ cần tối thiểu các quyền để sử dụng LDAP. Với trường hợp, cần quyền đọc các thuộc tính user và group.
* Thu hồi quyền tài khoản, không yêu cầu quyền truy cập vào mật khẩu. 
* Ưu điểm:
	* không duy trì bản sao của tài khoản người dùng.
	* Keystone không hành động như một nhà cung cấp nhận dạng (identity provider).
* Nhược điểm:
	* dịch vụ tài khoản sẽ lưu ở đâu đó và LDAP không muốn có tài khoản trong LDAP.
	* Keystone có thể thấy mật khẩu người dùng, lúc mật khẩu được yêu cầu authentication.
	* Keystone đơn giản thì chuyển các yêu cầu, nhưng tốt nhất là Keystone không nhìn thấy mật khẩu.

<a name="multiple_backend"></a>
###3.1.3 Multiple Backends
* Từ phiên bản Juno, Keystone hỗ trợ nhiều idenity backend từ phiên bản v3. 

[hình ảnh]
* Identity service có thể có nhiều backend cho mỗi domain.
* Ví dụ: LDAPs for Domain A and B. SQL-based backend for service accounts and Assignment.

* Ưu điểm:
	* Hỗ trợ nhiều backend đồng thời.
	* Sử dụng lại LDAP đã có.
 
* Nhược điểm
	* phức tạp trong cài đặt.
	* Xác thực tài khoản người dùng phải trong miền scoped

<a name="identity_provider"></a>
###3.1.4 idenity provider
* Sử dụng các giải pháp thứ ba để có thể xác thực.

<a name="use_case_identity_backend"></a>
###3.1.5 use cases for idenity backend
| identity source |    uses case|
|:------:|:------:|
|SQL| sử dụng cho testing hoặc developing. user nhỏ. openstack-specific accounts.|
|LDAP| sử dụng nếu đã có trước. chỉ sử dụng mỗi LDAP nếu bạn có khả năng tạo dịch vụ tài khoản cần thiết trong LDAP.|
|Multiple backend| trong môi trường doanh nghiệp. sử dụng nếu dịch vụ người dùng không được phép trong LDAP.|
|idenity provider| bạn có thể tận dụng lợi thế của cơ chế Federated. sử dụng nếu indentity provider đã tồn tại. Keystone không thể truy cập vào LDAP. Non-LDAP idenity source. sử dụng nếu LDAP tương tác đến underlying platform và web server.|

<a name="thanh_phan_authentication"></a>
##3.2. Authentication
<a name="auth_password"></a>
###3.2.1 Authentication password
* payload của request phải có đủ thông tin để tìm user nằm ở đâu
* xác nhận user và lấy dịch vụ catalog của user.
* định dang user xác định đến ID, 

![](http://i.imgur.com/fXzFnnH.png)


<a name="auth_token"></a>
###3.2.2 Authentication token
* user có thể yêu cầu 1 token mới đựa trên token hiện tại.
* tải của yêu cầu POST giảm đáng kê so với password.
* có nhiều lý do để token được sử dụng, như khi refreshing thì token sẽ hết hạn và đổi từ unscoped sang scoped token.

![](http://i.imgur.com/ZAK7w99.png)

<a name="Access_Management_and_Authorization"></a>
##3.3. Access Management and Authorization
* Keystone tạo ra policy Role-Based Access Controll (RBAC) được thực thi trên mỗi API public endpoint. Những chính sách này được lưu thành 1 file trên đĩa, có tên là policy.json

<a name="backend_services"></a>
##3.4 Backends and Services
xanh: thường SQL
tím: LDAP hoặc SQL.
Xanh da trời: SQL hoặc Memcache.
policy: lưu ở file.

<a name="token"></a>
#4. Token format

<a name="uuid"></a>
##4.1 UUID (universally unique identifier):
* Là tiêu chuẩn định dạnh được sử dụng trong xây dựng phần mềm. Mục đích của UUIDs là cho phép các hệ thống phân phối để nhận diện thông tin mà không cần điều phối trung tâm. 
* A UUID is a 16-octet (128-bit) number.
* UUID được đại diện bởi 32 chữ số thập lục phân,hiển thị trong năm nhóm, phân cách bằng dấu gạch nối, với dạng `8-4-4-4-12`. Có tổng cộng 36 ký tự, trong đó 32 ký tự chữ với 4 dấu gạch ngang.
* UUID có tổng cộng 5 phiên bản, trong đó keystone sử dụng UUIDv4.
* Các bạn có thể xem chi tiết tại:
	* https://en.wikipedia.org/wiki/Universally_unique_identifier#Definition
	* https://tools.ietf.org/html/rfc4122.html
	* https://docs.python.org/3/library/uuid.html

<a name="uuid_phien_ban"></a>
###4.1.1 Các phiên bản UUID
<a name="uuid_v4"></a>
####4.1.1.1: UUID v4
* Keystone sử dụng UUID phiên bản v4:
* Token được tạo ra bằng các con số ngẫu nhiên. 
* Phiên bản UUIDv4 có dạng
```sh
xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
```
* Ví dụ:
```sh
f10700e7-1ff0-45cb-b850-072a0bd6a4e6
```
* Trong đó:
	* x là số bất kỳ trong hệ 16.
	* 4 chỉ phiên bản uuid.
	* y là một trong các ký tự 8,9,A,B.

<a name="uuid_keystone"></a>
###4.1.2 Đặc điểm UUID trong keystone
* Có độ dài 32 byte, nhỏ, dễ sử dụng, không nén.
* Không mang theo đủ thông tin, do đó luôn phải gửi lại keystone để xác thực hoạt động ủy quyền => thắt nút cổ chai.
* Được lưu vào database.
* Sử dụng thời gian dài làm giảm hiệu suất hoạt động, CPU tăng và thời gian đáp ứng lâu.
* Sử dụng câu lệnh `keystone-manager token flush` để làm tăng hiệu suất hoạt động.
* Ví dụ 1 đoạn token
```sh
468da447bd1c4821bbc5def0498fd441
```

<a name="uuid_gen"></a>
###4.1.3 UUID Token Generation Workflow
![](http://i.imgur.com/UwkVx61.png)
* 1: Xác nhận user, lấy UserID.
* 2: Xác nhận project, lấy project id và domain id.
* 3: Lấy roles cho user trên project hoặc domain đó. Trả lại kết quả `Failure` nếu user không có roles đó.
* 4: Lấy các services và endpoitns
* 5: Gộp các thông tin Identity, Resource, Assignment, Catalog vào token payload. Tạo token id bằng hàm `uuid.uuid4().hex`.
* Lưu giữ các thông tin Token ID, Expiration, Valid, User ID, Extra vào backend.

<a name="uuid_vali"></a>
###4.1.4 UUID Token Validation Workflow
![](http://image.prntscr.com/image/b729f99bc1884eba827e6f2581444a5a.png)

* 1: Xác nhận token bằng cách gửi một phương thức GET đến Token KVS.
* 2: Token KVS sẽ kiểm tra trong backend. Kết quả trả về nếu không là Token not found, nếu có, chuyển sang bước 3.
* 3: Phân tích token và lấy các metadata: UserID, Project ID, Audit ID, Token Expiry.
* 4: Kiểm tra thời gian hiện tại với thời gian hết hạn của token. Nếu token hết hạn, trả về Token not found. Nếu còn hạn, chuyển sang bước 5
* 5: Kiểm tra token có bị thu hồi không, nếu no, trả về cho người dùng thông điệp HTTP/1.1 200OK (token sử dụng được).

<a name="uuid_revo"></a>
###4.1.5 UUID Token Revocation Workflow
![](http://image.prntscr.com/image/76fc28c8e9fb42b4893acb75d462bd39.png)


* 1: Gửi một yêu cầu DELETE token. Trước khi revoke token thì phải xác nhận lại token (Token validation workflow)
* 2: Kiểm tra Audit ID. Nếu không có audit ID, chuyển sang bước 3. Nếu có audit ID, chuyển sang bước 6.
* 3: Token được thu hồi khi hết hạn, chuyển sang bước 4.
* 4: Tạo một event revoke với các thông tin: User ID, Project ID, Revoke At, Issued Before, Token expiry.
.
* 5: Chuyển sang bước 9.
* 6: Token được thu hồi bởi audit id.
* 7: Tạo event revoke với các thông tin: audit id và thời điểm revoke trước khi hết hạn.
* 8: Lọc các event revoke đang tồn tại dựa trên Revoke At.
* 9: Set giá trị false vào token avs của token.

<a name="uuid_uunhuocidem"></a>
###4.1.6 Ưu nhược điểm
* Ưu điểm:
	* Định dạng token đơn giản và nhỏ.
	* Đề nghị được sử dụng trong các môi trường OpenStack đơn giản.

* Nhược điểm
	* Định dạng token cố định.
	* Xác nhận token chỉ được hoàn thành bởi dịch vụ Identity.
	* Không khả thi cho môi trường OpenStack multiple.

<a name="pki_pkiz"></a>
##4.2 PKI - PKIZ:
* Mã hóa bằng Private Key, kết hợp Public key để giải mã, lấy thông tin.
* Token chứa nhiều thông tin như Userid, project id, domain, role, service catalog, create time, exp time,...
* Xác thực ngay tại user, không cần phải gửi yêu cầu xác thực đến Keystone.
* Có bộ nhớ cache, sử dụng cho đến khi hết hạn hoặc bị thu hồi => truy vấn đến keystone ít hơn.
* Kích thước lớn, chuyển token qua HTTP, sử dụng base64.
* Kích thước lớn chủ yếu do chứa thông tin service catalog.
* Tuy nhiên, Header của HTTP chỉ giới hạn 8kb. Web server không thể xử lý nếu không cấu hình lại, khó khăn hơn UUID
* Để khắc phục lỗi trên thì phải tăng kích thước header HTTP của web server, tuy nhiên đây không phải là giải pháp cuối cùng hoặc swift có thể thiết lập không cần catalog service.
* Lưu token vào database.
* Ví dụ 1 đoạn token
```sh
MIIDsAYCCAokGCSqGSIb3DQEHAaCCAnoEggJ2ew0KICAgICJhY2QogICAgICAgI...EBMFwwVzELMAkGA
1UEBhMCVVMxDjAMBgNVBAgTBVVuc2V0MCoIIDoTCCA50CAQExCTAHBgUrDgMQ4wDAYDVQQHEwVVbnNldD
EOMAwGA1UEChM7r0iosFscpnfCuc8jGMobyfApz/dZqJnsk4lt1ahlNTpXQeVFxNK/ydKL+tzEjg
```
##PKIZ
* Tương tự PKI.
* Khắc phục nhược điểm của PKI, token sẽ được nén lại để có thể truyền qua HTTP.
* Tuy nhiên, token dạng này vẫn có kích thước lớn.

<a name="pki/pkiz cer"></a>
###4.2.1 PKI/PKIZ Certificates
* Signing Key (signing_key.pem): Generate private key in PEM format
* Signing Certificate (signing_cert.pem):
	* Generate CSR using Signing Key
	* Submit CSR to CA
	* Receive Certificate from CA
* Certificate Authority Certificate (ca.pem)

* Đường dẫn
    * certfile = /etc/keystone/ssl/certs/signing_cert.pem
    * keyfile = /etc/keystone/ssl/private/signing_key.pem
    * ca_certs = /etc/keystone/ssl/certs/ca.pem



<a name="pki_gen"></a>
###4.2.1 Token PKI/PKIZ Generation Workflow

![](http://image.prntscr.com/image/811ddc50e8eb411da7c83ac7eb161ea6.png)

* 1: User request token với các thông tin là: username, password, project name.
* 2: Keystone sẽ xác nhận định danh, resource và assignmetn.
* 3: Tạo một JSON, chứa token payload.
* 4: Sign JSON này với các Signing Key và Signing Certificate. Sau đó, với dạng PKI chuyển sang bước 5. Nếu là dạng PKIZ chuyển sang bước 11.
* 5: Convert JSON trên sang dạng UTF-8.
* 6: Convert CMS Signed Token in PEM format to custom URL Safe format:

```sh
“/” replaced with “-”
Deleted: “\n”, “----BEGIN CMS----”,“----END CMS-
```
* 7: Sử dụng zlib để nén JSON.
* 8: Mã hóa Base64 URL Safe.
* 9: Convert JSON sang dạng UTF-8
* 10: PKIZAppend Prefix
* 11: Lưu trữ token vào SQL/KVS




<a name="pki_vali"></a>
###4.3.2 Token PKI/PKIZ Validation Workflow
![](http://image.prntscr.com/image/235e55be478d458e9942a9a3eef2171f.png)

Cũng tương tự UUID, chỉ khác ở chỗ là:
* Trước khi gửi yêu cầu GET đến Token KVS thì pki token sẽ được hash với thuật toán đã cấu hình trước.

<a name="pki_revo"></a>
###4.3.3 Token PKI/PKIZ Revocation Workflow
**Tương tự UUID**

![](http://image.prntscr.com/image/7d3d7eed29614b238ed46be52c7b5f57.png)

<a name="pki_mulit"></a>
###4.3.4 PKI/PKIZ - Multiple Data Centers
**LDAP Replication (Directory Tree is always in sync) - MySQL Replication (Database is always in sync)**

1[](http://image.prntscr.com/image/d7b91d36751d4494a5288ec7d83c525b.png)

<a name="pki_uunhuocidem"></a>
###4.3.5 PKI/PKIZ - Ưu nhược điểm.
* Ưu điểm: 
	* Token có thể được xác nhận mà không cần gửi request đến keystone.

* Nhược điểm
	* Kích thước lớn hơn HTTP Header
	* Cấu hình phức tạp.
	* base64 –d <pki_token
	* Không tốt cho việc triển khai multiple OpenStack


<a name="fernet"></a>
##4.4 Fernet: 
* Sử dụng mã hóa đối xưng (Sử dụng chung key để mã hóa và giải mã).
* Có kích thước khoảng 255 byte, không nén, lớn hơn UUID và nhỏ hơn PKI.
* Chứa các thông tin cần thiết như userid, projectid, domainid, methods, expiresat,....Không chứa serivce catalog.
* Không lưu token vào database.			
* Cần phải gửi lại keystone để xác nhận, tương tự UUID.
* Cần phải phân phối khóa cho các khu vực khác nhau trong OpenStack.
* Sử dụng cơ chế xoay khóa để tăng tính bảo mật.
* Nhanh hơn 85% so với UUID và 89% so với PKI.
* Ví dụ 1 đoạn token
```sh
gAAAAABU7roWGiCuOvgFcckec-0ytpGnMZDBLG9hA7Hr9qfvdZDHjsak39YN98HXxoYLIqVm19Egku5YR
3wyI7heVrOmPNEtmr-fIM1rtahudEdEAPM4HCiMrBmiA1Lw6SU8jc2rPLC7FK7nBCia_BGhG17NVHuQu0
S7waA306jyKNhHwUnpsBQ%3D
```


<a name="key_format"></a>
###4.4.1 Key format
```sh
Signing-key ‖ Encryption-key
```
* Signing-key, 128 bits
* Encryption-key, 128 bits

<a name="loai_key"></a>
###4.4.2 Các loại key
* Primary key: Sử dụng cho mã hóa và giải mã token fernet. (Chỉ số khóa cao nhất)
* Secondary key: Giải mã token. (chỉ số khóa nằm giữa primary key và secondary key)
* Staged key: Tương tự Sencondary key. Khác ở chỗ là Stage key sẽ trở thành primary key ở lần xoay khóa tiếp theo. (Chỉ số khóa thấp nhất).

<a name="gen_key"></a>
###4.4.3 Generate key
Dưới đây là đoạn mã đến sinh ra key

```sh
>>> import base64
>>> import os
>>>
>>> b_key = os.urandom(32) # the fernet key in binary
>>> b_key
'2g\x06\xb3O\xe2D\x7f\x86\xc9\xb0\xb8\xd4\x071v\xd8/\x80\x88\xb8\x92M\xd3\xf7\x86\xc0\xaa\x82\xfb\x97\xe9'
>>>
>>> b_key[:16] # signing key is the first 16 bytes of the fernet key
'2g\x06\xb3O\xe2D\x7f\x86\xc9\xb0\xb8\xd4\x071v'
>>>
>>> b_key[16:] # encrypting key is the last 16 bytes of the fernet key
'\xd8/\x80\x88\xb8\x92M\xd3\xf7\x86\xc0\xaa\x82\xfb\x97\xe9'
>>>
>>> key = base64.urlsafe_b64encode(b_key) # base64 encoded fernet key
>>> key
'MmcGs0_iRH-GybC41AcxdtgvgIi4kk3T94bAqoL7l-k='
```

<a name="rotation_key"></a>
###4.4.4 Rotation Key

![](http://www.mattfischer.com/blog/wp-content/uploads/2015/05/fernet-rotation1.png)

* Hiện tại:
	* Primary key là 2.
	* Secondary key là 1.
	* Staged key là 0.
* Quá trình xoay khóa.
	* Khóa Primary key 2 trở thành khóa Secondary key.
	* Khóa Staged key 0 trở thành khóa Primary key.
	* Khóa Secondary key 1 có thể giữ nguyên hoặc bị xóa đi. Vậy khi nào xóa đi, đó là khi mình cấu hình có tối đa bao nhiêu key trong file `/etc/keystone/`. Nếu cấu hình là 3 key thì Secondary key 1 sẽ bị xóa đi.

<a name="token_format"></a>
###4.4.4 Token format
```sh
Version ‖ Timestamp ‖ IV ‖ Ciphertext ‖ HMAC
```
* Version: 8bits, chỉ phiên bản token được sử dụng. Hiện tại thì chỉ có 1 phiên bản token. Bắt đầu bằng `0x80`.
* timestamp: kiểu nguyên, 64 bits. Là khoảng thời gian từ ngày 1/1/1970 đến ngày mà token được sinh ra.
* IV (Initialization Vector): 128bits. Với mỗi token sẽ có một giá trị IV.
* Ciphertext: Có kích thước khác nhau, nhưng là bội số 128bits. Chứa các thông điệp nhập vào.
* HMAC: có độ dài 256bits, chứa các trường sau
```sh
Version ‖ Timestamp ‖ IV ‖ Ciphertext
```
Cuối cùng Fernet Token sử dụng Base64 URL safe để encoded các thành phần trên.

<a name="gen_token"></a>
###4.4.5 Generating token

Given a key and message, generate a fernet token with the following steps, in order:

* Ghi lại thời gian hiện tại ở trường timestamp.
* Chọn một giá trị IV.
* Xây dựng ciphertext:
	* Pad các tin nhắn là bội số của 128bit (16byte).
	* mã hóa các thông điệp sử dụng AES128-CBC, với tùy chọn IV ở trên và sử dụng encryption-key (trong keyformat).
* Tính HMAC bằng cách sử dụng Signing-key
* Ghép tất cả các trường trên lại với nhau.
* Token được tạo ra bằng cách mã hóa base64url các trường trên


<a name="ver_token"></a>
###4.4.6 Verifying token
* Giải mã base64url token.
* Đảm bảo các bye đầu tiên của mã thông bảo là 0x80 (phiên bản token).
* Nếu người dùng quy định time-to-live cho token thì phải đảm bảo timestamp không phải trong quá khứ.

* Recompute HMAC từ các trường, sử dụng signing-key
* Đảm bảo HMAC được recompute lại phù hợp với trường HMAC lưu trong token
* Giải mã ciphertext sử dụng thuật toán AES/128-CBC với chế độ IV và sử dụng Encryption key.
* Thông điệp ban đầu được giải mã

<a name="fernet_gen"></a>
###4.4.7 Fernet Token Generation Workflow
![](http://i.imgur.com/kd2oZWD.png)

* 1: Các thông tin bao gồm: Version, User ID, Methods, Project ID, Expiry time, Audit ID kết hợp với Padding
* 2: Các thông tin trê được mã hóa bằng Encrypting key, chính là Cipher Text.
* 3: Cipher Text kết hợp với các trường là Fernet Token version, Current timestamp, iv được signed bằng Signing key.
* 4: Thông tin được Signing trên chính là HMAC.

<a name="fernet_vali"></a>
###4.4.8 Fernet Token Validation Workflow
![](http://image.prntscr.com/image/8a39a8307fe246a9aac3b511734e4c77.png)

* 1: Restore Padding: Re-inflate token with “=” and return token with correct padding 
* 2: Giải mã fernet key để nhận token payload.
* 3: Xác định phiên bản token payload.
	* Unscoped Payload : 0
	* Domain Scoped Payload : 1
	* Project Scoped Payload : 2
* 4: Xác định các trường thông tin: 
	* User ID
	* Project ID
	* Methods
	* Token Expiry
	* Audit ID
* 5: So sánh thời gian hiện tại với thời gian hết hạn của token.
* 6: Kiểm tra token có bị thu hồi hay không.
* 7: Trả về token

<a name="fernet_revo"></a>
###4.4.9 Fernet Token Revocation Workflow
**Tương tự UUID/PKI/PKIZ**

![](http://image.prntscr.com/image/4df950ddc94a48348c84049ce6ab05fa.png)

<a name="fernet_multi"></a>
###4.4.10 Fernet - Multiple Data Centers
**LDAP Replication (Directory Tree is always in sync) - MySQL Replication (Database is always in sync)**

![](http://image.prntscr.com/image/705e9f84a9014a309c6e45faf0ed61fd.png)

<a name="fernet_uunhuocdiem"></a>
###4.4.11 Fernet - Ưu nhược điểm
* Ưu điểm:
	* No persistence
	* Reasonable Token Size
	* Multiple Data Center

* Nhược điểm:
	* Token validation impacted by the number of revocation events

<a name="so_sanh_token"></a>
##4.5 Bảng so sánh các loại token

|Token Types | UUID | PKI | PKIZ | Fernet|
|:----------:|:----:|:---:|:----:|:-----:|
|Size	|32 Byte	|KB Level	|KB Level	|About 255 Byte|
|Support |local authentication	|not support	|stand by	|stand by|	not support|
|Keystone load|Big	|small	|small|	Big|
|Stored in the database	|Yes|	Yes|	Yes	|no|
|Carry information	|no	|user, catalog, etc.|	user, catalog, etc.|	user, etc.|
|Involving encryption	|no	|Asymmetric encryption|	Asymmetric encryption|	Symmetric encryption (AES)|
|Compress	|no	|no	|Yes|	no|
|Supported	|D	|G	|J	|K|



#5. LDAP


#6. Federated Identity



<a name="hoat_dong_keystone"></a>
#7. Cách hoạt động của Keystone

![](http://i.imgur.com/uDzPLna.png)

* 1: User gửi thông tin đến Keystone (Username và Password)
* 2: Keystone kiểm tra thông tin. Nếu đúng, nó sẽ gửi về user 1 token.
* 3: User gửi token và yêu cầu đến Nova.
* 4: Nova gửi token đến Keystone để kiểm tra token này có đúng không? có những quyền hạn gì. Keystone sẽ trả lời lại cho Nova.
* 5: Nếu token có quyền, Nova gửi token và yêu cầu image đến Glance.
* 6: Glance gửi token về Keystone để xác thực và kiểm tra xem user này có quyền với file image này không. Keystone sẽ trả lời đến Glance.
* 7: Nova gửi token, và yêu cầu về mạng đến Neutron.
* 8: Neutron gửi token đến Keystone. Keystone sẽ trả lời cho Neutron là user này có được phép hay không.
* 9: Neutron trả lời cho Nova..
* 10: Nova trả lời cho người dùng.

<a name="tham_khao"></a>
#8. Tài liệu tham khảo
* *Steve Martinelli, Henry Nash & Brad Topol*: Identity, Authentication & Access Management in OpenStack
* http://www.slideshare.net/openstackindia/openstack-keystone-identity-service
* https://github.com/fernet/spec/blob/master/Spec.md
* https://developer.ibm.com/opentech/2015/11/11/deep-dive-keystone-fernet-tokens/
* http://www.openstack.cn/?p=5120



