#Cinder Backup
Mục lục:

[1 Cài đặt cinder-backup](#1)

[2 Tính năng Scalable Backup Service](#2)

- [2.1 Scalable Backup + backend GlusterFS](#2.1)

- [2.2 Scalable Backup + Backend Volume GlusterFS(Lab-6) + Backend Backup NFS(Lab-9)](#2.2)

- [2.3 Scalable với multi-backup](#2.3)

===========================

<a name="1"></a>
##1 Cài đặt cinder-backup

Cài đặt trên Storage đã cài cinder-volume 

<img src=http://i.imgur.com/K38igmX.png>

Mô hình

command: 
```sh
apt-get install sysfsutils
apt-get install cinder-backup
```

File cấu hình **/etc/cinder/cinder.conf**

Thêm cấu hình backup vào section [DEFAULT]

- Với backend Glusterfs 
```sh
backup_driver = cinder.backup.drivers.glusterfs
glusterfs_backup_share = 10.10.10.6:/gluster_cinder_backup
glusterfs_backup_mount_point = /mnt/backup_mount
```

`10.10.10.6:/gluster_cinder_backup` Địa chỉ backend và volume gluster lưu trữ backup.

`/mnt/backup_mount` Thư mục mount Volume cinder về để tạo backup(Có thể ko cần, mặc định Volume được mount về /var/lib/cinder/mnt/.....). 

- Với backend NFS
```sh
backup_driver = cinder.backup.drivers.nfs
backup_mount_point_base = /mnt/backup_mount
backup_share = 10.10.10.9:/mnt/cinder_backup
```

Note: Nếu cấu hình backup cả GlusterFS và NFS trên cùng 1 máy cinder_backup thì backup chỉ nhận cấu hình backup bên dưới. 

Ví dụ bên dưới, máy chỉ nhận backup về NFS

<img src=http://i.imgur.com/uD9nWfU.png>

Command create backup:

<img src=http://i.imgur.com/e4kVjjc.png>

Ví dụ: cinder backup-create --name backup-volume1 volume1


<a name="2"></a>
##2 Tính năng Scalable Backup Service

Tính năng cho phép tách 2 dịch vụ **cinder-volume** và **cinder-backup** trên 2 note khác nhau.

<a name="2.1"></a>
###2.1 Scalable Backup + backend GlusterFS

<img src=http://i.imgur.com/hzoIy5T.png>

Trên Storage 1 cài **cinder-volume**

Trên Storage 2 cài **cinder-backup**, ta cài thêm **cinder-volume** và **apt-get install sysfsutils** sau đó stop cinder-volume lại. 

Trường hợp ko cài cinder-volume thì sẽ phải mount thư mục chứa volume, backup thủ công bằng lệnh. Sau khi tạo backup ta sẽ check cinder-backup.log và mount thư mục.

Log tạo backup khi chỉ cài cinder-backup. 

<img src=http://i.imgur.com/or6DUUc.png>

- Với Volume trên NFS

Ko cần đổi quyền volume đc mount về để tạo backup. 

- Với Volume trên GlusterFS

Phải đổi quyền volume đc mount về để tạo backup. Hạn chế là khi tạo volume mới thì cần quay lại để đổi quyền volume về cho user Cinder. 

<img src=http://i.imgur.com/7WPInzI.png>

<a name="2.2"></a>
###2.2 Scalable Backup + Backend Volume GlusterFS(Lab-6) + Backend Backup NFS(Lab-9)

Trường hợp đặt ra: Tạo backup lưu vào NFS(Lab-9) từ volume lưu trên GlusterFS(Lab-6)

<img src=http://i.imgur.com/rA6Tsdu.png>

Kết quả:

Thông tin file backup

<img src=http://i.imgur.com/d3HUHgo.png>

File backup trên NFS(Lab-9)

<img src=http://i.imgur.com/RfZdb6w.png>

<a name="2.3"></a>
###2.3 Scalable với multi-backup

Trường hợp đặt ra: Chạy 2 Note cinder-backup và 2 backend lưu trữ backup

<img src=http://i.imgur.com/7r0mYcS.png>

Khi tạo backup thì hệ thống sẽ tự lựa chọn 1 trong 2 note cinder-backup luân phiên nhau. 







