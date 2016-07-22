#Multi-backends và tính năng Oversubscription in thin provisioning trên LVM
**Mục lục:**

[1 Triển khai multi-backends](#1)

[2 Tính năng Oversubscription in thin provisioning trên LVM](#2)

==========================

<a name="1"></a>
###1 Triển khai multi-backends

<img src=http://i.imgur.com/TpE8mSB.png>

Tham khảo các bước cấu hình: https://www.server-world.info/en/note?os=Ubuntu_14.04&p=openstack_liberty2&f=2

Các backends chạy các dịch vụ server còn trên Cinder ta chạy các dịch vụ client

Ví dụ file cấu hình trên storage Cinder: /etc/cinder/cinder.config
```sh
[DEFAULT]
rootwrap_config = /etc/cinder/rootwrap.conf
api_paste_confg = /etc/cinder/api-paste.ini
iscsi_helper = tgtadm
volume_name_template = volume-%s
volume_group = cinder-volumes
verbose = True
auth_strategy = keystone
state_path = /var/lib/cinder
lock_path = /var/lock/cinder
volumes_dir = /var/lib/cinder/volumes
rpc_backend = rabbit
auth_strategy = keystone
my_ip = 10.10.10.42
enabled_backends = lvm,lvm1,nfs,glusterfs
glance_api_servers = http://controller:9292

[database]
connection = mysql+pymysql://cinder:Welcome123@controller/cinder

[oslo_messaging_rabbit]
rabbit_host = controller
rabbit_userid = openstack
rabbit_password = Welcome123

[keystone_authtoken]
auth_uri = http://controller:5000
auth_url = http://controller:35357
memcached_servers = controller:11211
auth_type = password
project_domain_name = default
user_domain_name = default
project_name = service
username = cinder
password = Welcome123

[lvm1]
volume_driver = cinder.volume.drivers.lvm.LVMVolumeDriver
volume_group = cinder-volumes-1
iscsi_protocol = iscsi
iscsi_helper = tgtadm
volume_backend_name=LVM

[lvm]
volume_driver = cinder.volume.drivers.lvm.LVMVolumeDriver
volume_group = cinder-volumes
iscsi_protocol = iscsi
iscsi_helper = tgtadm
volume_backend_name=LVM-1

[nfs]
volume_driver = cinder.volume.drivers.nfs.NfsDriver
nfs_shares_config = /etc/cinder/nfsshares
volume_backend_name = NFS

[glusterfs]
volume_driver = cinder.volume.drivers.glusterfs.GlusterfsDriver
volume_backend_name = GlusterFS
glusterfs_shares_config = /etc/cinder/glusterfs_shares

[oslo_concurrency]
lock_path = /var/lib/cinder/tmp
```

Trên file cấu hình, ta khai báo:
```sh
enabled_backends = .... (Các backends muốn sử dụng)
my_ip (địa chỉ storage)
```

Các section như [lvm], [nfs] (Khai báo thông số backends)

Trên [nfs] vào [glusterfs] có thêm khai báo tới tập tin chứa đường dẫn backends 

Ví dụ: nfs_shares_config = /etc/cinder/nfsshares 

<a name="2"></a>
###2 Tính năng Oversubscription in thin provisioning trên LVM


Khai báo vào section [lvm]
```sh
lvm_type = thin 
lvm_max_over_subscription _ratio = Mức độ muốn tăng lên ví dụ 2.0 3.5 ...
```

Kết quả:

<img src=





