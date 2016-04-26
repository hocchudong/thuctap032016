#Báo cáo cài đặt UbuntuServer 16.04
##Mục lục

##Cài đặt

-B1: download bộ cài từ trang http://www.ubuntu.com/download/server
 
-B2: cấu hình máy ảo như hình sau

<img src=http://imgur.com/lo4QnEp.png>

-b3: thực hiện như bình thường nếu như máy hỏi chọn card mạng nào chọn card ens33 và để lưu hđh vào ổ 1 thì chọn /dev/sda

<img src=http://imgur.com/lo4QnEp.png>

<img src=http://imgur.com/dPmhtVy.png>

##Cấu hình card mạng

-B1:dùng lệnh `vi` để mở file `/etc/network/interfaces`

`vi /etc/network/interfaces`

-B2:Cấu hình mạng như hình sau:
<ul>
<li>Ở đây ta để ip card VMnet2 là static còn của card NAT là dhcp</li>
<img src=http://imgur.com/0A6J1pz.png>
<li>Cấu hình mạng trước khi cấu hình</li>
<img src=http://imgur.com/8waLjbH.png>
<li>Cấu hình card mạng</li>
<img src=http://imgur.com/0A6J1pz.png>
<li>Kết quả</li>
</ul>

##Cài đặt SSH để dùng Putty

-B1: chạy lênh `sudo apt-get update`

-B2: chạy lệnh `sudo apt-get install ssh`

-B3: đẻ chạy ssh sang putty ta cần chạy lệnh

`vi /etc/ssh/sshd_config`

-B4: Tìm dòng 28: PermitRootLogin thành yes


