#Module In Ansible.

- Các module hay còn gọi là các thư viện module cung cấp cho Ansible các phương tiện để điều khiển hoặc quản lý tài nguyên trên local hoặc các remote server. Chúng thực hiện một loạt các chức năng . VÍ dụ một module có thể chịu trách nhiệm khởi động lại một máy hoặc có thể đơn giản hiển thị một tin nhắn trên màn hình.
- Ansible cho phép người dùng viết các module của riêng mình và cũng cung cấp các module core và bổ sung.

**Các module core**

- Là các module được đội Ansible duy trì và luôn luôn đi kèm với Ansible. CHúng cũng nhận được thứ tự ưu tiên cao hơn tất cả các request so với các module bổ sung.
- Có thể tham khảo các module đó ở [đây](https://github.com/ansible/ansible-modules-core)

**Các module bổ sung**

- Các module này hiện tại đi kèm với Ansible, nhưng có thể sẽ tách ra trong tương lai. Chúng hầu như được duy trì bởi cộng đồng . Các modulw non-core hoàn toàn có thể sử dụng, nhưng có thể nhận được tỉ lệ trả lời thấp hơn cho các vấn đề (iussue) và các pull request.
- Các module bổ sung có thể trở thành các module core the thời gian.
- Có thể xem thêm về các module nà ở [đây](https://github.com/ansible/ansible-modules-extras)

##Các module PostgreSQL của Ansible.

- Ansible cung cấp các module cho PostgreSQL . Một số là các module core một số khác là các module bổ sung. 
- Tất cả các module PostgreSQL của Ansible yêu cầu gói `psycopg2` của python phải được cài đặt trên cùng một máy với server của PostgreSQL. `Psyconpg2` là một bộ chuyển đổi cơ sở dữ liệu trong ngôn ngữ lập trình python.
- Trên các hệ thống Debian/Ubuntu, gói `psyconpg2` có thể được cài đặt như sau : 

```sh
apt-get install python-psycopg2
```

- Bây giờ chúng ta sẽ xem xét các module này một cách chi tiết. Chúng ta sẽ làm trên Server PostgreSQL trên cổng 5432 với user `postgres` và password trống.

**Postgresql_db**

- Module core này sẽ tạo hoặc loại bỏ một cơ sở dữ liệu PostgreSQL . Trong thuật ngữ của Ansible , nó đảm bảo cung cấp một cơ sở dữ liệu trong PostgreSQL với 2 trạng thái là `present` hoặc `absent`.
- Tùy chọn quan trọng nhất là yêu cầu tham số `name`. Nó là tên CSDL trong một server PostgreSQL . Một tham số quan trọng khác là "state" . Nó yêu cầu một trong 2 giá trị : `present` hoặc `absent` . Điều này cho phép chúng ta tạo hoặc loại bỏ một CSDL cái mà được xác định bởi giá trị cung cấp cho tham số `name`.
- Một số quy trình có thể yêu cầu các tham số kết nối chẳng hạn như : login_host ; port ; login_user ; và login password.
- Hãy tạo một cơ sở dữ liệu gọi là `module_test` trên server PostgreSQL bằng cách thêm các dòng dưới đây vào playbook của chúng ta :

```sh
postgresql_db: name=module_test
                state=present
                login_host=db.example.com
                port=5432
                login_user=postgres
```

- Ở đây, chúng ta kết nối tới server CSDL để test lại db.example.com với user `postgres` . Tuy nhiên không nhất thiết user phải là postgres có thể sử dụng các tên khác.
- Loại bỏ một DB bằng cách thêm những dòng này vào playbook của chúng ta.

```sh
postgresql_db: name=module_test
                state=absent
                login_host=db.example.com
                port=5432
                login_user=postgres
```

**Postgresql_ext**

- PostgreSQL được biết đến là có các extension rất hữu ích và mạnh mẽ. Ví dụ, một extension gần đây là `tsm_system_rows` giúp lấy chính xác số lượng các dòng trong [tablesampling](http://blog.2ndquadrant.com/tablesample-and-other-methods-for-getting-random-tuples/).
- Tạo extension :

```sh
 postgresql_ext: db=module_test
                 name=tsm_system_rows
                 state=present
                 login_host=db.example.com
                 port=5432
                 login_user=postgres
```

**postgresql_user**

- Module core này cho phép thêm hoặc xóa các user, role từ một cơ sở dữ liệu .
- Nó là một module mạng mẽ bởi vì trong khi đảm bảo rằng một người dùng đang hiện diện trên cơ sở dữ liệu, nó cũng cho phép chỉnh sửa các đặc quyền (privilege) hoặc các role cùng lúc.
- Hãy bắt đầu bằng cách xem xét các tham số. Tham số bắt buộc duy nhất ở đây là `name` , cái đề cập tới một user hoặc tên một role. Ngoài ra, như trong hầu hết các module của Ansible, thâm số `state` cũng quan trọng. Nó có thể có một trong 2 giá trị `present` hoặc `absent`.
- Ngoài những tham số kết nối trong các module trước, một vài tham số quan trọng trong mục tùy chọn như là :
 <ul>
 <li>db : Tên CSDL nơi quyền sẽ được cấp.</li>
 <li>Password : passwword của user.</li>
 <li>priv : các đặc quyền trong (privileges) "priv1/priv2" hoặc các bảng đặc quyền (table privileges) trong bảng định dạng "table:priv1,priv2,...". </li>
 <li>role_attr_flags : Các thuộc tính của Role. Các giá trị có thể là :
  <ul>
  <li>[NO]SUPERUSER</li>
  <li>[NO]CREATEROLE</li>
  <li>[NO]CREATUSER</li>
  <li>[NO]CREATEDB</li>
  <li>[NO]INHERIT</li>
  <li>[NO]LOGIN</li>
  <li>[NO]REPLICATION</li>
  </ul>
 </li>
 </ul>

- Trong thứ tự để tạo một user mới gọi là `ada` với password là `lovelace` và một kết nối đặc quyền (privilege) tới cơ sở dữ liệu `modulw_test`, chúng ta có thể thêm các dòng sau :

```sh
postgresql_user: db=module_test
                  name=ada
                  password=lovelace
                  state=present
                  priv=CONNECT
                  login_host=db.example.com
                  port=5432
                  login_user=postgres
```

- Bây giờ chúng ta có một user đã sẵn sàng, chúng ta có thể gán cho user một vài role để cho user `ada` này login và tạo CSDL .

```sh
postgresql_user: name=ada
                  role_attr_flags=LOGIN,CREATEDB
                  login_host=db.example.com
                  port=5432
                  login_user=postgres
```

- CHúng ta có thể cung cấp các đặc quyền dựa trên global hoặc table chẳng hạn như "INSERT" , "UPDATE" , "SELECT" , và "DELETE" sử dụng tham số `priv`. Một trong những điểm quan trọng cần xem xét là một user không thể loại bỏ cho tới khi tất cả các đặc quyền (privileges) được cấp bị thu hồi.

**postgresql_privs**

- Module core này cấp hoặc thu hồi các đặc quyền trên các đối tượng cơ sở dữ liệu PostgreSQL . Các đối tượng được hỗ trợ là : table, sequence, function, database, schema, langue, tablespace và gruop.
- Các tham số yêu cầu là "database" ; tên của cơ sở dữ liệu để cấp/thu hồi các đặc quyền và "role"; một danh sách tên các role được ngăn cách bằng dấu phẩy;
- Các tham số tùy chon quan trọng nhất là : 
 <ul>
 <li>Type : kiểu đối tượng thiết lập đặc quyền. CÓ thể là một trong các kiểu table, sequence, function, database, schema, language, tablesace, group. Giá trị mặc định là table.</li>
 <li>obj : Các đối tượng cơ sở sữ liệu được thiết lập đặc quyền. Có thể có nhiều giá trị. Trong trường hợp đó, các đối tượng sẽ được ngăn cách bằng dấu phẩy.</li>
 <li>privs : Một danh sách các đặc quyền được ngăn cách bằng dấy phẩy để gọi hoặc thu hồi. Các giá trị có thể bao gồm : ALL, SELECT, UPDATE, INSERT.</li>
 </ul>

- Một ví dụ cụ thể :

```sh
postgresql_privs: db=module_test
                   privs=ALL
                   type=schema
                   objs=public
                   role=ada
                   login_host=db.example.com
                   port=5432
                   login_user=postgres
```

