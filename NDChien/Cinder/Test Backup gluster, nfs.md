#Test Backup Glusterfs, NFS

Mô hình 3 PC:

1- Controller Note 

2- Storage Note

3- Backend glusterfs hoặc nfs

**Cấu hình**

Chú ý các thư mục lưu trữ cần cấp quyền write. 

Khai báo trong section [DEFAULT]

- Glusterfs 

```sh
backup_driver = cinder.backup.drivers.glusterfs
glusterfs_backup_share = 10.10.10.6:/gluster_cinder_backup
glusterfs_backup_mount_point = /mnt/backup_mount (Thay đổi thư mục mặc định chứa backup)
```

- NFS

```sh
backup_driver = cinder.backup.drivers.nfs
backup_mount_point_base = /mnt/backup_mount
backup_share = 10.10.10.9:/mnt/cinder_backup
```

**Test**

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



