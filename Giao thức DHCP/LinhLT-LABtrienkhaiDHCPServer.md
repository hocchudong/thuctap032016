#LAB triển khai DHCP

#Mục lục
* [1. Mô hình](#mo_hinh)
* [2. Các bước thực hiện](#cac_buoc_thuc_hien)
	* [2.1 Cài đặt gói isc-dhcp-server](#cai_dat_isc)
	* [2.2 Cấu hình DHCP Server](#cau_hinh)
	* [2.3 Khởi chạy dịch vụ](#chay)
* [3. Kết quả](#ket_qua)
<a name="mo_hinh"></a>
#1. Mô hình
![](http://i.imgur.com/7udOnmc.jpg)

* DHCP server chạy trên hệ điều hành Ubuntu server 14.04, sử dụng gói phần mềm isc-dhcp-server để chạy DHCP server. Địa chỉ ip: 10.10.20.2/24
* Có 2 client sử dụng 2 hệ điều hành là WinXP và Ubuntu Server 14.04, sử dụng dịch vụ dhcp để nhận địa chỉ ip.

<a name="cac_buoc_thuc_hien"></a>
#2. Các bước thực hiện

<a name="cai_dat_isc"></a>
##2.1 Cài đặt gói isc-dhcp-server để triển khai dịch vụ DHCP Server.
```sh
apt-get install -y install isc-dhcp-server 
```
<a name="cau_hinh"></a>
##2.2 Cấu hình DHCP Server
* Đường dẫn file cấu hình: `/etc/dhcp/dhcpd.conf`
* Nội dung file cấu hình
```sh
# The ddns-updates-style parameter controls whether or not the server will
# attempt to do a DNS update when a lease is confirmed. We default to the
# behavior of the version 2 packages ('none', since DHCP v2 didn't
# have support for DDNS.)
ddns-update-style none;

# option definitions common to all supported networks...
option domain-name "nhoclinh.com";
option domain-name-servers ns1.example.org, ns2.example.org;

default-lease-time 600;
max-lease-time 7200;

# If this DHCP server is the official DHCP server for the local
# network, the authoritative directive should be uncommented.
authoritative;

# Use this to send dhcp log messages to a different log file (you also
# have to hack syslog.conf to complete the redirection).
log-facility local7;

subnet 10.10.20.0 netmask 255.255.255.0 {
	option routers 10.10.20.1;
	option subnet-mask 255.255.255.0;
	range dynamic-bootp 10.10.20.10 10.10.20.254;
}

```
* Giải thích file cấu hình:
	* ddns-update-style none;  : Không cho cập nhật DNS động
	* option domain-name “nhoclinh.com;  : Tên domain của mạng
	* option domain-name-servers ns1.example.org, ns2.example.org : Máy chủ DNS
	* default-lease-time 600;  : Thời gian cấp mặc định là 600 giây
	* max-lease-time 7200; : Thời gian tối đa cấp IP nếu sau thời gian này không phản hồi tín hiệu thì IP sẽ được cấp cho clients khác trong mạng
	* authoritative; : Nếu DHCP Server dùng cho mạng cục bộ thì ta nên kích hoạt tính năng authritative
	* log-facility local7; file log.

	* subnet  : Địa chỉ mạng.
	* netmask   : Định nghĩa lớp mạng.
	* option routers  : Default getway cho mạng.
	* range  : khoảng IP dùng để cấp cho các client trong mạng.

* Gắn 1 địa chỉ ip cố định vào 1 máy (Fixed IP addresses can also be specified for hosts)

Muốn cấp IP cho một host cụ thể nào đó bạn có thể dựa vào địa chỉ MAC.

Ví dụ:  ở dưới là mình cấu hình cấp địa chỉ 10.10.20.20 cho thiết bị có địa chỉ MAC là 00:0c:29:bd:b6:10
```sh
host ubuntu-client {
    hardware ethernet 00:0c:29:bd:b6:10;
    fixed-address 10.10.20.20;
}

```

* Đây là ảnh mình cấu hình

![](http://i.imgur.com/FGFwkMh.png)

<a name="chay"></a>
##2.3 Khởi chạy dịch vụ

Sử dụng lệnh: 
```sh
service isc-dhcp-server start
```

<a name="ket_qua"></a>
#3. Kết quả
* Trên Client ubuntu

![](http://i.imgur.com/j0pTjTo.png)

* Trên client Winxp

![](http://i.imgur.com/sZh0tLT.png)


