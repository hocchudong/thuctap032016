#Các module DB của Ansible.

##1. Các module DB mà Ansible hỗ trợ.

- Influxdb.
- Misc.
- Mssql.
- Mysql.
- Postgresql.
- Vertica.

##2. Mysql.

###2.1. Add or remove Mysql DB from a remote host.

**Các Yêu cầu.**

- MySQLdb.
- Mysql (command line binary).
- Mysqldump (command line binary).

**Các lựa chọn**

 <table>
  <tr>
  <td>Parameter</td>
  <td>Required</td>
  <td>Default</td>
  <td>Choices</td>
  <td>Comments</td>
  </tr>
  <tr>
  <td>collation</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Collation mode (mode. Chỉ áp dụng cho bảng/DB mới và không cập nhật những cái hiện có, đây là một trong những hạn chế của Mysql</td>
  </tr>
  <tr>
  <td>Config_file (added in 2.0)</td>
  <td>no</td>
  <td>~/.my.cnf</td>
  <td></td>
  <td>Xác định file config từ đó user và password sẽ được đọc.</td>
  </tr>
  </tr>
  <tr>
  <td>Connect_timeout (added in 2.1)</td>
  <td>no</td>
  <td>30</td>
  <td></td>
  <td>Thời gian chờ khi kết nối tới Mysql server.</td>
  </tr>
  </tr>
  <tr>
  <td>encoding</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Chế độ mã hóa sử dụng. Ví dụ như `utf8` và `latin1_swedish_ci`</td>
  </tr>
  <tr>
  <td>login_host</td>
  <td>no</td>
  <td>localhost</td>
  <td></td>
  <td>Host chạy DB</td>
  </tr>
  <tr>
  <td>login_password</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Password sử dụng để xác thực.</td>
  </tr>
  <tr>
  <td>Loggin_port</td>
  <td>no</td>
  <td>3306</td>
  <td></td>
  <td>Port của MySQL server.</td>
  </tr>
  <tr>
  <td>Login_unix_socket</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Đường dẫn đến một Unix domain socket cho tất cả các kết nối local.</td>
  </tr>
  <tr>
  <td>Login_user</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Username được dùng để xác thực.</td>
  </tr>
  <tr>
  <td>Name</td>
  <td>Yes</td>
  <td></td>
  <td></td>
  <td>Tên của database để add hoặc remove , name=all Chỉ có thể được cung cấp nếu State là `dump` hoặc `import`, Nếu name=all làm việc giống như --all-databases được quyền lựa chọn cho mysqldump (added 2.0)</td>
  </tr>
  <tr>
  <td>Quick (added 2.1)</td>
  <td>no</td>
  <td>True</td>
  <td></td>
  <td>Option used for dumping large tables.</td>
  </tr>
  <tr>
  <td>Single_transaction (added in 2.1)</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Thực hiện dump một giao dịch đơn lẻ.</td>
  </tr>
  <tr>
  <td>ssl_ca (added in 2.0)</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Đường dẫn tới một chứng chỉ Certificate Authorize (CA). Với lựa chọn này phải chỉ rõ được sự tương đồng của chứng chỉ bởi server.</td>
  </tr>
  <tr>
  <td>ssl_cert (added in 2.0)</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Đường dẫn tới một client private key.</td>
  </tr>
  <tr>
  <td>ssl_key (added in 2.0)</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Đường dẫn tới client private key.</td>
  </tr>
  <tr>
  <td>State</td>
  <td>no</td>
  <td>present</td>
  <td>
   - present
   - absent
   - dump
   - import
  </td>
  <td>Các trạng thái của CSDL.</td>
  </tr>
  <tr>
  <td>Target</td>
  <td>no</td>
  <td></td>
  <td></td>
  <td>Vị trí, trên các máy chủ từ xa, của tập tin dump dùng để đọc từ hay ghi vào . Không nén tập tin SQL (.sql) cũng như bzip2 (.Bz2) , gzip (.gz) và xz (added in 2.0) nén các file được hỗ trợ.</td>
  </tr>
 </table>

**Ví dụ**

```sh
#Tạo một database
---
mysql_db : name=datpt state=present

#coppy 
```