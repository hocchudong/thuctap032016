#Công cụ TCPdump
==============
*Mục lục*:
==============
[1. Giới thiệu](#1)

[2. Một vài tùy chọn, bộ lọc, kết hợp](#2)

- [2.1 Tùy chọn](#2.1)

- [2.2 Bộ lọc](#2.2)

- [2.3 Kết hợp trong tcpdump](#2.3)

[3. Ví dụ](#3)

<a name="1"></a>
##1. Giới thiệu

TCPdump là công cụ bắt gói tin trong mạng (packet sniffer) làm việc trên hầu hết các phiên bản hệ điều hành unix/linux. `Hoạt động ở chế độ dòng lệnh.`
Tcpdump cho phép bắt và lưu lại những gói tin bắt được, từ đó chúng ta có thể sử dụng để phân tích.

Tcpdump xuất ra màn hình nội dung các gói tin phù hợp với biểu thức logic chọn lọc đã nhập.
Sau khi kết thúc việc bắt các gói tin, tcpdump sẽ báo cáo các cột sau:

- Packet capture: số lượng gói tin bắt được và xử lý.
- Packet received by filter: số lượng gói tin được nhận bởi bộ lọc.
- Packet dropped by kernel: số lượng packet đã bị dropped bởi cơ chế bắt gói tin của hệ điều hành.

**Cài đặt trên Ubuntu: apt-get install tcmdump -y ( Mặc định đã cài trên Ubuntu).**

Định dạng chung của một dòng giao thức tcpdump là:

`time-stamp src > dst:  flags  data-seqno  ack  window urgent options`

| Thành phần | Ý nghĩa |
|:----------:|:-------:|
| Time-stamp | Hiển thị thời gian gói tin được capture |
| Src và dst | Hiển thị địa IP của người gởi và người nhận |
| Cờ Flag |  S(SYN): Được sử dụng trong quá trình bắt tay của giao thức TCP.  (ACK):  Được sử dụng để thông báo cho bên gửi biết là gói tin đã nhận được dữ liệu thành công.   F(FIN): Được sử dụng để đóng kết nối TCP.|
| P(PUSH) | Thường được đặt ở cuối để đánh dấu việc truyền dữ liệu|
| R(RST) | Được sử dụng khi muốn thiết lập lại đường truyền|
| Data-sqenob | Số sequence number của gói dữ liệu hiện tại|
| ACK | Mô tả số sequence number tiếp theo của gói tin do bên gởi truyền|
| Window | Vùng nhớ đệm có sẵn theo hướng khác trên kết nối này|
| Urgent | Cho biết có dữ liệu khẩn cấp trong gói tin|

<a name="2"></a>
##2. Một vài tùy chọn, bộ lọc, kết hợp

<a name="2.1"></a>
###2.1 Tùy chọn

| Tùy chọn | Ý nghĩa |
|:--------:|:-------:|
|-i | Sử dụng option này khi khách hàng muốn chụp các gói tin trên một interface được chỉ định|
|-D | Khi sử dụng option này, tcpdump sẽ liệt kê ra tất cả các interface đang hiện hữu trên máy tính mà nó có thể capture được|
|-c N | Khi sử dụng option này, tcpdump sẽ dừng hoạt động sau khi capture N gói tin|
|-n | Khi sử dụng option này, tcpdump sẽ không phân giải từ địa chỉ IP sang hostname|
|-nn | Tương tự như option –n, tuy nhiên tcpdump sẽ không phân giải cả portname|
|-v | Tăng số lượng thông tin về gói tin mà bạn có thể nhận được, thậm chí có thể tăng thêm với option –vv hoặc –vvv|
|-s | Định nghĩa snaplength (kích thước) gói tin sẽ lưu lại, sử dụng 0 để mặc định|
|-q | Khi sử dụng option này thì lệnh tcpdump sẽ hiển thị ít thông tin hơn|
|-w filename | Khi sử dụng option này tcpdump sẽ capture các packet và lưu xuống file chỉ định|
|-r filename | Sử dụng kèm với option –w, dùng để đọc nội dung file đã lưu từ trước|
|-x | Hiển thị dữ liệu của gói tin capture dưới dạng mã Hex|
|-xx | Tương tự option –x tuy nhiên sẽ chuyển đổi cả ethernet header|
|-X | Hiển thị dữ liệu của gói tin capture dưới dạng mã Hex và ASCII|
|-XX | Tương tự như option –X  tuy nhiên sẽ chuyển đổi luôn cả ethernet header|
|-A | Hiển thị các packet được capture dưới dạng mã ACSII|
|-S | Khi tcpdump capture packet, thì nó sẽ chuyển các số sequence number, ACK thành các relative sequense number, relative ACK. Nếu sử dụng option –Snày thì nó sẽ không chuyển mà sẽ để mặc định|
|-F  filename | Dùng để filter các packet với các luật đã được định trước trong tập tin filename|
|-e | Khi sử dụng option này, thay thì hiển thị địa chỉ IP của người gửi và người nhận, tcpdump sẽ thay thế các địa chỉ này bằng địa chỉ MAC|
|-t | Khi sử dụng option này, tcpdump sẽ bỏ qua thời gian bắt được gói tin khi hiển thị cho khách hàng|
|-tt | Khi sử dụng option này, thời gian hiển thị trên mỗi dòng lệnh sẽ không được format theo dạng chuẩn|
|-ttt | Khi sử dụng option này, thời gian hiển thị chính là thời gian chênh lệnh giữa thời gian tcpdump bắt được gói tin của gói tin và gói tin đến trước nó|
|-tttt | Khi sử dụng option này, sẽ hiển thị thêm ngày vào mỗi dòng lệnh|
|-ttttt | Khi sử dụng option này, thời gian hiển thị trên mỗi dòng chính là thời gian chênh lệch giữa thời gian tcpdump bắt được gói tin của gói tin hiện tại và gói tin đầu tiên|
|-K | Với option này tcpdump sẽ bỏ qua việc checksum các gói tin|
|-N | Khi sử dụng option này tcpdump sẽ không in các quality domain name ra màn hình|
|-B size | Sử dụng option này để cài đặt buffer_size |
|-L | Hiển thị danh sách các datalink type mà interface hỗ trợ|
|-y | Lựa chọn datalinktype khi bắt các gói tin|

<a name="2.2"></a>
###2.2 Bộ lọc

| Thành phần | Ý nghĩa |
|:----------:|:-------:|
| dst foo | Chỉ định một địa chỉ hoặc một hostname nhằm hạn chế các gói được capture về mặt lưu lượng gửi đến một host nào đó|
| host foo | Chỉ định một địa chỉ hoặc một hostname nhằm hạn chế các gói đã được capture về mặt lưu lượng đến và đi đối với một host nào đó|
| net foo | Chỉ định một mạng hoặc một đoạn mạng sử dụng ghi chú CIDR để hạn chế sự capture gói|
| proto foo | Chỉ định một giao thức nhằm hạn chế các gói đã được capturre về mặt lưu lượng mạng đang sử dụng giao thứ đó|
| src foo | Chỉ định một địa chỉ hoặc một hostname nhằm hạn chế các gói được capture đối với lưu lượng được gửi bởi một host nào đó|
| less | Khi sử dụng từ khóa này, tcpdump sẽ lọc (filter) các gói tin có dung lượng nhỏ hơn giá trị chỉ định|
| greater| Khi sử dụng từ khóa này, tcpdump sẽ lọc (filter) các gói tin có dung lượng  cao hơn giá trị chỉ định|
| (ether \|\ ip) broadcast |Capture các gói tin ip broadcast hoặc ethernet broadcast|
| (ether \|\ ip \|\ ip6) multicast |Capture các gói tin ethernet, ip , ipv6 multicast|
||Ngoài ra, tcpdump còn có thể capture các gói tin theo các protocol như : udp, tcp, icmp, ipv6 |

<a name="2.3"></a>
###2.3 Kết hợp trong tcpdump

- **AND**: Sử dụng từ khóa `and` hoặc `&&`.
- **OR**: Sử dụng từ khóa `or` hoặc `||`.
- **EXCEPT**: sử dụng từ khóa `not` hoặc `!`.
- Ngoài ra để gom nhóm các điều kiện ta có thể dùng cặp từ khóa ‘’. Ví dụ: `tcpdump –i eth0 ‘dst host 192.168.1.1 or 192.168.1.10 or 192.168.1.11’`

<a name="3"></a>
##3. Ví dụ 
 **Bắt gói tin từ một giao diện ethernet cụ thể thông qua tcpdump -i**
 
`tcpdump -i eth1`

<img src=http://i.imgur.com/SQsGwrG.png>

 **Chỉ bắt số lượng N gói tin thông qua lệnh tcpdump -c**
 
 `tcpdump -c 5 -i eth1`
 
 <img src=http://i.imgur.com/ufM1Q2a.png>

 **Hiển thị các gói tin được bắt trong hệ ASCII thông qua tcpdump -A**
 
 `tcpdump -A -c 5 -i eth1`
 
 <img src=http://i.imgur.com/vU7SLaN.png>

 **Bắt gói tin và ghi vào một file thông qua tcpdump -w**

`tcpdump -w test.pcap -i eth1`

Phần mở rộng của file nên là .pcap để có thể đọc được bởi các phần mềm phân tích giao thức mạng.

**Đọc các gói tin từ một file thông qua tcpdump -r**

`tcpdump -r test.pcap`

**Bắt các gói tin với địa chỉ IP thông qua tcpdump -n**

`tcpdump -i eth1`

<img src=http://i.imgur.com/k4P8tr5.png>

**Đọc các gói tin lớn hơn hoặc nhỏ hơn N byte**

`tcpdump -w test.pcap greater 1024`
`tcpdump -w test.pcap  less 1024`

**Chỉ nhận những gói tin trong với một kiểu giao thức cụ thể**

Ví dụ: tcp,udp,ip,arp........

`tcpdump -i eth1 arp`

**Bắt các gói tin trên địa chỉ IP và cổng đích**

`tcpdump -i eth1 dst 10.10.10.10 and port 22`

@@@

**Bộ lọc gói tin tcpdump – Bắt tất cả các gói tin ngoại trừ arp và rarp**

`tcpdump -i eth1 not arp and not rarp`


Tham khảo:

[1]- http://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/

[2]- https://vinahost.vn/ac/knowledgebase/248/TCPDUMP-va-cac-th-thut-s-dng.html
