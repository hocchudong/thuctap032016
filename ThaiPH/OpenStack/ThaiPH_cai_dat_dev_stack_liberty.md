# Cài đặt DevStack Liberty AIO
# Mục lục
<h3><a href="#preparation">1. Chuẩn bị</a></h3>
<h3><a href="#config">2. Cài đặt và cấu hình</a></h3>

---

<h2><a name="preparation">1. Chuẩn bị</a></h2>
<div>
<ul>
    <li>Máy ảo cài ubuntu server 14.04. Tải <a href="http://releases.ubuntu.com/14.04/ubuntu-14.04.4-server-amd64.iso">image ubuntu server 14.04.</a></li>
    <li>Yêu cầu của máy ảo ubuntu 14.04
    <ul>
        <li>RAM: cỡ 4GB hoặc hơn</li>
        <li>Ổ cứng: cỡ 60GB hoặc hơn, có thể thiết lập 2 ổ
        </li>
        <li>Network: 2 card mạng
            <ul>
                <li><b>eth0</b>: Chế độ NAT, thiết lập trước trong VMWare dải NAT với địa chỉ: 172.16.69.0/24</li>
                <li><b>eth1</b>: Chế độ Host Only, thiết lập trước trong VMWare dải Host Only (ở đây sử dụng dải VMNet2), với địa chỉ: 10.10.10.0/24</li>
            </ul>
        <br><br>
        <img src="http://i.imgur.com/QiBtSu2.png">
        <br><br>        
        Sau khi cài xong máy tiến hành cấu hình hai card mạng cho máy ảo như sau:
<pre>
    <code>
# mo file cau hinh network
vi /etc/network/interfaces

# doi noi dung file nhu sau
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth1
iface eth1 inet static
address 10.10.10.173/24

auto eth0
iface eth0 inet static
address 172.16.69.174/24
gateway 172.16.69.1
dns-nameservers 8.8.8.8
    </code>
</pre>
        </li>
        <li>CPU: chuẩn bị 4 CPU core, kích hoạt chế độ hỗ trợ ảo hóa VT-X và AMD-V của CPU.
        <br><br>
        <img src="http://i.imgur.com/sVaxtFN.png">
        <br><br>            
        </li>
    </ul>
    </li>
</ul>
</div>
<h2><a name="config">2. Cài đặt và cấu hình</a></h2>
<div>
    <ul>
        <li><b>Bước 1: </b>
Đăng nhập với tài khoản root rồi thực hiện update hệ thống:
<pre>
<code>
apt-get update && apt-get dist-upgrade -y
</code>
</pre>
        </li>
        <li>
<b>Bước 2: </b>
Tạo tài khoản <b>stack</b> rồi gán quyền <b>sudoer</b> cho người dùng <b>stack</b>
<pre>
    <code>
adduser stack
echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
    </code>
</pre>       
        </li>

        <li><b>Bước 3: </b>
Cài đặt <b>git</b>, chuyển qua tài khoản <b>stack</b> rồi clone mã nguồn devstack bản Liberty về:
<pre>
    <code>
apt-get -y install git
su - stack
git clone -b stable/liberty https://github.com/openstack-dev/devstack.git
    </code>
</pre>            
        </li>

        <li><b>Bước 4: </b> Tạo file <b>local.conf.</b> File <b>local.conf</b> định nghĩa các cấu hình mà các shell trong devstack sẽ sử dụng để cài đặt hệ thống. Tùy theo nhu cầu của người dùng mà định nghĩa file này khác nhau. Ở đây chủ yếu quan tâm tới việc thiết lập mật khẩu cho các dịch vụ, thiết lập network theo mô hình <b>self-service</b> cho hệ thống. Theo như mô hình cài đặt sau đây, cần chú ý hai dải network:
        <ul>
            <li><b>Internal: </b>Dải này là dải địa chỉ private cung cấp cho các máy ảo. Ở đây sử dụng dải <code>10.0.0.0/24</code></li>
            <li><b>External: </b>Hay dải <b>provider network</b>. Dải này cung cấp floating IP để NAT địa chỉ private của các máy ảo sang, cung cấp kết nối internet cho các máy ảo. Ở đây chính là dải: <code>172.16.69.0/24</code></li>
        </ul>

        Tạo file <code>vi local.conf</code> với nội dung như sau:
        <pre>
            <code>
[[local|localrc]]
DEST=/opt/stack

# Khai bao log cho devstack
LOGFILE=$DEST/logs/stack.sh.log
VERBOSE=True
SCREEN_LOGDIR=$DEST/logs/screen
OFFLINE=False

# Khai bao IP cua may cai dat devstack
HOST_IP=172.16.69.174

# Khai bao mat khau cho cac dich vu
ADMIN_PASSWORD=Welcome123
MYSQL_PASSWORD=Welcome123
RABBIT_PASSWORD=Welcome123
SERVICE_PASSWORD=Welcome123
SERVICE_TOKEN=Welcome123


disable_service n-net
enable_service q-svc
enable_service q-agt
enable_service q-dhcp
enable_service q-meta
enable_service q-l3

#ml2
Q_PLUGIN=ml2
Q_AGENT=openvswitch

# vxlan
Q_ML2_TENANT_NETWORK_TYPE=vxlan

# Networking
FLOATING_RANGE=172.16.69.0/24
Q_FLOATING_ALLOCATION_POOL=start=172.16.69.210,end=172.16.69.240
PUBLIC_NETWORK_GATEWAY=172.16.69.1

FIXED_RANGE=10.0.0.0/24
NETWORK_GATEWAY=10.0.0.1

PUBLIC_INTERFACE=eth0

Q_USE_PROVIDERNET_FOR_PUBLIC=True
Q_L3_ENABLED=True
Q_USE_SECGROUP=True
OVS_PHYSICAL_BRIDGE=br-ex
PUBLIC_BRIDGE=br-ex
OVS_BRIDGE_MAPPINGS=public:br-ex


# Neu dung de dev thi thay enable_service cho dong duoi
disable_service tempest


#vnc
enable_service n-novnc
enable_service n-cauth
            </code>
        </pre>
        </li>

        <li>
        <b>Bước 5: </b>
        Đảm bảo bạn đang ở thư mục <code>/home/stack/devstack</code>. Thực hiện lệnh sau để cài devstack:
<pre>
    <code>
./stack.sh  
    </code>
</pre>      
Sau khi cài đặt xong, truy cập devstack trên trình duyệt qua địa chỉ <code>http://172.16.69.174/dashboard</code>      
        </li>
        <li>
            <b>Chú ý: </b> Khi khởi động lại devstack cần chuyển sang tài khoản <b>stack</b>, chuyển qua thư mục <code>cd /home/stack/devstack</code>. Thực hiện các lệnh sau để khởi động các dịch vụ của devstack:
            <pre>
                <code>
# fix loi network
ifconfig eth0 0
ifconfig br-ex 172.16.69.174/24
route add default gw 172.16.69.1

# fix loi cinder
sudo losetup /dev/loop0 /opt/stack/data/stack-volumes-default-backing-file
sudo losetup /dev/loop1 /opt/stack/data/stack-volumes-lvmdriver-1-backing-file
# rejoin stack
sudo ./rejoin-stack.sh
                </code>
            </pre>
        </li>
    </ul>
</div>
