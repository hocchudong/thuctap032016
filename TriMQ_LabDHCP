#LAB dịch vụ DHCP

##Mục lục

####[1.Mô hình dịch vụ](#mohinh)
####[2.Triển khai dịch vụ](#trienkhai)
<li>[2.1.Cài đặt card mạng nhận DHCP](#caidat)</li>
<li>[2.2.Cài đặt gói tin DHCP](#goitin)</li>
<li>[2.3.Cấu hình dịch vụ](#cauhinh)</li>
<li>[2.4.Khởi chạy dịch vụ](#khoichay)</li>
####[3.Gán địa chỉ IP cho client theo địa chỉ MAC](#mac)

<a name="mohinh"></a>
####1.Mô hình triển khai:
<img src="">
<ul>
<li>Sử dụng 3 máy: 1 máy Ubuntu server 14.04 (DHCP) có nhiệm vụ cấp phát IP động, 1 máy Ubuntu 14.04 đóng vai trò client nhận IP, máy Window đóng vai trò client.</li>
<li>2 máy Ubuntu 14.04 sẽ được gán 2 card mạng.</li>
</ul>

<a name="trienkhai"></a>
####2.Triển khai dịch vụ:
<a name="caidat"></a>
#####2.1.Cài đặt card mạng cấp phát IP:
Trên máy Ubuntu (DHCP), em cấu hình 2 card mạng và trong đó sử dụng card mạng eth1 là card để cấp phát IP cho các máy client.
```sh
vi /etc/default/isc-dhcp-server
```
<img src="http://i.imgur.com/38qhNID.png">

<a name="goitin"></a>
#####2.2.Cài đặt gói isc-dhcp-server trên máy DHCP để có thể sử dụng dịch vụ DHCP.
```sh
apt-get install -y install isc-dhcp-server
```

<a name="cauhinh"></a>
#####2.3.Cấu hình dịch vụ:
<li>Trên máy DHCP sử dụng lệnh `vi /etc/dhcp/dhcpd.conf`</li>
<li>Trong file cấu hình, sửa lại như sau:</li>
<img src="http://i.imgur.com/ZjcvqPk.png">
<img src="http://i.imgur.com/ZjcvqPk.png">
-Giải thích file cấu hình:
<ul>
<li>subnet 11.0.0.0: Dải mạng cấp IP</li>
<li>netmask 255.255.255.0: Lớp mạng</li>
<li>option routers 11.0.0.1: default gateway của mạng</li>
<li>range 11.0.0.100 11.0.0.200: là khoảng IP dùng để cấp cho client trong giải mạng</li>
<li>option domain-name "hanu.vn": tên domain của mạng.</li>
<li>default-lease-time 600; : Thời gian cấp mặc định là 600 giây</li>
<li>max-lease-time 7200; : Thời gian tối đa cấp IP nếu sau thời gian này không phản hồi tín hiệu thì IP sẽ được cấp cho clients khác trong mạng</li>
<li>ddns-update-style none; : Không cho cập nhật DNS động</li>
<li>authoritative; : Nếu DHCP Server dùng cho mạng cục bộ thì ta nên kích hoạt tính năng authritative</li>
<li>log-facility local7; file log.</li>
</ul>
-Trên máy Ubuntu client, cấu hình cho card mạng eth1 nhận IP động:
<li>Sửa file interfaces</li>

```sh
vi /etc/network/interfaces
```
<li>Ta sửa như sau</li>
<img src="http://i.imgur.com/AK1nmFT.png">

<a name="khoichay"></a>
#####2.4.Khởi chạy dịch vụ:
Sử dụng lệnh:
```sh
service isc-dhcp-server restart
```
-Sau khi khởi chạy dịch vụ, kiểm tra IP trên 2 máy client:
<ul>
<li>Trên Ubuntu</li>
<img src="http://i.imgur.com/WzXYAN3.png">
<li>Trên máy Window 7</li>
<img src="http://i.imgur.com/YMsCtxa.png">
</ul>

<a name="mac"></a>
####3.Gán địa chỉ IP cho client theo địa chỉ MAC:
-Trên máy DHCP sửa file dhcpd.conf
<li>sử dụng lệnh</li>
```sh
vi /etc/dhcp/dhcp/dhcpd.conf
```
<li>sửa file cấu hình như sau</li>
<img src="http://i.imgur.com/Pw6PAgy.png">
Giải thích file cấu hình:
<li>hardware ethernet 00:0c:29:ca:6c:d0; :địa chỉ MAC của máy mà ta muốn gán IP</li>
<li>fixed-address 11.0.0.110; : địa chỉ IP mà ta muốn gán</li>









