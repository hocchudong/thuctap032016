# Mục lục
[I. Keystone Fundamental](#I)
- [1. Keystone & Keystone Endpoint](#I.1)
- [2. Keystone Backend](#I.2)
- [3. Authentication](#I.3)  

[II. Keystone Token](#II)
- [1. UUID Token](#II.1)
- [2. PKI & PKIz Token](#II.2)
- [3. Fernet Token](#II.3)
- [4. How to choose token](#choose-token)

[III. Tài liệu tham khảo](#III)

<a name="I"></a>
# I. Keystone Fundamental

<a name="I.1"></a>
## 1. Keystone & Keystone endpoint
Keystone là một project trong openstack cung cấp các dịch vụ Identity (danh tính), Token (công cụ xác thực), Policy (Xác định quyền của người dùng/nhóm người dùng) chuyên dụng dùng cho các project khác trong openstack. Được truy cập thông qua Keystone Indentity API.
Indentity service gồm có 2 chức năng chính:
 - User management (Quản lý người dùng): Theo dõi người dùng và quyền mà người dùng được phép làm
 - Catalog service (danh sách dịch vụ): Theo dõi danh sách các dịch vụ, lưu vị trí của các project trong openstack và các APIs của các project đó  
 
Keystone tổ chức các dịch vụ bên trong nó thành các endpoints (đầu cuối)
 - Indentity: ID service cung cấp dịch vụ xác thực và lưu trữ danh tính người dùng (User), nhóm người dùng (tenants), Quyền người dùng (Roles) và các thông tin liên quan.
 - Token: Token service dùng để xác nhận và quản lý token list, các token cho phép xác thực các yêu cầu của Users, tenants, sau khi thông tin của user/tenant đó đã được verified bởi ID service
 - Catalog: lưu danh sách các endpoints (các project) 
 - Policy: Cung cấp dịch vụ liên quan quyền của người dùng (User right, based-rules)
Khả năng cung cấp xác thực danh tính (ID service) của keystone với các project khác
<img src="http://i.imgur.com/8kvuzbf.png">

Lưu đồ phối hợp giữa các project sử dụng keystone để xác thực các bước thực hiện tạo một VM
<img src="http://i.imgur.com/FKu4Xyc.png">

<img src="http://i.imgur.com/nNJMARr.png">

<a name="I.2"></a>
## 2. Keystone Backend
Keystone services sử dụng một số backend nhằm phục vụ mục đích quản lý dữ liệu. Các backend được định nghĩa trong keystone.conf.
 - KVS backend: backend interface hỗ trợ primary key lookups
 - SQL backend: dựa trên SQL, lưu trữ/truy xuất dữ liệu liên tục
 - PAM backend: Sử dụng chính PAM service của hệ điều hành để xác thực và cung cấp các liên kết giữa user - tenant (1-1)
 - LDAP backend: Lưu trữ user và tenant trong các cấu trúc cây (subtrees) 
 - Templated backed: Template để configure keystone
<img src="http://i.imgur.com/hDIqMCo.png">
Usecase for ID backend
<img src="http://i.imgur.com/Ofe9xtU.png">

<a name="I.3"></a>
## 3. Authentication
Có nhiều cách để xác thực trong keystone. tuy nhiên có 2 cách chính dùng để xác thực: cung cấp mật khẩu hoặc sử dụng token  
- Phương pháp đơn giản nhất là sử dụng mật khẩu:  
<img src="http://i.imgur.com/SztWXIO.png">  
Trong payload của các request cần chứa đầy đủ thông tin về việc tồn tại của user, xác thực user, ngoài ra có thể có service catalog dựa trên các quyền mà user có. Người dùng sẽ cung cấp user mật khẩu và được keystone trả về token để truy cập vào một số dịch vụ tương ứng của Openstack   
<img src="http://i.imgur.com/SaxR0R8.png">

- Sử dụng token đang có để generate token khác 
Người dùng sẽ sử dụng token đang có để yêu cầu một token mới. Cách này sẽ giảm được lượng code hơn là sử dụng password. Có nhiều nguyên nhân để sử dụng trường hợp này: có thể token đang dùng sắp hết hạn, hoặc cần token khác để truy cập vào những phạm vi khác mà token hiện tại không đáp ứng.

<img src="http://i.imgur.com/Ax2oGx2.png">
<img src="http://i.imgur.com/twm8wo4.png">

- Access management and Authorization (Quản lý quyền truy cập và xác thực)
Access management and Authorization là chức năng quan trọng của Keystone. Để thực hiện điều này, Keystone tạo ra các Role-based Access Control (RBAC) policy (Quyền truy cập dựa trên các Role) cho mỗi API endpoint. Các policy được lưu trên một file policy.json với cấu trúc nội dung  
<img src="http://i.imgur.com/hLNQDoX.png">  

<a name="II"></a>
# II. Keystone token
<img src="http://7xp2eu.com1.z0.glb.clouddn.com/uuid.png">

- **(UUID token)** Vào những ngày đầu thì keystone hỗ trợ UUID token (32 character string bearer token) dùng để xác thực và cấp quyền. Lợi ích của Token format này là token nhỏ (ngắn) và dễ sử dụng, đủ đơn giản để  có thể thêm vào trong các lệnh cURL. tuy nhiên nhược điểm của nó là ko mang theo được đủ những thông tin để có thể xác thực một cách trực tiếp các dữ liệu và request. Các dịch vụ của openstack cứ liên tục phải gửi lại token về phía keystone server để xác thực các request đến các service đó. Dẫn đến bất kì hành động nào trong Openstack đều phải thông qua keystone server.  
- **(PKI token)** Để giải quyết vấn đề đó thì Token format mới ra đời gọi là PKI. Token do PKI tạo ra chứa đủ các thành phần có thể xác thực trực tiếp tại các hoạt động của openstack mà không cần phải hỏi về lại Keystone server. Token sẽ được chứng nhận (signed) và các Openstack service có thể lưu trữ (cached) nó và sử dụng nó đến khi nào expried hoặc bị revoke (hủy bỏ). Kết quả là sẽ có ít yêu cầu đến keystone server hơn nhưng đồng thời dung lượng của các token sẽ lớn hơn nhiều (cỡ 8K) và có thể ko vừa với các header của các gói tin HTTP (nếu như HTTP server không được chỉnh lại config). các token này cũng khó có thể nhét vừa vào các cURL command nên tạo ra trải nghiệm người dùng kém (Bad user experience).   
    - Keystone team đã thử tạo ra một loại biến thể của token này gọi là PKIz. loại biến thể này là PKI token đã được nén lại, tuy nhiên theo phản hồi từ cộng đồng thì kích cỡ của nó vẫn còn quá lớn
- **(Fernet token)** Từ vấn đề của PKI token thì một dạng token mới được ra đời gọi là Fernet token. Kích cỡ loại token này khá nhỏ (255 characters) nhưng chứa đầy đủ thông tin để có thể local authorization mà không phải gửi lại request về keystone server. 
    - Lợi ích của loại token này là các thông tin trong token đủ để keystone không cần lưu trữ các thông tin thêm trong token database mà các token đời đầu luôn cần phải lưu trữ các thông tin trong một DB và khi DB có dung lượng lớn sẽ ảnh hưởng đến hiệu năng.
    - Fernet token sử dụng một khóa đối xứng để ký chứng nhận (signed) cho các token. Khóa này cần được phân phối và thay đổi. Openstack Operator (Nhà vận hành Openstack) cần phải xử lý vấn đề này. Tuy vậy việc sử dụng Fernet token vẫn có ích lợi hơn là việc sử dụng các token đời đầu.
<a name="II.1"></a>
## 1. UUID token:
Là một chuỗi 32 character được random. các character là các ký tự của hệ số thập lục phân (hệ 16, hexadecimal) giúp cho token thân thiện với người dùng và có thể truyền đi an toàn. UUID cần lưu trữ trong một backend phù hợp với nó (Thường là sử dụng cơ sở dữ liệu - DB) để validate. UUID token có thể dễ dàng revoke bằng cách dùng yêu cầu ```DELETE -tokenid-``` Tuy vậy, token vẫn chưa thực sự bị remove khỏi backend, nó mới chi bị đánh dấu là revoke. Kích cỡ của nó trong HTTP header là 32byte. có thể sử dụng dễ dàng với các lệnh cURL. Tuy nhiên bất lợi là Keystone có thể bị tắc nghẽn tùy thuộc vào kích cỡ của Openstack và số lượng request trong các hoạt động của openstack.

<a name="II.2"></a>
## 2. PKI token:
**PKI**
<img src="http://7xp2eu.com1.z0.glb.clouddn.com/pki.png">
**PKIz**
<img src="http://7xp2eu.com1.z0.glb.clouddn.com/pkiz.png">

- Token sẽ chứa toàn bộ các validation response của keystone. Do đó token sẽ chứa một lượng lớn các thông tin như nó được issue lúc nào, hết hạn lúc nào, thuộc về user nào, thông tin project, domain, role, thông tin về user, service cataloge. v.v... Các thông tin được mô tả trong một cấu trúc JSON và được ký bằng một CMS(Cryptographic Message syntax). Với PKIz thì các thông tin được nén sử dụng zlib để nén. Khi sử dụng token này thì không cần phải quay lại về keystone để verify lại nữa.
- Để có thể truyền token qua giao thức HTTP cần phải mã hóa nó dưới dạng base64. Với một yêu cầu đơn giản, một endpoint và catalog, kích cỡ xấp xỉ của nó có thể lên đến 1700bytes. Với một hệ thống lớn với nhiều endpoint, PKI token có thể lớn tới cỡ 8KB, ngay cả khi được nén lại (PKIz) nó vẫn thường không thể vừa với các HTTP header của các webserver thông thường. 
- Mặc dù PKI và PKIz token có thể cached nhưng nó cũng có những nhược điểm như khó có thể config keystone để sử dụng loại token này vì nó phải sử dụng certificate được tạo từ nhà cung cấp certificate tin cậy, và kích thước nó quá lớn sẽ gây ảnh hưởng đến các openstack service khác về hiệu năng. Keystone vẫn phải lưu trữ PKI ở backend nhằm mục đích ví dụ như tạo danh sách các revoked token
<a name="II.3"></a>
## 3. Fernet token
<img src="http://7xp2eu.com1.z0.glb.clouddn.com/fernet.png">
- Fernet token được sinh ra để cải tiến các loại token trên. Độ dài của fernet token rơi vào 255 kí tự, lớn hơn UDID token nhưng nhỏ hơn PKI token. Fernet token chứa đủ thông tin đủ để Keystone không cần lưu cứng những thông tin đó vào DB, nó cũng chứa đầy đủ thông tin cần thiết để có thể generate ra các thông tin khác như user role.. Ở trong các hệ thống lớn, các token được indentified bằng key contributor nhằm mục đích hiệu năng cao, không lưu vào trong token DB 
- Fernet token chứa một lượng nhỏ các thông tin: User Identifier, project identifier, token expiration, other information. Token được ký (signed) bởi một khóa đối xứng (symmetric key) để tránh bị can thiệp giả mạo. Key này cần phải được phân phối tới tất cả các thành phần của openstack
- Fernet token cũng có workflow như UUID token. và nó cũng phải được xác thực bằng các quá trình như UUID (Vẫn phải request về Keystone server)

<a name="choose-token"></a>
<img src="http://i.imgur.com/UvCYGM4.png">
<a name="III"></a>
# III. Tài liệu tham khảo:
- *Openstack keystone identity service*, Kavit Munshi, CTO, Aptira (Slide)
- *Identity, Authentication & Access Management in OpenStack*, implementing and deploying keystone, Steve Martinelli, Henry Nash & Brad Topol (Book, o'reilly)
- http://www.openstack.cn/?p=5120