#Quá trình boot một VM trong OpenStack
#Mục lục
<h4><a href="#components">1. Một số component tham gia vào quá trình khởi tạo và dự phòng cho máy ảo</a></h4>
<h4><a href="#flow">2. Request flow trong quá trình tạo máy ảo</a></h4>

---

<i><b>Nội dung: </b>Quá trình khởi tạo máy ảo từ lúc nhận request, mô tả luồng request, sự tương tác giữa các component trong OpenStack. Chú ý: quantum là tên trước đây của neutron, đổi sang neutron từ bản Havana.</i>

<img src="http://i.imgur.com/K0RR6NC.png"/>

<h3><a name="components">1. Một số component tham gia vào quá trình khởi tạo và dự phòng cho máy ảo</a></h3>
<ul>
<li>CLI: Command Line Interpreter - là giao diện dòng lệnh để thực hiện các command gửi tới OpenStack Compute</li>
<li>Dashboard (Horizon): cung cấp giao diện web cho việc quản trị các dịch vụ trong OpenStack</li>
<li>Compute(Nova): quản lý vòng đời máy ảo, từ lúc khởi tạo cho tới lúc ngừng hoạt động, tiếp nhận yêu cầu tạo máy ảo từ người dùng.</li>
<li>Network - Quantum (hiện tại là Neutron): cung cấp kết nối mạng cho Compute, cho phép người dùng tạo ra mạng riêng của họ và kết nối các máy ảo vào mạng riêng đó.</li>
<li>Block Storage (Cinder): Cung cấp khối lưu trữ bền vững cho các máy ảo</li>
<li>Image(Glance): lưu trữ đĩa ảo trên Image Store</li>
<li>Identity(Keystone): cung cấp dịch vụ xác thưc và ủy quyền cho toàn bộ các thành phần trong OpenStack.</li>
<li>Message Queue(RabbitMQ): thực hiện việc giao tiếp giữa các component trong OpenStack như Nova, Neutron, Cinder.</li>
</ul>
<h3><a name="flow">2. Request flow trong quá trình tạo máy ảo</a></h3>
<ul>
<li><b>Bước 1</b>: Từ Dashboard hoặc CLI, nhập thông tin chứng thực (ví dụ: user name và password) và thực hiện lời gọi REST tới Keystone để xác thực</li>
<li><b>Bước 2</b>: Keystone xác thực thông tin người dùng và tạo ra một token xác thực gửi trở lại cho người dùng, mục đích là để xác thực trong các bản tin request tới các dịch vụ khác thông qua REST</li>
<li><b>Bước 3</b>: Dashboard hoặc CLI sẽ chuyển yêu cầu tạo máy ảo mới thông qua thao tác "launch instance" trên openstack dashboard hoặc "nova-boot" trên CLI, các thao tác này thực hiện REST API request và gửi yêu cầu tới nova-api</li>
<li><b>Bước 4</b>: nova-api nhận yêu cầu và hỏi lại keystone xem auth-token mang theo yêu cầu tạo máy ảo của người dùng có hợp lệ không và nếu có thì hỏi quyền hạn truy cập của người dùng đó.</li>
<li><b>Bước 5</b>: Keystone xác nhận token và update lại trong header xác thực với roles và quyền hạn truy cập dịch vụ lại cho nova-api</li>
<li><b>Bước 6</b>: nova-api tương tác với nova-database</li>
<li><b>Bước 7</b>: Dababase tạo ra entry lưu thông tin máy ảo mới</li>
<li><b>Bước 8</b>: nova-api gửi rpc.call request tới nova-scheduler để cập cập entry của máy ảo mới với giá trị host ID (ID của máy compute mà máy ảo sẽ được triển khai trên đó). C(Chú ý: yêu cầu này lưu trong hàng đợi của Message Broker - RabbitMQ)</li>
<li><b>Bước 9</b>: nova-scheduler lấy yêu cầu từ hàng đợi</li>
<li><b>Bước 10</b>: nova-scheduler tương tác với nova-database để tìm host compute phù hợp thông qua việc sàng lọc theo cấu hình và yêu cầu cấu hình của máy ảo</li>
<li><b>Bước 11</b>: nova-database cập nhật lại entry của máy ảo mới với host ID phù hợp sau khi lọc.</li>
<li><b>Bước 12</b>: nova-scheduler gửi rpc.cast request tới nova-compute, mang theo yêu cầu tạo máy ảo mới với host phù hợp.</li>
<li><b>Bước 13</b>: nova-compute lấy yêu cầu từ hàng đợi.</li>
<li><b>Bước 14</b>: nova-compute gửi rpc.call request tới nova-conductor để lấy thông tin như host ID và flavor(thông tin về RAM, CPU, disk) (chú ý, nova-compute lấy các thông tin này từ database thông qua nova-conductor vì lý do bảo mật, tránh trường hợp nova-compute mang theo yêu cầu bất hợp lệ tới instance entry trong database)</li>
<li><b>Bước 15</b>: nova-conductor lấy yêu cầu từ hàng đợi</li>
<li><b>Bước 16</b>: nova-conductor tương tác với nova-database</li>
<li><b>Bước 17</b>: nova-database trả lại thông tin của máy ảo mới cho nova-conductor, nova condutor gửi thông tin máy ảo vào hàng đợi.</li>
<li><b>Bước 18</b>: nova-compute lấy thông tin máy ảo từ hàng đợi</li>
<li><b>Bước 19</b>: nova-compute thực hiện lời gọi REST bằng việc gửi token xác thực tới glance-api để lấy Image URI với Image ID và upload image từ image storage.</li>
<li><b>Bước 20</b>: glance-api xác thực auth-token với keystone</li>
<li><b>Bước 21</b>: nova-compute lấy metadata của image(image type, size, etc.)</li>
<li><b>Bước 22</b>: nova-compute thực hiện REST-call mang theo auth-token tới Network API để xin cấp phát IP và cấu hình mạng cho máy ảo</li>
<li><b>Bước 23</b>: quantum-server (neutron server) xác thực auth-token với keystone</li>
<li><b>Bước 24</b>: nova-compute lấy thông tin về network</li>
<li><b>Bước 25</b>: nova-compute thực hiện Rest call mang theo auth-token tới Volume API để yêu cầu volumes gắn vào máy ảo</li>
<li><b>Bước 26</b>: cinder-api xác thực auth-token với keystone</li>
<li><b>Bước 27</b>: nova-compute lấy thông tin block storage cấp cho máy ảo</li>
<li><b>Bước 28</b>: nova-compute tạo ra dữ liệu cho hypervisor driver và thực thi yêu cầu tạo máy ảo trên Hypervisor (thông qua libvirt hoặc api - các thư viện tương tác với hypervisor)</li>
</ul>