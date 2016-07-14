# Báo cáo tìm hiểu về syslog và rsyslog

## I.Tổng quát

- `Log` là file `clear-text` có thể dễ dàng đọc bởi các lệnh `cat,tail,head` và chỉnh sửa bởi  `vi,nano` dùng để ghi lại hoạt động của máy tính,phần mềm, tiến trình

- `Log` thường lưu tại `/var/log/`

- `TCP`: là viết tắt của `Transmission Control Protocol`. Đó là giao thức phổ biến nhất được sử dụng trên `Internet`.

<p>`TCP` hoạt động theo hướng kết nối ``(connection-oriented)``,
trước khi truyền dữ liệu giữa 2 máy, nó thiết lập một kết nối giữa 2 máy theo phương thức bắt tay
 3 bước ``(three-way-hand-shake)`` bằng cách gửi gói tin `ACK` từ máy đích sang máy nhận, trong suốt
 quá trình truyền gói tin, máy gửi yêu cầu máy đích xác nhận đã nhận đủ các gói tin đã gửi, nếu có
 gói tin bị mất, máy đích sẽ yêu cầu máy gửi gửi lại, thường xuyên kiểm tra gói tin có bị lỗi hay ko,
 ngoài ra còn cho phép qui định số lượng gói tin được gửi trong một lần gửi (window-sizing), điều này
  đảm bảo máy nhận nhận được đầy đủ các gói tin mà máy gửi gửi đi --> truyền dữ liệu chậm hơn `UDP` nhưng đáng tin cậy hơn `UDP`<p>

- `UDP` là viết tắt của `User Datagram Protocol` - một gói tương tự như một gói của thông tin.

`UDP` hoạt động theo hướng không kết nối ``(connectionless)``, không yêu cầu thiết lập kết nối giữa 2 máy gửi và nhận, ko có sự đảm bảo gói tin khi truyền đi cũng như không thông báo về việc mất gói tin, ko kiểm tra lỗi của gói tin --> truyền dữ liệu nhanh hơn UDP do cơ chế hoạt động có phần đơn giản hơn tuy nhiên lại ko đáng tin cậy bằng `TCP`

- `SSL/TLS`:là giao thức để xác thực và mã thông tin giữa `client` và `server` cụ thể là xác thực `server` , xác thực `client`, mã hóa đường truyền, hoạt động trên `TCP/IP` và dưới `HTTP`, `IMAP`, `FTP`

- Trong `syslog` thì `UDP`, `TCP` đảm bảo truyền nhận log từ `client` tới `server` và `SSL/TLS` đảm bảo an toàn đường truyền `log `

- `Syslog` là giao thức `client/server` dùng để chuyển log và thông điệp đến máy nhận log.Máy nhận thường gọi là `syslogd,syslog daemon,syslog server.syslog` gửi qua `UDP` hoặc `TCP` dưới dạng `clear-text` qua cổng `514`

- Mục cơ bản `syslog`:

|Mục|Miêu tả|
|---|-------|
|Facility (cơ sở)|Dấu hiệu nhận diện được sử dụng để miêu tả ứng dụng hoặc tiến trình mà đệ trình tới thông báo log. Các ví dụ là `mail`, `kernel`, và `ftp`.|
|Priority (độ ưu tiên)|Xác định độ ưu tiên của `log`|
|Selector (bộ chọn)|Sự kết hợp của nhiều `Facility` và `Priority` để xử lý sự kiện|
|Action (hành động)|Ghi thông tin tới `log`phản xạ thông tin tới một bàn điều khiển hoặc thiết bị khác, ghi thông báo tới hệ thống ghi `log` của người sử dụng hoặc gửi thông báo cùng với máy chủ `syslog` khác|

- Nguốn sinh `log`:

|Facility code|Keyword|Mô tả|
|-------------|-------|-----|
|0|kernel|Thông điệp từ kernel|
|1|user|Log ghi lại cấp độ người dùng|
|2|mail|Log của lại hệ thống mail|
|3|deamon|Log cảu hệ thống deamon|
|4|auth|Log bảo mật và xác thực|
|5|syslog|Log từ chương trình syslogd|
|6|lpr|Log từ quá trình in ấn|
|7|news|Thông tin từ hệ thống|
|8|uucp|Log UUCP ubsystem|
|9|-|Clock daemon|
|10|authpriv|giống auth|
|11|ftp|Log của FTP deamon|
|12|-|Log từ NTP sbsystem|
|13|-|Kiểm tra đăng nhập|
|14|-|Log cảnh báo|
|15|-|Log từ clock daemon|
|16-23|local 0 - local 7|Log dự trữ cho sử dụng nội bộ|

- Mức độ cảnh báo

|Code|Mức cảnh báo|Ý nghĩa|
|----|------------|-------|
|0|emerg|Tình trạng khẩn cẩp|
|1|alert|Hệ thống cần can thiệp ngay|
|2|crit|Tình trạng nguy kịch|
|3|error|Thông báo lỗi với hệ thống|
|4|warn|Mức cảnh báo với hệ thống|
|5|notice|Chú ý với hệ thống|
|6|info|Thông tin của hệ thống|
|7|debug|Quá trình kiểm tra hệ thống|

- Định dạng gói tin `syslog`:

< PRI > HEADER  MSG

Độ dài một thông báo không được vượt quá 1024 bytes

PRI
Phần PRI là một số được đặt trong ngoặc nhọn, thể hiện cơ sở sinh ra log hoặc mức độ
nghiêm trọng. là 1 số 8bit. 3 bit đầu tiên thể hiện cho tính nghiêm trọng của thông báo.5
bit còn lại đại diện cho sơ sở sinh ra thông báo.

Giá trị Priority được tính như sau: Cơ sở sinh ra log x 8 + Mức độ nghiêm trọng. Ví dụ,
thông báo từ kernel (Facility = 0) với mức độ nghiêm trọng (Severity =0) thì giá trị
Priority = 0x8 +0 = 0. Trường hợp khác,với "local use 4" (Facility =20) mức độ nghiêm
trọng (Severity =5) thì số Priority là 20 x 8 + 5 = 165.

Vậy biết một số Priority thì làm thế nào để biết nguồn sinh log và mức độ nghiêm trọng
của nó. Ta xét 1 ví dụ sau:

Priority = 191 Lấy 191:8 = 23.875 -> Facility = 23 ("local 7") -> Severity = 191 - (23 * 8 ) = 7 (debug)

HEADER

Phần Header thì gồm các phần chính sau
Time stamp -- Thời gian mà thông báo được tạo ra. Thời gian này được lấy từ thời gian hệ thống ( Chú ý nếu như thời gian của server và thời gian của client khác nhau thì thông báo ghi trên log được gửi lên server là thời gian của máy client)
Hostname hoặc IP
Message

Phần MSG chứa một số thông tin về quá trình tạo ra thông điệp đó. Gồm 2 phần chính:
Tag field
Content field

Tag field là tên chương trình tạo ra thông báo. Content field chứa các chi tiết của thông báo

## II.Tìm hiểu Rsyslog

### 1.Tổng quan về đầu vào thông điệp và đối tượng

Qua các module đầu vào, các thông điệp sẽ vào `rsyslog` rồi sao đó sẽ đến tập quy tắc để áp dụng quy tắc theo điều kiện.Khi đúng quy tắc , thông điệp sẽ được thực thi các yêu cầu của nó

### 2.Nguyên tắc xử lý

- Các thông điệp sẽ được đưa tới tập quy tắc ,nếu tập quy tắc không được ràng buộc cụ thể thì tập quy tắc mặc định sẽ được dùng

- Chỉ có một tập quy tắc mặc định

- Người dùng có thể thêm tập quy tắc

- Mỗi tập quy tắc có nhiều quy tắc hoặc không có quy tắc nào, nếu như không có không có quy tắc nào thì sẽ làm tập quy tắc trở nên vô nghĩa

- Mỗi tập quy tắc có một bộ lọc danh sách các hoạt động

- Bộ lọc đưa ra các quyết định `yes`/`no` do đó nó có khả năng kiểm soát khả năng của dòng thông điệp

- Nếu bộ lọc phù hợp(trả về `yes`) thì danh sách hoạt động sẽ được thực thi còn nếu là `no` thì chẳng có gì xảy ra

- Các quy tắc sẽ được đánh giá theo thứ tự từ đầu đến cuối trong tập quy tắc. Các quy tắc không thuộc tập quy tắc nào sẽ không được xử lý

- Mọi tập quy tắc đều luôn luôn được xử lý, không vấn đê gì nếu bộ lọc có phù hợp hay không. Nếu xử lý thông điệp có vấn đề thì hành động loại bỏ(`discard`) sẽ thực hiện,sau đó thông điệp sẽ dừng lại lập tức và không đánh giá thêm quy tắc nào nữa

- Một danh sách hành động thì gồm một hoặc nhiều hành động và không có thêm bộ lọc nào nữa

- Để thực hiện nhiều hoạt động cùng lúc thì có dấu `$` trong bộ lọc và nằm giữa hai hoạt động

- Các hoạt động bao gồm hoạt động gọi đến chính nó như các câu lệnh cấu hình tất cả hành động xác định????

- Nếu như định dạng `legacy` được $Action(hoạt động)... phải được xác định trước hành động họ định cấu hình

- Vài cấu hình  tự động chỉ thị cầu hình tham khảo  tới giá trị cũ sau khi được áp dụng, một số khác lại không

### 3.Đâu vào và đầu ra(input and output)

- Mọi đầu vào cần có module để tải chúng và định nghĩa hoạt động ,khi được nạp vào đầu vào được định nghĩa qua đối tượng `input()`

- Đầu ra thường dược gọi là `action`(hành động),một tập nhỏ các đầu ra sẽ được nạp vào còn lại sẽ nạp giống đầu vào


### 4. Các loại lệnh và file cáu hình

- File cấu hình là `/etc/rsyslog.conf`

- `sysklogd`: định dạng lệnh cũ , dùng cho các trường hợp sử dụng nhỏ,vài cấu trúc không được hỗ trợ và không tương thích với tính năng mới

- `legacy syslog`:tập câu lệnh bắt đầu với dấu '$',thiết lập cấu hình và sử đổi cách thức vận hành của hoạt động, định dạng duy nhất của các phiên bản trước v6 và vẫn được hỗ trợ bởi v6 và mới hơn, một tính năng chỉ hỗ trợ định dạng này  

- `RainerScript`:định dạng mới, dùng cho trường hợp sử dụng(`use case`) phức tạp

### 5.Lệnh điều khiển dòng thông điệp và và dữ liệu

- Điều khiển dòng thông điệp cung cấp bởi:
<ul>
<li>Cấu trúc lệnh điều khiển: http://www.rsyslog.com/doc/v8-stable/rainerscript/control_structures.html</li>
<li>Điều kiện bộ lọc</li>
</ul>

#### Điều kiện lọc

- Gồm có 4 loại:
<ul>
<li>Lựa chon theo kiểu truyền thống dựa trên mức độ nghiêm trọng và cơ sở</li>
<li>Lọc theo thuộc tính</li>
<li>Lọc theo biểu hiện</li>
<li>Theo khả năng tương thích với khối BSD</li>
</ul>

##### 1.Selector

- Cách truyền thống lọc thông điệp ,lưu trong `rsyslog` với cú pháp nguyên bản, vì nó phổ biến, hiệu năng cao và khả năng tương thích với file cấu hình của `syslogd`.Loại này dùng cho trường hợp lọc theo mức ưu tiên và theo cơ sở

- Gồm 2 thành phần: cơ sở và độ ưu tiên phân cách bởi dấu "."

- Cơ sở là một trong số lựa chọn sau:`auth`, `authpriv`, `cron`, `daemon`, `kern`, `lpr`, `mail`, `mark`, `news`, `security` (như `auth`), `syslog`, `user`, `uucp` và `local0` thông qua `local7`
.Mức độ ưu tiên định nghĩa mức độ nghiêm trọng  của thông điệp ,không phải qua các từ như lỗi thảm họa,...
