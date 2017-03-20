# Lab thực hành cấu hình KVM với giao diện WebVirt
# Mục lục
### [1. Giới thiệu WebVirt](#intro)
### [2. Mô hình cài đặt](#topo)
### [3. Cài đặt và cấu hình WebVirt](#install)
### [3.1. Cài đặt WebVirtMgr(Web panel)](#web)
### [3.2. Cài đặt host server(server chứa các VM)](#host)
### [4. Sử dụng WebVirt](#features)
### [5. Tham khảo](#ref)
---

## <a name="intro"></a>1. Giới thiệu WebVirt
WebVirtMgr là công cụ quản lý các máy ảo libvirt-based(hỗ trợ tương tác với KVM thông qua libvirt nhờ các API của libvirt) có giao diện nền web. Nó cho phép tạo và cấu hình các domain mới, chỉnh sửa tài nguyên cấp phát cho domain. Ngoài ra WebVirtMgr cũng cung cấp một VNC viewer sử dụng SSH tunnel để truy cập máy ảo thông qua một console đồ họa. Hiện tại WebVirtMgr mới chỉ hỗ trợ KVM.

## <a name="topo"></a>2. Mô hình cài đặt

![topo](http://i.imgur.com/LF8uEMg.jpg)

Mô hình lab bao gồm 2 node(cài đặt dưới dạng máy ảo trên VMWare Workstation)
 
 - __WebVirtMgr host__: Cài đặt WebVirtMgr
 - __Host Server__: Server cài đặt KVM để tạo các máy ảo

Cả hai máy đều cài đặt __ubuntu 14.04 LTS__ và cùng thuộc dải mạng: __172.16.69.0/24__

## <a name="install"></a>3. Cài đặt và cấu hình WebVirt

## <a name="web"></a>3.1. Cài đặt WebVirtMgr(Web panel)
- Cài đặt các gói cần thiết:

```sh
sudo apt-get install git python-pip python-libvirt python-libxml2 novnc supervisor nginx
```

- Cài đặt python và môi trường cho Django:

```sh
cd ~/
git clone git://github.com/retspen/webvirtmgr.git
cd webvirtmgr
sudo pip install -r requirements.txt
./manage.py syncdb
```

Nhập các thông tin cần thiết trong quá trình cài đặt:

```sh
You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): yes (Put: yes)
Username (Leave blank to use 'admin'): admin (Put: your username or login)
E-mail address: username@domain.local (Put: your email)
Password: xxxxxx (Put: your password)
Password (again): xxxxxx (Put: confirm password)
Superuser created successfully.
```

- Cấu hình cho nginx
  - Chuyển thư mục webvirtmgr: `sudo mv ~/webvirtmgr /var/www/webvirtmgr`
  - Thêm file cấu hình cho webvirtmgr: 
  ```sh
  sudo -i

  cat << EOF > /etc/nginx/conf.d/webvirtmgr.conf
  server {
      listen 80 default_server;
  server_name $hostname;
  #access_log /var/log/nginx/webvirtmgr_access_log; 
  
  location /static/ {
      root /var/www/webvirtmgr/webvirtmgr; # or /srv instead of /var
      expires max;
  }
  
  location / {
      proxy_pass http://127.0.0.1:8000;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-for $proxy_add_x_forwarded_for;
      proxy_set_header Host $host:$server_port;
      proxy_set_header X-Forwarded-Proto $scheme;
      proxy_connect_timeout 600;
      proxy_read_timeout 600;
      proxy_send_timeout 600;
      client_max_body_size 1024M; # Set higher depending on your needs 
  }
  
  }
  EOF
  ```

  - Chỉnh sửa lại file cấu hình nginx: `sudo vi /etc/nginx/sites-enabled/default` với nội dung tương tự như sau(comment lại section server):
  ```sh
  #    server {
  #        listen       80 default_server;
  #        server_name  localhost;
  #        root         /usr/share/nginx/html;
  #
  #        #charset koi8-r;
  #
  #        #access_log  /var/log/nginx/host.access.log  main;
  #
  #        # Load configuration files for the default server block.
  #        include /etc/nginx/default.d/*.conf;
  #
  #        location / {
  #        }
  #
  #        # redirect server error pages to the static page /40x.html
  #        #
  #        error_page  404              /404.html;
  #        location = /40x.html {
  #        }
  #
  #        # redirect server error pages to the static page /50x.html
  #        #
  #        error_page   500 502 503 504  /50x.html;
  #        location = /50x.html {
  #        }
  #    }
  ```

  - Khởi động lại nginx: `sudo service nginx restart`
  - Kích hoạt __supervisord__ khi khởi động:
    - Với ubuntu 14.04:
    ```sh
    sudo -i
    curl https://gist.github.com/howthebodyworks/176149/raw/88d0d68c4af22a7474ad1d011659ea2d27e35b8d/supervisord.sh > /etc/init.d/supervisord
    chmod +x /etc/init.d/supervisord
    update-rc.d supervisord defaults
    service supervisord stop
    service supervisord start
    exit
    ```

    - Với ubuntu 16.04:
    ```sh
    sudo systemctl enable supervisor
    sudo systemctl start supervisor
    ```

  - Cấu hình supervisor:
    ```
    sudo -i
    service novnc stop
    insserv -r novnc

    cat << EOF > /etc/insserv/overrides/novnc
    #!/bin/sh
    ### BEGIN INIT INFO
    # Provides:          nova-novncproxy
    # Required-Start:    $network $local_fs $remote_fs $syslog
    # Required-Stop:     $remote_fs
    # Default-Start:     
    # Default-Stop:      
    # Short-Description: Nova NoVNC proxy
    # Description:       Nova NoVNC proxy
    ### END INIT INFO
    EOF

    chown -R www-data:www-data /var/www/webvirtmgr

    cat << EOF > /etc/supervisor/conf.d/webvirtmgr.conf
    [program:webvirtmgr]
    command=/usr/bin/python /var/www/webvirtmgr/manage.py run_gunicorn -c /var/www/webvirtmgr/conf/gunicorn.conf.py
    directory=/var/www/webvirtmgr
    autostart=true
    autorestart=true
    stdout_logfile=/var/log/supervisor/webvirtmgr.log
    redirect_stderr=true
    user=www-data
    
    [program:webvirtmgr-console]
    command=/usr/bin/python /var/www/webvirtmgr/console/webvirtmgr-console
    directory=/var/www/webvirtmgr
    autostart=true
    autorestart=true
    stdout_logfile=/var/log/supervisor/webvirtmgr-console.log
    redirect_stderr=true
    user=www-data
    EOF
    
    sudo service supervisor stop
    sudo service supervisor start
    exit 
    ```

## <a name="host"></a>3.2. Cài đặt host server(server chứa các VM)
- Thao tác này thực hiện trên server host. Trước khi cài đặt KVM lên node này, cần kiểm tra xem bộ xử lý của máy có hỗ trợ ảo hóa không (VT-x hoặc AMD-V). Nếu thực hiện lab trên máy thật cần khởi động lại máy này vào BIOS thiết lập chế độ hỗ trợ ảo hóa. Tuy nhiên bài lab này thực hiện trên VMWare nên trước khi cài đặt cần thiết lập cho máy ảo hỗ trợ ảo hóa như sau: 

![vm](http://i.imgur.com/XwwRHUl.png)

- Cài đặt KVM:

```sh
sudo apt-get install qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils
sudo adduser `id -un` libvirtd
```

- Cấu hình libvirt:

```sh
sudo -i

cat << EOF > /etc/libvirt/libvirtd.conf
listen_tls = 0
listen_tcp = 1
listen_addr = "0.0.0.0"
unix_sock_group = "libvirtd"
unix_sock_ro_perms = "0777"
unix_sock_rw_perms = "0770"
auth_unix_ro = "none"
auth_unix_rw = "none"
auth_tcp = "none"
EOF

cat << EOF > /etc/default/libvirt-bin
start_libvirtd="yes"
libvirtd_opts="-l -d"
EOF

service libvirt-bin restart
```

- Kiểm tra lại việc cài đặt:
```sh
root@ubuntu:~# ps ax | grep [l]ibvirtd
  1638 ?        Sl     1:24 /usr/sbin/libvirtd -l -d
root@ubuntu:~# sudo netstat -pantu | grep libvirtd
tcp        0      0 0.0.0.0:16509           0.0.0.0:*               LISTEN                                                                                              1638/libvirtd
tcp        0      0 172.16.69.136:16509     172.16.69.133:44438     ESTABLISH                                                                                        ED 1638/libvirtd
tcp        0      0 172.16.69.136:16509     172.16.69.133:44418     ESTABLISH                                                                                        ED 1638/libvirtd
tcp        0      0 172.16.69.136:16509     172.16.69.133:44444     ESTABLISH                                                                                        ED 1638/libvirtd
tcp        0      0 172.16.69.136:16509     172.16.69.133:44430     ESTABLISH                                                                                        ED 1638/libvirtd
tcp        0      0 172.16.69.136:16509     172.16.69.133:44448     ESTABLISH                                                                                        ED 1638/libvirtd
root@ubuntu:~# virsh -c qemu+tcp://127.0.0.1/system
Welcome to virsh, the virtualization interactive terminal.
Type:  'help' for help with commands
'quit' to quit


virsh # exit
```

_Chú ý: virsh là một công cụ quản lý máy ảo tương tự như webvirt, virt-manager, etc. nhưng có giao diện dòng lệnh._

_Ba bước tiếp theo có thể bỏ qua_
- Cài đặt OpenvSwitch để thiết lập chế độ Bridge cho các máy ảo KVM: 

```sh
apt-get install -y openvswitch-switch openvswitch-datapath-dkms
```

- Thiết lập tạo thêm bridge `br-ex` và gắn card `eth0` của host vào bridge này:

```sh
ovs-vsctl add-br br-ex
ovs-vsctl add-port br-ex eth0
ifconfig eth0 0
ifconfig br-ex 172.16.69.136/24
route add default gw 172.16.69.1
```

- Cấu hình card `br-ex` trong file: `vi /etc/network/interfaces`

```sh
auto br-ex
iface br-ex inet static
address 172.16.69.136/24
gateway 172.16.69.1
dns-nameservers 8.8.8.8
  
auto eth0
iface eth0 inet manual
  up ifconfig $IFACE 0.0.0.0 up
  up ip link set $IFACE promisc on
  down ip link set $IFACE promisc off
  down ifconfig $IFACE down
```

- Tạo thư mục chứa các images hệ điều hành: `mkdir -p /var/www/webvirtmgr/images`
- Thực hiện upload iso image lên host server sử dụng winscp hoặc scp thông qua một ssh client:

![upload](http://i.imgur.com/yGt7hOy.png)

## <a name="features"></a>4. Sử dụng WebVirt
- Thêm host mới

![add host](http://i.imgur.com/KscFtCF.png)

- Tạo thư mục chứa image các máy ảo và iso các image

![add dir](http://i.imgur.com/xTULGSt.png)
![add dir](http://i.imgur.com/t5eDWOJ.png)

- Thêm bridge

![add bridge](http://i.imgur.com/bi0hVCm.png)

- Tạo máy ảo mới
  - Click vào domain kvm-136 đã khởi tạo như ở trên, chuyển qua tab Storage

  ![storage](http://i.imgur.com/4RHM0CY.png)

  - Click vào nút "Add image", tạo image của hệ điều hành, thiết lập tên, định dạng và kích thước phù hợp

  ![image](http://i.imgur.com/Ms8gtE6.png)

  - Tạo instance(máy ảo) mới 

  ![instance](http://i.imgur.com/bS9IGMi.png)

  - Tùy chỉnh các thông số của máy ảo

  ![mod](http://i.imgur.com/bYj9zI7.png)
  ![mod](http://i.imgur.com/IpNdPBM.png)

  - Chọn file iso để cài đặt hệ điều hành

  ![iso](http://i.imgur.com/9YYnG06.png)

  - Bật máy ảo 

  ![on](http://i.imgur.com/unGOo9Z.png)

  - Bật VNC viewer
  
  ![vnc](http://i.imgur.com/02xFtIY.png)
  ![vnc](http://i.imgur.com/rK6qwTo.png)

## <a name="ref"></a>5. Tham khảo
- [howtoforge](https://www.howtoforge.com/tutorial/kvm-on-ubuntu-14.04/)
- [webvirt](https://github.com/retspen/webvirtmgr)
