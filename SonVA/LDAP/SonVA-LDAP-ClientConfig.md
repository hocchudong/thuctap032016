## Cài đặt LDAP Client truy cập LDAP server để xác thực đăng nhập vào máy client
Cài đặt các gói cần thiết:  
```sudo apt-get install libnss-ldap libpam-ldap ldap-utils```   
(1) specify LDAP server's URI -> Nhập URL ldap server, ví dụ ldap://192.168.198.10/ (Nhớ phải có dấu / cuối cùng)  
(2) specify suffix -> Domain component của directory  
(3) specify LDAP version -> ver 3  
Make local root Database admin:   -> YES  
Does the LDAP database require login?    -> YES (hoặc No, tùy)  
(6)specify LDAP admin account's suffix -> Nhập ldap admin DN, ví dụ cn=admin,dc=test,dc=com
(7) specify password for LDAP admin account -> Password admin

- sửa tập tin ```/etc/nsswitch.conf```  
thêm 'ldap' vào sau 3 'compat'  
```
passwd:     compat ldap  
group:     compat ldap  
shadow:     compat ldap  
```  

- Sửa tập tin ```/etc/pam.d/common-password```  
Sửa dòng 26, bỏ 'use_authtok' đi  
```password     [success=1 user_unknown=ignore default=die]     pam_ldap.so try_first_pass```  

- Sửa tập tin ```/etc/pam.d/common-session```
Thêm vào dòng cuối cùng nếu muốn mỗi user khi đăng nhập sẽ tự động tạo một thư mục user trong home  
```session optional  pam_mkhomedir.so skel=/etc/skel umask=077```  

- Restart lại service ```/etc/init.d/libnss-ldap restart ```

exit và đăng nhập lại bằng user account trong directory ở  ldap server. done  
<img src="http://i.imgur.com/fO2alTX.png">