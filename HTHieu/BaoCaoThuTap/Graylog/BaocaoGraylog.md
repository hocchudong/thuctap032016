Elasticsearch là nền tẳng tìm kiếm thời gian thực nghĩa thời gian tìm kiếm thấp

Cluster là cụm máy lưu trữ toàn bộ dữ liệu, đánh chỉ số và thực hiện tìm kiếm dữ liệu.Mỗi Cluster xác định 1 tên duy nhất

Node là 1 máy trong cụm Cluster xác định bằng tên

Index là 1 bộ các tài liệu có đặc điểm tương tự nhau xác định bằng tên

Type là thành phần trong index,có thể có 1 hoặc nhiều type là một danh mục/phân vùng logic trong index, có vài trường phổ biến,

Document là đơn vị cơ bản của thông tin mà có thể đánh chỉ số,có thể lưu số lượng tùy ý trong 1 index/Type,cho dù trong 1 index nhưng vẫn phải phân vào type nhát định trong type

Shard & Replica
Chỉ số thể hiện khả năng luuw trữ vượt giới hạn về phần cứng
Shard:các tài liệu nhỏ được chia ra từ lại liệu gôc bởi Elasticsearch
Shard có thể thay đôi kích thước nội dung, cho phép phân tán và thực hiện song với phép toán
Replica là bản copy index của shard nhằm tránh mất mát dữ liệu khi truyền giữa các máy hoặc khi node offline

Cluster

Tương tác qua REST api để xem tình trạn của cluster,điều khiển,thực hiện lệnh,xử lý tìm kiếm nâng cao

Elasticsearch làm  nhiệm vụ lưu trữ và tìm kiếm dữ liệu dựa trên thư viện lucene

Mongodb là một mã nguồn mở và hệ quản trị dữ liệu nosql viết = c++ và trên khái niệm collection và Document

Collection là một nhóm tài liệu tương đương với table và không có ràng buộc
Document có cấu trúc như Json

Mongodb thực hiện lưu trữ các file cấu hình của dashboard,stream,...,metadata

Mongodb tương tác với graylog server qua cơ chế client server

Elasticsearch tương tác vơi graylog server qua api bằng việc coi nó như 1 node trong Cluster

Chú ý cấu hình graylog collector

file cấu hình trên linux /etc/graylog/collector/collector.conf

server-url:gửi các hoạt động tới graylog server

Nhập đầu vào trong input cần chú ý type(nên đê là file) và path
