#KeyStone
##Mục lục:

[1 Giới thiệu](#1)

- [1.1 Các dịch vụ cung cấp](#1.1)

- [1.2 Backend](#1.2)

[2 Các chủ đề cơ bản của KeyStone](#2)

- [2.1 Các khái niệm](#2.1)

- [2.2. Use Cases for Identity Backends](#2.2)

- [2.3 Authentication](#2.3)

- [2.4 Managing access and authorizing](#2.4)

- [2.5 Mô hình Backends and Services](#2.5)

[3 Các dạng token](#3)

- [3.1 UUID Tokens](#3.1)

- [3.2 PKI/PKIz](#3.2)

- [3.3 Fernet](#3.3)

[4 Federated Identity](#4)

- [4.1 Authentication Flow](#4.1)

- [4.2 Single Sign-On](#4.2)

[5 Các cải tiến mới trên Mitaka](#5)


=================

<a name="1"></a>
##1 Giới thiệu

Keystone là một dự án OpenStack, cung cấp chức năng xác thực và ủy quyền cho các phần tử trong OpenStack. 
Người dùng khai báo chứng thực với Keystone và dựa trên kết quả của tiến trình xác thực, nó sẽ gán "role" cùng với một token xác thực cho người dùng. "Role" này mô tả quyền hạn cũng như vai trò trong thực hiện việc vận hành OpenStack.

2 tính năng chính:
- Theo dõi người dùng và quyền hạn của họ
- Cung cấp một catalog của các dịch vụ đang sẵn sàng với các API endpoints để truy cập các dịch vụ đó

<img src=http://i.imgur.com/BkImy6d.png>

Mô hình liên kết với các project

<a name="1.1"></a>
###1.1 Các dịch vụ cung cấp

- Identity: Các dịch vụ cung cấp danh tính, xác nhận chứng chỉ và dữ liệu về người sử dụng, thuê và vai trò, cũng như bất kỳ siêu dữ liệu liên quan.
- Token: Xác nhận và quản lý các tokens được sử dụng để xác thực yêu cầu khi thông tin của người dùng đã được xác minh.
- Catalog: Cung cấp endpoint registry sử dụng để phát hiện endpoint.
- Policy: Cung cấp engine để ủy quyền dựa trên rule và kết nối với giao diện quản lý rule.

<a name="1.2"></a>
###1.2 Backend

Mỗi dịch vụ được cấu hình để sử dựng các backend cho phù hợp với các môi trường và yêu cầu.
Các backend được quy định tại file keystone.conf

- KVS: Cung cấp giao diện hỗ trợ tìm kiếm theo khóa
- SQL: Sử dụng SQLAlchemy để lưu trữ dữ liệu bền vững
- PAM: Sử dụng dịch vụ PAM của hệ thống cục bộ cho việc xác thực
- LDAP: Kết nối thông qua LDAP tới một thư mục back-end, như Active Directory để xác thực các user và lấy thông tin về role
- Memcached: hệ thống phân phối và lưu trữ bộ nhớ đệm

<img src=http://i.imgur.com/RhQssJH.png>

Mô hình dịch vụ và backend


<a name="2"></a>
##2 Các chủ đề cơ bản của KeyStone

<a name="2.1"></a>
###2.1 Các khái niệm

Khái niệm |	|
--- | --- |
| Project | Một khái niệm trừu tượng được dùng bởi các dịch vụ của OpenStack để nhóm và cô lập các tài nguyên. Các User và Groups được phép truy cập vào Project với các Role. |
| Domain |  Một nhóm các Project và User. Giúp tránh va chạm giữa nhiều Project. |
| Users and User Groups (Actors) || Các thực thể tiếp cận với nguồn tài nguyên ở các Domain, Project. |
| Roles | Dùng để ủy quyền. Ví dụ: Vai trò của quản lý là giao cho user quyền sử dụng máy tính của một phòng. |
| Assignment | Cấp phép, thu hồi, di chuyển. | 
| Targets |
| Token | Xác thực lại với Keystone, chứa ID được đảm bảo là duy nhất và payload chứa dữ liệu về người dùng. |
| Catalog | Danh mục các dịch vụ,chứa các URL và endpoints. |


<a name="2.2"></a>
###2.2 Use Cases for Identity Backends


**2.2.1 SQL**

KeyStone lưu trữ các User và Groups trong SQL, Hỗ trợ MySQL, DB2, PostgreSQL. 

-Quản lý người dùng và nhóm thông qua OpenStack API
- Keystone không phải là một nhà cung cấp danh
- Không luân chuyển mật khẩu
- Không khôi phục mật khẩu
- Cần lưu trữ thông tin người dùng
- Triển khai cho kiểm thử, phát triển hoặc nhóm dùng nhỏ

**2.2.2 LDAP**

- KeyStone lấy và lưu Users, Groups trong LDAP giống như các ứng dụng khác sử dụng LDAP.
- Không cần lưu trữ các bản sao tài khoản
- KeyStone nhìn được password
- Triển khai cho kinh doanh

**2.2.3 Multiple Backends**

<img src=http://i.imgur.com/M10BBe2.png>

- Hỗ trợ đồng thời nhiều LDAP
- Chỉ xác thực tài khoản trong miền Domain
- Triển khai cho doanh nghiệp

**2.2.4 Identity Providers**

- Xác thực thông qua Apache modul
- Người dùng ko cần lưu trữ trên KeyStone 
- Các vai trò được ánh xạ
- Hỗ trợ nhiều backends (LDAP, AD, MôngDB)
- Giảm tải việc xác thực và nhận dạng
- Tận dụng được cơ sở hạ tầng và phần mềm cho việc xác thực, lấy thông tin người dùng
- Phân tách KeyStone với thông tin người dùng
- Thiết lập phức tạp
- Triển khi các IdP đã có, KeyStone không thể truy cập LDAP.

<a name="2.3"</a>
###2.3 Authentication

**2.3.1 Password**

Cách phổ biến để xác thực là cung cấp mật khẩu. 

Vd Payload dưới được gửi cho KeyStone

<img src=http://i.imgur.com/hzsdiXI.png>

Payload yêu cầu phải chứa thông tin đủ để xác thực.
Phần Scope là tùy chọn thường được sử dụng vì nếu người dùng không có scope thì không thể truy xuất dịch vụ Catalog.

<img src=http://i.imgur.com/2xIoZgJ.png>

Mô hình yêu cầu token dùng password

**2.3.2 Token**

Người dùng có thể yêu cầu token mới bằng cách cung cấp token đang có.

<img src=http://i.imgur.com/9fOOjUg.png>

<a name="2.4"></a>
###2.4 Managing access and authorizing

KeyStone tạo ra một chính sách Role-Based Access Control (RBAC), thực thi tại mỗi public API endpoint. Các chính sách được lưu trong file policy.json, nó bao gồm mục tiêu và quy tắc. Mỗi luật bắt đầu với " identity:".

Ví dụ:

<img src=http://i.imgur.com/2Wo5Z8v.png>

<a name="2.5"></a>
###2.5 Mô hình Backends and Services

<img src=http://i.imgur.com/vGovfpD.png>

Màu xanh lá cây: backend là SQL

Màu hồng: backend là SQL hoặc LDAP

Màu xanh dương: backend là SQL hoặc memcache

<a name="3"></a>
##3 Các dạng token

**Token** là một dạng thông tin của một user, token được sinh ra khi ta sử dụng username,password đúng để xác thực với keystone. Khi đó user sẽ dùng token này để truy cập vào Openstack API.

<img src=http://i.imgur.com/gKDcTez.png>

<a name="3.1"></a>
###3.1 UUID Tokens

<ul>
<li>UUID là dạng token đầu tiên của Keystone. </li>
<li>Phiên bản mới nhất UUID4.</li>
<li>Một chuỗi hex 32 ký tự được tạo ra ngẫu nhiên.</li>
<li>Được phát hành và xác nhận online bởi dịch vụ nhận dạng.</li>
<li>Token cần được lưu trữ ở vùng backend để có thể sẵn sàng xác nhận. Khi hệ thống lớn thì nó có thể làm giảm hiệu suất của KeyStone.</li>
<li>Token ko chứa định danh hoặc ủy quyền. Vì vậy cần thông qua xác minh FIG token để có thông tin định danh, ủy quyền.</li>
</ul>

Ví dụ UUID token

`2887731d2a1a46118af2340b60125865`

Câu lệnh tạo token
```sh
def _get_token_id(self, token_data):
return uuid.uuid4().hex
```

**Mô hình hoạt động**

<img src=<http://i.imgur.com/tDMetYq.png>

<ul>
<li>Client cung cấp user/password.</li>
<li>Keystone tạo một token UUID. Lưu trữ các thẻ UUID ở backend. Gửi một bản sao của UUID token cho khách hàng.</li>
<li>Các khách hàng sẽ cache token.</li>
<li>UUID sau đó sẽ được thông qua cùng với mỗi cuộc gọi API của khách hàng.</li>
<li>Mỗi khi có yêu cầu của người dùng, các thiết bị đầu cuối API sẽ gửi UUID này trở lại Keystone để xác nhận.</li>
<li>Keystone sẽ trả về "thành công" hoặc thông báo "thất bại" đến điểm cuối API.</li>
</ul>

**Cách tạo UUID token**

<img src=http://i.imgur.com/fFONEHZ.png>

**Cách xác thực token**

<img src=http://i.imgur.com/EOg1FTf.png>

**Cách thu hồi token**

<img src=http://i.imgur.com/WVQcqnj.png>


**Ưu điểm:**
<ul>
<li>Là định dạng token nhỏ và đơn giản. </li>
<li>Đơn giản cho triển khai. </li>
</ul>

**Nhược điểm:**
<ul>
<li>Cần lưu trữ.</li>
<li>Chỉ xác nhận được bằng dịch vụ nhận dạng.</li>
<li>Ko khả thi khi triển khai mô hình lớn.</li>
</ul>

<a name="3.2"></a>
###3.2 PKI/PKIz

<ul>
<li>Là định dạng token thứ 2 của keystone.</li>
<li>Nó chưa một lượng lớn thông tin như: ngày phát hành, hạn dùng, nhận dạng người dùng, dự án, vai trò... </li>
<li>Các thông tin được thể hiện trong JSON payload và đc ký bằng dạng tin nhắn mã hóa CMS.</li>
<li>Với PKIz sau khi đc ký thì được nén bằng zlib.</li>
</ul>

Ví dụ PKI token: 
```sh
MIIDsAYCCAokGCSqGSIb3DQEHAaCCAnoEggJ2ew0KICAgICJhY2QogICAgICAgI...EBMFwwVzELMAkGA
1UEBhMCVVMxDjAMBgNVBAgTBVVuc2V0MCoIIDoTCCA50CAQExCTAHBgUrDgMQ4wDAYDVQQHEwVVbnNldD
EOMAwGA1UEChM7r0iosFscpnfCuc8jGMobyfApz/dZqJnsk4lt1ahlNTpXQeVFxNK/ydKL+tzEjg
```

Xảy ra trường hợp vượt quá kích thước của HTTP header.

**Cách tạo token**

<img src=http://i.imgur.com/RC9SCmO.png>

**Mô hình làm việc**

<img src=<http://i.imgur.com/9zDORjE.png>

Với thẻ PKI/PKIz, Keystone trở thành một Certificate Authority (CA). Nó sử dụng signing key và certificate (không mã hóa) để ký token của user.

Mỗi điểm cuối API giữ một bản sao của Keystone của:
<ul>
<li>Signing certificate.</li>
<li>Revocation list.</li>
<li>CA certificate.</li>
</ul>
Các thiết bị đầu cuối API sử dụng các bit để xác nhận các yêu cầu sử dụng. Không cần cho yêu cầu trực tiếp đến Keystone với từng xác nhận. Những gì được xác nhận là chữ ký Keystone đặt trên thẻ người dùng và danh sách thu hồi Keystone của. Điểm cuối API sử dụng các dữ liệu trên để thực hiện quá trình này offline.</li>


**Ưu điểm:**

- Không cần xác nhận bở Keystone

**Nhược điểm:**

- Lớn hơn kích thước http header

- Cấu hình phức tạp


<a name="3.3"></a>
###3.3 Fernet

Để giải quyết các nhược điểm của UUID, PKI, PKIz thì Openstack đã phát triển Fernet token.

<ul>
<li>Dạng token khoảng 255 ký tự, chứa thông tin đủ để xác thực</li>
<li>Ko cần lưu trữ, không cần đồng bộ</li>
<li>Token payload chứa userID, Project ID, metadata, timestamp, lifespam, cách xác thực...</li>
<li>Sử dụng mã hóa đối xứng AES-CBC (Chung 1 key) để mã hóa và giải mã.</li>
<li>Nó không chứa service_catalog vì vậy khi region tăng lên thì không ảnh hưởng tới kích thước của token.</li>
</ul>

Ví dụ fernet token:

```sh
gAAAAABWfX8riU57aj0tkWdoIL6UdbViV-632pv0rw4zk9igCZXgC-sKwhVuVb-wyMVC9e5TFc  
7uPfKwNlT6cnzLalb3Hj0K3bc1X9ZXhde9C2ghsSfVuudMhfR8rThNBnh55RzOB8YTyBnl9MoQ  
XBO5UIFvC7wLTh_2klihb6hKuUqB6Sj3i_8
```

Các **Fernet Keys** sử dụng chứa trong thư mục ` /etc/keystone/fernet-keys/ `
```sh
Encrypted bởi Primary Fernet Key
Decrypted bởi một danh sách Fernet Keys
```

**Type of Fernet Keys**

Type 1: Primary Key
<ul>
<li>Encrypt and Decrypt</li>
<li>Key file named with the highest index</li>
</ul>
Type 2: Secondary Key
<ul>
<li>Only Decrypt</li>
<li>Lowest Index < Secondary Key File Name < Highest Index</li>
</ul>
Type 3: Staged Key
<li>Decrypt and  Next In Line to become Primary Key</li>
<li>Key file named with lowest index (of 0)</li>
</ul>

**Key format**

<img src=http://i.imgur.com/OiaNpoY.png>

**Token format**

Được mã hóa base64

Version | Timestamp | IV | Ciphertext | HMAC |
--- | --- | --- | --- | --- |
8bit	|	 64bit	|  128bit |	128bit	|	256bit |

<ul>
<li>Timestamp: Khoảng thời gian từ 01/01/1970 đến lúc token được tạo </li>
<li>IV: Vecto khởi tạo</li>
<li>Ciphertext: Message, paddes, encrypt</li>
<li>HMAC: Để xác nhận tính toàn vẹn của 4 trường phía trước</li>
</ul>

**Mô hình sinh Fernet token**

<img src=http://i.imgur.com/dQWPGle.png>

<ul>
<li> Các thông tin được cho vào Token Payload và được Padding cho đủ khối kích thước.</li>
<li> Dùng Encrypting key để mã hóa khối trên và chuyển vào Ciphertext.</li>
<li> Các trường Version, Timestamp, IV do hệ thống tự tạo ra.</li>
<li> Dùng Signing key(SHA) để mã hóa 4 trường Version, Timestamp, IV, Ciphertext sau đó chuyển vào HMAC.</li>
</ul>

**Cách xác thực Fernet token**

<img src=http://i.imgur.com/Y7bkwzq.png>

**Ưu Điểm:**


Bên dưới là bảng so sánh 4 kiểu token với các thông số chính ta có thể chọn loại token phù hợp với hệ thống của mình.

<img src=http://i.imgur.com/F92AgPQ.png>

<a name="4"></a>
##4 Federated Identity

Tạo lập các liên kết danh tính

Các thuật ngữ trong Federated Identity

- Identity Provider (IdP): Cung cấp thông tin nhận dạng
- Service Provider (SP): Dịch vụ sử dụng thông tin nhận dạng
- SAML: 
- OpenID Connect: Một chuẩn mới của Federated Identity để nhận dạng
- Assertions and Claims: Một chuẩn về thông tin, thuộc tính của người dùng. Sử dụng SP để xử lý

<img src=http://i.imgur.com/m2wii2a.png>

Mô hình Federated
	
<a name="4.1"></a>
###4.1 Authentication Flow

<img src=http://i.imgur.com/sCfgIfq.png>

- User truy cập các URL thông qua Apache modul để xác thực với IdP
- IdP trả về thuộc tính, Apache modul nén vào http header chuyển tới Keystone
- KeyStone xác định kết nối từ các nhà cung cấp để tạo token
- User chuyển token tới project 

<a name="4.2"></a>
###4.2 Single Sign-On Flow

Kết hợp KeyStone + Horizon hỗ trợ đăng nhập tự động

<img src=http://i.imgur.com/SYlhefS.png>

- User truy cập các trang trên Horizon -> chọn cách xác thực
- User được chuyển tới trang đăng nhập
- Các thuộc tính chuyển tới KeyStone và mapping sau đó trả về token
- Khi KeyStone làm việc với token thì phải trả về ID token cho Horizon
- Horizon có token, nó tạo ra client session và người dùng đăng nhập
 
<a name="5"></a>
##5 Các cải tiến mới trên Mitaka
<ul>
<li>Cải tiến bộ nhớ đệm</li>
<li>Hỗ trợ TOTP (Time based one time password) Xác thực mật khẩu 1 lần</li>
<li>User có nhiều roles</li>
<li>Thống nhất nhận dạng (Trường hợp 2 user có tên giống nhau)</li>
</ul>

 Note: 
 Tìm hiểu thêm về các hoạt động của các token.
 

	
	
	
	
	
	
	
 
