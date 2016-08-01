# Báo cáo tìm hiểu graylog

## I.Tìm hiểu chung

- <b>`Graylog`</b> là phần mềm mã nguồn mở được tạo ra với mục đích là thu thập log có thể chạy trên linux

- Link trang chủ : <b><u>https://www.graylog.org/</u></b>

- Phiên bản mới <b>`Graylog`</b> nhất là `v2.0.3` ra đời ngày `20/06/2016`

- <b>`Graylog`</b> tạo bỏi <b>`Lennart Koopman`</b> vào năm `2010` với tên bản `beta`(phiên bản `0.x.x`) là <b>`Graylog2`</b>

- `2/2014`, phát hành <b>`Graylog2`</b> `V0.20.0 Final`.

- 19/02/2015, ra mắt bản chính thức tên <b>`Graylog`</b> phiên bản `1.0.0`

- <b>`Graylog`</b> viết bằng ngôn ngữ <b>`java`</b>

- Từ bản `1.0.0` đến bản mới nhất có `21` phiên bản chính thức

- Ứng dung <b>`Graylog`</b> trong `cloud computing`:
<ul>
<li><b>SSH</b> : Thống kê <b>user</b>, <b>ip</b> đăng nhập, số lần đăng nhập <b>SSH</b> thành công, thất bại, tổng số lần đăng nhập.</li>
<li><b>OpenVPN</b> : Thống kê <b>user</b>, <b>ip</b> đăng nhập , <b>ip</b> được cấp <b>VPN</b> trên hệ thống Lab và hệ thống thực.</li>
<li><b>OpenStack</b> : Thống kê <b>user</b>, số lần đăng nhập <b>dashboard</b> thành công và thật bại, số máy ảo được tạo, xóa, hỏng.</li>

<li> `SSH` : Thống kê `user`, `ip` đăng nhập, số lần đăng nhập `ssh` thành công, thất bại, tổng số lần đăng nhập.</li>
<li> `OpenVPN` : Thống kê `user`, `ip` đăng nhập , `ip` được cấp `VPN` trên hệ thống Lab và hệ thống thực.</li>
<li> <b>OpenStack</b> : Thống kê `user`, số lần đăng nhập `dashboard` thành công và thật bại, số máy ảo được tạo, xóa, hỏng.</li>
</ul>

## II.Kiến trúc Graylog

### 2.1 Kiến trúc tổng quát
<br>
<img src=http://imgur.com/5pNaT07.png>
<br>

- <b>`Graylog`</b> có 4 thành phần chính là:
<ul>
<li><b>`Graylog-server`</b>
<li><b>`Mongodb-server`(gọi tắt là `Mongodb`)</b></li>
<li><b>`Elasticsearch`</b></li>
<li><b>`Web-interface`</b></li>
</ul>
<br>
- 2 mô hình triển khai là [`all-in-one`](#all in one),[`mô hình mở rông ( Bigger Production )`](#mo rong)

- Trong mô hình <b>`Graylog2-server`</b> sẽ nhận `log` từ các `log source` từ các `Log Source` qua các giao thức mạng là <b>`TCP,UDP,HTTP`</b>

- <b>`Graylog-server`</b>: thực hiện xử lý `log`, kết nối ,truyền thông tới <b>`Mongodb`</b> và <b>`Elasticsearch`</b>, và quản lý <b>`Web-interface`</b> nên bị ảnh hưởng bởi `CPU`

- <b>`Elasticsearch`</b> thực hiện lưu trữ tìm kiếm `log` nên bị ảnh hưởng bởi tốc độ `I/O`,`RAM`,tốc độ ổ đĩa

- <b>`Mongodb`</b> lưu trữ cấu hình người dùng,`metadata` nên cần cấu hình thấp

- <b>`Web-interface`</b> cung cấp giao diện trên `web` cho người dùng

### 2.2 Mô hình triển khai

#### 2.2.1 Mô hình triển khai trên 1 máy ( all-in-one )<a name="all in one"/>
<br>
<img src=http://docs.graylog.org/en/2.0/_images/simple_setup.png>
<br>

#### 2.2.2 Mô hình triển khai mở rộng ( Bigger Production )<a name="mo rong"/>

<br>
<img src=http://docs.graylog.org/en/2.0/_images/extended_setup.png>
<br>

### 2.3 Tương tác Graylog-server với Elasticsearch
<br>
<img src=http://i.imgur.com/VtXdsGw.png>
<br>
- <b>`Graylog-server`</b> được coi như là một `Node` trong `Elasticsearch Cluster` tương tác `Node` qua `API` cụ thể là `Discovery-zen-ping`

- <b>`Graylog-server`</b> sẽ phải khai báo như là một `Node` để kết nối với `Elasticsearch Cluster`

- Phiên bản <b>`Elasticsearch`</b> với <b>`Graylog-server`</b>

|Graylog version|Elasticsearch version|
|---------------|---------------------|
|1.2.0-1.2.1|1.7.1|
|1.3.0-1.3.3|1.7.3|
|1.3.4|1.7.5|
|2.0.0|2.3.1|
|2.0.1-2.0.3|2.3.2|
<br>
#### Tương tác Mongodb với Graylog-server
<br>
<img src=http://i.imgur.com/ZhUFhBg.png>
<br>
- <b>`Graylog-server`</b> tương tác với <b>`Mongodb`</b> theo cơ chế `client-server` với <b>`Graylog-server`</b> là `client` được cài `Mongodb client driver` và  <b>`Mongodb`</b> là `server`

## III.Elasticsearch

### 3.1 Tổng quát Elasticsearch
- <b>`Elasticsearch`</b> là server chạy trên nền tảng `Apache Lucene` cung cấp `API` tìm kiếm lưu trữ
hay đơn giản là một `search engine`

- `Elasticsearch` phát triển bằng `java`

- Phần mềm tương tự:`Solr`

- `Node` là một `server` `Elasticsearch`, trung tâm hoạt động của `Elasticsearch`,lưu trữ toàn bộ dữ liệu để có thể thực hiện công việc lưu trữ và tìm kiếm.

- `Cluster` là tập hợp `node` chia sẻ cùng thuộc tính `Cluster.name`. Mỗi `Cluster` có một node chính(`master`) được lựa chọn tự động . Một `server` có thể có 1 hoặc nhiều `node`.Các nốt kết nối với nhau qua giao thức `unicast`

- `Type` là `document` , thành phần trong `index`,có thể có 1 hoặc nhiều `type`

- `Document` là đơn vị cơ bản của thông tin mà có thể đánh chỉ số,ở đinh dạng `JSON`(`JavaScript Object Notation`) ,phải có `type` nhất định

### 3.2 Cấu trúc Elasticsearch
<br>
<img src=http://i.imgur.com/0dGwgsZ.png>

- Trong `Cluster` các `node` liên lạc với nhau bằng `API` và nhận diện nhau bằng `unicast-discovery`

### 3.3 Shard

- `Shard` phần được chia nhỏ `index`

- `Shard` được tạo ra với mục đích quản lý khối lượng nội dung theo chiều ngang(`horizontally`),phân phát và thực hiện đồng bộ qua `shard` do đó dẫn đến nâng cao hiệu năng chương trình

- `Shard` dùng để lưu trữ dữ liệu có hai loại là `primary shard` và `replica shard`

- `Primary Shard` Nếu hình dung quan hệ `master-slave` như `MySQL` thì `primary shard` là `master`. Dữ liệu được lưu tại 1 `primary shard`, được đánh `index` ở đây trước khi chuyển đến `replica shard`

- `Replica Shard` có thể có hoặc không có, dùng để `backup` dữ liệu cho `primary shard` để bảo toàn dữ liệu khi gặp sự cố,đồng thời ngăn chặn truy cập vào `node` gặp sự cố và tự động chuyển `node`
<br>

<img src=http://i.imgur.com/PcPzxUt.png>

### 3.4 index

- `Index` là 1 bộ các tài liệu(`document`) có đặc điểm tương tự nhau xác định bằng tên

- <b>`Graylog-server`</b> sẽ phải khai báo như là một `Node` để kết nối với `Elasticsearch Cluster`

- Phiên bản <b>`Elasticsearch`</b> với <b>`Graylog-server`</b>

|Graylog version|Elasticsearch version|
|---------------|---------------------|
|1.2.0-1.2.1|1.7.1|
|1.3.0-1.3.3|1.7.3|
|1.3.4|1.7.5|
|2.0.0|2.3.1|
|2.0.1-2.0.3|2.3.2|
<br>
#### Tương tác Mongodb với Graylog-server
<br>
<img src=http://i.imgur.com/ZhUFhBg.png>
<br>
- <b>`Graylog-server`</b> tương tác với <b>`Mongodb`</b> theo cơ chế `client-server` với <b>`Graylog-server`</b> là `client` được cài `Mongodb client driver` và  <b>`Mongodb`</b> là `server`

## III.Elasticsearch

### 3.1 Tổng quát Elasticsearch
- <b>`Elasticsearch`</b> là server chạy trên nền tảng `Apache Lucene` cung cấp `API` tìm kiếm lưu trữ

- `Node` là một `server` `Elasticsearch`, trung tâm hoạt động của `Elasticsearch`. Lưu trữ toàn bộ dữ liệu để có thể thực hiện công việc lưu trữ và tìm kiếm.

- `Cluster` là tập hợp `node` chia sẻ cùng thuộc tính `Cluster.name`. Mỗi `Cluster` có một node chính(`master`) được lựa chọn tự động . Một `server` có thể có 1 hoặc nhiều `node`.Các nốt kết nối với nhau qua giao thức `unicast`

- `Index` là 1 bộ các tài liệu có đặc điểm tương tự nhau xác định bằng tên

- `Type` là thành phần trong index,có thể có 1 hoặc nhiều type là một danh mục/phân vùng logic trong index, có vài trường phổ biến,

- `Document` là đơn vị cơ bản của thông tin mà có thể đánh chỉ số,có thể lưu số lượng tùy ý trong 1 index/Type,cho dù trong 1 index nhưng vẫn phải phân vào type nhát định trong type

- `Shard` là các đối tượng của Lucene dùng để lưu trữ dữ liệu có hai loại là primary shard và replica shard

- `Primary Shard` Nếu hình dung quan hệ master-slave như MySQL thì primary shard là master. Dữ liệu được lưu tại 1 primary shard, được đánh index ở đây trước khi chuyển đến replica shard

- `Replica Shard` có thể có hoặc không có, đảm bảo khi primary shard có sự cố thì dữ liệu vẫn toàn vẹn và thay thế được primary shard, đồng thời tăng tốc độ đọc

- Điểm mạnh của Elasticsearch chính là tính phân tán cũng như khả năng mở rộng rất tốt của nó.

- Elasticsearch cho phép bạn mở rộng server theo chiều ngang một cách đơn giản, không có bất cứ thay đổi gì ở phía ứng dụng, cũng gần như không tốn chút nỗ lực nào.

- Lưu trữ dữ liệu:
<ul>
<li>Công thức : `Default
shard = hash(routing) % number_of_primary_shards`</li>
<li> Hash là một hàm tính toán cố định của Elasticsearch, routing là 1 đoạn text duy nhất theo document, thường là _id của document đó. number_of_primary_shards là số lượng primary shard của cluster. Gía trị shard này là đi kèm với document, nó được dùng để xác định shard nào sẽ lưu document và cũng dùng để cho routing</li>
</ul>

- Qúa trình lưu dữ liệu
<img src=https://viblo.asia/uploads/images/12825aa8ddacf0cbbe0a1a8e2009c461d467c567/154cb73dc5085cc32483e3964963d5459a43623f.png>
<ul>
<li> B1 : Request được gửi đến node master (Node 1). Tại đây thực hiện tính toán với công thức ở trên để tìm ra primary shard của document sẽ là 0.</li><br>
<li>B2:Sau khi xác định được primary shard là 0, request sẽ được gửi đến node 3, nơi chứa P0</li><br>
<li>B3:Node 3 thực hiện request và xử lý dữ liệu. Sau khi thành công, nó gửi tiếp request đến các replica shard ở Node 1 và Node 2 để đảm bảo dữ liệu thống nhất giữa các node.</li><br>
</ul>

- Qúa trình lấy dữ liệu

<img src=https://viblo.asia/uploads/images/12825aa8ddacf0cbbe0a1a8e2009c461d467c567/356483459fafa708f9cb9ad674466811236125ae.png>
<ul>
<li>B1 : Request được gửi đến node master (Node 1). Tại đây xác định primary shard cho document sẽ là 0.</li><br>
<li>B2 : Do tất cả node đều lưu dữ liệu, nên master node sẽ chọn ra 1 node và lấy dữ liệu ở shard số 0. Việc chọn này giúp giảm tập trung vào một node. Thuật toán Round-robin được sử dụng để các shard được chọn khác nhau ở mỗi request. Trong trường hợp này Node 2 được chọn.</li><br>
<li>B3 : Replica 0 ở Node 2 trả về kết qủa cho master node.</li>
</ul>

- Tìm kiếm dữ liệu phân tán
<ul><br>
<li>B1 : Công đoạn truy vấn
Node nhận request (node trung gian) sẽ gửi broadcast request đó đến tất cả các node khác. Tại mỗi node này sẽ chỉ định shard thực hiện công việc tìm kiếm theo yêu cầu. Shard có thể là primary hoặc replica shard.
Mỗi shard sẽ thực hiện công việc tìm kiếm, trả về id và score của document. Trong đó score là gía trị dùng để sắp xếp. Danh sách gồm id, score này là một danh sách đã được sắp xếp, mang tính chất cục bộ.
Node trung gian sau khi nhận kết qủa trả về từ các node khác sẽ thực hiện công việc sắp xếp toàn cục tất cả các document, dựa theo id và score. Cuối cùng trả ra kết qủa về phía client.</li><br>
<li>B2: Công đoạn lấy dữ liệu
Gói gọn trong hai bước query (truy vấn) và fetch (lấy dữ liệu)
Trong mọi trường hợp, Elasticsearch sẽ phải tính toán score cho from + size bản ghi TRÊN MỖI SHARD. Do vậy, số lượng bản ghi cần được cho vào sắp xếp là number_of_shards * (from + size).
Elasticsearch vẫn có biện pháp giải quyết cho việc phân trang sâu, sử dụng scroll</li>
</ul>

## III.Graylog

- Graylog-collector:ứng dụng viết bằng java dùng để  thu thập log và tương tác Graylog-server qua api


## IV.Mongodb

- Collection: là nhóm các tài liệu(document), tương đương table trong csdl

- Document : cấu trúc như kiểu JSON

## V.Tài liệu

https://viblo.asia/dinhhoanglong91/posts/ZnbRlr6lG2Xo
