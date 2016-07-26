#Module Mysql - Adds or Removes a use from a MYSQL database.

- Add hoặc remove một user từ một Mysql db.
- Yêu cầu trên host thực hiện module phảo có MySQLdb.
- Các tùy chọn:

 <table>
 <tr>
  <td>Parameter</td>
  <td>Required</td>
  <td>default</td>
  <td>choices</td>
  <td>comments</td>
 </tr>
 <tr>
  <td>Append_privs (added in 1.4)</td>
  <td>no</td>
  <td>no</td>
  <td>
   - yes
   - no
  </td>
  <td>Nối các đặc quyền được được định nghĩa bởi priv đến những cái hiện có cho người dùng thay vì ghi đè lên những cái hiện có.</td>
 </tr>
 <tr>
  <td>Check_implicit_admin</td>
  <td>no</td>
  <td>no</td>
  <td>
   - yes
   - no
  </td>
  <td>Kiểm tra nếu Mysql cho phép login với root/nopassword trước khi cố gắng lấy được thông tin credentials.</td>
 </tr>
 <tr>
  <td>Config_file</td>
  <td>no</td>
  <td>~/.my.cnf</td>
  <td></td>
  <td>Chỉ ra file config mà user password được đọc.</td>
 </tr>
 <tr>
  <td>encrypted</td>
  <td>no</td>
  <td>no</td>
  <td>
   - yes
   - no
  </td>
  <td>Chỉ ra trường mật khẩu là một hàm băm `mysql_native_password`</td>
 </tr>
 <tr>
  <td>host</td>
  <td>no</td>
  <td>localhost</td>
  <td></td>
  <td>'host' một phần của tên người dùng.</td>
 </tr>
 <tr>
  <td>Host_all</td>
  <td>no</td>
  <td>no</td>
  <td>
   - yes
   - no
  </td>
  <td>Ghi đè tùy chọn máy chủ, khiến cho ansible áp dụng thay đổi cho tất cả các hostname cho một người dùng nhất định. Tùy chọn này có thể không được sử dụng khi khởi tạo người sử dụng.</td>
 </tr>
 <tr>
  <td>Priv</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Là chuỗi các đặc quyền được định dạng : `db.table:priv1,priv2`.</td>
 </tr>
 <tr>
  <td>ssl_log_bin</td>
  <td>no</td>
  <td>yes</td>
  <td>
   - yes
   - no
  </td>
  <td>Là nhị phân nền có thể cho phép hoặc không cho phép kết nối.</td>
 </tr>
 <tr>
  <td>Update_password</td>
  <td>no</td>
  <td>always</td>
  <td>
   - always
   - on_create
  </td>
  <td>`always` sẽ cập nhật password nếu chúng khác nhau. `on_create` sẽ chỉ cài đặt password cho user tạo mới.</td>
 </tr>
 </table>

**Ví dụ**

```sh
#Remove một user 
---

- mysql_user: name=datpt host=localhost state=absent

#Remove tất cả user
---

- mysql_user: name="" hostall=yes state=absent

#Tạo DB có tên là datpt với pass là "bananhdat" và tất cả đặc quyền

---

- mysql_user: name=datpt password=bananhdat priv=*.*:ALL state=present
```