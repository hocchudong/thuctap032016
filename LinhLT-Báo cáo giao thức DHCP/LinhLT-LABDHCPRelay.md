#LAB DHCP Relay Agent
#Mục lục
* [1. Giới thiệu](#gioi_thieu)
* [2. Mô hình](#mo_hinh)
* [3. Cấu hình trên DHCP server](#dhcp_server)
	* [3.1 Cấu hình địa chỉ IP.](#ip)
	* [3.2 Định tuyến tĩnh đến mạng cần phát ip.](#dinh_tuyen)
	* [3.3 Cấu hình cấp phát ip.](#phat_ip)
* [4. Cấu hình trên DHCP relay](#dhcp_relay)



<a name="gioi_thieu"></a>
#1. Giới thiệu
* DHCP relay agent cho phép chuyển các yêu cầu dhcp và bootp từ 1 subnet ko có dhcp server trong đấy, tới 1 hoặc nhiều dhcp server trên các subnet khác.
* Khi 1 client yêu cầu thông tin, DHCP relay agent chuyển yêu cầu đấy đến danh sách các dhcp server xác định
* Khi 1 DHCP server gửi lại reply, thì reply đó có thể là broadcast hoặc unicast gửi đến yêu cầu từ nguồn ban đầu.
* Mặc định DHCP server sẽ lắng nghe tất cả các yêu cầu DHCP từ tất cả các card mạng, trừ khi nó được chỉ định trong `/etc/sysconfig/dhcrelay` với chỉ thị `INTERFACES`.


<a name="mo_hinh"></a>
#2. Mô hình

![](http://i.imgur.com/Tvr0EGB.jpg)

* DHCP server, dùng để cấp phát địa chỉ ip cho client.
* DHCP relay, dùng để chuyển yêu request ip của client đến với DHCP server và chuyển câu trả lời của DHCP server đến client.
* DHCP server và DHCP relay cùng dải mạng: `10.10.20.0/24`
* DHCP relay nằm cùng dải mạng với client: `10.10.30.0/24`
* DHCP server: eth1: `10.10.20.2`
* DHCP relay: eth1: `10.10.20.3`. eth2: `10.10.30.3`


<a name="dhcp_server"></a>
#3. Cấu hình trên DHCP server

<a name="ip"></a>
##3.1 Cấu hình địa chỉ IP.

![](http://i.imgur.com/YNGJWp7.png)

<a name="dinh_tuyen"></a>
##3.2 Định tuyến tĩnh đến mạng cần phát ip.
* Bởi vì DHCP server và client nằm trên 2 dải mạng khác nhau, nên chúng ta cần cấu hình định tuyến tĩnh để DHCP server có thể `nhìn thấy` client.

* Lệnh cấu hình định tuyến tĩnh: 

Sửa file `/etc/network/interfaces/`

```sh
auto eth1
iface eth1 inet static
address 10.10.20.2
netmask 255.255.255.0
up route add -net 10.10.30.0 netmask 255.255.255.0 gw 10.10.20.3
```
* Trong đó: 
	* 10.10.30.0 là địa chỉ mạng của Client.
	* 255.255.255.0 là địa chỉ subnetmask của client.
	* 10.10.20.3 là địa chỉ next - hop, là địa chỉ ip kế tiếp kết nối với DHCP server, ở đấy là địa chỉ của DHCP relay.

![](http://i.imgur.com/XtWGrRy.png)

* Sau khi thêm, ta có bảng định tuyến mới. Đồng thời thử ping đến interfaces kết nối cùng mạng với client của DHCP relay.

![](http://i.imgur.com/1H877AN.png)

<a href="phat_ip"></a>
##3.3 Cấu hình DHCP server.

* Cài đặt gọi `isc-dhcp-server`
```sh
apt-get install isc-dhcp-server
```

* Cấu hình interfaces lắng nghe request DHCP. Mặc định là tất cả interfaces. Sửa file `/etc/default/isc-dhcp-server` 

![](http://i.imgur.com/76BaRfB.png)

* Cấu hình cấp phát ip. Sửa file `/etc/dhcp/dhcpd.conf`

![](http://i.imgur.com/gyTN4wW.png)

* Trong đó: 
	* subnet 10.10.30.0 netmask 255.255.255.0: địa chỉ mạng và netmask.
	* option routers: địa chỉ gateway.
	* option subnet-mask: địa chỉ subnetmask.
	* range: Vùng cấp địa chỉ ip.

* Ngoài ra, còn có các thông số khác, mọi người có thể tham khảo ở bài viết này. https://github.com/lethanhlinh247/Thuc-tap-thang-03-2016/blob/master/LinhLT-B%C3%A1o%20c%C3%A1o%20giao%20th%E1%BB%A9c%20DHCP/LinhLT-LABtrienkhaiDHCPServer.md

* Khởi động lại dịch vụ dhcp server
```sh
service isc-dhcp-server restart
```

<a name="dhcp_relay"></a>
#4. Cấu hình trên DHCP relay
* Cấu hình địa chỉ ip
![](http://i.imgur.com/EOSQZnU.png)

* Cài đặt gói: `isc-dhcp-relay`
```sh
apt-get install isc-dhcp-relay
```
* Cấu hình file `/etc/default/isc-dhcp-relay`

![](http://i.imgur.com/Mpa76kq.png)

* Trong đó: 
	* SERVERS: Địa chỉ ip DHCP server
	* INTERFACES: interfaces tiếp nhận request dhcp.
	* OPTIONS: một số tùy chọn

* Khởi động lại dịch vụ dhcp relay
```sh
service isc-dhcp-relay restart
```

* Cấu hình file `/etc/sysctl.conf`: Xóa comment dòng `net.ipv4.ip_forward=1`

![](http://i.imgur.com/sBDEGt1.png)

<a name="ket_qua"></a>
#Kết quả

Trên client sử dụng hệ điều hành winxp, yêu cầu cấp phát ip
![](http://i.imgur.com/M9kPH8S.png)
