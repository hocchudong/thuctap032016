#Báo cáo tìm hiểu về các Project trong Keystone.

****
##Mục lục

[I. Vai trò của Project Keystone.] (#vaitro)

[II. Các thành phần trong Keystone] (#cacthanhphan)
 <ul>
 <li>[Keystone enpoint] (#enpoint) </li>
 <li>[Keystone backend] (#backend) </li>
 </ul>
[III. Các phương pháp xác thực trong Keystone.] (#method)
 <ul>
 <li>[1. Xác thực bằng password.] (#password) </li>
 <li>[2. Xác thực bằng Token.] (#token) </li>
 <li>[3. Xác thực tập chung (Identity Provider).] (#provider) </li>
 </ul>

****

<a name="vaitro"></a>
##I. Vai trò của project Keystone.

- Keystone có những vai trò sau đối với OpenStack :
 <ul>
 <li>Xác thực user và vấn đề token để truy cập vào các dịch vụ.</li>
 <li>Lưu trữ user và người thuê cho  vai trò kiểm soát truy cập (role-based access control (RBAC).</li>
 <li>Cung cấp catalog của dịch vụ trên cloud.</li>
 <li>Tạo các chính sách giữa user và dịch vụ.</li>
 </ul>

- Trong đó : 
 <ul>
 <li>Identity : các dịch vụ cung cấp xác thực xác nhận chứng chỉ và dữ liệu về người sử dụng, các tenant và role, cũng như bất kì matadata nào liên quan.</li>
 <li>Token : Xác nhận dịch vụ token và quản lý sử dụng cho các Token. Thẩm định yêu cầu một khi thông tin user/tenant đã được xác minh.</li>
 <li>RBAC : Role-Based-Access-Control (RBAC) là một cơ chế chính sách kiểm soát truy cập trung gian xác định xung quanh vai trò và đặc quyền.  Các thành phần của RBAC như vai trò-quyền, sử dụng vai trò và mối quan hệ vai trò làm cho nó đơn giản để làm nhiệm vụ người dùng. Một nghiên cứu ở NIST đã chứng minh rằng RBAC giải quyết được nhiều nhu cầu của tổ chức thương mại và chính phủ. RBAC có thể được sử dụng để tạo điều kiện quản lý về an ninh trong các tổ chức lớn với hàng trăm người và hàng ngàn quyền. Mặc dù RBAC là khác nhau từ các khuôn khổ kiểm soát truy cập MAC và DAC, nó có thể thực thi các chính sách mà không cần bất kỳ biến chứng. phổ biến của nó là hiển nhiên từ thực tế rằng nhiều sản phẩm và doanh nghiệp đang sử dụng nó trực tiếp hoặc gián tiếp.</li>
 <li>catalog service : dịch vụ catalog cung cấp một enpoint registry sử dụng cho các enpoint discovery.</li>
 </ul>
<a name="cacthanhphan"></a>
##II. Các thành phần trong Keystone.

**Keystone architecture**

![scr10](http://i.imgur.com/i0cyZ06.png)

<a name="enpoint"></a>
- Keystone được tổ chức như một nhóm các dịch vụ nội bộ tiếp xúc trên một hoặc nhiều thiết bị đầu cuối.

  <ul>
  <li>Identity : các dịch vụ cung cấp xác thực xác nhận chứng chỉ và dữ liệu về người sử dụng, các tenant và role, cũng như bất kì matadata nào liên quan.</li>
  <li>Token : Xác nhận dịch vụ và quản lý sử dụng cho các Token. Thẩm định yêu cầu một khi thông tin người dùng đã được xác minh.</li>
  <li>Catalog : dịch vụ catalog cung cấp một enpoint registry sử dụng cho các enpoint discovery. </li>
  <li>Policy : Các dịch vụ Policy cung cấp một cơ cấu ủy quyền dựa trên các nguyên tắc.</li>
  </ul>

<a name="backend"></a>
- Mỗi dịch vụ có thể được cấu hình để sử dụng một backend, cho phép Keystone phù hợp với một hay nhiều môi trường  và nhu cầu. Các backend cho mỗi dịch vụ được quy đinh tại file `keystone.conf`
 <ul>
 <li>KVS backend : một giao diện backend đơn giản có nghĩa là để được tiếp tục phụ trợ về bất cứ điều gì bạn có thể tra cứu khóa chính.</li>
 <li>SQL backend : một SQL dựa trên backend sử dụng SQLAlchemy để lưu trữ dữ liệu liên tục.</li>
 <li>PAM backend : backend sử dụng PAM của hệ thống hiện tại của dịch vụ để xác thực, cung cấp một mối quan hệ một - một giữa người sử dụng và người thuê.</li>
 <li>LDAP backend : Các LDAP backend lưu trữ user và
tenants riêng biệt ở các subtrees</li>
 <li>Templated backend : Một mẫu đơn giản dùng để cấu hình Keystone.</li>
 </ul> 


<a name="method"></a>
##III. Các phương pháp xác thực Keystone.

###1. Xác thực là gì?

- Là quá trình xác minh danh tính người dùng, trong nhiều trường hợp chứng thực ban đầu được thực hiện bởi một đăng nhập với user identity của họ. Trong môi trường OpenStack thô sơ Keystone có khả năng biểu diễn tất cả các bước chứng thực, điều này không được khuyến cáo trong môi trường sản xuất và môi trường doanh nghiệp. ĐỐi với môi trường thực sự nơi mật khẩu cần được bảo vệ và quản lý, Keystone có thể dễ dàng tích hợp với một hệ thống với một dịch vụ xác thực hiện có như là LDAP hay Active Directory.
- Trong khi một User Identity thường ban đầu xác định bằng mật khẩu , nó rất phổ biến như là một phần của xác thực ban đầu này để tạo ra một mã thông báo xác thực cho sau này . Điều này làm giảm số lượng của tầm nhìn tiếp xúc của các mật khẩu mà cần được giấu kín và bảo vệ nhiều càng tốt. OpenStack dựa chủ yếu trên thẻ để xác thực và các mục đích khác. Keystone là một dịch vụ OpenStack duy nhất có thể cung cấp cho chúng ta, hiện nay Keystone sử dụng một hình thức mã thông báo được gọi là "a bearer token" điều này có nghĩa là bất kì ai đã có quyền sở hữu dấu hiệu cho dù là đúng hay sai (cho dù đã bị đánh cắp) có khả năng sử dụng thẻ để xác thực và truy cập tài nguyên. Kết quả là, sau khi sử dụng Keystone nó rất quan trọng để bảo vệ thẻ và tài nguyên của chúng ta.

###2. Các hình thức xác thực.

- Bao gồm các hình thức:
 <ul>
 <li>Xác thực bằng password.</li>
 <li>Xác thực bằng token.</li>
 <li>Xác thực tập chung (Identity Provider).</li>
 </ul>
<a name="password"></a>

####2.1. Xác thực bằng Password.

![scr4](http://i.imgur.com/BNLN8Ln.png)

- Cách phổ biến nhất đối với người sử dụng dịch vụ để xác thực là cung cấp một mật khẩu.
- Các tải trọng dưới đây là một yêu cầu mẫu POST tới Keystone. Đó là hữu ích để hiển thị toàn bộ tải trọng để người đọc nhận ra những thông tin đó là cần thiết để xác thực.

```sh
{
"auth": {
"identity": {
"methods": [
"password"
],
"password": {
"user": {
"domain": {
"name": "example.com"
},
"name": "Joe",
"password": "secretsecret"
}
}
},
"scope": {
"project": {
"domain": {
"name": "example.com"
},
"name": "project-x"
}
}
}
}
```

```sh
"Payload là một phần của dữ liệu được truyền, đó là thống điệp đích thực. Payload không bao gồm các thông tin gửi đi với nó như tiêu đề hay metadata, đôi khi được gọi là dữ liệu trên không, gửi chỉ đề đủ điều kiện giao hàng Payload."
```

- Payload của request phải đầy đủ thông tin để tìm nơi người dùng tồn tại, xác thực người dùng và tùy chọn truy xuất danh mục dịch vụ dựa trên quyền sử dụng của người sử dụng trên một phạm vi (Project).
- Phần người sử dụng xác định người dùng đến nên có thông tin tên miền (hoặc tên miền hoặc ID), trừ khi toàn cầu chỉ có duy nhất ID của người dùng được sử dụng trong đó, trường hợp đó là đủ để xác định người sử dụng. Điều này là vì trong một triển khai đa miền có thể có nhiều người sử dụng cùng tên, nên phạm vi thích hợp là cần thiết để xác định người dùng được chứng thực.
- Phần phạm vi là tùy chọn nhưng thường được sử dụng, vì ko có một phạm vi người sử dụng không thể truy xuất danh mục dịch vụ. Phạm vi được sử dụng để chỉ ra các dự án người sử dụng muốn làm việc lại. Nếu một người dùng không có vai trò trong dự án, yêu cầu sẽ bị từ chối.
- Tương tự như phần người dùng phần phạm vi phải có đủ thông tin về dự án để tìm thấy nó, vì vậy các miền sở hữu phải được xác định. Như trong trường hợp của người dùng và các nhóm, tên dự án cũng có thể xung đột trên domain. Tuy nhiên phải được đảm bảo là duy nhất nếu được chỉ định, không thông tin tên miền là cần thiết.
<a name="token"></a>

####2.2. Token.

![scr5](http://i.imgur.com/6LpW9Db.png)

- Tương tự như `Password` người dùng có thể yêu cầu một token mới bằng cách cung cấp một mã thông báo hiện tại 
- Tải trọng yêu cầu của POST này là ít hơn so với phải dùng Password.

```sh
{
"auth": {
"identity": {
"methods": [
"token"
],
"token": {
"id": "e80b74"
}
}
}
}
```

- Có nhiều lý do tại sao một token sẽ được sử dụng để khôi phục, giống như làm mới một mã thông báo rằng sẽ sớm hết hạn hoặc thay đổi một token từ unscoped token đến scoped token.

```sh
- Một unscoped token là một trong những nơi mà người dùng được xác thực nhưng không phải là cho một Project cụ thể hoặc domain. Đây là loại token hữu ích cho việc truy vấn như là xác định những gì dự án một người dùng có quyền truy cập vào. Một dấu hiệu chỉnh phạm vi được xảy ra khi người dùng được xác thực cho một dự án hay một domain cụ thể.
- Scoped token có vai trò thông tin liên quan đến Scoped tokens và các loại token được sử dụng bởi OpenStack service để xác định những loại hoạt động được phép.
```
<a name="provider"></a>

####2.3. Xác thực tập chung (Identity Provider).

- Keystone có khả năng xử lý xác thực thông qua
Apache module cho nhiều nhà cung cấp nhận dạng đáng tin cậy. Những người dùng này không được lưu trữ trong
Keystone. Một tập hợp những người dùng sẽ có thuộc tính của riêng họ đc ánh xạ vào nhóm các vai trò. Từ một Keystone chủ chốt, bộ phận cấp phát Identity là một nguồn của các Identity. Nó có thể liên quan đến phần mềm được hỗ trợ bởi nhiều phần backends (LDAP, AD, MongoDB) hoặc Logins xã hội (Google, Facebook, Twitter). Nó là phần mềm (IBM’s Tivoli Federated Identity Manager, for instance) nó trừu tượng hóa các phần phụ trợ và biên dịch thuộc tính người dùng thành 1 tổ chức thuộc tính chuẩn định dạng giao thức (SAML, OpenID Connect).  Điều này cũng phù hợp hơn trong Keystone có kế hoạch để giảm tải việc xác thực và nhận dạng các phần liên quan đến một dịch vụ đã thực hiện điều này trong một doanh nghiệp. Identiy Provider có nhiều lợi thế và vài nhược điểm.

**Lợi thế**

 <ul>
 <li>Có khả năng tận dụng cơ sở hạ tầng và phần mềm hiện có để xác thực người dùng và
lấy thông tin về người sử dụng.</li>
 <li>tách nhiều hơn nữa giữa Keystone và thông tin nhận dạng xử lý</li>
 <li>Mở cửa cho khả năng mới trong các lĩnh vực liên bang, chẳng hạn như signon đơn và đám mây lai</li>
 </li>Keystone không thấy bất kỳ mật khẩu người dùng</li>
 <li>Cung cấp nhận dạng xử lý xác thực hoàn toàn, vì vậy cho dù đó là mật khẩu, giấy chứng nhận, hoặc hai yếu tố dựa trên là không liên quan đến Keystone.</li>
 </ul>

**Nhược điểm**

 <ul>
 <li>Hầu hết các thiết lập phức tạp của Identity sources.</li>
 </ul>
 
 **Các Phần đã và đang tìm hiểu :**
  <ul>
  <li>https://github.com/datkk06/Thuc-tap-VDC/blob/master/Keystone-domain.md</li>
  <li>https://github.com/datkk06/Thuc-tap-VDC/blob/master/Keystone-Identityservice-and-config-keystone-mitaka.md</li>
  <li>https://github.com/datkk06/Thuc-tap-VDC/blob/master/performance-liberty-and-mitaka.md</li>
  </ul>
