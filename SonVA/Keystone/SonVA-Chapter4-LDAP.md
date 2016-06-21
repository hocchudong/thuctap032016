# CHAPTER 4: LDAP

LDAP và AD (Microsoft) là 2 loại phổ biến nhất của hệ thống quản lý identity của doanh nghiệp. Được sử dụng bởi rất nhiều doanh nghiệp lớn. 
## Config keystone để tích hợp với LDAP:
Keystone hiện tại đã hỗ trợ LDAP. Bằng việc khai báo trong keystone.conf, keystone sẽ chuyển các API call thành dạng mà LDAP có thể xử lý đc. Có 1 hạn chế rất lớn trong loại classic LDAP là chỉ được phép có duy nhất 1 domain trong keystone (Default domain). Việc sử dụng nhiều domain được hỗ trợ trong bản LDAP mới hơn. 

- Mapping user và group ở keystone vào LDAP:  
    - Trước hết ta có định dạng của một user như sau:  
    <img src="http://i.imgur.com/KXjlnRS.png">  
    - Định dạng một group:
    <img src="http://i.imgur.com/EejxbKk.png">  
    Nhiệm vụ của chúng ta là làm thế nào để map được các thông số như ID, name, password... vào dạng mà LDAP xử lý và lưu trữ
    - Keystone cung cấp cho chúng ta một số config để giải quyết điều nà. Phía bên trái là các thuộc tính của Keystone và phía bên phải là các thuộc tính tương ứng trong LDAP:
    <img src="http://i.imgur.com/WRX7Une.png">  
    Tương tự với group:
    <img src="http://i.imgur.com/FVjHmhC.png">
- Keystone cần biết được một số thông số để connect tới LDAP server:
```
[identity] 
driver = ldap   //cho keystone biết  ID backend dùng LDAP
[ldap] 
url = ldap://myservice.acme.com 
query_scope = sub
user_tree_dn = "ou=users,o=acme.com" 
user_objectclass = person 
user_id_attribute = mail 
user_name_attribute = mail 
user_mail_attribute = mail
user_pass_attribute = userPassword 
user_enabled_attribute = enabled 
group_tree_dn = "ou=memberlist,ou=groups,o=acme.com" 
group_objectclass = groupOfUniqueNames 
group_id_attribute = cn 
group_name_attribute = cn 
group_member_attribute = uniquemember 
group_desc_attribute = description
user_allow_create = false 
user_allow_update = false 
user_allow_delete = false 
group_allow_create = false 
group_allow_update = false 
group_allow_delete = false 
```

