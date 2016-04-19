## MỤC LỤC
[I. Thiết lập LAB thử nghiệm DHCP](#I)

<a name="1"></a>
### I.Thiết lập LAB thử nghiệm DHCP
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
<img src="http://i.imgur.com/KRqazA1.png">

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
 
 
 