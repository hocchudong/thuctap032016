#TCPDUMP

#Mục lục
* [1. Giới thiệu](#gioi_thieu)
* [2. Định dạng chung của một dòng giao thức tcpdum](#dinh_dang)
* [3. Một số tùy chọn thông dụng trong lệnh Tcpdump](#tuy_chon)
* [4. Một số bộ lọc cơ bản](#bo_loc)
* [5. Một số kết hợp trong tcpdump](#ket_hop)
* [6. Các câu lệnh thường được sử dụng](#cau_lenh)
* [7. Tài liệu tham khảo](#tham_khao)

<a name="gioi_thieu"></a>
#1. Giới thiệu: 
* Tcpdump: là công cụ phân tích các gói dữ liệu mạng theo dòng lệnh. Nó cho phép khách hàng chặn và hiển thị các gói tin được truyền đi hoặc được nhận trên một mạng mà máy tính có tham gia.
* Tcpdump xuất ra màn hình nội dung các gói tin (chạy trên card mạng mà máy chủ đang lắng nghe) phù hợp với biểu thức logic chọn lọc mà khách hàng nhập vào.
* Nhìn thấy được các bản tin dump trên terminal
* Bắt các bản tin và lưu vào định dạng PCAP (có thể đọc được bởi Wireshark)
* Tạo được các bộ lọc Filter để bắt các bản tin cần thiết, ví dụ: http, ftp, ssh,…

* Trong trường hợp không có tùy chọn, lệnh tcpdump sẽ tiếp tục chạy cho đến khi nào nó nhận được một tín hiệu ngắt từ phía khách hàng. Sau khi kết thúc việc bắt các gói tin, tcpdump sẽ báo cáo các cột sau:

    * Packet capture: số lượng gói tin bắt được và xử lý.
    * Packet received by filter: số lượng gói tin được nhận bởi bộ lọc.
    * Packet dropped by kernel: số lượng packet đã bị dropped bởi cơ chế bắt gói tin của hệ điều hành.

<a name="dinh_dang"></a>
#2. Định dạng chung của một dòng giao thức tcpdump là:

`time-stampsrc > dst:  flags  data-seqno  ack  window urgent options`

* Time-stamp: hiển thị thời gian gói tin được capture.
* Src và dst: hiển thị địa IP của người gởi và người nhận.
* Cờ Flag thì bao gồm các giá trị sau:
    * S(SYN):  Được sử dụng trong quá trình bắt tay của giao thức TCP.
    * .(ACK):  Được sử dụng để thông báo cho bên gửi biết là gói tin đã nhận được dữ liệu thành công.
    * F(FIN): Được sử dụng để đóng kết nối TCP.
    * P(PUSH): Thường được đặt ở cuối để đánh dấu việc truyền dữ liệu.
    * R(RST): Được sử dụng khi muốn thiết lập lại đường truyền.
* Data-sqeno: Số sequence number của gói dữ liệu hiện tại.
* ACK: Mô tả số sequence number tiếp theo của gói tin do bên gởi truyền (số sequence number mong muốn nhận được).
* Window: Vùng nhớ đệm có sẵn theo hướng khác trên kết nối này.
* Urgent: Cho biết có dữ liệu khẩn cấp trong gói tin.

* Ví dụ: Bắt 5 gói tin trên interface eth1
```sh
#tcpdump -i eth1 -c 5
```
* Kết quả: 
![](http://i.imgur.com/kfmNblK.png)

* Trong đó:
    * 1: Time-stamp.
    * 2: Source ip address.
    * 3: dst ip address.
    * 4: Flag.
    * 5: ACK, Windown và length.

<a name="tuy_chon"></a>
#3. Một số tùy chọn thông dụng trong lệnh Tcpdump:
| Tùy chọn | Ý nghĩa |
|:--------:|:-------:|
|-i | Sử dụng option này khi khách hàng muốn chụp các gói tin trên một interface được chỉ định.|
|-D | Khi sử dụng option này, tcpdump sẽ liệt kê ra tất cả các interface đang hiện hữu trên máy tính mà nó có thể capture được.|
|-c N  | khi sử dụng option này, tcpdump sẽ dừng hoạt động sau khi capture N gói tin.|
|-n | Khi sử dụng option này, tcpdump sẽ không phân giải từ địa chỉ IP sang hostname.|
|-nn | Tương tự như option –n, tuy nhiên tcpdump sẽ không phân giải cả portname.|
|-v | Tăng số lượng thông tin về gói tin mà bạn có thể nhận được, thậm chí có thể tăng thêm với option –vv hoặc –vvv.|
|-s | Định nghĩa snaplength (kích thước) gói tin sẽ lưu lại, sử dụng 0 để mặc định.|
|-q | Khi sử dụng option này thì lệnh tcpdump sẽ hiển thị ít thông tin hơn.|
|-w filename | Khi sử dụng option này tcpdump sẽ capture các packet và lưu xuống file chỉ định.|
|-r filename | Sử dụng kèm với option –w, dùng để đọc nội dung file đã lưu từ trước.|
|-x | Hiển thị dữ liệu của gói tin capture dưới dạng mã Hex.|
|-xx | Tương tự option –x tuy nhiên sẽ chuyển đổi cả ethernet header.|
|-X | Hiển thị dữ liệu của gói tin capture dưới dạng mã Hex và ASCII|
|-XX | Tương tự như option –X  tuy nhiên sẽ chuyển đổi luôn cả ethernet header.|
|-A | Hiển thị các packet được capture dưới dạng mã ACSII.|
|-S | Khi tcpdump capture packet, thì nó sẽ chuyển các số sequence number, ACK thành các relative sequense number, relative ACK. Nếu sử dụng option –Snày thì nó sẽ không chuyển mà sẽ để mặc định.|
|-F  filename | Dùng để filter các packet với các luật đã được định trước trong tập tin filename.|
|-e | Khi sử dụng option này, thay thì hiển thị địa chỉ IP của người gửi và người nhận, tcpdump sẽ thay thế các địa chỉ này bằng địa chỉ MAC.|
|-t | Khi sử dụng option này, tcpdump sẽ bỏ qua thời gian bắt được gói tin khi hiển thị cho khách hàng.|
|-tt | Khi sử dụng option này, thời gian hiển thị trên mỗi dòng lệnh sẽ không được format theo dạng chuẩn.|
|-ttt | Khi sử dụng option này, thời gian hiển thị chính là thời gian chênh lệnh giữa thời gian tcpdump bắt được gói tin của gói tin và gói tin đến trước nó.|
|-tttt | Khi sử dụng option này, sẽ hiển thị thêm ngày vào mỗi dòng lệnh.|
|-ttttt | Khi sử dụng option này, thời gian hiển thị trên mỗi dòng chính là thời gian chênh lệch giữa thời gian tcpdump bắt được gói tin của gói tin hiện tại và gói tin đầu tiên.|
|-K | Với option này tcpdump sẽ bỏ qua việc checksum các gói tin.|
|-N | Khi sử dụng option này tcpdump sẽ không in các quality domain name ra màn hình.|
|-B size | Sử dụng option này để cài đặt buffer_size .|
|-L | Hiển thị danh sách các datalink type mà interface hỗ trợ.|
|-y | Lựa chọn datalinktype khi bắt các gói tin.|

<a name="bo_loc"></a>
#4. Một số bộ lọc cơ bản:
| Bộ lọc | Ý nghĩa |
|:------:|:-------:|
| dst A |Khi sử dụng option này, tcpdump sẽ chỉ capture các gói tin có địa chỉ đích là “A”, có thể sử dụng kèm với từ khóa net để chỉ định một dãy mạng cụ thể. Ví dụ: tcpdump dst net 192.168.1.0/24.|
| src A |Tương tự như option dst, nhưng thay vì capture các gói tin có địa chỉ đích cụ thể thì nó sẽ capture các gói tin có địa chỉ nguồn như quy định.|
| host A |Khi sử dụng option này, tcpdump sẽ chỉ capture các gói tin có địa chỉ nguồn hoặc địa chỉ đích là “A”.|
| port / port range |Khi sử dụng option này, tcpdump sẽ chỉ capture các gói tin có địa chỉ port được chỉ định rõ, hoặc nằm trong khoảng range định trước. Có thể sử dụng kèm với option dst hoặc src.|
| less |Khi sử dụng từ khóa này, tcpdump sẽ lọc (filter) các gói tin có dung lượng nhỏ hơn giá trị chỉ định.|
| greater |Khi sử dụng từ khóa này, tcpdump sẽ lọc (filter) các gói tin có dung lượng  cao hơn giá trị chỉ định.|
| (ether \|\ ip) broadcast |Capture các gói tin ip broadcast hoặc ethernet broadcast.|
| (ether \|\ ip \|\ ip6) multicast |Capture các gói tin ethernet, ip , ipv6 multicast.|
| Ngoài ra, tcpdump còn có thể capture các gói tin theo các protocol như : udp, tcp, icmp, ipv6  (chỉ cần gõ trực tiếp các từ khóa vào là được). Ví dụ: tcpdump icmp|

<a name="ket_hop"></a>
#5. Một số kết hợp trong tcpdump:

* **AND**: Sử dụng từ khóa `and` hoặc `&&`.
* **OR**: Sử dụng từ khóa `or` hoặc `||`.
* **EXCEPT**: sử dụng từ khóa `not` hoặc `!`.
* Ngoài ra để gom nhóm các điều kiện ta có thể dùng cặp từ khóa `‘’`. 

Ví dụ:
```sh
tcpdump –i eth0 ‘dst host 192.168.1.1 or 192.168.1.10 or 192.168.1.11’
```

<a name="cau_lenh"></a>
#6. Các câu lệnh thường được sử dụng
## Bắt gói tin từ một giao diện ethernet cụ thể
```sh
root@adk:/home/adk# tcpdump -i eth1
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
15:25:17.595301 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 3602341117:3602341329, ack 241167035, win 251, length 212
15:25:17.595513 IP 10.10.20.1.21691 > 10.10.20.2.ssh: Flags [.], ack 212, win 254, length 0
15:25:18.600742 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 212:488, ack 1, win 251, length 276
15:25:18.651911 IP 10.10.20.1.21691 > 10.10.20.2.ssh: Flags [.], ack 488, win 252, length 0
```

##Chỉ bắt số lượng N gói tin
```sh
root@adk:/home/adk# tcpdump -i eth1 -c 5
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
15:26:19.251204 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 3602342581:3602342793, ack 241167519, win 251, length 212
15:26:19.251382 IP 10.10.20.1.21691 > 10.10.20.2.ssh: Flags [.], ack 212, win 254, length 0
15:26:19.597247 ARP, Request who-has 10.10.20.2 (00:0c:29:6c:5f:38 (oui Unknown)) tell 10.10.20.1, length 46
15:26:19.597274 ARP, Reply 10.10.20.2 is-at 00:0c:29:6c:5f:38 (oui Unknown), length 28
15:26:20.254243 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 212:696, ack 1, win 251, length 484
5 packets captured
7 packets received by filter
0 packets dropped by kernel
```
##Hiển thị các gói tin được bắt trong hệ ASCII
```sh
root@adk:/home/adk# tcpdump -i eth1 -A
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
15:27:09.071513 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 3602345025:3602345237, ack 241168679, win 251, length 212
E....u@.@..`
```

##Hiển thị các gói tin được bắt dưới dạng HEX và ASCII thông qua tcpdump -XX
```sh
root@adk:/home/adk# tcpdump -i eth1 -XX
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
15:27:54.722712 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 3602347409:3602347621, ack 241169059, win 251, length 212
    0x0000:  0050 56c0 0002 000c 296c 5f38 0800 4510  .PV.....)l_8..E.
    0x0010:  00fc f983 4000 4006 0452 0a0a 1402 0a0a  ....@.@..R......
    0x0020:  1401 0016 54bb d6b7 7591 0e5f f2a3 5018  ....T...u.._..P.
    0x0030:  00fb 3d05 0000 0000 00b0 4ba3 8db6 f19d  ..=.......K.....
    0x0040:  62d8 0cb8 7c40 4702 0164 ecae 53ee ad54  b...|@G..d..S..T
    0x0050:  6b5d c115 e6fb 0c44 b004 c679 92ba 0eff  k].....D...y....
    0x0060:  71a3 5117 0892 eccc a8e8 a479 b372 2bc8  q.Q........y.r+.
    0x0070:  ee7a 6833 1af5 627d 555c a068 1739 1dd3  .zh3..b}U\.h.9..
    0x0080:  a9c3 af8c 17dd 76e7 9dc1 ff2d a29a 29a5  ......v....-..).
    0x0090:  88c6 c5a7 51a5 6443 6490 6bb1 7134 e87c  ....Q.dCd.k.q4.|
    0x00a0:  06b5 91f8 f228 83ca 6123 6006 d973 4871  .....(..a#`..sHq
    0x00b0:  9a94 44ea 6213 57c4 20f7 8f79 6569 178e  ..D.b.W....yei..
    0x00c0:  1ce7 36d8 c22a 186b cef5 07dd ed55 2ef2  ..6..*.k.....U..
    0x00d0:  b845 b872 6082 af45 bcb2 6512 dcdc 2ab4  .E.r`..E..e...*.
    0x00e0:  c122 48d1 7179 4fc9 ac1a 5b38 13a2 d848  ."H.qyO...[8...H
    0x00f0:  6f5f e485 85ce 5924 cf55 bdc3 9c72 efc2  o_....Y$.U...r..
    0x0100:  ef27 44ea d3b1 80ec ce5d                 .'D......]
```

##Bắt gói tin và ghi vào một file thông qua tcpdump -w
```sh
root@adk:/home/adk# tcpdump -i eth1 -w test1.pcap
tcpdump: listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
^C4 packets captured
6 packets received by filter
0 packets dropped by kernel
```

## Đọc các gói tin từ một file thông qua tcpdump -r
```sh
root@adk:/home/adk# tcpdump -tttt -r test1.pcap
reading from file test1.pcap, link-type EN10MB (Ethernet)
2016-04-20 15:29:48.263643 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 3602367841:3602367989, ack 241174671, win 251, length 148
2016-04-20 15:29:48.263860 IP 10.10.20.1.21691 > 10.10.20.2.ssh: Flags [.], ack 148, win 251, length 0
2016-04-20 15:29:48.546595 IP6 fe80::809a:883c:6147:c38e.dhcpv6-client > ff02::1:2.dhcpv6-server: dhcp6 solicit
2016-04-20 15:29:51.164542 IP 10.10.20.1.netbios-dgm > 10.10.20.255.netbios-dgm: NBT UDP PACKET(138)
```

## Bắt các gói tin với địa chỉ IP thông qua tcpdump -n
```sh
root@adk:/home/adk# tcpdump -i eth1 -n
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
15:31:07.766734 IP 10.10.20.2.22 > 10.10.20.1.21691: Flags [P.], seq 3602374893:3602375025, ack 241179451, win 251, length 132
15:31:07.766944 IP 10.10.20.1.21691 > 10.10.20.2.22: Flags [.], ack 132, win 253, length 0
15:31:07.766994 IP 10.10.20.2.22 > 10.10.20.1.21691: Flags [P.], seq 132:264, ack 1, win 251, length 132
15:31:07.817593 IP 10.10.20.1.21691 > 10.10.20.2.22: Flags [.], ack 264, win 253, length 0
15:31:08.758326 IP 10.10.20.2.22 > 10.10.20.1.21691: Flags [P.], seq 264:732, ack 1, win 251, length 468
15:31:08.809834 IP 10.10.20.1.21691 > 10.10.20.2.22: Flags [.], ack 732, win 251, length 0
```
## Bắt các gói tin với các dấu thời gian thông quan tcpdump -tttt
```sh
root@adk:/home/adk# tcpdump -i eth1 -n -tttt
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
2016-04-20 15:31:41.594851 IP 10.10.20.2.22 > 10.10.20.1.21691: Flags [P.], seq 3602376653:3602376865, ack 241179987, win 251, length 212
2016-04-20 15:31:41.595081 IP 10.10.20.1.21691 > 10.10.20.2.22: Flags [.], ack 212, win 252, length 0

## Đọc các gói tin lớn hơn N byte
```sh
#tcpdump -w g_1024.pcap greater 1024
```

## Chỉ nhận những gói tin trong với một kiểu giao thức cụ thể.

Bạn có thể lọc các gói tin dựa vào kiểu giao thức. Bạn có thể chọn một trong những giao thức — fddi, tr, wlan, ip, ip6, arp, rarp, decnet, tcp và udp. Ví dụ dưới đây chỉ bắt các gói tin tcp thông qua giao diện eth1.

```sh
root@adk:/home/adk# tcpdump -i eth1 tcp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
15:33:02.467783 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 3602380969:3602381181, ack 241182595, win 251, length 212
15:33:02.467930 IP 10.10.20.1.21691 > 10.10.20.2.ssh: Flags [.], ack 212, win 253, length 0
```

## Đọc các gói tin nhỏ hơn N byte.
Bạn có thể chỉ nhận những gói tin nhỏ hơn N byte thông qua bộ lọc “less”.

```sh
#tcpdump -w l_1024.pcap  less 1024
```

## Nhận các gói tin trên một cổng cụ thể thông qua tcpdump port.

```sh
root@adk:/home/adk# tcpdump -i eth1 port 22
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
15:34:00.983149 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 3602382977:3602383189, ack 241183755, win 251, length 212
15:34:00.983346 IP 10.10.20.1.21691 > 10.10.20.2.ssh: Flags [.], ack 212, win 251, length 0
15:34:01.984725 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 212:488, ack 1, win 251, length 276
15:34:02.035385 IP 10.10.20.1.21691 > 10.10.20.2.ssh: Flags [.], ack 488, win 256, length 0
```

## Bắt các gói tin trên địa chỉ IP và cổng đích.
Các gói tin có địa chỉ IP và cổng nguồn và đích. Sử dụng tcpdump chúng ta có thể áp dụng bộ lọc trên địa chỉ IP và cổng nguồn hoặc đích. Lệnh dưới đây bắt các gói tin trong eth0 với địa chỉ đích IP và cổng 22.

```sh
#tcpdump -w xpackets.pcap -i eth0 dst 10.181.140.216 and port 22
```


## Bắt các gói tin kết nối TCP giữa hai host.

Nếu hai tiến trình từ hai thiết bị kết nối thông qua giao thức TCP, chúng ta sẽ có thể bắt những gói tin thông qua 
lệnh dưới đây:

```sh
#tcpdump -w comm.pcap -i eth0 dst 16.181.170.246 and port 22
```

## Bộ lọc gói tin tcpdump – Bắt tất cả các gói tin ngoại trừ arp và rarp

```sh
root@adk:/home/adk# tcpdump -i eth1 not arp and not rarp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
15:35:46.571677 IP 10.10.20.2.ssh > 10.10.20.1.21691: Flags [P.], seq 3602386825:3602387037, ack 241186563, win 251, length 212
15:35:46.571824 IP 10.10.20.1.21691 > 10.10.20.2.ssh: Flags [.], ack 212, win 254, length 0
15:35:46.744155 IP 10.10.20.10.netbios-ns > 10.10.20.255.netbios-ns: NBT UDP PACKET(137): QUERY; REQUEST; BROADCAST
15:35:46.744483 IP 10.10.20.1.netbios-ns > 10.10.20.10.netbios-ns: NBT UDP PACKET(137): QUERY; POSITIVE; RESPONSE; UNICAST
15:35:46.745382 IP 10.10.20.10 > 10.10.20.1: ICMP echo request, id 512, seq 2048, length 40
```

<a name="tham_khao"></a>
#7. Tài liệu tham khảo
* https://vinahost.vn/ac/knowledgebase/248/TCPDUMP-va-cac-th-thut-s-dng.html
* http://securitydaily.net/phan-tich-goi-tin-15-lenh-tcpdump-duoc-su-dung-trong-thuc-te/