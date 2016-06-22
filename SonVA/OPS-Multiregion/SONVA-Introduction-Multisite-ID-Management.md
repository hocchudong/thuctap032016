# Note Openstack Multi-region for IDENTITY MANAGEMENT
## 1 Use case: 
User có thể quản lý các tài nguyên ảo trên toàn bộ các region của openstack, chỉ cần sử dụng 1 điểm xác thực duy nhất (Single Authentication Point)
## 2. Requirement Analysis (Tính toán yêu cầu)
User được cung cấp một đường dẫn tới Identity Service (Keystone). User sử dụng URL này để xác thực với keystone bằng việc nhập username, mật khẩu sau đó lấy token. Keystone xác thực username, mật khẩu, có thể gọi LDAP/AD (Nếu như LDAP/AD làm backend) và trả về token cho user. Nếu là loại token UUID hoặc Fernet thì user sẽ yêu cầu gửi thêm service catalog, với token PKI thì service catalog đi kèm token. User sau đó sẽ gửi yêu cầu cung cấp dịch vụ mà họ mong muốn tới region đã chọn cùng với token đó. Sau đó service nhận request sẽ xác thực lại token. Ví dụ nova, Nova sẽ sử dụng địa chỉ của keystone cùng với tài khoản admin (?) của nó để gọi tới keystone và check token. Việc xác thực bằng Keystone được hoàn thành trên cùng một region với nova. Tiếp đó, keystone sẽ validate (Kiểm tra) token (có chứa projectID) để đảm bảo rằng user sẽ được quyền sử dụng Nova. ProjectID được lưu dưới Backend (Keystone SQL Database). Để xác thực projectID thì Assignment Backend Database đó có một bản ghi cùng nội dung với project ID được yêu cầu trong token.  
Thế nên: 
- (1)Các service ở tất cả các region được config chung một keystone. tại keystone endpoint trung tâm này sẽ diễn ra tất cả các hoạt động xác thực trên toàn hệ thống hoặc;
- (2) Keystone được cài ở các vùng , keystone backend database được sao chép thành nhiều bản và phân bổ các bản đó ở local của mỗi vùng, backend được đồng bộ thường xuyên.   

Phương pháp 2 là phương pháp cân bằng tải được áp dụng cho mức độ sử dụng dịch vụ thông thường. Khi dữ liệu ở Assignment Backend Database, các dữ liệu đồng bộ sao chép sẽ được gửi đi giữa các region. Assignment B.DB Data bao gồm Project, domain, role, role Assignment

## 3.Key Tech Point 
- Triển khai keystone:  
    - Centralize: Cài keystone ở một vị trí nhất định. có thể là ở region chính hoặc cài riêng biệt tách hẳn ra khỏi các openstack sevice  
    - Distribute: Cài keystone ở mỗi region.
- Loại token: UUID, PKI, Fernet, CryptoGraphic
- Bố trí cơ sở dữ liệu: Master/Slave không đồng bộ, Master đồng bộ, Đối xứng/không đối xứng
- Chia sẻ Database server: Openstack điều khiển nhiều database từ các service khác nhau cung cấp từ cùng một Database server. Vì lí do High Availability, Database server thường đồng bộ tới một số node. Chỉ có database của keystone được đồng bộ đến các region khác, việc đồng bộ các database của các service khác sẽ dẫn đến lỗi hệ thống.

## 4. Giải pháp
<img src="http://i.imgur.com/3J1ec7D.png">
**Keystone Service (Distributed) với Fernet Token và Async replication** (Star mode)  
Một Keystone master cluster sử dụng fernet token cho 2 site (Mục đích HA), các site còn lại cài tối thiểu 2 node slave được config bằng DB Async replication từ một cluster ở DB master, 1 slave đi với 1 cluster master trên site 1 và 1 slave còn lại đi với 1 cluster master trên site 2. Chỉ có cluster ở node master mới được phép write. Các node slave đợi được sao chép từ master (thời gian đợi ngắn). Vấn đề phát sinh ở phương pháp này  là phân phối key và sự thay đổi của fernet token (Key rotate).  

**Ưu điểm: ** 
- Vì sao cluster lại nằm trong master site? có nhiều masternode ở trong cluster, các slave có thể sao chép song song cùng lúc được. 
- 2 site giúp đảm bảo High Availability (For writing request). 
- Tại sao phải dùng nhiều slave trên mỗi site? các slave độc lập với nhau, dễ quản lý hơn trong 1 site hơn là cluster (do bị phụ thuộc) tuy vậy cách làm này làm dư thừa instance.  

** Nhược điểm**  
Phân phối và thay đổi key. (Key distribution/rotation)

