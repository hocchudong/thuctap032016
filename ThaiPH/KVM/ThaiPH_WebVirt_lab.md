# Lab thực hành cấu hình KVM với giao diện WebVirt
#Mục lục
<h3><a href="#intro">1. Giới thiệu WebVirt</a></h3>
<h3><a href="#topo">2. Mô hình lab</a></h3>
<h3><a href="#install">3. Cài đặt và cấu hình WebVirt</a></h3>
<ul>
<li><a href="#web">3.1. Cài đặt WebVirtMgr(Web panel)</a></li>
<li><a href="#host">3.2. Cài đặt host server(server chứa các VM)</a></li>
</ul>

<h3><a href="#features">4. Sử dụng WebVirt</a></h3>
<h3><a href="#ref">5. Tham khảo</a></h3>

---

<h2><a name="intro">1. Giới thiệu WebVirt</a></h2>
<div>
WebVirtMgr là công cụ quản lý các máy ảo libvirt-based(hỗ trợ tương tác với KVM thông qua libvirt nhờ các API của libvirt) có giao diện nền web. Nó cho phép tạo và cấu hình các domain mới, chỉnh sửa tài nguyên cấp phát cho domain. Ngoài ra WebVirtMgr cũng cung cấp một VNC viewer sử dụng SSH tunnel để truy cập máy ảo thông qua một console đồ họa. Hiện tại WebVirtMgr mới chỉ hỗ trợ KVM.
</div>
<h2><a name="topo">2. Mô hình lab</a></h2>
<div>
<img src="http://i.imgur.com/LF8uEMg.jpg"/>
<br><br>
Mô hình lab bao gồm 2 node(cài đặt dưới dạng máy ảo trên VMWare Workstation)
<ul>
<li><b>WebVirtMgr host:</b> Cài đặt WebVirtMgr</li>
<li><b>Host Server</b>: Server cài đặt KVM để tạo các máy ảo</li>
</ul>
Cả hai máy đều cài đặt <b>ubuntu 14.04 LTS</b> và cùng thuộc dải mạng: <b>172.16.69.0/24</b>
</div>
<h2><a name="install">3. Cài đặt và cấu hình WebVirt</a></h2>
<ul>
<li><h3><a name="web">3.1. Cài đặt WebVirtMgr(Web panel)</a></h3>
<div>
<ul>
<li>Cài đặt các gói cần thiết:
<pre>
<code>
sudo apt-get install git python-pip python-libvirt python-libxml2 novnc supervisor nginx
</code>
</pre>
</li>
<li>Cài đặt python và môi trường cho Django:
<pre>
<code>
cd ~/
git clone git://github.com/retspen/webvirtmgr.git
cd webvirtmgr
sudo pip install -r requirements.txt
./manage.py syncdb
</code>
</pre>
Nhập các thông tin cần thiết trong quá trình cài đặt:
<pre>
<code>
You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): yes (Put: yes)
Username (Leave blank to use 'admin'): admin (Put: your username or login)
E-mail address: username@domain.local (Put: your email)
Password: xxxxxx (Put: your password)
Password (again): xxxxxx (Put: confirm password)
Superuser created successfully.
</code>
</pre>
</li>
<li>Cấu hình cho nginx
<ul>

<li>Chuyển thư mục webvirtmgr:
<pre> 
<code>
sudo mv ~/webvirtmgr /var/www/webvirtmgr
</code>
</pre>
</li>

<li>Thêm file cấu hình cho webvirtmgr: <code>sudo vim /etc/nginx/conf.d/webvirtmgr.conf</code>  với nội dung như bên dưới
<pre>
<code>
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
</code>
</pre>
</li> 
<li>Chỉnh sửa lại file cấu hình nginx: <code>sudo vim /etc/nginx/sites-enabled/default</code> với nội dung tương tự như sau(comment lại section <code>server</code>):
<pre>
<code>
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
</code>
</pre>

</li> 

<li>Khởi động lại nginx: <code>sudo service nginx restart</code></li>
<li>Kích hoạt <code>supervisord</code> khi khởi động:
<ul>
<li>Với Ubuntu 14.04:
<pre>
<code>
sudo -i
curl https://gist.github.com/howthebodyworks/176149/raw/88d0d68c4af22a7474ad1d011659ea2d27e35b8d/supervisord.sh > /etc/init.d/supervisord
chmod +x /etc/init.d/supervisord
update-rc.d supervisord defaults
service supervisord stop
service supervisord start
exit
</code>
</pre>
</li>
<li>Với Ubuntu 16.04:
<pre>
<code>
sudo systemctl enable supervisor
sudo systemctl start supervisor
</code>
</pre>
</li>
</ul>
</li>



</ul>

</li>

<li>Cấu hình supervisor:
<pre>
<code>
sudo service novnc stop
sudo insserv -r novnc
sudo vi /etc/insserv/overrides/novnc
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
sudo chown -R www-data:www-data /var/www/webvirtmgr
</code>
</pre>
Tạo file: <code>sudo vim /etc/supervisor/conf.d/webvirtmgr.conf</code> với nội dung như sau:
<pre>
<code>
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
</code>
</pre>

Khởi động lại supervisor:
<pre>
<code>
sudo service supervisor stop
sudo service supervisor start
</code>
</pre>
</li>
</ul>
</div>
</li>
<li><h3><a name="host">3.2. Cài đặt host server(server chứa các VM)</a></h3>
<ul>
<li>
Thao tác này thực hiện trên server host. Trước khi cài đặt KVM lên node này, cần kiểm tra xem bộ xử lý của máy có hỗ trợ ảo hóa không (VT-x hoặc AMD-V). Nếu thực hiện lab trên máy thật cần khởi động lại máy này vào BIOS thiết lập chế độ hỗ trợ ảo hóa. Tuy nhiên bài lab này thực hiện trên VMWare nên trước khi cài đặt cần thiết lập cho máy ảo hỗ trợ ảo hóa như sau:
<br><br>
<img src="http://i.imgur.com/XwwRHUl.png"/>
<br><br>
</li>
<li>
Cài đặt KVM:
<pre>
<code>sudo apt-get install qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils</code>
</pre>
Thêm người dùng hiện tại vào group <b>libvirtd:</b>
<pre>
<code>sudo adduser `id -un` libvirtd</code>
</pre>
</li>
<li>Tiến hành cấu hình libvirt:
<ul>
<li>Mở file <code>vi /etc/libvirt/libvirtd.conf</code>. Uncomment và chỉnh sửa lại các dòng với giá trị như dưới đây:
<pre>
<code>
listen_tls = 0
listen_tcp = 1
listen_addr = "0.0.0.0"
auth_tcp = "none"
</code>
</pre>
</li>
<li>Mở file <code>vi /etc/default/libvirt-bin</code>. Chỉnh sửa lại như sau:
<pre>
<code>
libvirtd_opts="-l -d"
</code>
</pre>
</li>
</ul>
</li>
<li>Kiểm tra lại việc cài đặt
<pre>
<code>
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
</code>
</pre>
<i>Chú ý: <b>virsh</b> là một công cụ quản lý máy ảo tương tự như webvirt, virt-manager, etc. nhưng có giao diện dòng lệnh.</i>
</li>

<li>Cài đặt OpenvSwitch để thiết lập chế độ Bridge cho các máy ảo KVM
<pre>
<code>
apt-get install -y openvswitch-switch openvswitch-datapath-dkms
</code>
</pre>
</li>

<li>Thiết lập tạo thêm bridge <code>br-ex</code> và gắn card eth0 của host vào bridge này:
<pre>
<code>
ovs-vsctl add-br br-ex
ovs-vsctl add-port br-ex eth0
</code>
</pre>
Kết quả sẽ tương tự như sau:
<pre>
<code>
root@ubuntu:~# ovs-vsctl add-br br-ex
root@ubuntu:~# ovs-vsctl add-port br-ex eth0
root@ubuntu:~# ovs-vsctl show
e157d0df-54b9-4092-9eb7-3f5b6becb6e6
    Bridge br-ex
        Port "eth0"
            Interface "eth0"
        Port br-ex
            Interface br-ex
                type: internal
    ovs_version: "2.0.2"
</code>
</pre>
</li>
<li>Cấu hình card br-ex trong file: <code>vi /etc/network/interfaces</code>:
<pre>
<code>
auto br-ex
iface br-ex inet static
address 172.16.69.136/24
gateway 172.16.69.1
dns-nameservers 8.8.8.8
bridge_ports eth0
bridge_fd 9
bridge_hello 2
bridge_maxage 12
bridge_stp off

auto eth0
iface eth0 inet manual
up ip link set dev $IFACE up
down ip link set dev $IFACE down
</code>
</pre>
</li>

<li>Tạo thư mục chứa các images hệ điều hành:
<pre>
<code>
mkdir -p /var/www/webvirtmgr/images
</code>
</pre>
</li>

<li>Thực hiện upload iso image lên 
host server sử dụng winscp hoặc scp thông qua một ssh client.
<br><br><img src="http://i.imgur.com/yGt7hOy.png"/><br><br>
</li>

</ul>

</li>

</ul>

<h2><a name="features">4. Sử dụng WebVirt</a></h2>
<div>
<ul>
<li><h3>a. Thêm host mới</h3>
<br><br>
<img src="http://i.imgur.com/KscFtCF.png"/>
<br><br>
</li>
<li><h3>b. Tạo thư mục chứa image các máy ảo và iso các image</h3>
<br><br>
<img src="http://i.imgur.com/xTULGSt.png"/>
<br><br>
<img src="http://i.imgur.com/t5eDWOJ.png"/>
<br><br>
</li>
<li><h3>c. Thêm bridge</h3>
<br><br>
<img src="http://i.imgur.com/bi0hVCm.png"/>
<br><br>
</li>
<li><h3>d. Tạo máy ảo mới</h3>
Click vào domain kvm-136 đã khởi tạo như ở trên, chuyển qua tab <code>Storage</code>
<br><br>
<img src="http://i.imgur.com/4RHM0CY.png"/>
<br><br>
Click vào nút "Add image", tạo image của hệ điều hành, thiết lập tên, định dạng và kích thước phù hợp:
<br><br>
<img src="http://i.imgur.com/Ms8gtE6.png"/>
<br><br>
Tạo instance(máy ảo) mới:
<br><br>
<img src="http://i.imgur.com/bS9IGMi.png"/>
<br><br>
Tùy chỉnh các thông số của máy ảo:
<br><br>
<img src="http://i.imgur.com/bYj9zI7.png"/>
<br><br>
<br><br>
<img src="http://i.imgur.com/IpNdPBM.png"/>
<br><br>
Chọn file iso để cài đặt hệ điều hành:
<br><br>
<img src="http://i.imgur.com/9YYnG06.png"/>
<br><br>
Bật máy ảo
<br><br>
<img src="http://i.imgur.com/unGOo9Z.png"/>
<br><br>
Bật VNC viewer:
<br><br>
<img src="http://i.imgur.com/02xFtIY.png"/>
<img src="http://i.imgur.com/rK6qwTo.png"/>
<br><br>
</li>
</ul>
</div>
<h2><a name="ref">5. Tham khảo</a></h3>
<div>
[1] - <a href="https://www.howtoforge.com/tutorial/kvm-on-ubuntu-14.04/">https://www.howtoforge.com/tutorial/kvm-on-ubuntu-14.04/</a>
<br>
[2] - <a href="https://github.com/retspen/webvirtmgr">https://github.com/retspen/webvirtmgr</a>
<br>
[3] - <a href="https://github.com/caongocuy/Install-Webvirtmgr-KVM-simple">https://github.com/caongocuy/Install-Webvirtmgr-KVM-simple</a>
</div>

