#Một số khái niệm.

**Module**

- Module hay các thư viện module cung cấp cho Ansible các thư viện để điều khiển hoặc quản lý tài nguyên trên local hoặc các remote các server.

**Playbook**

- Ansible playbook được viết bằng cú pháp YAML. Nó có thể chứa nhiều hơn một play. Mỗi play chứa tên các nhóm máy chủ để kết nối tới và các nhiệm vụ ,à nó cần thực hiện. Nó cũng có chứa các biến/các role/các handler, nếu đã định nghĩa.
- Một ví dụ về playbook :

```sh
---

- hosts: dbservers
 gather_facts: no

 vars:
   who: World

 tasks:
 - name: say hello
   debug: msg="Hello {{ who }}"

 - name: retrieve the uptime
   command: uptime
```

**Inventory**

- File iventory để giúp Ansible biết các server mà nó cần kết nối sử dụng SSH , thông tin kết nối nó yêu cầu và các tùy chọn biến gắn liền với các server này. 
- File inventory có định dạng là INI. Trong file inventory, chúng ta có thể chỉ định nhiều hơn một máy chủ và gom chúng thành nhiều nhóm.
- Ví dụ file iventory hosts.ini như sau :

```sh
[dbservers]
db.example.com
```
**Task**

- Một khái niệm quan trọng khác đó là nhiệm vụ. Mỗi nhiệm của Ansible chưa một tên, một module để gọi , các tham số của module, và tùy chọn các điều kiện trước sau. CHúng cho phép chúng ta gọi các module Ansible và truyền thông tin tới các nhiệm vụ liên tiếp.

**Các biến (vars)**

- Biến rất hữu dụng trong việc tái sử dụng thông tin chúng ta cung cấp hoặc tập hợp . Chúng ta có thể định nghĩa biến trong các file iventory, các file YAML hoặc trong các playbook.