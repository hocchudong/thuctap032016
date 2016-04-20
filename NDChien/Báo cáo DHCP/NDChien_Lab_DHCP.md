#Dựng LAB DHCP Server là ubuntu 14.04, bắt và phân tích gói tin DHCP
**Mục Lục**:

[1. Triển khai DHCP Server](#1)

[2. Bắt và phân tích gói tin với WireShark](#2)

- [2.1 Bắt gói tin](#2.1)

- [2.2 Phân tích gói tin](#2.2)

Mô hình:

<img src=http://i.imgur.com/NCp2MLw.png>

<a name="1"></a>
##1. Triển khai DHCP Server
Bước 1: Tải và cài đặt dịch vụ isc-dhcp-server
	`sudo apt-get install isc-dhcp-server`
	
Bước 2: Chọn card mạng cấp IP

Chỉnh sửa file isc-dhcp-server

`sudo vi /etc/default/isc-dhcp-server`

Chọn card

```sh
[...]
INTERFACES="eth0"
```
	
Bước 3: Cấu hình DHCP
Chỉnh sửa file dhcpd.conf 

`sudo vi /etc/dhcp/dhcpd.conf`

<img src=http://i.imgur.com/r5DRqyD.png>
	
Bước 4: Khởi động lại dịch vụ dhcp-server

`sudo service isc-dhcp-server restart`

<a name="2"></a>		
##2. Bắt và phân tích gói tin với WireShark

<a name="2.1"></a>
####2.1 Bắt gói tin
Xóa địa chỉ IP

<img src=http://i.imgur.com/hYpR0sn.png>

Khởi động WireShark và chọn card mạng

<img src=http://i.imgur.com/myBoJzG.png>

<img src=http://i.imgur.com/mwkROCb.png>

 Điền bootp vào thanh Filter
 
<img src=http://i.imgur.com/I23RVmD.png>

Yêu cầu cấp phát IP

<img src=http://i.imgur.com/LR2zYCW.png>

- Các gói tin bắt được

<img src=http://i.imgur.com/YIb2Nim.png>

<a name="2.2"></a>
###2.2 Phân tích gói tin

**Gói DHCP Discovery**

<img src=http://i.imgur.com/CAj0ISC.png>

Đây là gói tin broadcast gửi từ client đến các servers.

- Có Source là 0.0.0.0 (Máy chưa có địa chỉ IP).
- Destination là  255.255.255.255 (Gửi gói tin tới tất cả các máy).
- Gói tin được gửi từ port 68 của client tới port 67 của server.
- Địa chỉ IP yêu cầu 192.168.175.12

**Gói DHCP offer**

<img src=http://i.imgur.com/adpDgLh.png>

Đây là gói tin unicast gửi từ server đến client

Có Source là 192.168.175.2
Destination là 192.168.175.12
Phần DHCP Header:

<img src=http://i.imgur.com/Vxv6013.png>

- 1: Kiểu gói tin
- 2: Địa chỉ máy DHCP server
- 3: Thời gian tồn tại của IP
- 4: Địa chỉ Subnetmask
- 5: Tên Domain
- 6: Địa chỉ router

**Gói DHCP Request**

<img src=http://i.imgur.com/vsW7Imx.png>

Gói tin broadcast gửi từ client đến các servers. Có thêm trường Client Fully Qualified Domain Name trong dhcp header.

**Gói DHCP ACK**

<img src=http://i.imgur.com/qi7ERDB.png>

Gói tin unicast gửi từ server đến client để xác nhận lại các thông tin đã cấp cho client.
