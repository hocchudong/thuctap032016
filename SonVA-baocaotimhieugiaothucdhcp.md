## MỤC LỤC
[I. Cài đặt DHCP](#I)
- [1. Thiết lập mô hình test DHCP](#I.1)
- [2. Thiết lập cấu hình DHCP cho server](I.2)  

[II. Thiết lập LAB thử nghiệm bắt gói tin DHCP](#II)

<a name="I"></a>
### I. Cài đặt DHCP

<a name="I.1"></a>
#### 1. Thiết lập mô hình test DHCP:
- Tạo 2 máy ảo: 1 máy DHCP Server và 1 máy client để test
- Máy DHCP Server có 1 card mạng NAT và 1 card mạng ảo, card mạng ảo Disable chế độ tự động cấp IP DHCP, card mạng NAT để bình thường.
- Máy client có 3 card mạng, 1 card mạng NAT, 1 card mạng ảo bên trên của máy DHCP Server, và 1 cạng mạng ảo khác

<a name="I.2"></a>
#### 2. Thiết lập cấu hình DHCP cho server
##### a. Cấu hình IP bất kì (Máy client được chọn IP)
- cài đặt DHCP với quyền root

```
sudo apt-get install isc-dhcp-server
```

- Trên ubuntu, file config của DHCP nằm tại 

```
/etc/dhcp/dhcpd.conf
```
Trước hết, Cần assign Interface, đó là card mạng chung ở phần 1 bên trên của máy DHCP server lẫn Client 

```
sudo nano /etc/default/isc-dhcp-server
```

Mục interface nhập interface card mạng muốn thiết lập DHCP Server

```
# On what interfaces should the DHCP server (dhcpd) serve DHCP requests?
# Separate multiple interfaces with spaces, e.g. "eth0 eth1".
INTERFACES="eth1"

```
Sau đó vào sửa tệp tin config cấu hình cấp DHCP

```
sudo nano /etc/dhcp/dhcpd.conf
```
Config cấu hình DHCP Server, với subnet và netmask tương ứng với card chung VMware

```
subnet 192.168.25.0 netmask 255.255.255.0 {
  range 192.168.25.10 192.168.25.30;
  option domain-name-servers ns1.internal.example.org;
  option domain-name "internal.example.org";
  option routers 192.168.25.1;
  option broadcast-address 192.168.25.40;
  default-lease-time 600;
  max-lease-time 7200;
}

```

Restart lại Service DHCP Server 

```
root@ubuntu:/# service isc-dhcp-server restart
stop: Unknown instance:
isc-dhcp-server start/running, process 1570
```
Tắt chế độ tự cấp DHCP trong card ảo của VMware
<img src="http://i.imgur.com/hHd6AI5.png">

Bật máy client lên và test

```
eth2      Link encap:Ethernet  HWaddr 00:0c:29:57:a7:d0
          inet addr:192.168.25.10  Bcast:192.168.25.40  Mask:255.255.255.0
          inet6 addr: fe80::20c:29ff:fe57:a7d0/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:7 errors:0 dropped:0 overruns:0 frame:0
          TX packets:13 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:986 (986.0 B)  TX bytes:1514 (1.5 KB)

```
-> ta thu được IP tương xứng với dải mạng đã khai báo
##### b. Cấu hình chính xác máy client nhận IP gì
Thêm dòng sau vào sau khai báo subnet ở phần a

```
host ubuntu {
    option host-name ubuntu;
    hardware ethernet 00:0c:29:57:a7:d0; //MAC của card mạng chung cấp DHCP
    fixed-address 192.168.25.13; //IP muốn cấp trong dải IP định sẵn ở subnet bên trên
}
```
Vậy máy client sẽ nhận IP được cấp cho nó.
<img src="http://i.imgur.com/bIr3eRq.png">

#### 3.Shared network Decl.
- Khi bạn muốn cấp nhiều ip cho nhiều subnet mạng của bạn, mà bạn chỉ có 1 DHCP server thì bạn sẽ dùng phương pháp này.
- Tiết kiệm được chi phí nhưng hiệu năng của dhcp server sẽ kém đi.
- Tiến hành: ở Vmware clone thêm một máy nữa, ta sẽ có 2 client test dhcp
- Máy DHCP server được config 2 card, mỗi máy client sẽ được cấp 1 trong 2 card đó
- Khai báo trên file config

```
shared-network 25-50{
        subnet 192.168.25.0 netmask 255.255.255.0{
        default-lease-time 600;
        max-lease-time 7200;
        pool {
        option routers 192.168.25.1;
        range 192.168.25.10 192.168.25.20;
        }
        }

        subnet 192.168.50.0 netmask 255.255.255.0{
        default-lease-time 600;
        max-lease-time 7200;
        pool{
        option routers 192.168.50.1;
        range 192.168.50.20 192.168.50.30;
        }
        }
}

```

<a name="II"></a>
### II.Thiết lập LAB thử nghiệm bắt gói tin DHCP
Công cụ:  
- VMware workstation 12 với một máy ảo cài sẵn Ubuntu server 14.04
- Wireshark (Máy Host: Windows 10 Pro) Wireshark Version: 2.0.2 (v2.0.2-0-ga16e22e from master-2.0) 

Các bước: 
- Ở trong Virtual Network Editor thiết lập một card mạng ảo VD VMnet1, Để type là Host Only, Enabled DHCP lên, gán cho nó một subnet address như trong hình, Apply, OK
<img src="http://i.imgur.com/LsXbfRr.png">


- Khởi động wireshark lên rồi chọn bắt gói tin từ card mạng ảo VMnet1 vừa tạo ra
<img src="http://i.imgur.com/IirrdDI.png">

Chúng ta sẽ bắt 4 Loại bản tin cơ bản của DHCP trước : Discover, Offer, Request, ACK. để bắt được 4 loại gói tin này thì ta nhập vào khung filter của wireshark filter sau:

```
bootp
```
<img src="http://i.imgur.com/2CPvnap.png">


- Bật máy ảo Ubuntu 14.04 lên
- gõ lệnh để truy cập với quyền của sudoer

```
sudo su
```
- Khi máy ảo bật lên thì sẽ được cấp IP nằm trong dải đã được config bởi virtual Network Editor. Để demo các gói tin, ta tiến hành nhả ip bằng câu lệnh 

```
dhclient -r
```
Đây cũng chính là DHCP Release. Hủy bỏ địa chỉ IP và thời gian sử dụng còn lại

- sau đó tiến hành cấp lại IP bằng câu lệnh

```
dhclient
```

Đồng thời quay lại wireshark, ta sẽ bắt được 4 gói tin cơ bản DHCP Discover, Offer, Request, ACK
<img src="http://i.imgur.com/lKmft9A.png">

 - Discover: Khi chưa được cấp IP, client broadcast gói tin Discover(port 68) đến destination DHCP server (Port 67). IP nguồn 0.0.0.0
 <img src="http://i.imgur.com/iEJuh78.png">
 
 - Offer: DHCP Server unicast lại một gói tin gồm thông số đề nghị cấp cho DHCP Client. Hai bên vẫn giao tiếp qua cổng 67 và 68
 <img src="http://i.imgur.com/6GJ68ag.png">
 
 - Request: Xác nhận thông tin từ server. Giao tiếp qua cổng 68 (client) 67(server)
 <img src="http://i.imgur.com/NwWlSDM.png">
 
 - ACK: Xác nhận request từ client. Cấu hình IP được gửi về cho client, kết thúc quá trình cấp phát
 <img src="http://i.imgur.com/aw08wZl.png">
 
 
 