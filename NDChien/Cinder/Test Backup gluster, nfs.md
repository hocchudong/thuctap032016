#Test Backup Glusterfs, NFS

*Cấu hình*

- Glusterfs 

```sh
backup_driver = cinder.backup.drivers.glusterfs
glusterfs_backup_share = 10.10.10.6:/gluster_cinder_backup
glusterfs_backup_mount_point = /mnt/backup_mount
```

- NFS

```sh
backup_driver = cinder.backup.drivers.nfs
backup_mount_point_base = /mnt/backup_mount
backup_share = 10.10.10.9:/mnt/cinder_backup
```

*Test*

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
Nhận xét: Mức độ ram tiêu thụ của service cinder_backup lớn hơn dung lượng volume backup.


