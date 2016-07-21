#Giải thích Rsyslog Data flow

<img src=http://www.rsyslog.com/doc/dataflow.png>

- Tin nhắn(`messages`) vào từ bên trái ở 'input modules' qua `Preprocessor`(tiền xử lý) vào hàng đợi chính(`main queue`) ra khỏi hàng đợi vào hệ thống lọc và phân tích(`parser & filter engine`)
sau đó lại được đưa vào hàng đợi của hành động sao đó rời `rsyslog` tại `output module`

- Mỗi hành động có thể được thiết lập một chế độ hàng đợi, hàng đợi mặc đinh còn gọi là 'direct mode' mà nó không thực sự `enqueue data`

- Chuyển luồng:
