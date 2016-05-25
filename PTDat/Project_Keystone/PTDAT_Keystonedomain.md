##Keystone domain là gì?

- Domain trong Keystone là abstract resources và đã được giới thiệu trong phiên bản 3 của API Keystone.
- Một domain là một bộ sưu tập của các user và các project tồn tại trong môi trường OpenStack. Thông thường, resource mapping có thể được tóm tắt là "Một user có một vai trò trong một project".Người sử dụng thường là một các nhân giao tiếp với cloud service để thực hiện các yêu cầu cung cấp và hủy cơ sở hạ tầng. Một vài trò là một arbitrary bit of metadata được sử dụng để gây ảnh hưởng đến quyền của người dùng trong môi trường. Dự án này là một container sử dụng group và các resrorce cô lập với nhau. Với mô hình mapping ban đầu, khi vài trò quản trị được áp dụng cho một người sử dụng, người sử dụng đó sẽ trở thành một cloud adminstrator thay vì một quản trị dự án như đã dự định.
- Với domain : các resource mapping có thể được tóm lược là "domain được tạo ra của người sử dụng, trong đó người dùng có thể có vài trò tại các dự án và các tên miền cấp cao". Với mô hình này , nó bây giờ có thể là một người dùng admin cho toàn bộ domain, cho phép người dùng có thể quản lý toàn bộ tài nguyên như người sử dụng và các dự án cho domain cụ thể. Nhưng người dùng cũng có thể có vai trò áp dụng chỉ cho một project cụ thể mà hành xử giống như nó đã làm với các mô hình trước đó.
- Một số lợi ích khi sử dụng Domain là :
 <ul>
 <li>More fine grained Role Based Access Control (RBAC) capabilities.</li>
 <li>Tạo cloud adminstator có khả năng ủy thác cho người sử dụng.</li>
 <li>Hỗ trợ chồng chéo cho tài nguyên như tên người dùng.</li>
 <li>Khả năng cho các tổ chức riêng biệt có thể tận dụng phần phụ trợ khác nhau. Ví dụ : Một user có thể dựa trên SQL, hoặc có thể dựa trên LDAP.</li>
 </ul>

### Sử dụng OpenStack Keystone Domain như thế nào?

```sh
#bạn có thể tạo một doamin : 
$ openstack domain create <name>

#bạn có thể list các domain : 
$ openstack domain list

#Mỗi một domain bạn tạo có thể tạo một user trong domain tồn tại đó : 
$ openstack user create –domain <name> –email <email> –password <pass> <username>

#Bạn có thể tạo một project bên trong một domain : 
$ openstack project create –domain <name> –description <desc> <project_name>

#Từ control access, bạn có thể thiết lập vai trò của một user trong một project : 
$ openstack role add –project-domain <name> –project <project_name> –user <username>

#Bạn có thể xóa một domain và tất cả các resource trong nó : 
$ openstack domain set –disable <name>
$ openstack domain delete <name>
```

##Tổng kết.

- Keystone domains cung cấp cho người phát triển OpenStack tính linh hoạt khi chia môi trường của họ vào phân vùng hợp lý sẽ được sử dụng bởi các thành viên của các phòng ban khác nhau . Các chi tiết kết quả trong mô hình cho phép cung cấp một kết hợp tuyệt vời của khả năng tự phục vụ trong khi vẫn đảm bảo sự các ly giữa người sử dụng và các dự án của họ.