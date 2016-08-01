#Cinder Backup

1 Cài đặt cinder-backup

<img src=http://i.imgur.com/K38igmX.png>

command: 
```sh
apt-get install sysfsutils
apt-get install cinder-backup
```

2 Tính năng Scalable Backup Service


##2 Tính năng Scalable Backup Service

Tách 2 dịch vụ cinder-volume và cinder-backup trên 2 note khác nhau.

<img src=http://i.imgur.com/hzoIy5T.png>

Mô hình backup với backend GlusterFS

Trên Storage 1 cài **cinder-volume**

Trên Storage 2 cài **cinder-backup**, ta cài thêm **cinder-volume** và **apt-get install sysfsutils** sau đó stop cinder-volume lại. 

Trường hợp ko cài cinder-volume thì sẽ ko mount đc backend về. 

Log cinder-backup:

<img src=http://i.imgur.com/or6DUUc.png>

Kết quả:

<img src=http://i.imgur.com/jBQTtnR.png>

Backup lỗi khi chưa cài cinder-volume

Backup thành công sau khi cài thêm cinder-volume





