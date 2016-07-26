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

Vid dụ: gửi 1tb dữ liệu

TH1:Gửi từ vn qua sing thì phải dùng tcp để đảm bảo không mất dữ liệu hoặc giả mạo dữ liệu dù tốc độ có chậm hơn không thẻ dùng udp vì dẫn đến mất mát dữ liệu hoặc bị giả mạo dữ liệu

TH2:Gửi từ tầng 15 xuống tầng 3 trong 1 toàn nhà thì dùng udp để thực hiện nhanh việc truyền dữ liệu qua hệ thống mạng lan trong tòa nhà vì mạng lan có tính bảo mật cao

- Ưu điểm log tập trung:

Ví dụ:để quản lý,theo dõi 100 máy chủ nếu không dùng log tập trung thì ta cần ssh vào từng máy hay đến từng máy để theo dõi và cần một lượng lớn quản trị viên để thực hiện gây nhiều bất tiện,gây tiêu tốn tiền bạc,thời gian,nhân lực đặc biệt khi các máy chủ ở các địa điểm khác nhau.Với log tập trung ta chỉ cần 1 máy chủ log sau đó cần vài người để phân tích các log hay cài tiện ích để phân tích log làm tiết kiệm chi phí, nhân lực

## Cấu trúc Rsyslog

- Có thể chia thành 3 phân chính: module đầu vào, hệ thống xử lý, module đầu ra

- Module đầu vào làm nhiệm vụ tiếp nhận các luồng tin nhắn

- Hệ thống xử lý gồm có Preprocessor,hàng đợi chính,hệ thống lọc và phân tích tin nhắn,hàng đợi của các hành động,Xử lý hành động

- Module đầu ra tạo thành các output

- Cơ chế làm việc:các module đầu vào nhận các tin nhắn qua các luồng khác nhau, chuyển đên Preprocessor để xử lý tin nhắn và đưa vào hàng đợi chính rồi vào hệ thống lcoj và phân tích tin nhắn rồi vào hàng đợi cảu hành đông tương úng và vào hệ thống xử lý hành động và thành output
