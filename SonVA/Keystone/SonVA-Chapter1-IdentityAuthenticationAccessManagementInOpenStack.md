# CHAPTER I: FUNDAMENTAL KEYSTONE TOPIC

<a name="1.1"></a>
## 1.1. Khái niệm trong keystone
- Project:
    Là Tập hợp các tài nguyên của openstack (server, images...). Bản thân Project không bao gồm user, nhưng user và usergroup được truy cập vào Project thông qua Role Assignment (Grant Access).
- Domain: Vào thời kì đầu của openstack, chưa có cách để hạn chế truy cập vào các Project giữa các user trong các Organization khác nhau. Để phục vụ mục đích này, domain ra đời để chia một tập hợp các project và User, usergroup cho các organization khác nhau. Mỗi Organization sở hữu riêng một lượng tài nguyên và các organization không thể truy cập tự do vào tài nguyên của organization khác.
- Actor (User, Usergroup): Group là một tập hợp các users. Mối quan hệ giữa Domain, Project, User, Group được mô tả  
<img src="http://i.imgur.com/BZsmBOx.png">  
- Role: Actor có thể có các quyền khác nhau trên các project khác nhau, những quyền đó kết hợp thành role.
- Assignment: Actor-Role-Target, là việc gắn quyền (granted) hoặc hủy quyền truy cập (revoked)
- Target: Là project hoặc Domain gọi chung.
- Token: Để gọi được APIs thì phải cung cấp thông tin truy cập và token để xác định quyền truy cập. Token bao gồm ID và payload. Ví dụ về payload:  
<img src="http://i.imgur.com/b50dPCs.png">  
- Catalog: Chứa các đường dẫn và danh sách các endpoint đến các openstack service hoặc các service ngoài. Ví dụ về catalog:  
<img src="http://i.imgur.com/ucRMWTp.png">  

## 1.2 Identity:
### 1.2.1 SQL: 
Keystone cho phép lưu trữ các Actor (User, group) trong SQL, hỗ trợ các loại SQL như MySQL, PostgreSQL, DB2. Keystone lưu trữ thông tin như tên, mật khẩu, và một số thông tin khác. SQL không phải là dạng lưu trữ tốt nhất trong môi trường doanh nghiệp.
- Ưu điểm: Dễ để cài đặt, quản lý Actor qua Openstack APIs
- Nhược: Keystone không trở thành Identity Provider được, chỉ hỗ trợ mật khẩu thông thường, yếu. bị giới hạn trong môi trường doanh nghiệp. User cần phải nhớ username và password.  

### 1.2.2 LDAP:
Keystone cho phép lưu trữ các Actor (User, group) trong LDAP (Lightweight Dicrectory Access Protocol). Keystone truy cập vào LDAP như bao nhiêu chương trình khác (System login, mail, WebApp..)  
<img src="http://i.imgur.com/XcYa3or.png">  
- Ưu: Không cần công bảo trì vì không phải lưu Actor riêng biệt. (DÙng chung với các dịch vụ khác nên chỉ cần bảo trì 1 lần cho tất cả các dịch vụ). Keystone không hoạt động như công cụ cung cấp Identity.
- Nhược: Một vài tài khoản dịch vụ (service account) cần lưu trữ ở chỗ khác nếu như Admin quản lý LDAP không muốn lưu vào trong LDAP của họ. Password vẫn còn có thể thấy được trong quá trình xác thực, keystone chỉ đóng vai trò chuyển tiếp request mà thôi

### 1.2.3 Multiple Backend: (Từ bản Juno)
Mỗi một backend cho một domain. Default domain sử dụng SQL để lưu trữ các service account (là các account Giúp cho các Openstack Service tương tác với keystone). Các domain khác có thể sử dụng LDAP để lưu trữ Actor.  
<img src="http://i.imgur.com/x38IYZo.png">  
- Ưu điểm: Hỗ trợ nhiều loại backend, tích hợp được với các LDAP có sẵn của tổ chức, doanh nghiệp
- Nhược: Authenticate user phải khai báo thêm domain mà user đó nằm trong. Setup các dịch vụ Phức tạp.

### 1.2.4 Identity Provider
Từ bản IceHouse, keystone hỗ trợ federate authentication thông qua Apache Module với nhiều Identity Provider. User không lưu trữ ở keystone. Identity Provider là các nguồn lưu trữ thông tin về Identity được lưu bởi các loại backend như Ldap, AD, MongoDB hoặc Social Login (FB, Twitter).  
- Ưu: có thể tích hợp với các hệ thống có sẵn để xác thực người dùng và lấy các thông tin người dùng sẵn có, có sự biệt lập giữa keystone và việc xử lí thông tin ID. Mở ra khả năng single sign-on và hibrid cloud. Keystone không thể xem được bất kì password nào (an toàn). Identity Provider quản lý việc xác thực hoàn toàn nên việc sử dụng kiểu xác thực nào (password, cert, two-factor...) không liên quan đến keystone.
- Nhược: Setup cho từng loại nguồn Identity 

### 1.2.5 Usecase cho ID backend

