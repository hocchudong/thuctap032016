#Test Backup với Glusterfs, NFS. Snapshot Instance,volume
Mục lục:

[1 Backup với Glusterfs, NFS](#1)

[2 Snapshot Instance,volume](#2)


<a name="1"></a>

##1 Backup với Glusterfs, NFS

Command: 

cinder backup-create [--incremental] [--force] VOLUME

**Test:**

- GlusterFS

Backend 20GB replicate

Storage Note ram 2GB

```sh
1- backup 1GB volume trống - OK
2- backup 3GB volume trống - Error memory 
3- backup 2GB volume trống - Error memory
4- backup 1GB volume chứa image 12mb - Error memory
```

- NFS

Backend 20GB

Storage Note ram 3GB

```sh
1- backup 1GB volume trống - OK
2- backup 2GB volume trống - Error memory
3- backup 1GB volume chứa image 12mb - OK
```
Nhận xét: Mức độ tiêu thụ ram của service cinder_backup lớn hơn dung lượng volume cần backup.


<a name="2"></a>

##2 Snapshot Instance,volume

**Check: NFS ko có tính năng snapshot**

<img src=http://i.imgur.com/VXaGmR8.png>

####2.1 Backend GlusterFS 

* Volume

Command:

`cinder snapshot-create volume`

Snapshot thành công sẽ có 2 file chứa cùng 1 thư mục với volume. Dung lượng 200K và 4k

Snapshot lỗi sẽ có 1 file 200k đc tạo ra.

Từ snapshot có thể tạo volume mới. 

**Test:**
```sh
1- Volume rỗng, status available - OK
2- Volume chứa image, status available - OK
3- Volume chứa image, status: in-use - Fault
```

* Instance

Command: nova image-create --poll myInstance myInstanceSnapshot

**Test:**
```sh
1- Instance create from image, status: Running,SHUTOFF - OK
2- Instance create from volume, status: Running,SHUTOFF - fault
```

####2.2 Backend LVM

* Volume

`1- Volume attack instance, status: in-use - OK`

* Instance
```sh
1- Instance create from volume, status Running - OK -> volume snapshot
2- Instance create from image, status Running - OK -> image
```












