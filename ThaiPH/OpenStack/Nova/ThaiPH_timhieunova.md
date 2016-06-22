# Tìm hiểu OpenStack Nova
# Mục lục
<h3><a href="#sysarch">1. Kiến trúc hệ thống của Nova</a></h3>
<ul>
<li><a href="#intro">1.1. Giới thiệu Nova</a></li>
<li><a href="#components">1.2. Các thành phần của Nova</a></li>
</ul>
<h3><a href="#services">2. Compute Services</a></h3>
---

<h2><a name="sysarch">1. Kiến trúc hệ thống của Nova</a></h2>
<ul>
<li><h3><a name="intro">1.1. Giới thiệu Nova</a></h3>
<div>
<ul>
<li>Nova bao gồm nhiều tiến trình trên server, mỗi tiến trình lại thực hiện một chức năng khác nhau.</li>
<li>Nova cung cấp REST API để tương tác với ứng dụng client phía người dùng, trong khi các thành phần bên trong Nova tương tác với nhau thông qua RPC.</li>
<li>Các API servers thực hiện các REST request, điển hình nhất là thao tác đọc, ghi vào cơ sở dữ liệu, với tùy chọn là gửi các bản tin RPC tới các dịch vụ khác của Nova. Các bản tin RPC dược thực hiện nhờ thư viện  <b>oslo.messaging</b> - lớp trừu tượng ở phía trên của các message queue. Hầu hết các thành phần của nova có thể chạy trên nhiều server và có một trình quản lý lắng nghe các bản tin RPC. Ngoại trừ <b>nova-compute</b>, vì dịch vụ <b>nova-compute</b> được cài đặt trên các máy compute - các máy cài đặt hypervisor mà <b>nova-compute</b> quản lý.</li>
<li>Nova cũng sử dụng một cơ sở dữ liệu trung tâm chia sẻ chung giữa các thành phần. Tuy nhiên, vì mục tiêu nâng cấp, các cơ sở dữ liệu được truy cập thông qua một lớp đối tượng dể đảm bảo các thành phần kiểm soát đã nâng cấp vẫn có thể giao tiếp với nova-compute ở phiên bản trước đó. Để thực hiện điều này, nova-compute ủy nhiệm các yêu cầu tới cơ sở dữ liệu thông qua RPC tới một trình quản lý trung tâm, chính là dịch vụ <b>nova-conductor</b>.</li>
</ul>
</div>
</li>

<li><h3><a name="components">1.2. Các thành phần của Nova</a></h3>
<div>
<br>
<img src="http://i.imgur.com/tMJ2NWN.png">
<br><br>
Các thành phần của nova:
<ul>
<li><b>DB:</b> cơ sở dữ liệu quan hệ SQL để lưu trữ thông tin</li>
<li><b>API:</b> thành phần tiếp nhận các HTTP request, chuyển thành các lệnh hệ thống và tương tác với các thành phần khác thông qua hàng đợi <b>oslo.messaging</b> hoặc HTTP.</li>
<li><b>Scheduler:</b>  quyết định xem host nào sẽ vận hành instance</li>
<li><b>Network:</b> quản lý ip forwarding, bridges, vlans</li>
<li><b>Compute:</b> quản lý giao tiếp giữa hypervisor và máy ảo.</li>
<li><b>Conductor:</b> thực hiện các yêu cầu mà cần tới sự phối hợp (build/resize), được coi như một database proxy hoặc thực hiện thao tác chuyển đổi các đối tượng.</li>
</ul>
</div>
</li>
</ul>

<h2><a name="services">2. Compute Services</a></h2>
<div>
OpenStack Compute bao gồm các thành phần sau:
<ul>
<li><b>nova-api </b>Tiếp nhận và phản hồi các lời gọi API từ người dùng cuối. Dịch vụ này hỗ trợ OpenStack Compute API, Amazon EC2 API và một API quản trị đặc biệt cho những người dùng thực hiện các tác vụ quản trị. Nó thực hiện một số chính sách và khởi tạo hầu hết các hoạt động điều phối, chẳng hạn như tạo máy ảo.</li>
<li><b>nova-api-metadata </b>Tiếp nhận yêu cầu lấy metadata từ các instance. Dịch vụ này thường được sử dụng khi triển khai chế độ multi-host với <b>nova-network</b>.</li>
<li><b>nova-compute </b>Một worker daemon thực hiện tác vụ quản lý vòng đời các máy ảo như: tạo và hủy các instance thông qua các hypervisor APIs. Ví dụ:
<ul>
<li>XenAPI đối với XenServer/XCP</li>
<li>libvirt đối với KVM hoặc QEMU</li>
<li>VMwareAPI đối với VMware</li>
</ul>
Tiến trình xử lý của <b>nova-compute</b> khá phức tạp, về cơ bản thì daemon này sẽ tiếp nhận các hành động từ hàng đợi và thực hiện một chuỗi các lệnh hệ thống như vận hành máy ảo KVM và cập nhật trạng thái của máy ảo đó vào cơ sở dữ liệu.
</li>
<li><b>nova-scheduler </b>Daemon này lấy các yêu cầu tạo máy ảo từ hàng đợi và xác định xem server compute nào sẽ được chọn để vận hành máy ảo.</li>
<li><b>nova-conductor </b>Là module trung gian tương tác giữa <b>nova-compute</b> và cơ sở dữ liệu. Nó hủy tất cả các truy cập trự tiếp vào cơ sở dữ liệu tạo ra bởi <b>nova-compute</b> nhằm mục đích bảo mật, tránh trường hợp máy ảo bị xóa mà không có chủ ý của người dùng.</li>
<li><b>nova-cert </b>Là một worker daemon phục vụ dịch vụ Nova Cert cho chứng chỉ X509, được sử dụng để tạo các chứng chỉ cho <b>euca-bundle-image</b>. Dịch vụ này chỉ cần thiết khi sử dụng EC2 API.</li>
<li><b>nova-network </b>Tương tự như nova-compute, tiếp nhận yêu cầu về network từ hàng đợi và điều khiển mạng, thực hiện các tác vụ như thiết lập các giao diện bridging và thay đổi các luật của IPtables. </li>
<li><b>nova-consoleauth </b>ỦY quyền tokens cho người dùng mà console proxies cung cấp. Dịch vụ này phải chạy với console proxies để làm việc.</li>
<li><b>nova-novncproxy </b>Cung cấp một proxy để truy cập máy ảo đang chạy thông qua kết nối VNC. Hỗ trợ các novnc client chạy trên trình duyệt.</li>
<li><b>nova-spicehtml5proxy </b>Cung cấp một proxy truy cấp máy ảo đang chạy thông qua kết nối SPICE. Hỗ trợ các client chạy trên trình duyệt hỗ trợ HTML5.</li>
<li><b>nova-xvpvncproxy </b>Cung cấp một proxy truy cập máy ảo đang chạy thông qua kết nối VNC.</li>
<li><b>nova client</b>Cho phép người dùng thực hiện tác vụ quản trị hoặc các tác vụ thông thường của người dùng cuối.</li>
<li><b>The queue </b>Là một trung tâm chuyển giao bản tin giữa các daemon. Thông thường queue này cung cấp bởi một phần mềm message queue hỗ trợ giao thức AMQP: RabbitMQ, Zero MQ.</li>
<li><b>SQL database </b>Lưu trữ hầu hết trạng thái ở thời điểm biên dịch và thời điểm chạy cho hạ tầng cloud:
<ul>
<li>Các loại máy ảo đang có sẵn</li>
<li>Các máy tính đang đưa vào sử dụng</li>
<li>Hệ thống mạng sẵn sàng</li>
<li>Các projects.</li>
</ul>
Về cơ bản, OpenStack Compute hỗ trợ bất kỳ hệ quản trị cơ sở dữ liệu nào như SQLite3 (cho việc kiểm tra và phát triển công việc), MySQL, PostgreSQL.
</li>
</ul>
</div>