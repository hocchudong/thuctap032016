#Báo cáo tìm hiểu Keystone
##Mục lục

##Tổng quan

- Là dự án trong OpenStack đảm nhiệm định danh, tạo token, danh mục và quyền hạn

- Định danh gồm có:
<ul>
<li>Quản lý người dùng: thực hiện theo dõi quyền của người dùng</li>
<li>Dịch vụ danh mục: cung cấp danh mục endpoint</li>
</ul>

- Tổ chức thành các nhóm dịch vụ tương tác qua endpoints

- Dịch vụ định danh:xác nhận người dùng và thông tin liên quan

- Danh mục: cung cấp danh sách mục endpoint

- Dịch vụ quyền hạn:cung cấp việc xác thực

- Mỗi dịch vụ có 1 khu lưu trữ để cho Keystone phù hợp với nhiều môi trường và nhu cầu
<ul>
<li>KVS backend:giao diện backend đon giản đẻ tra cứu khóa chính<\li>
<li>SQLbackend:cơ sở dữ liệu SQL lưu trữ dữ liệu</li>
<li>PAM backend: cơ sở dữ liệu dùng hệ thông PAM để ủy quyền, cung cấp mốt quan hệ 1-1 giữa người thuê và người dùng</li>
<li>LDAP backend:lưu trữ người dùng và người thuê nhánh kacs nhau</li>
<li> Templated backend: một mẫu  dùng để chỉnh sửa Keystone</li>
</ul>

- Sơ đồ kiến trúc vật lý Keystone
<img src=https://allthingsopendotcom.files.wordpress.com/2014/07/keystone.png>

<img src=http://26a0ff8ca8ba32139f7d-db711c577a50b6bdc946ea71aaca027d.r97.cf1.rackcdn.com/openstack-conceptual-arch-folsom.jpg>

- Sơ đồ hoạt động
<img src=https://www.mirantis.com/wp-content/uploads/2012/05/Keystoneflowchart.jpg>
<ul>
<li>Người dùng sẽ đưa chứng chỉ đến Keystone sau đó nhận lại token sau đí dùng token đó để yêu cầu đến các projects các projects sẽ gửi lại token đến keystone để xác nhận và quá trình này lặp lại đến khi máy ảo tạo ra </li>
</ul>

- 3 loại người dùng:
<ul>
<li>Người dùng(users):người dùng là con người có thông tin là tên người dùng, mật khẩu ,email</li>
<li>Người thuê(tenants):là dự án,nhóm hoặc tổ chức .Khi yêu cầu dịch vụ OpenStack bạn phải là người thuê</li>
<li>Quyền hạn(roles):cho phép người dùng làm gì với OpenStack</li>
</ul>

- Keystone cung cấp danh mục để các hệ thống OpenStack biết các API các dịch vụ OpenStack cụ thể là gồm có:dịch vụ và endpoints

##II.Khái niệm

- Domain:sinh ra với mục đích hạn chế quyền các người dùng hay là phân quyền người dùng,gồm user,group,...

- User và group(actor): người dùng hoặc người dùng hoặc thậm chí là 1 project

- Roles:chỉ vai trò người dùng, mỗi người có vai trò khác nhau với từng projects

- Assignment:kết hợp actor,mục tiêu, và role,có thể cấp phát thu hồi hoặc thừa kết

- Target:thực thể coi project và domain là một

- Token:chứa ID và payload dùng để cấp quyền tạo ra bằng việc xác thực người dùng

- Catalog: cung cấp danh sách endpoints và URL để biết ở đâu tạo máy ảo

##III.Thành phần keystone

###1.SQL

