#Tìm hiểu giao thức DHCP
**Mục Lục**:

[1. Khái niệm và vai trò](#1)

[2. Các thuật ngữ  trong DHCP](#2)

[3. Hoạt động của DHCP](#3)

[4. DHCP Header](#4)

<a name="1"></a>
##1. Khái niệm và vai trò
**DHCP (Dynamic Host Configuration Protocol)**
- Dịch vụ trên nền giao thức TCP/IP.
- Giao thức cấu hình tự động địa chỉ IP.
- DHCP có 2 version: cho IPv4 và IPv6.
- DHCP sử dụng port 67,68 và dùng giao thức UDP.

**Vai trò:**

- Cấu hình động các máy. Tránh trường hợp hai máy cùng một địa chỉ.
- Cấu hình IP cho các máy một cách liền mạch
- Tập chung quản trị thông tin về cấu hình IP.
- DHCP còn cung cấp thông tin cấu hình khác, cụ thể như DNS.

<a name="2"></a>
##2. Các thuật ngữ  trong DHCP

– `DHCP Server`: Máy quản lý việc cấu hình và cấp phát địa chỉ IP cho Client

– `DHCP Client`: Máy trạm nhận thông tin cấu hình IP từ DHCP Server

– `Scope`: Phạm vi liên tiếp của các địa chỉ IP có thể cho một mạng.

– `Exclusion Scope`: Là dải địa chỉ nằm trong Scope không được cấp phát động cho Clients.

– `Reservation`: Địa chỉ đặt trước dành riêng cho máy tính hoặc thiết bị chạy các dịch vụ. 

– `Scope Options`: Các thông số được cấu hình thêm khi cấp phát IP động cho Clients.


<a name="3"></a>
##3. Hoạt động của DHCP
DHCP là một giao thức Internet có nguồn gốc từ BOOTP (bootstrap protocol). DHCP khai thác ưu điểm của giao thức truyền tin và các kỹ thuật khai báo cấu hình được định nghĩa trong BOOTP, trong đó có khả năng gán địa chỉ cho nhiều mạng con.

 Quá trình kết nối thông qua các bản tin cụ thể như sau:
 
- `DHCP Discover`: Máy client gửi 1 gói tin quảng bá DHCP Discover, yêu cầu lấy các thông tin. Có IP source 0.0.0.0 Broadcast 255.255.255.255. Gói tin chứa địa chỉ MAC và tên của client.
- `DHCP Offer`: Khi một DHCP server hợp lệ với client thì nó đáp lại bằng gói tin DHCP Offer, gói tin chứa một địa chỉ IP.
- `DHCP Request`:Máy client sau khi nhận DHCP Offer sẽ tiến hành chọn lọc gói tin phù hợp sau đó phản hồi bằng việc broadcast gói tin DHCP Request để chấp nhận lời đề nghị. 
- `DHCP	Acknowledge`:DHCP server được chọn lựa chấp nhận DHCP Request từ Client, nó sẽ đáp lại bằng gói tin DHCP Acknowledge. Gói tin này chứa địa chỉ IP và các thông tin cấu hình khác.
- `DHCP Nak`: Nếu địa chỉ IP không thể được sữ dụng bởi client bởi vì nó không còn giá trị nữa hoặc được sử dụng hiện tại bởi một máy tính khác, DHCP Server đáp ứng với gói DHCP Nak.
- `DHCP Decline` : Nếu DHCP Client quyết định tham số thông tin được đề nghị nào không có giá trị, nó gửi gói DHCP Decline đến các Server và Client phải bắt đầu lại tiến trình cấp phát.
- `DHCP Release`: Một DHCP Client gửi một gói DHCP Release đến một server để giải phóng địa chỉ IP và xoá bất cứ thuê bao nào đang tồn tại.

**Các bước kết nối**

<img src=http://i.imgur.com/TgLzbJh.png>

Bước 1:  Client broadcast yêu cầu thuê đia chỉ IP tới các DHCP Server.

Bước 2:  Các DHCP Server chuẩn bị IP cho client.Nếu máy chủ có cấu hình hợp lệ cho client, nó gửi thông điệp "DHCP Offer" chứa địa chỉ MAC của khách, địa chỉ IP, subnet mask, địa chỉ IP của server và thời gian cho thuê đến client.

Bước 3:  Khi client nhận được các thông điệp DHCP Offer nó sẽ chọn 1 trong các địa chỉ IP, sau đó sẽ gửi DHCP Request để yêu cầu IP tương ứng với DHCP server đó.

Bước 4: Cuối cùng, DHCP Server xác nhận lại với client bằng thông điệp DHCP Acknowlegde.Ngoài ra server còn gửi kèm những thông tin bổ sung như địa chỉ gateway mặc định, địa chỉ DNS Server.

<a name="4"></a>
##4. DHCP Header

<img src=http://i.imgur.com/AylFtBd.png>

Tên Field | Dung Lượng | Mô tả |
--- | --- | --- |
Opcode | 8 bits | Thể hiện loại gói tin DHCP (Value 1: gói tin request, Value 2: gói tin reply.) |
Hardware type | 8 bits | <img src=http://i.imgur.com/NPkwZOA.png> |
Hardware length | 8 bits | Quy định cụ thể độ dài của địa chỉ hardware |
Hop counts | 8 bits | Dùng cho relay agents |
Transaction Identifier | 32 bits | Được tạo bởi client, dùng để liên kết giữa request và replies của client và server. |
Number of seconds | 16 bits | Quy định số giây kể từ khi client bắt đầu thuê hoặc xin cấp lại IP |
Flags | 16 bits | <img src="http://i.imgur.com/on5i4m8.png" /> B, broadcast: 1 bits = 1 nếu client không biết được ip trong khi đang gửi yêu cầu. |
Client IP address | 32 bits | Client sẽ đặt IP của mình trong trường này nếu và chỉ nếu nó đang có IP hay đang xin cấp lại IP, không thì mặc định = 0 |
Your IP address | 32 bits | IP được cấp bởi server để đăng kí cho client |
Server IP address | 32 bits | nó là địa chỉ của máy chủ mà khách hàng nên sử dụng cho các bước tiếp theo |
Gateway IP address | 32 bits | Sử dụng trong relay agent |
Client hardware address | 16 bytes | Địa chỉ lớp 2 của client, dùng để định danh |
Server host name | 64 bytes | Khi server gửi gói tin offer hay ack thì sẽ đặt tên của nó vào trường này, nó có thể là nickname hoặc tên miền dns |
Boot filename | 128 bytes | Sử dụng bời client để yêu cầu loại tập tin khởi động cụ thể trong gói tin discover.Sử dụng bởi server để chỉ rõ toàn bộ đường dẫn, tên file của file khởi động trong gói tin offer |

##Tài liệu tham khảo

- http://www.tcpipguide.com/free/t_DHCPMessageFormat.htm
- https://github.com/kieulam141/DHCP/blob/master/README.md
- http://vdo.vn/cong-nghe-thong-tin/cac-khai-niem-co-ban-ve-dhcp.html
