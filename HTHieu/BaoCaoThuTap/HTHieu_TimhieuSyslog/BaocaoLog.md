# Báo cáo tim hiểu log

## Khái niêm

- Log là file clear text lưu lại nọi hoạt động của máy tính

- Syslog là giao thức truyền file log thông qua giao thức mạng tcp hoạc udp

- Rsyslog là ừng dụng truyền log qua giao thức syslog và viết bằng c chạy trên linux

- Log tập trung là tập trung log nhiều máy về 1 máy hay 1 cụm máy chủ chứa log

- So sánh udp vs tcp:

Giống nhau: đều để truyền file log

Khác nhau: Tcp dùng truyền tin có hướng tức là có hoạt động theo dõi gói tin gửi đi còn udp thì ngược lại.Do đó udp sẽ nhanh hơn tcp và tcp sẽ đảm bảo an toàn hơn udp

Trường hợp sử dung:udp dùng cho hệ thống mạng có tính bảo mật cao hoặc truyền tin có mức độ quan trọng thấp.Tcp dùng trong hệ thống mạng có tính bảo mật thấp

Ví dụ: gửi 1tb dữ liệu

TH1 :Gửi từ vn qua sing thì phải dùng tcp để đảm bảo không mất dữ liệu hoặc giả mạo dữ liệu dù tốc độ có chậm hơn không thẻ dùng udp vì dẫn đến mất mát dữ liệu hoặc bị giả mạo dữ liệu

TH2:Gửi từ tầng 15 xuống tầng 3 trong 1 toàn nhà thì dùng udp để thực hiện nhanh việc truyền dữ liệu qua hệ thống mạng lan trong tòa nhà vì mạng lan có tính bảo mật cao

- Ưu điểm log tập trung:

Ví dụ:để quản lý,theo dõi 100 máy chủ nếu không dùng log tập trung thì ta cần ssh vào từng máy hay đến từng máy để theo dõi và cần một lượng lớn quản trị viên để thực hiện gây nhiều bất tiện,gây tiêu tốn tiền bạc,thời gian,nhân lực đặc biệt khi các máy chủ ở các địa điểm khác nhau.Với log tập trung ta chỉ cần 1 máy chủ log sau đó cần vài người để phân tích các log hay cài tiện ích để phân tích log làm tiết kiệm chi phí, nhân lực

## Log tập trung

- Log tập trung ra đời dựa trên yêu cầu các kĩ sư cần cái nhìn tổng quan về hệ thống mà đảm bảo tính chính xác dữ liệu và đáp ứng theo dõi hệ thống liên tục

- Log tập trung là tập trung các log của các máy khác nhau về 1 máy hay cụm máy chủ log

- Cấu trúc gồm có máy gửi log và máy nhận log

- Giao thức log tập trung sử dụng là syslog và tiện ích ở đây là Rsyslog

- Cơ chế làm việc: các máy gửi log sẽ gửi log thông qua giao thức mạng(tcp,udp) và giao thức log(syslog) đế máy nhận log và sử dụng phần mềm hỗ trợ như Rsyslog

- Ưu điểm:giúp quản trị viên có cái nhìn tổng quát về hệ thống, tiết kiêm thời gian và nhân lực, nếu bị tấn công thì sẽ xác định xu hướng tấn công,đả bảo tính toàn vẹn của hệ thống tức là biết chính xác những gì đã xảy ra hệ thống

- Nhược điểm:đòi hỏi tinh bảo mật cao nên yêu cầu về vật lực lớn,log có từ nhiều nguồn nhiều chủng loại, định dạng,hệ điều hành gây khó khă trong quản lý, yêu cầu về đội ngũ phân tích log

## Cấu trúc Rsyslog

- Có thể chia thành 3 phân chính: module đầu vào, hệ thống xử lý, module đầu ra

- Module đầu vào làm nhiệm vụ tiếp nhận các luồng tin nhắn

- Hệ thống xử lý gồm có Preprocessor,hàng đợi chính,hệ thống lọc và phân tích tin nhắn,hàng đợi của các hành động,Xử lý hành động

- Module đầu ra tạo thành các output

- Cơ chế làm việc:các module đầu vào nhận các tin nhắn qua các luồng khác nhau, chuyển đên Preprocessor để xử lý tin nhắn và đưa vào hàng đợi chính rồi vào hệ thống lcoj và phân tích tin nhắn rồi vào hàng đợi cảu hành đông tương úng và vào hệ thống xử lý hành động và thành output

- Bộ lọc filter sẽ thực hiện lọc tin nhắn và thực hiện hành động được xác đinh trong file cấu hình Rsyslog

Ví dụ Bạn muốn lọc một tin nhắn có cơ sở là local0 ,bắt đầu với "DEVNAME" và có "error1" hoặc "error0" trong nội dung dùng lệnh sau:
'if $syslogfacility-text == 'local0' and $msg startswith 'DEVNAME' and ($msg contains 'error1' or $msg contains 'error0') then /var/log/somelog'

Chú ý tất cả lệnh trên cùng 1 dòng. Trong đó `$syslogfacility-text` là cơ sở của log đang được lọc,`$msg` là nội dung của file log



## Cấu trúc tin nhắn


- pri là header field chứa thông tin về cơ sở và mức cảnh báo,không giải mã(giá trị đơn)

- rawmsg-after-pri: loại bỏ pri header thì giống rawmsg

- hostname:tên miền của máy gửi tin nhắn

- source: tên giả cho hostname

- fromhost:đưa ra thông tin của máy gửi

- fromhost-ip:giống fromhost nhưng trả lại là địa chỉ ip

- syslogTag:tag của tin nhắn

- programname:một phần của tag,xác định bởi BSD syslogd.

- pri-text:pri trong đinh dạng văn bản với sô pri nối vào trong dấu <>

- iut: phần mềm giám sát InfoUnitType

- syslogfacility:cơ sở của tin nhắn biểu hiện bằng số

- syslogfacility-text:giống trên nhưng thể hiện bằng dạng văn bản

- syslogseverity:mức cảnh báo của tin nhắn thể hiện dạng số

- syslogseverity-text:giống như trên nhưng thể hiện dạng văn bản

- syslogpriority:bí danh cho syslogseverity(vẫn là mức độ nghiêm trọng không giống pri)

- syslogpriority-text:giống trên nhưng ở dạng văn bản

- timegenerated:đánh dấu thời gian nhận được tin nhắn
