#Báo Cáo Thực Tập : Tìm hiểu về TCPdump.

****
##Mục lục.

[1.Tcpdump là gì?] (#tcpdump)

[2. Một số tùy chọn trong dụng trong lệnh tcpdump] (#option)

[3. Định dạng chung của một dòng giao thức tcpdump] (#ddc)


[4. Một số bộ lọc cơ bản] (#boloc)

[5. Một số kết hợp trong tcpdump.] (#kethop)

****

<a name="tcpdump"></a>
###1.Tcpdump là gì?]

- Là công cụ được phát triển để nhằm mục đích phân tích các gói dữ liệu mạng theo dòng lệnh. Nó cho phép khách hàng chặn và hiển thị các gói tin được truyền đi hoặc được nhận trên một mạng máy tính có tham gia.
- Tcpdump xuất ra màn hình nột dung các gói tin (chạy trên card mạng mà máy chủ đang lắng nghe) phù hợp với biểu thức logic chọn lọc mà khách hàng nhập vào. Với từng loại tùy chọn khác nhau thì người sử dụng có thể xuất những mô tả về gói tin này ra một file "pcap" với tùy chọn `-r` của lệnh tcpdump, hoặc sử dụng các phần mềm khác như là WireShark, windump.
- Trong trường hợp không có tùy chọn thì lệnh Tcpdump sẽ tiếp tục chạy cho đến khi nào đó nhận được một tín hiệu ngắt từ khách hàng. Sau khi kết thúc việc bắt các gói tin, tcpdump sẽ báo cho người sử dụng những cột sau:
 <ul>
 <li>Packet capture : số lượng gói tin bắt được và xử lý.</li>
 <li>Packet received by filter : số lượng gói tin được nhận bởi bộ lọc.</li>
 <li>Packet dropped by kernel : Số lượng packet đã bị dropped bởi cơ chế bắt gói tin của hệ điều hành.</li>
 </ul>
<a name="option"></a>
###2. Một số tùy chọn trong dụng trong lệnh tcpdump.

- `-i` sử dụng tùy chọn này khi người sử dụng cần chụp các gói tin trên interfaces chỉ định.
- `-D` khi sử dụng tùy chọn này tcpdump sẽ liệt kê ra tất cả các interface hiện hữu trên máy mà có thể capture được.
- `-c N` khi sử dụng tùy chọn này tcpdump sẽ ngừng hoạt động khi đã capture N gói tin.
- `-n` khi sử dụng tùy chọn này tcpdump sẽ không phân giải địa chỉ IP sang hostname.
- `-nn` khii sử dụng tùy chọn này tcpdump không phân giải địa chỉ sang host name và cũng không phân giải cả portname.
- `-v` tăng khối lượng thông tin mà bạn mà gói tin có thể nhận được , thậm chí có thể tăng thêm với tùy chọn `-vv` và `-vvv`
- `-X` hiển thị thông tin dưới dạng mã HEX hoặc ACSII.
- `-XX` hiển thị thông tin dưới dạng mã HEX hoặc ACSII chuyển đôi luôn cả Ethernet header.
- `-A` hiển thị các packet được capture dưới dạng ACSII.
- `-S` Khi tcpdump capture packet, thì nó sẽ chuyển các số sequence number, ACK thành các relative sequense number, relative ACK. Nếu sử dụng option –S này thì nó sẽ không chuyển mà sẽ để mặc định.
- `-F filename`  Dùng để filter các packet với các luật đã được định trước trong tập tin filename.
- `-e`  Khi sử dụng option này, thay thì hiển thị địa chỉ IP của người gửi và người nhận, tcpdump sẽ thay thế các địa chỉ này bằng địa chỉ MAC.
- `-t`  Khi sử dụng option này, tcpdump sẽ bỏ qua thời gian bắt được gói tin khi hiển thị cho khách hàng.
- `-tt` Khi sử dụng option này, thời gian hiển thị chính là thời gian chênh lệnh giữa thời gian tcpdump bắt được gói tin của gói tin và gói tin đến trước nó.
- `-ttt`  Khi sử dụng option này, sẽ hiển thị thêm ngày vào mỗi dòng lệnh.
- `-tttt` Khi sử dụng option này, sẽ hiển thị thêm ngày vào mỗi dòng lệnh.
- `-ttttt` Khi sử dụng option này, thời gian hiển thị trên mỗi dòng chính là thời gian chênh lệch giữa thời gian tcpdump bắt được gói tin của gói tin hiện tại và gói tin đầu tiên.
- `-K` Với option này tcpdump sẽ bỏ qua việc checksum các gói tin.
- `-N` Khi sử dụng option này tcpdump sẽ không in các quality domain name ra màn hình.
- `-B size` Sử dụng option này để cài đặt buffer_size .
- `-L` Hiển thị danh sách các datalink type mà interface hỗ trợ.
- `-y` Lựa chọn datalinktype khi bắt các gói tin.
<a name="ddc"></a>

###3. Định dạng chung của một dòng giao thức tcpdump.

Định dạng chung của một dòng giao thức tcpdump là :

> time-stamp src > dst:  flags  data-seqno  ack  window urgent options

Trong đó: 
 <ul>
 <li>Time-stamp: hiển thị thời gian gói tin được capture.</li>
 <li>Src và dst: hiển thị địa IP của người gởi và người nhận.</li>
 <li>Cờ Flag thì bao gồm các giá trị sau:
  <ul>
  <li>S(SYN):  Được sử dụng trong quá trình bắt tay của giao thức TCP.</li>
  <li>.(ACK):  Được sử dụng để thông báo cho bên gửi biết là gói tin đã nhận được dữ liệu thành công.</li>
  <li>F(FIN): Được sử dụng để đóng kết nối TCP.</li>
  <li>P(PUSH): Thường được đặt ở cuối để đánh dấu việc truyền dữ liệu.</li>
  <li>R(RST): Được sử dụng khi muốn thiết lập lại đường truyền.</li>
  </ul>
 <li>Data-sqeno: Số sequence number của gói dữ liệu hiện tại.</li>
 <li>ACK: Mô tả số sequence number tiếp theo của gói tin do bên gởi truyền (số sequence number mong muốn nhận được).</li>
 </li>
 <li>Window: Vùng nhớ đệm có sẵn theo hướng khác trên kết nối này.</li>
 <li>Urgent: Cho biết có dữ liệu khẩn cấp trong gói tin.</li>
 </ul>

Ví dụ khi bắt gói tin khi kết nối FTP vào trong máy ảo.

![scr2](http://i.imgur.com/C4ZzLmn.png)
<a name="boloc"></a>
###4. Một số bộ lọc cơ bản.

- `dst A` Khi sử dụng option này, tcpdump sẽ chỉ capture các gói tin có địa chỉ đích là “A”, có thể sử dụng kèm với từ khóa net để chỉ định một dãy mạng cụ thể. Ví dụ: tcpdump dst net 192.168.1.0/24.
- `src A` Tương tự như option dst, nhưng thay vì capture các gói tin có địa chỉ đích cụ thể thì nó sẽ capture các gói tin có địa chỉ nguồn như quy định.
- `host A`  Khi sử dụng option này, tcpdump sẽ chỉ capture các gói tin có địa chỉ nguồn hoặc địa chỉ đích là “A”.
- `port / port range` Khi sử dụng option này, tcpdump sẽ chỉ capture các gói tin có địa chỉ port được chỉ định rõ, hoặc nằm trong khoảng range định trước. Có thể sử dụng kèm với option dst hoặc src.
- `less` Khi sử dụng từ khóa này, tcpdump sẽ lọc (filter) các gói tin có dung lượng nhỏ hơn giá trị chỉ định.
- `greater` Khi sử dụng từ khóa này, tcpdump sẽ lọc (filter) các gói tin có dung lượng  cao hơn giá trị chỉ định.
- `(ether | ip) broadcast` Capture các gói tin ip broadcast hoặc ethernet broadcast.
- `(ether | ip | ip6) multicast` Capture các gói tin ethernet, ip , ipv6 multicast.
Ngoài ra, tcpdump còn có thể capture các gói tin theo các protocol như : udp, tcp, icmp, ipv6  (chỉ cần gõ trực tiếp các từ khóa vào là được). Ví dụ: tcpdump icmp.
<a name="kethop"></a>
###5. Một số kết hợp trong tcpdump.

- AND: Sử dụng từ khóa and hoặc &&.
- OR: Sử dụng từ khóa or hoặc ||.
- EXCEPT: sử dụng từ khóa not hoặc !.
- Ngoài ra để gom nhóm các điều kiện ta có thể dùng cặp từ khóa ‘’.  Ví dụ: tcpdump –i eth0 ‘dst host 192.168.1.1 or 192.168.1.10 or 192.168.1.11’.
