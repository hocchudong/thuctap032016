#Cinder Backup
Mục lục:

[1 Cài đặt cinder-backup](#1)

[2 Tính năng Scalable Backup Service](#2)

[2.1 Scalable Backup + backend GlusterFS](#2.1)

[2.2 Scalable Backup + Backend Volume GlusterFS(Lab-6) + Backend Backup NFS(Lab-9)](#2.2)

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

<a name="2"></a>
##2 Tính năng Scalable Backup Service

Tính năng cho phép tách 2 dịch vụ **cinder-volume** và **cinder-backup** trên 2 note khác nhau.

2.1 Scalable Backup + backend GlusterFS

<img src=http://i.imgur.com/hzoIy5T.png>

Trên Storage 1 cài **cinder-volume**

Trên Storage 2 cài **cinder-backup**, ta cài thêm **cinder-volume** và **apt-get install sysfsutils** sau đó stop cinder-volume lại. 

Trường hợp ko cài cinder-volume thì sẽ phải mount thư mục chứa volume và backup thủ công.

Trường hợp ko cài cinder-volume thì sau khi tạo backup ta sẽ check cinder-backup.log và mount thư mục thủ công. 

Log tạo backup khi chỉ cài cinder-backup. 

<img src=http://i.imgur.com/or6DUUc.png>

- Với NFS

Ko cần đổi quyền volume đc mount về để tạo backup. 

- Với GlusterFS

Phải đổi quyền volume đc mount về để tạo backup. Hạn chế là khi tạo volume mới thì cần quay lại để đổi quyền volume về cho user Cinder. 

<img src=http://i.imgur.com/7WPInzI.png>

2.2 Scalable Backup + Backend Volume GlusterFS(Lab-6) + Backend Backup NFS(Lab-9)

Trường hợp đặt ra: Tạo backup lưu vào NFS(Lab-9) từ volume lưu trên GlusterFS(Lab-6)

<img src=http://i.imgur.com/rA6Tsdu.png>

Kết quả:

Thông tin file backup

<img src=http://i.imgur.com/d3HUHgo.png>

File backup trên NFS(Lab-9)

<img src=http://i.imgur.com/RfZdb6w.png>

2.3 Scalable với multi-backup

Trường hợp đặt ra: Chạy 2 Note cinder-backup và 2 backend lưu backup

<img src=http://i.imgur.com/7r0mYcS.png>

Khi tạo backup thì hệ thống sẽ tự lựa chọn 1 trong 2 note cinder-backup luân phiên nhau. 







