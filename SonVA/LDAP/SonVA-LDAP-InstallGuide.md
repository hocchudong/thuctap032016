# Cài Đặt LDAP

### Bước 1: Cài LDAP  
Cài gói slapd (OpenLDAP server) trên ubuntu:  
```
sudo apt-get update  
sudo apt-get install slapd ldap-utils
```  
Config lại Slapd
```
sudo dpkg-reconfigure slapd
```  
và thực hiện cấu hình:

- Omit OpenLDAP server configuration? No
- DNS domain name? test.com
- Organization name? test
- Administrator password?
- Database backend? HDB
- Database removed when slapd is purged? No
- Move old database? Yes
- Allow LDAPv2? No

### Bước 2: Cài PHPLDAPAdmin  
```
sudo apt-get install phpldapadmin
```  
Config LDAPAdmin:  
- Mở tệp tin   
```sudo nano /etc/phpldapadmin/config.php```  
- Sửa   
```$servers->setValue('server','host','domain_name_or_IP_address');```  
- Với domain_name_or_IP_address là domain name /IP của server ldap .   
- Sửa dc thành dc tương ứng của cây thư mục trong ldap, ví dụ LDAP có domain name là sonva.abc.com thì domain component dc=sonva,dc=abc,dc=com   
```$servers->setValue('server','base',array('dc=sonva,dc=abc,dc=com'));```
- Update DC value của tài khoản login 
```$servers->setValue('login','bind_id','cn=admin,dc=sonva,dc=abc,dc=com');```  
- Tìm dòng sau, bỏ chú thích đi, sửa false thành true  
```$config->custom->appearance['hide_template_warning'] = true;```
- Lưu lại và thoát

Truy cập vào domainname-or-serverip/phpldapadmin, nhập password tương ứng với cn để truy cập vào dn   
<img src="http://i.imgur.com/BfiAe3B.png">  
Truy cập thành công. sau đó có thể tạo user và group
<img src="http://i.imgur.com/v1J24d9.png">

Trong trường hợp gặp lỗi Error trying to get a non-existent value (appearance, password_hash), mở tập tin  
```nano /usr/share/phpldapadmin/lib/TemplateRender.php```  
dòng 2469 sửa password_hash thành password_hash_custom