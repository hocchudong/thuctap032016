# Báo cáo tìm hiểu graylog

## I.Khái niệm

- Elasticsearch là server chạy trên Apache lucene cung cấp API tìm kiếm lưu trữ

- Graylog Tương tác Elasticsearch qua REST api để xem tình trạn của cluster,điều khiển,thực hiện lệnh,xử lý tìm kiếm nâng cao

- Mongodb là một mã nguồn mở và hệ quản trị dữ liệu nosql viết = c++ và trên khái niệm collection và Document

- Mongodb thực hiện lưu trữ các file cấu hình của dashboard,stream,...,metadata

- Mongodb tương tác với graylog server qua cơ chế client server

- Elasticsearch tương tác vơi graylog server qua api bằng việc coi nó như 1 node trong Cluster

## II.Elasticsearch

- Điểm mạnh của Elasticsearch chính là tính phân tán cũng như khả năng mở rộng rất tốt của nó.

- Elasticsearch cho phép bạn mở rộng server theo chiều ngang một cách đơn giản, không có bất cứ thay đổi gì ở phía ứng dụng, cũng gần như không tốn chút nỗ lực nào.

- Node Một server Elasticsearch, trung tâm hoạt động của Elasticsearch. Lưu trữ toàn bộ dữ liệu để có thể thực hiện công việc lưu trữ và tìm kiếm.

-Collection là một nhóm tài liệu tương đương với table và không có ràng buộc

- Document có cấu trúc như Json là bản ghi lưu trữ dữ liệu

- Cluster là tập hợp node chia sẻ cùng thuộc tính Cluster.name. Mỗi Cluster có một node chính(master) được lựa chọn tự động . Một server có thể có 1 hoặc nhiều node.Các nốt kết nối với nhau qua giao thức unicast

- Index là 1 bộ các tài liệu có đặc điểm tương tự nhau xác định bằng tên

- Type là thành phần trong index,có thể có 1 hoặc nhiều type là một danh mục/phân vùng logic trong index, có vài trường phổ biến,

- Document là đơn vị cơ bản của thông tin mà có thể đánh chỉ số,có thể lưu số lượng tùy ý trong 1 index/Type,cho dù trong 1 index nhưng vẫn phải phân vào type nhát định trong type

- Shard là các đối tượng của Lucene dùng để lưu trữ dữ liệu có hai loại là primary shard và replica shard

- Primary Shard Nếu hình dung quan hệ master-slave như MySQL thì primary shard là master. Dữ liệu được lưu tại 1 primary shard, được đánh index ở đây trước khi chuyển đến replica shard

- Replica Shard có thể có hoặc không có, đảm bảo khi primary shard có sự cố thì dữ liệu vẫn toàn vẹn và thay thế được primary shard, đồng thời tăng tốc độ đọc

- Lưu trữ dữ liệu:công thức
<ul>
<li>`Default
shard = hash(routing) % number_of_primary_shards`</li>
<li> Hash là một hàm tính toán cố định của Elasticsearch, routing là 1 đoạn text duy nhất theo document, thường là _id của document đó. number_of_primary_shards là số lượng primary shard của cluster. Gía trị shard này là đi kèm với document, nó được dùng để xác định shard nào sẽ lưu document và cũng dùng để cho routing</li>
</ul>

- Qúa trình lưu dữ liệu
<img src=https://viblo.asia/uploads/images/12825aa8ddacf0cbbe0a1a8e2009c461d467c567/154cb73dc5085cc32483e3964963d5459a43623f.png>
<ul>
<li> B1 : Request được gửi đến node master (Node 1). Tại đây thực hiện tính toán với công thức ở trên để tìm ra primary shard của document sẽ là 0.</li>
<li>B2:Sau khi xác định được primary shard là 0, request sẽ được gửi đến node 3, nơi chứa P0</li>
<li>B3:Node 3 thực hiện request và xử lý dữ liệu. Sau khi thành công, nó gửi tiếp request đến các replica shard ở Node 1 và Node 2 để đảm bảo dữ liệu thống nhất giữa các node.</li>
</ul>

- Qúa trình lấy dữ liệu

<img src=https://viblo.asia/uploads/images/12825aa8ddacf0cbbe0a1a8e2009c461d467c567/356483459fafa708f9cb9ad674466811236125ae.png>
<ul>
<li>b1:Request được gửi đến node master (Node 1). Tại đây xác định primary shard cho document sẽ là 0.</li>
<li>B2 : Do tất cả node đều lưu dữ liệu, nên master node sẽ chọn ra 1 node và lấy dữ liệu ở shard số 0. Việc chọn này giúp giảm tập trung vào một node. Thuật toán Round-robin được sử dụng để các shard được chọn khác nhau ở mỗi request. Trong trường hợp này Node 2 được chọn.</li>
<li>B3 : Replica 0 ở Node 2 trả về kết qủa cho master node.</li>
</ul>
- Tìm kiếm dữ liệu phân tán
<ul>
<li>B1:Công đoạn truy vấn
Node nhận request (node trung gian) sẽ gửi broadcast request đó đến tất cả các node khác. Tại mỗi node này sẽ chỉ định shard thực hiện công việc tìm kiếm theo yêu cầu. Shard có thể là primary hoặc replica shard.
Mỗi shard sẽ thực hiện công việc tìm kiếm, trả về id và score của document. Trong đó score là gía trị dùng để sắp xếp. Danh sách gồm id, score này là một danh sách đã được sắp xếp, mang tính chất cục bộ.
Node trung gian sau khi nhận kết qủa trả về từ các node khác sẽ thực hiện công việc sắp xếp toàn cục tất cả các document, dựa theo id và score. Cuối cùng trả ra kết qủa về phía client.</li>
<li>B2:Công đoạn lấy dữ liệu
Gói gọn trong hai bước query (truy vấn) và fetch (lấy dữ liệu)
Trong mọi trường hợp, Elasticsearch sẽ phải tính toán score cho from + size bản ghi TRÊN MỖI SHARD. Do vậy, số lượng bản ghi cần được cho vào sắp xếp là number_of_shards * (from + size).
Elasticsearch vẫn có biện pháp giải quyết cho việc phân trang sâu, sử dụng scroll</li>
</ul>

## II.Graylog

- Graylog-collector:ứng dụng viết bằng java dùng để  thu thập log và tương tác Graylog-server qua api
