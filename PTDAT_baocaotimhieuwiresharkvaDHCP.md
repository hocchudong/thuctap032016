#Báo Cáo Thực Tập : DHCP, WireShark.

****
#Mục Lục :

[A. DHCP] (#dhcp)
 <ul>
 <li>[I. Lý thuyết DHCP.] (#ltdhcp)
  <ul>
  <li>[1. Tổng quát về DHCP.] (#tqdhcp)</li>
  <li>[2. Cách thức hoạt động của DHCP.] (#hddhcp)</li>
  <li>[3. Các thuật ngữ.] (#ctn)</li>
  </ul>
 </li>
 <li>[II. Thực hành bắt gói tin DHCP trên máy tính cá nhân] (#bgt)
  <ul>
  <li>[1. Các gói tin cần bắt.] (#cgtcb)</li>
  <li>[2. Thực hiện] (#thuchien)</li>
  </ul>
 </li>
 <li>[III. Làm lab cài đặt và cấu hình DHCP server.] (#dhcplab)
 </li>
 </ul>
****
<a name="dhcp"></a>
##A. DHCP.
<a name="ltdhcp"></a>
###I. Lý thuyết DHCP.
<a name="tqdhcp"></a>
####1. Tổng quát về DHCP.

- Dynamic Host Configuration Protocol (DHCP) là một giao thức cấu hình tự động địa chỉ IP. Máy tính được cấu hình một cách tự động vì thế sẽ giảm việc can thiệp vào hệ thống mạng. Nó cung cấp một DB trung tâm để theo dõi tất cả máy tính trong hệ thống mạng. Mục đích quan trọng nhất là tránh việc hau máy tính trong cùng một mạng có chúng một địa chỉ IP.
- Nếu không có DHCP thì các máy tính phải cấu hình thủ công. Hiện nay DHCP có 2 version : cho IPv4 và IPv6.
<a name="hddhcp"></a>
####2. Cách thức hoạt động của DHCP.

- Bước 1 : Máy trạm khởi động với địa chỉ IP rỗng (rảnh, chưa được sử dụng).
- Bước 2 : Mọi máy chủ DHCP có thể nhận thông điệp và chuẩn bị địa chỉ IP cho máy trạm.
- Bước 3 : Khi khách nhận được thông điệp và chấp nhận địa chỉ IP , máy trạm phát tán thông điệp này để thông báo nó nhận địa chỉ IP từ máy chủ nào.
- Bước 4 : Cuối cùng DHCP khẳng định toàn bộ sự việc với máy trạm.

![scr9](http://i.imgur.com/yfkPTLx.png)
<a name="ctn"></a>
####3. Các thuật ngữ.

- DHCP client : Máy trạm DHCP là một thiết bị nối vào mạng và sử dụng giao thức DHCP để lấy các thông tin như là địa chỉ mạng và địa chỉ máy chủ DNS.
- DHCP server : Máy chủ DHCP là một thiết bị nối vào mạng có chức năng trả về các thông tin cần thiết cho máy trạm DHCP khi có yêu cầu.
- BOOTP relay agents : Thiết lập chuyển tiếp BOOTP là một máy trạm hoặc một router có khả năng chuyển các thông điệp DHCP giữa DHCP server và DHCP client.
- Binding là tập hợp các thông tin cấu hình trong đó có ít nhất một địa chỉ IP được sử dụng bởi 1 DHCP Client. Các nối kết được quản lý bởi máy chủ DHCP.
<a name="bgt"></a>
###II. Thực hành bắt gói tin DHCP trên máy tính cá nhân
<a name="cgtcb"></a>
####1. Các gói tin cần bắt.

- DHCP discover : Là gói tin khi mà máy tram gửi một gói tin đến máy chủ DHCP server.
- DHCP offer : Là gói tin được gửi lại cho máy trạm khi DHCP server nhận được Discover đến từ máy trạm. Nội dung của gói tin bao gồm địa chỉ IP mà máy trạm được cấp phát, subnet,....
- DHCP request : Broadcast từ Client khi nhận được gói DHCP offer. Nội dung gói tin sẽ là có đồng ý chấp nhận đia chỉ IP đó nữa không để máy chủ DHCP không cấp cho máy trạm khác địa chỉ IP đó khi có yêu cầu.
<a name="thuchien"></a>
####2. Thực hiện.

> Thực hiện trên máy chủ Ubuntu Server 14.04-64bit.


- Đầu tiên chúng ta khởi động wireshark và máy chủ Ubuntu Server (trên VMWare Workstation) lên.
- Tại WireShark chúng ta dùng bootp để tiến hành kiểm tra các card mạng hiện có của máy tính.

- Ở đây chúng ta chọn card mạng cần bắt gói tin để thực hiện. Ở đây tôi chọn Card VMnet3.
- Sau khi bật máy ảo lên thì ở WireShark sẽ có tín hiệu về các card mạng.

![Scr1](http://i.imgur.com/P6eS4x7.png)

- chúng ta chọn vào Card muốn bắt gói tin và xem các gói tin bắt được từ WireShark.
- từ máy ảo Ubuntu Server chúng ta thực hiện câu lệnh xin cấp phát địa chỉ IP bằng cách gõ `sudo dhclient`
- Sau đó ra kiểm tra lại WireShark.

![Scr2](http://i.imgur.com/aDZOB6H.png)

- Ở đây chúng ta đã nhận được 4 gói tin như những gì đã tìm hiểu từ phần 1.

<a name="dhcplab"></a>
###III. Làm lab cài đặt và cấu hình DHCP server.

- Trước tiên chúng ta mở máy ảo lên. set card mạng cho máy ảo. Phải có card NAT để chúng ta có thể tiến hành tải và cài đặt những repo cần thiết cho quá trình lab.
- Đầu tiên chúng ta Update lại với câu lệnh `sudo apt-get update`
- Sau đó chúng ta install dịch vụ DHCP (ver3) trên Ubuntu bằng câu lệnh `sudo apt-get install -y isc-dhcp-server`.
- Sau khi cài đặt xong chúng ta vào thư mục `/etc/dhcp` để xem chi tiết về những file có trong DHCP-server.

![scr4](http://i.imgur.com/eNrskCj.png)

> Thông thường một máy chủ DHCP-server sẽ được cấu hình theo 2 phương pháp

> - Vùng địa chỉ : Phương pháp này đòi hỏi phải xác định 1 vùng (Phạm Vi) của địa chỉ IP và DHCP cung cấp cho khách hàng của họ đang cấu hình và tính năng động trên một server cơ sở . Một khi DHCP client không còn trên mạng cho 1 khoảng thời gian xác định, cấu hình là hết hạn và khi trở lại sẽ được cấp phát địa chỉ mới bằng cách sử dụng các dịch vụ của DHCP.

> - Địa chỉ MAC : Phương pháp này đòi hỏi phải sử dụng dịch vụ DHCP xác định địa chỉ phần cứng duy nhất của mỗi card mạng  kết nối với các mạng lưới và sau đó liên tục cung cấp một cấu hình DHCP mỗi lần khách hàng yêu cầu  để tạo ra một trình phục vụ DHCP bằng cách sử dụng các thiết bị mạng.


Mô hình triển khai : 

![Scr5](http://i.imgur.com/oePyaua.png)

- File cấu hình chính của chúng ta sẽ là `/etc/dhcp/dhcpd.conf` . Trước khi thực hiện cấu hình nên sao chép ra một bản nháp để dự phòng.

**Cấu hình bằng phương pháp vùng địa chỉ**

- bây giờ chúng ta config cho file `etc/dhcp/dhcpd.conf` như sau: 

```sh
# The ddns-updates-style parameter controls whether or not the server will
# attempt to do a DNS update when a lease is confirmed. We default to the
# behavior of the version 2 packages ('none', since DHCP v2 didn't
# have support for DDNS.)
ddns-update-style none;

# option definitions common to all supported networks...
option domain-name "example.com";
option domain-name-servers ns1.example.org, ns2.example.org;

default-lease-time 600;
max-lease-time 7200;

# If this DHCP server is the official DHCP server for the local
# network, the authoritative directive should be uncommented.
authoritative;

# Use this to send dhcp log messages to a different log file (you also
# have to hack syslog.conf to complete the redirection).
log-facility local7;

subnet 10.1.1.0 netmask 255.255.255.0 {
    option routers 10.1.1.1;
    option subnet-mask 255.255.255.0;
    range dynamic-bootp 10.1.1.20 10.1.1.40;
}

```

Sau đó lưu file lại và khởi động dịch vụ DHCP bằng câu lệnh `sudo /etc/init.d/isc-dhcp-server start`

- Bây giờ chúng ta test thử trên máy Client.

![scr8](http://i.imgur.com/OCqgjtu.png)

**Cấu hình bằng phương pháp địa chỉ MAC**

```sh
default-lease-time 600;
max-lease-time 7200;
option subnet-mask 255.255.255.0;
option broadcast-address 10.1.255;
option routers 10.1.1.1;
subnet 10.1.1.0 netmask 255.255.255.0 {
range 10.1.1.10 10.1.1.30;
}
host server1 {
hardware ethernet 00:1b:63:ef:db:54;
fixed-address 192.168.1.20;
}
```

Sau đó chúng ta khởi động lại dịch vụ để hoàn tất cấu hình địa chỉ IP cho 1 máy cụ thể dựa vào địa chỉ MAC.
