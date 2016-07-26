#Giải thích Rsyslog Data flow

<img src=http://www.rsyslog.com/doc/dataflow.png>

- Tin nhắn(`messages`) vào từ bên trái ở 'input modules' qua `Preprocessor`(tiền xử lý) vào hàng đợi chính(`main queue`) ra khỏi hàng đợi vào hệ thống lọc và phân tích(`parser & filter engine`)
sau đó lại được đưa vào hàng đợi của hành động sao đó rời `rsyslog` tại `output module`

- Mỗi hành động có thể được thiết lập một chế độ hàng đợi, hàng đợi mặc đinh còn gọi là 'direct mode' mà nó không thực sự `enqueue data`

- Ảnh hưởng đến Preprocessor là cpu vì thực hiện việc phân luồn nhiều luồngtin nhắn 1 lúc

- Ảnh hưởng đến queue là bộ nhớ do nó à 1 cấu trúc dữ liệu dùng để sắp xếp lưu trữ tin nhắn

- Ảnh hưởng đến parser & filter là cpu vì thực hiện việc phân tích tin nhắn

- Ảnh hưởng đến action queue là bộ nhớ vi nó lưu tin nhắn trước khi thực hiện hành động

- Ảnh hưởng đến Action-processor là cpu và bộ nhớ vì thực hiện các hành động và tạo ra output

Ưu điểm log tập trung:

Có 100 máy để theo dõi thì cần ssh 100 máy này hoặc đẩy log về 100 máy khác để theo dõi hoặc đến tạn địa đểm 100 máy này và đội ngũ quản trị viên để quản lý =>tốn thêm chi phí ,nhân lực
Dùng log tập trung thì việc tập trung 100 máy này về 1 máy thì sẽ tiết kiệm chi phí và nhân lực
và ta có thể viết các tiện ích để giám sát máy dễ dàng

so sánh tcp và dp:

|TCP|UDP|
|---|---|
|Đều là giao thưc mạng để truyên tin||
| 20buyte header|8bytes header|
|Hoạt động theo hướng kết nối|Hoạt động theo hướng không kết nối|
|Bảo mật cao|Bảo mật thấp|
|Vì có theo dõi gói tin gửi đi nên khi mất mát gói tin thì ta sẽ biết được và thực hiện thao tác phòng ngừa bảo mật|không giám sát gói tin nên dễ bị giả mạo ip đích đến dẫn đến mất dữ liệu|
|Dùng khi hệ thống mạng nhiều nguy cơ như internet hoặc trong hệ thống mạng có tính bảo mật cao nhưng dung lượng chuyển log không quá lớn hoặc file gửi đi có mức độ quan trọng lớn|dùng trong mạng hệ thống bảo mật cao hoặc file gửi đi mức độ quan trọng thấp|
|use case: có 1tb gói tin gửi từ vn đến sing thì dùng giao thức nào||
|dùng tcp vì để chuyển 1tb dữ liệu dung lượng tuy lớn nhưng sử dụng internet vì từ vn qua sing không dùng mạng lan được thế nên đảm bảo an toàn thì phải dùng tcp||
|nếu co 1tb dữ liệu nhưng trong cùng một tòa nhà cùng hệ thống mạng lan vì nhanh và mạng lan có tính bảo mật cao||
|tcp chậm hơn udp vì phải thực hiên 2 thao tác gửi và đợi,kiểm tra gói tin gửi đi còn udp thì chỉ gửi không kiểm tra gói tin||
