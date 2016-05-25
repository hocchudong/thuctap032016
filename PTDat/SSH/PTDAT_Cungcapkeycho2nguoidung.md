**Chứng thực bằng 2 key cho 2 người khác nhau**

Cấu hình file `/etc/ssh/sshd_config` sửa lại file cấu hình như hình sau :

![1](http://i.imgur.com/tE1PO3Q.png)

- Khởi động lại dịch vụ :

```sh
sudo service ssh restart
```
- Tạo khóa RSA bằng lệnh sau:

```sh
ssh-keygen -t rsa -b 1024
```

- Tại đây ta đặt tên file và mật khẩu cho người thứ nhất muốn truy cập vào máy chủ. Ví dụ ở đây mình đặt người thứ nhất có tên file là `anhdat` và mật khẩu để mở file này là `anhdat`

![scr1](http://i.imgur.com/hjGpEye.png)

- Sau đó ta phân quyền cho 2 file `anhdat` và `anhdat.pub`.

![scr2](http://i.imgur.com/8oq6zPI.png)


- Với người muốn truy cập vào máy chủ thứ 2 mình đặt tên file là `emhao` mật khẩu là `emhao`

![scr3](http://i.imgur.com/jGaWw8T.png)

- Sau đó phân quyền cho 2 file `emhao` và `emhao.pub`.

![scr4](http://i.imgur.com/mZyWM5G.png)

- Sau đó ta mang 2 file `anhdat` và `emhao` về máy và dùng chương trình `puttygen` để load file và tạo ra key để đăng nhập vào máy chủ.

![scr5](http://i.imgur.com/duLRhuk.png)

![scr7](http://i.imgur.com/KmlBXpr.png)
- Sau khi load xong ta lưu lại private key với đuôi `.ppk` 

![scr8](http://i.imgur.com/8wMjkap.png)

- Mở `putty` lên chon phần `SSH` và chon `auth` sau đó mở đường dẫn đến file `.ppk` ta đã lưu lại từ trước đó.

![scr9](http://i.imgur.com/zmoK9eg.png)

- Trở lại phần session điền IP máy chủ và truy cập như bình thường.

![scr6](http://i.imgur.com/WXYsBCk.png)

![scr10](http://i.imgur.com/EDffPF8.png)

**Kết quả thu được**

- Cả 2 key đều đăng nhập vào máy chủ và thao tác bình thường.