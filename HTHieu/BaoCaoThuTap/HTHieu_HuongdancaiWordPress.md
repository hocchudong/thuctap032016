#Hưóng dẫn cài word press trên ubuntu

##Hướng dẫn cài Xampp

- Download bộ cài tại trang này https://www.apachefriends.org/download.html

- Di chuyển đến thư mực chứa bộ cài và chạy lệnh sau :

`cd Downloads/`

`ls`

`chmod +x xampp-linux-5.6.3-0-installer.run`

`sudo ./xampp-linux-5.6.3-0-installer.run`

- Sau đó thực hiện cài đặt như với phần mềm bình thươc (ấn next liên tuc)

- Để bật giao diện xampp dùng lệnh /opt/lampp/manager-linux-x64.run

##Tạo db cho wordpress

- Truy cập `http://localhost/phpmyadmin/` và làm theo bước sau

<img src=http://www.nguyenvanquan7826.com/wp-content/uploads/2015/03/phpMyAdmin.png>

<img src=http://www.nguyenvanquan7826.com/wp-content/uploads/2015/03/create-database.png>

- Các bạn chú ý là khi tạo csdl chúng ta không đặt passwrod cho nó và user mặc định là root.

##Cài đặt Wordpress

- Truy cập localhost/(tên thư mục tạo trong htdoc)/

<img src=http://www.nguyenvanquan7826.com/wp-content/uploads/2015/03/start-install-wordpress.png>

- Điền thông tin

<img src=http://www.nguyenvanquan7826.com/wp-content/uploads/2015/03/info-blog.png>

<img src=http://www.nguyenvanquan7826.com/wp-content/uploads/2015/03/create-wp-config.png>

- Chạy lệnh `sudo gedit /opt/lampp/htdocs/nguyenvanquan7826/wp-config.php` và paste đoạn copy vào và save lại

<img src=http://www.nguyenvanquan7826.com/wp-content/uploads/2015/03/info-blog1.png>

<img src=http://www.nguyenvanquan7826.com/wp-content/uploads/2015/03/login-blog.png>

- Đăng nhập lại có kết quả:
<img src=http://www.nguyenvanquan7826.com/wp-content/uploads/2015/03/my-blog.png>

Nguồn:
http://www.nguyenvanquan7826.com/2015/03/14/cai-dat-xampp-tren-ubuntu/
http://www.nguyenvanquan7826.com/2015/03/14/cai-wordpress-tren-localhost-trong-ubuntu/
