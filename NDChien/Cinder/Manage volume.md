Manage_Volume

Backup volume

Có 3 loại backup: Full, incremental, deincremental
Bản backup đầu tiên phải là full backup. 


cinder backup-create [--incremental] [--force] VOLUME

Ko có [--force], volume chỉ đc backup ở trạng thái available. 
Với [--force], volume có thể backup ở trạng thái available hoặc in-use. 
(Nếu ở trạng thái in-use, backup volume có thể crash)

cinder backup-list
cinder backup-restore BACKUP_ID



Manage snapshoot

cinder snapshot-manage VOLUME_ID IDENTIFIER --id-type ID-TYPE \
  --name NAME --description DESCRIPTION --metadata METADATA
  
