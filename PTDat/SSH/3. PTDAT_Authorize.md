#Chứng thực và phân quyền người dùng đăng nhập vào SSH.

**Bài toán đặt ra** Nếu như có 2 người muốn truy cập SSH vào máy chủ, chúng ta cần chứng thực từng người và phân quyền khác nhau cho 2 người đó.

##Phương án giải quyết.

- Trước tiên tạo cho 2 người đó 2 user . Đối với người dùng thứ 1 chúng ta cho phép quyền thay đổi sửa xóa , cài đặt thêm các package, reboot và sử dụng quyền root dưới user của anh ta. Với người thứ 2 chúng ta chỉ cho phép anh ta truy cập vào máy chủ với quyền hạn chỉ được phép xem và không được phép làm gì khác, không được phép thay đổi file, reboot máy chủ , cài đặt thêm package,...

##Demo

- Trước tiên ta tạo 2 user, ở đây mình tạo 2 user là `anhdat` và `emhao`

```sh
useradd anhdat
```

và


```sh
useradd emhao
```

- Tuy nhiên mặc định khi tạo user thì chúng chưa có password chúng ta phải đặt password cho chúng.

```sh
passwd [tên user]
```

- Ở đây với user `anhdat` mình đặt password là "anhdat" và với user `emhao` mình đặt password là "emhao"

```sh
passwd anhdat
```

```sh
passwd emhao
```

![scr1](http://i.imgur.com/u7CNmqb.png)

- Khi đã tạo và đặt password xong chúng ta kiểm tra xem 2 user của chúng ta đã được thêm vào chưa. Tất cả user đều được lưu thông tin ở file `/etc/passwd`

```sh
cat /etc/passwd
```
![scr2](http://i.imgur.com/TPOEYd9.png)

- Tiếp theo đó chúng ta thêm quyền sử dụng SHELL cho user. ([SHELL là gì](https://manthang.wordpress.com/2010/11/27/doi-net-ve-chuong-trinh-shell-trong-linux/))

- Dùng trình soạn thảo `vi` để chỉnh sửa file `/etc/passwd` sau đó chỉnh sửa thêm `/bin/bash` vào sau user của chúng ta vừa tạo. Nếu có rồi có thể bỏ trống.

![scr3](http://i.imgur.com/1ktxbtR.png)

- Đối với user `emhao` hiện tại đã có thể truy cập vào máy chủ thực hiện những lệnh thông thường để xem và hiển  thị nhưng không thể : coppy, sửa , xóa ,....
- Đối với user `anhdat` chúng ta cho anh ta quyền có thể dùng lệnh sudo (dùng quyền admin dưới user `anhdat`).
- Để thực hiện được điều này chúng ta thiết lập chủ yếu ở file `/etc/sudoers`.

```sh
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# Host alias specification

# User alias specification

# User privilege specification
root    ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL
```

- Những thông số cần chú ý như sau.

```sh
root	ALL=(ALL:ALL) ALL
```

- Ở đây : 
 <ul>
 <li>root : là user root.</li>
 <li>ALL(1) : Quy tắc này áp dụng trên tất cả các host.</li>
 <li>ALL(2) : User root có thể chạy tất cả các lệnh như tất cả các người dùng.</li>
 <li>ALL(3) : User roor có thể chạy tất cả các lệnh như các nhóm.</li>
 <li>ALL(4) : Áp dụng cho tất cả các lệnh.</li>
 </ul>

Ví dụ : 

```sh
anhdat	ALL=(ALL:ALL) /etc/init.d/ssh restart
```

User `anhdat` trên tất cả các máy có thể mượn tất cả các quyền của người dùng và tất cả các quyền của các nhóm để thực thi lệnh `/etc/init.d/ssh restart`

```sh
%admin ALL=(ALL) ALL
```
- Với `%admin` nghĩa là group `admin`  : nhóm người dùng admin, trên tất cả các máy, có thể mượn quyền tất cả các người dùng, để thực thi tất cả các lệnh.

- OK. Bây giờ đến công việc chính là giúp cho user `anhdat` có thể thực hiện tất cả các quyền của root dưới user `anhdat`. Việc đầu tiên chúng ta tạo một group với tên bất kì, ở đây mình đặt là `ssh`

```sh
groupadd ssh
```

- Sau đó dùng trình soạn thảo vi để sửa file `/etc/sudoers` thêm dòng sau vào file:

```sh
%ssh	ALL=(ALL) ALL
```

- Tiếp theo chúng ta cấp quyền user `anhdat` vào group `ssh`:

```sh
usermod -G ssh anhdat
```
- OK vậy là bây giờ chúng ta đã có thể phân quyền thành công cho từng người. Bây giờ cần tạo 2 key chứng thực RSA để gửi cho 2 người đó mã hóa và đăng nhập vào máy chủ để sử dụng.

[Tạo 2 key cho 2 người sử dụng khác nhau](https://github.com/hocchudong/Thuc-tap-thang-03-2016/blob/master/PTDat/SSH/PTDAT_Cungcapkeycho2nguoidung.md)

##Nguồn : 
- http://thachpham.com/hosting-domain/vps-basic-quan-ly-user-va-sudo.html
- https://support.ssh.com/manuals/server-zos-admin/61/Using_the_z_OS_System_Authorization_Facility.html
- https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centoshttps://help.ubuntu.com/community/RootSudo#Allowing_other_users_to_run_sudo
- https://kythuatmaytinh.wordpress.com/2008/03/21/c%E1%BA%A5p-quy%E1%BB%81n-th%E1%BB%B1c-thi-v%E1%BB%9Bi-sudo/

