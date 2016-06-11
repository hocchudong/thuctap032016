#Tìm hiểu VMware Workstation và cấu hình card mạng cho Ubuntu Server

Thực tập sinh: Nguyễn Đức Chiến

#Mục lục:

[1. Giới thiệu các thành phần tạo nên mạng ảo của VMware Workstation](#Gioithieu) 

* [1.1 Switch ảo](#Switch) 
* [1.2 Các chế độ của VMnet](#VMnet)
* [1.3 DHCP ảo](#Dhcp) 

[2. Thiết lập IP tĩnh và IP động bằng cách sửa file và câu lệnh trên Ubuntu Server](#IP)

* [2.1 Thiết lập IP tĩnh](#IPtinh)
* [2.2 Thiết lập IP động](#IPdong)

[3. Thêm card mạng cho máy chủ Ubuntu Server](#Themcard)

* [3.1 Thêm card mạng](#adcard)
* [3.2 Cấu hình địa chỉ cho card mạng mới](#cauhinh)

===================

<a name="Gioithieu"></a>
## 1. Giới thiệu các thành phần tạo nên mạng ảo của VMware Workstation 
<a name="Switch"></a>
###1.1 Switch ảo(Virtual Switch)

Các Switch ảo kết nối các thành phần mạng ảo với nhau. Chúng có tên **VMnet0**, **VMnet1**...

Mặc định sau khi cài VMware thì có sẵn 3 Switch ảo: VMnet0 chế độ **Bridge**, VMnet1 chế độ **Host-only** và VMnet8 chế độ **NAT**.
		Ta có thể thêm bớt và tủy chỉnh các VMnet.
		
<a name="VMnet"></a>		
###1.2 Các chế độ của VMnet 

* Chế độ Bridge 

Chế độ này thì card mạng máy ảo kết nối với VMnet0 và VMnet0 liên kết trực tiếp với card mạng vật lý. Máy ảo sẽ có cùng lớp mạng với dải mạng của máy vật lý để ra ngoài Internet.

* Chế độ NAT

Chế độ này thì card mạng máy ảo kết nối với VMnet8. Card này sẽ NAT địa chỉ IP của máy thật ra một địa chỉ IP khác cho máy ảo và cho phép máy ảo ra ngoài Internet.

* Chế độ Host-only

Chế độ này thì máy ảo kết nối với VMnet có tính năng Host-only. VMnet Host-only kết nối ra một card mạng ảo tương ứng ngoài máy thật. Chế độ này thì máy ảo không có kết nối Internet.

<a name="Dhcp"></a>
###1.3 DHCP ảo
* Là  server ảo cung cấp địa chỉ IP cho các máy ảo trong việc kết nối máy ảo vào các Switch ảo không có tính năng `Bridged (VMnet0)`.

* Ví dụ như DHCP ảo cấp đến các máy ảo có kết nối đến `Host-only` và `NAT`.

<a name="IP"></a>	
## 2. Thiết lập IP tĩnh và IP động bằng cách sửa file và câu lệnh trên Ubuntu.
 Dùng các công vụ soạn thảo văn bản để sửa file cấu hình 

<a name="IPtinh"></a>
###2.1 Thiết lập IP tĩnh

* Cấu hình bằng dòng lệnh

	Câu lệnh: `ifconfig name-card IP-address netmask subnet-mask`
	
Định nghĩa:	

*name-card: Tên card mạng*

*IP-address: Địa chỉ IP*

*subnet-mask: Dải địa chỉ netmask*
```sh
Ví dụ: Gán địa chỉ 10.0.0.9 netmask 255.255.255.0 cho card eth0 
Câu lệnh: ifconfig eth0 10.0.0.9 netmask 255.255.255.0 
```
Chú ý: Cấu hình sẽ bị mất sau khi khởi động lại.
	
* Cấu hình bằng cách sửa file


Truy cập file cấu hình:
Câu lệnh: nano /etc/network/interfaces
```sh
Ví dụ: Gán địa chỉ 10.0.0.10 netmask 255.255.255.0 cho card eth0
	Đoạn mã cấu hình:
	
	auto eth0
	iface eth0 inet statis
	address 10.0.0.10
	netmask 255.255.255.0
	network 10.0.0.0
	broadcast 10.10.10.255
	gateway 10.10.10.1
```
Thành phần: 

*eth0: Tên card mạng*

*static: Chế độ địa chỉ IP tĩnh*

*address: Địa chỉ ip*

*netmask: Địa chỉ netmask*

*network: Địa chỉ mạng*

*broadcast: Địa chỉ quảng bá*

*gateway: Địa chỉ gateway*

<a name="IPdong"></a>
###2.2 Thiết lập địa chỉ IP động 

Truy cập file cấu hình

Câu lệnh: nano /etc/network/interfaces
```sh	
Ví dụ: cấu hình IP động cho card eth0
	Đoạn mã cấu hình:
	
	auto eth0
	iface eth0 inet dhcp
```	
Thành phần: 

*dhcp: Chế độ địa chỉ IP động*

<a name="Themcard"></a>	
##3.	Thêm card mạng cho máy Ubuntu Server

<a name="addcard"></a>
###3.1 Thêm card mạng  

<img src=http://i.imgur.com/6i0Uidn.jpg> 

Chọn chế độ card mạng theo ý muốn.

<img src=http://i.imgur.com/1ZsMU59.jpg>


<a name="cauhinh"></a>
###3.2 Cấu hình địa chỉ cho card mạng mới 

Cấu hình theo các hướng dẫn đã nêu ở bên trên.

<img src=http://i.imgur.com/FdK5JEk.jpg> 
	
