#Cinder Backup
Mục lục:

[1 Cài đặt cinder-backup](#1)

[2 Tính năng Scalable Backup Service](#2)

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

Tách 2 dịch vụ cinder-volume và cinder-backup trên 2 note khác nhau.

<img src=http://i.imgur.com/hzoIy5T.png>

Mô hình backup với backend GlusterFS

Trên Storage 1 cài **cinder-volume**

Trên Storage 2 cài **cinder-backup**, ta cài thêm **cinder-volume** và **apt-get install sysfsutils** sau đó stop cinder-volume lại. 

Trường hợp ko cài cinder-volume thì sau khi tạo backup ta sẽ check cinder-backup.log và mount thư mục thủ công. 

Log cinder-backup:

<img src=http://i.imgur.com/or6DUUc.png>

Kết quả:

<img src=http://i.imgur.com/jBQTtnR.png>

Backup lỗi khi chưa cài cinder-volume

Backup thành công sau khi cài thêm cinder-volume





