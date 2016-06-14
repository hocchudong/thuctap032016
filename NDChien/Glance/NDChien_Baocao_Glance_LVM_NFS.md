#Triển Khai Glance + LVM + NFS

Mô hình

<img src=http://i.imgur.com/xESEmq3.png>

Vấn đề đặt ra:

1- Người quản trị muốn lưu image của Glance sang 1 thư mục khác và lên 1 ổ cứng mới trên PC Controller.

2- Các image sẽ được mount tới PC NFS.

**PC Controller:** 

- Thêm 1 ổ cứng mới. Triển khai LVM và mount tới thư mục /mnt/nfsshare_glance

<img src=http://i.imgur.com/EiQUvBY.png>

- Chỉnh đường dẫn lưu image của Glance tới `/mnt/nfsshare_glance` . Phân quyền cho /mnt/nfsshare_glance thuộc user `glance` . Khởi động lại dịch vụ Glance

<img src=http://i.imgur.com/c8rr9TQ.png>

- Upload image

<img src=http://i.imgur.com/HDaGPXw.png>

- Cài dịch vụ NFS-Server lên controller

`apt-get -y install nfs-kernel-server`

- Chỉnh sửa file **exportfs** cho phép mount thư mục **/mnt/nfsshare_glance** tới dải 10.10.10.0/24

`/mnt/nfsnfsshare_glance        10.10.10.0/24(rw,no_root_squash)`

- Khởi động lại NFS

`/etc/init.d/nfs-kernel-server restart`

**PC NFS**:

- Cài đặt NFS client

`apt-get  -y install nfs-common`

- Tạo thư mục /mnt/glance_image  

<img src=http://i.imgur.com/2xFlWmn.png>

- mount /mnt/nfsshare_glance từ PC Controller về thư mục vừa tạo

`mount 10.10.10.40:/mnt/nfsshare_glance /mnt/glance_image`

- Dùng lệnh **df -h** để kiểm tra

<img src=http://i.imgur.com/dE8W481.png>
