#Báo cáo OpenStack
##Mục Lục
###[I.Tổng quan](#tq)
###[II.Keystone](#keystone)
###[III.Nova](#nova)
###[IV.Glance](#glance)
###[V.Cinder](#cinder)
###[VI.Swift](#swift)
###[VII.Neutron](#neutron)
###[VIII.Horizon](#horizon)
###[IX.Heat](#heat)
###[X.Ceilometer](#ceilometer)

<a name="tq"></a>
##I.Tổng quan OpenStack
- 1.Khái niệm
OpenStack là một nền tảng điện toán đám mây mã nguồn mở tạo nên bởi nhiều dịch vụ và mỗi dich vụ thực hiện một chức năng nhưng chúng có mối liên hệ với nhau.

- 2.Dịch vụ

|Dịch vụ|Tên Project|Mô tả|
|-------|-----------|-----|
|Dashboard|Horizon|Tạo 1 giao diện trên web để sử dụng|
|Compute|Nova|Quản lý vòng đời máy ảo trên môi trường OpenStack bao gồm tạo, lập lịch, hủy máy ảo theo yêu cầu|
|Networking|Neutron|Cung cấp dịch mạng cho các dịch vụ khác OpenStack, cung cấp APIs để người dùng tạo ra và đưa vào dịch vụ và hỗ trợ nhiều loại mạng và công nghệ|
|Object Storage|Swift|Lưu trữ và lấy các đối tượng dữ liệu qua một RESTful,API gốc HTTP,tạo bản sao,theo kiểu phân tán, có khả năng chống chịu lỗi,có thể triển khai thành dịch vu độc lập|
|Block Storage|Cinder|Cung cấp các khối dữ liệu để chạy máy ảo.Cung cấp volume,khởi tạo máy từ volume,có plugin để kết nố,có thể sao lưu, mở rộng volume|
|Identity service|Keystone|Cung cấp sự xác nhận và dịc vụ xác nhận OpenStack. Cung cấp danh sách endpoints cho OpenStack|
|Imange Service|Glance|Lưu trữ và nhận image đĩa của máy ảo.Compute sử dụng khi cung cấp thực thể|
|Telemetry|Ceilometer||Giám sát và tính toán để tính tiền,và thông kê|
|Orchestratiom|Heat|Điều phối tài nguyên và ứng dụng bằng sử dụng HOT,triển khai dựa vào templates dựng sẵn,tự động tính toán tài nguyên, là stack tab Horizon|
|Database Service|Trove|Dịch vụ cơ sở dữ liệu, cung cấp database,tự backup đảm bảo an toàn|

- 3.Sơ đồ các projects
<ul>
<li>Sơ đồ quan hệ các projects</li>
<img src=https://dague.net/wp-content/uploads/2014/08/screenshot_185.png>
<li>Sơ đồ lớp cảu OpenStack</li>
<img src=https://dague.net/wp-content/uploads/2014/08/screenshot_184.png>
<li>Sơ đồ projects OpenStack theo Node</li>
<img src=http://docs.openstack.org/icehouse/install-guide/install/apt-debian/content/figures/1/figures/installguide_arch-neutron.png>
</ul>

<a name="keystone></a>
##II.Keystone - Dịch vụ xác thực
- Định nghĩa: 
<ul>
<li>là dịch vụ theo dõi người dùng và quyền truy cập</li>
<li>Cung cấp danh sách endpoints vơi APTs endpoints</li>
</ul>
- Bản chất: cung cấp chức năng xác thực và ủy quyền cho môi trường khác nhau của OpenStack. Người dùng cung cấp ủy nhiệm cho Keystone và dựa vào kết quả xác thực chỉ định quyền hạn thông qua thẻ tới người dùng
Quyền hạn chỉ định rõ quyền hoặc đặc quyền thực hiện các công việc trong OpenStack.
- Người dùng: cá nhân,dịch vụ(Nova,Cinder,...),endpoints

Dự án,nhóm tổ chức được gộp lại thành tenant.

Keystone chỉ định quyền hạn tới người dùng. người dùng có nhiều quyền hạn trong các tenant khác nhau.

- Sơ đồ hoạt động Keystone
<img src=https://senecacd.files.wordpress.com/2012/11/identity-diagram.png>
 
 - Dịch vụ Keystone
 <ul>
 <li>Identity</li>
 <ul>
 <li>Dịch vụ nhận dạng cung cấp xác nhận dữ liệu về người dùng,nhóm, tên miền, vai trò hay bất kì dữ liệu liên quan.</li>
 <li>Trong mọi trường hợp dữ liệu được quản lý bởi dịch vụ,cho phép dịch vụ quản lý tất cả CRUD kết hợp với dữ liệu</li>
 <li>Mặt khác, dữ liệu được kéo lên theo mức độ khác nhau bởi dịch vụ phụ trợ có thẩm quyền</li>
 </ul>
 <li>Token: Dịch vụ  quản lý xác nhận mã thông báo dùng cho chứng thực yêu cầu mỗi khi thông tin người dùng đã được xác minh </li>
<li>Catalog: Tạo các endpoints và quản lý </li>
<li>Policy:dịch vụ ủy quyền cung cấp cơ chế ủy quyền và quản lý no</li>
<ul>
<li>Key Value Store: là giao diện tra cứu các khóa </li>
<li>Memcached:cung cấp bộ nhớ đệm</li>
<li>SQL:lưu trữ dữ liệu</li>
<li>LDAP:kết nối thông qua LDPA tới các thư mục ở cơ sở dữ liệu</li>
</ul>
</ul>

<a name="nova"></a>
##III.Nova-Dịch vụ tính toán

- Nova là modun quản lý máy ảo trong hạ tầng OpenStack bằng cách trở thành tầng ảo có giao diện hỗ trợ ảo hóa

- Hỗ tr công nghệ ảo hóa như KVM,ESXi,Hyper-V

- Chia làm 3 nhóm
<ul>
<li> Nhóm A: Trình điều khiển hỗ trợ đầy đủ. Đảm bảo thử nghiệm :</li>
<ul>
<li>Kiểm tra, thử nghiệm cổng vào</li>
<li>Trình điều khiển có: libvirt (qemu/KVM trên x86)</li>
</ul>
<li> Nhóm B</li>
<ul>
<li>Kiểm tra cổng vào</li>
<li>Kiểm tra chức năng hệ thông mà cổng không xác nhận nhưng gợi ý  kết quả trong gerit</li>
<li>Trình điều khiển:Hyper-V,Vmware,XenServer6.2</li>
</ul>
<li>Nhóm C</li>
<ul>
<li>Trình điều khiien thiết lập chế độ tối thiểu và có thể không hoạt động bất cứ lúc nào</li>
<li>Bao gồm:baremetal, docker, Xen via libvirt, LXC via libvirt </li>
</ul>
 </ul>

- 7 thành phần chính:
<ul>
<li>Cloud Controller :thành phần  đại diện cho hệ thống và làm việc với thnhaf phần khác</li>
<li>API Server: như là một dịch vụ web của ự điều khiển đám may</li>
<li>Compute Controller: cung cấp tài nguyên máy chủ</li>
<li>Object Store: cung cấp dịch vụ lưu reuwx</li>
<li>Auth Manager : cung cấp dịch vụ xác thực và uye quyền</li>
<li>Volume Controller: cung cấp nhanh, vĩnh viễn khối dữ liệu cho cụm máy chủ</li>
<li>Network Controller:cung cấp mạng</li>
</ul>
- Scheduler:chọn hệ thống tính toán phù hợp .

- Mối quan hệ thành phần trong Nova
<img src=http://2.bp.blogspot.com/-bYd9cxoncgs/VErn5ECWjZI/AAAAAAAAAF8/gYMkUCD51FQ/s1600/Nova_architecture.png>

<a name="glance"></a>
##IV.Glance - Dịch vụ image

- Cung cấp, lưu trữ thu hồi phân chia siêu dữ liệu cho image sử dụng bởi Nova.

- Cho phép người dùng lấy image qua một giao diện web đơn giản

- Làm việc với Nova hỗ trợ dự phòng cho máy ảo, tương tác Keystone xác thực API.
<img src=http://4.bp.blogspot.com/-8BGR7XSvuSw/VEr6NqccUKI/AAAAAAAAAGc/PP4yLwUYzpI/s1600/glance.png>

- Các tiến trình trong Glance
<ul>
<li>glance-api: chấp nhận lơi gọi của image api đẻ tìm,truy xuất,luuw trữ image</li>
<li>glance-registry:lưu trữ ,xử lý, nhận siêu dữ liệu về image</li>
<li>glance database: cơ sở dữ liệu </li>
<li>Một kho lưu trữ cho các tập tin hình ảnh thực tế. Glance hỗ trợ hệ thống tập tin bình thường,thiết bị khối RADOS , Amazon S3, HTTP và Swift</li>
</ul>

- Glance chấp nhân yêu cầu API cho image từ người dùng hoặc thành phần của Nova và lưu trữ trong dịch vụ đối tượng lưu trữ, Swift hoặc kho lưu trữ khác.

- Định dang đĩa
<ul>
<li>raw:Đây là một định dạng ảnh đĩa không có cấu trúc</li>
<li>vhd:là định dạng đĩa thông thường được sử dụng bởi các màn hình máy ảo từ VMware, Xen, Microsoft, VirtualBox, và những người khác</li>
<li>vmdk:định dạng đĩa phổ biến được hỗ trợ bởi nhiều máy ảo phổ biến</li>
<li>vdi:định dạng đĩa hỗ trợ bởi máy ảo VirtualBox và mô phỏng QEMU</li>
<li>iso: định dạng lưu trữ cho các nội dung dữ liệu của một đĩa quang học </li>
<li>qcow2:định dạng hỗz trợ bởi QEMU  mà có thể mở rộng hỗ trợ sao chép và viết</li>
<li>aki:lưu trữ trong Glance là một nhân Amazone Kernel image</li>
<li>ari:lưu trữ trong Glance là một  Amazon ramdisk image</li>
<li>ami: lưu trữ trong Glance  là một Amazon machine image</li>

- Định dạng container : image của máy ảo trong môt jđịnh dạng file chưa siêu dữ liệu về hoạt động máy ảo
<ul>
<li>bare:không có container hay siêu dữ liệu trong image</li>
<li>ovf: định dạng OVF</li>
<li>ova: chỉ những thứ lưu trữ trong Glance là một file nén OVA</li>

- oVirt liên kết vơi Glance
<img src=http://1.bp.blogspot.com/-8_hta2MsdqE/VEvpGcz_n1I/AAAAAAAAAGs/ekV15QqyzWo/s1600/discovery_glance_provider_small.png>

- Glance API:Có 2 phiên bản của Glance API - phiên bản 1 và phiên bản 2.Phiên bản 2 cung cấp một số chuẩn hóa của một số thuộc tính của image.Glance phụ thuộc vào Keystone và sự xác thực của OpenStack API.Glance sẽ truyền đạt lại cho Keystone để xác minh tính hợp lệ token và có được các thông tin nhận dạng của bạn.
 
 <a name="cinder"></a>
##V.Cinder- Dịch vụ lưu trữ khối dữ liệu
 
 - Kiểu lưu trữ: lưu tữu khối, lưu trữ tệp tin, lưu trữ đối tượng.
 
 - Từng là một phần của Nova sau đó tách ra khi Folson ra đơig
 
 - Có thể triển khai độc lộ không cần OpenStack
 
 - Cindẻ giống Amazon Web Services S3 khi cung cấp khối dữ liệu chắc chắn cho máy tính.
 
 - Cấu trúc Cinder
 <ul>
 <img src=http://4.bp.blogspot.com/-onbO2eMISfk/VEwBuGLkOvI/AAAAAAAAAHM/ryp2OhRTcBE/s1600/cinder_architecture.png>
 
 <li> Cinder API:Ứng dụng WSGI sẽ định hướng yêu cầu qua dịch vụ lưu trữ khối dữ liệu. Yêu cầu sẽ được gửi tới cinder-schelduler để điều phối dung lượng thích hợp</li>
 <li> Cinder-scheduler: dựa trên yêu cầu thích hợp dến dịch vụ cinder-volume qua AMPQ(RabbitMQ hoặc Qpid).Có thể được cấu hình để sử dụng round-robin</li>
 <li> Cinder-volume: lưu trữ backends khác nhau, tương tác trực tiếp phần mềm và phần cứng cung cấp khối lưu trữ, cho người dùng biết dung lượng cho </li>
 <li Cinder-backup:cung cấp dịch vụ sao lưu Cinder volume tới OpenStack Swift</li>
 </ul>
 
 - Thành phần Cinder
 <ul>
 <li> Back-end Storage Devices:Mặc định là để sử dụng LVM(Logical Volume Manager) trên một nhóm dung lượng là"cinder-volums', hỗ trợ các thiết bị khác, kích thước khối có thể điều chỉnh bằng cách dùng KVM hoặc QEMU như sự ảo hóa</li>
 <li>Người sử dụng và người thuê / Dự án:</li>
 <ul>
 <li> Dùng RBAC(Role-based Access Control) cho nhiều người thuê</li>
 <li> Sử dụng "policy.json" để duy trì các quy tắc cho mỗi vai trò</li>
 <li> truy cập khối lượng cho mỗi người dùng</li>
 <li> Hạn ngach để kiemr soát mức tiêu thụ mỗi người dùng</li>
 li> Hạn ngạch có thể được sử dụng để kiểm soát: số lượng và bức ảnh chụp mà có thể được tạo ra cũng như tổng số GBs phép cho mỗi người thuê(chia sẻ giữa khối lượng và ảnh chụp)</li>
 </ul>
 <li>Volumes, Snapshots and Backups </li>
 <ul>
 <li>Volumes:phân bổ tài nguyên lưu trữ, là khối R/W bền vững đính kèm vào nút tính toán qua iSCSI</li>
 <li>Snapshots:điểm chỉ có thể đọc trong lúc sao luwu volume</li>
 <li>Backups:Một bản sao lưu trữ của một khối lượng hiện đang được lưu trữ trong OpenStack</li>
 </ul>
 </ul>
 
 <a name="swift"></a>
 ##VI.Swift
 
 - Giống Cinder ở kiểu lưu trữ
 
 - So sánh 3 kiểu lưu trữ:
 
 <img src=http://2.bp.blogspot.com/-RccNUOyTSYc/VEwv4sviZuI/AAAAAAAAAHc/V7oUuQQko00/s1600/sidebyside_comparisonOfStorage.jpg>
 
 - Kiến trúc OpenStack Swift : Swift là dịch vụ lưu trữ đối tượng trong OpenStack	
 <img src=http://4.bp.blogspot.com/-ZfFbYCyMoeI/VFsE5cHEUOI/AAAAAAAAAQ4/YBCM4Bt5ddE/s1600/swift_2-Tier.png>

- Swift is composed of two types of nodes:     
<ul>
<li>Proxy Nodes:nút tiếp xúc với khách hàng Swift và xử lý mọi yêu cầu và tiến trình.Khách hàng chỉ tương tác với các nút Proxy</li>
<li>Storage Nodes.:Đây là nút mà host lưu trữ cho các đối tượng</li>
</ul>

- Thuật ngữ OpenStack Swift 
<img src=http://4.bp.blogspot.com/-0X0BEzbWHFg/VExD6_tPBoI/AAAAAAAAAHs/DGd2mmzD5ko/s1600/Swift_cluster_Architecture.jpg>
<ul>
<li>Partition: một dãy khóa hoàn chỉnh không chồng chéo như mỗi đối tượng,gói và tài khoản là một thành phần chính xác của một phân vùng như là mỗi giá trị khóa của nó</li>
<li>Ring:kết nối phân vùng theo một bản đồ tạo nên thiết bị vật lý </li>
<liObject: giá trị khóa ghi vào vùn lưu trữ đối trượng</li>
<li>Containers :nhóm đối tượng</li>
<li>Accounts :nhóm tài khoản</li>
<li>Object/Storage Server:lưu trữ, lấy và xóa các đối tượng được lưu trữ trên các thiết bị địa phương</li>
<li>Container Server : lưu trữ anh sách các đối tượng sử dụng cơ sở dữ liệu SQLite.</li>
<li>Account Server:tương tự như Container Server nhưng nó lưu trữ danh sách các container.</li>
<li>Proxy Server:có khả năng mở rộng API yêu cầu xử lý, xác định phân phối nút lưu trữ các đối tượng dựa trên URL</li>
<li>Replicator:	trình tiện ích để xử lý các bản sao dữ liệu</li>
<li>Updater :xử lý các bản cập nhật mà không phải thực hiện thành công để duy trì tính toàn vẹn của dữ liệu trong cụm Swift</li>
<li>Auditor :chạy trên mỗi nút để kiểm tra tính toàn vẹn của thông tin đối tượng, container và tài khoản.</li>
Từ đó ta có4 loại:
<li>Truy cập dữ liệu : ring và partition
<li>Trình chiếu dữ liệu: account, container và objects</li>
<li>Loại máy chủ:proxy, object, container và account server </li>
<li>Tiện ích: replicator, updater và auditor</li>
<img src=http://3.bp.blogspot.com/-1yp878OVa80/VFvVuafBqPI/AAAAAAAAASA/aMrBTQMaZIU/s1600/Swift_proxyServer_Arch.png>
</ul>

-Tất cả các đối tượng trong Swift có thể được truy cập thông qua các API RESTful.Định dạng API:
<ul>
<li>/account</li>
<ul>
<li>Các vị trí lưu trữ tài khoản là một khu vực lưu trữ tên duy nhất có chứa các siêu dữ liệu về tài khoản của nó cũng như danh sách gói dữ liệu trong tài khoản.</li>
<li>Chú ý  trong Swift, một tài khoản không phải là danh tính người dùng mà là khu vực lưu trữ</li>
</ul>
<li>/accounts/containers:khu vực lưu trữ gói dữ liệu trong kho lưu trữ định danh người dùng với ột tài khoản mà siêu dữ liệu về chính nó và danh sách các đối tượng được lưu trũ</li>
<li>/account/container/object:lưu trữ đối tượng và siêu dữ liệu</li>
<img src=http://3.bp.blogspot.com/-jI-4cWuMF9c/VExGQlxo1JI/AAAAAAAAAH4/jtWYQ5ZwvzQ/s1600/swift_URL_format.jpg>
</ul>

<a name="neutron"></a>
##VII.Neutron - Dịch vụ mạng

- Ban đầu mạng được cung cấp bởi Nova nhưng sau đó tách ra thành dự án tên là Quantumn và sau đổi tên thành Neutron.

- Thành phần Neutron:
<ul>
<li>Máy chủ neutron: chạy trên nút mạng cung cấp API mạng các mở rộng, tạo các mô hình mạng và địa chỉ IP mỗi cổng, yêu cầu truy cập cơ sở dữ liệu cho việc lưu trữ liên tục và hàng đợi thông điệp cho việc giao tiếp</li>
<li>Plugin agent:chạy trên nút máy để cấu hình switch ảo trên mỗi máy, yêu cầu truy cập hàng đợi thông điệp.</li>
<li>DHCP agent:cung cấp dịch vụ DHCP, bình đẳng trên mọi plugin và thực hiện duy trì cấu hình DHCP, yêu cầu truy cập hàng đợi thông điệp.</li>
<li>L3 agent: cung cấp mạng NAT để truy cập mạng, yêu cầu truy cập hàng đọi thông điệp.</li>
<li>Dịch vụ cung cấp mạng:cung cấp thêm dịch vụ mạng, tương tác neutron-server,plugin qua REST API hoặc qua kênh tương tác khác</li>
<img src=http://1.bp.blogspot.com/-Y2nFB5BI5Xw/VEyH2C5MaZI/AAAAAAAAAIU/ZbkJ2LEexbo/s1600/Neutron-PhysNet-Diagram.png>
</ul>

- Neutron API: định nghĩa
<ul>
<li>Network: đoan L2 biệt lập, tương tự VLAN trong mạng vật lý</li>
<li>Mạng con: khối địa chỉ IPv4,v6 và trạng thái cấu hình</li>
<li>Cổng: điểm kết nối để gắn một thiết bị,mô tả cấu hình ạng</li>
</ul>

- Neutron API Extension: người dùng thêm chức năng mạng thông qua Neutron plugins.

<img src=http://2.bp.blogspot.com/-pKluO0upSZw/VEyI9UaO5CI/AAAAAAAAAIc/iNJb13K9de8/s1600/SDN-diagram.jpg>
 
 - Mô tả mối liên kết giữa Neutron API,Neutron API Extension, Neutron plugins.
 
 - Neutron plugins: giao diên giữa Neutron và công nghệ backends,ví dụ:Open vSwitch, Linux Bridge,...
 
 <a name="horizon"></a>
 ##VIII.Horizon - Dịch vụ giao diện
 
 - Cung cấp giao diện dịch vụ Nova, Swift, Keystone,...
 
 - Thư mục Horizon lưu trữ thư viện chung có thể dùng cho bât kì dự án Django.
 
 - Thư mục Dashboard chứa một dự án Django mẫu dùng Horizon.
 
 - Horizon API Reference: triển khai cụm Apache Hoop nhanh chóng, giúp người dùng dễ dàng mở rộng bộ dữ liệu, mở rông hệ thống RBAC
 
 - Dashboard
 <ul>
 <li>Ứng dụng web hỗ trợ kiểm soát tính toán ,lưu trữ , dịch vụ mạng</li>
 <li> Nếu có quyền quản trị, cung cấp kích thước và trạng thái của cloud. Tạo người dùng và dự án, phân người dùng vào dự án và phân bổ tài nguyên cho dữ án.</li>
 <li> Cung cấp cổng dịch vụ để cung cấp tài nguyên trong giới hạn </li>
 </ul>
 <a name="heat"></a>
 ##IX.HEAT- Dịch vụ Orchestration
 
 - Cung cấp và quản lý tài nguyên của cloud
 
 - Là một yếu tố chỉ rõ mô hình ứng dụng
 
 - 	Thành phần Orchestration:
 <ul>
 </li>heat: Công cụ CLI giao tiếp với heat-api để xử lý AWS CloudFormation APIs.</li>
 <li>heat-api: là  ReST API xử lý yếu cầu cảu API bằng cách gửi tới heat-engine qua RPC.</li>
 <li>heat-api-cfn: cung cấp AWS-Query trương thích với AWS CloudFormation và xử lý yêu cầu API bằng việc gửi tới heat-engine qua RPC</li>
 <li>heat-engine: chạy các mẫu và trả lại sự kiện cho người dùng</li>
 <li>api-heat-cloudwatch:thu thập số liệu cho dịch vụ Orchestration</li>
 <li>heat-cfntools: gói các script hỗ trợ</li>
 </ul>
 
 - Heat Template:giúp mà người dùng có hạ tầng OpenStack như ý, tích hợp với công cụ quản trị, các cấu trúc:Description,Parameters,Mappings,Resources,Outputs.
 
 - Heat Engine:phương tiện từ người dùng thực hiện các công việc orchestation, gồm 2 tập API:API - OpenStack và REST API and AWS Query API, có thể mở rộng thu hẹp tài nguyên
 <img src=http://2.bp.blogspot.com/-me47JZk6Y44/VE3bwYfRHII/AAAAAAAAAJY/Qt22PGnFt7A/s1600/Heat_autoscaling.png>
 
 <a name="ceilometer"></a>
 ##X.Ceilometer - Dịch vụ giám sát và đo lường
 
 - Hạ tầng để thu thập thông tin cần thiết với OpenStack, thiết kế cho các công cụ đánh giá có thể tính tiền 
 
 - Công việc chính: đo lường, cảnh báo, đa xuất bản
 
 - Đo lường:
 <ul>
 <img src=http://3.bp.blogspot.com/-AutqWZ8U5zY/VFcAk1asIWI/AAAAAAAAAO0/t3ZW2RtSCTQ/s1600/ceilometer-options-push-pull.png>
 <li>Kiến trúc Ceilometer</li>
 <li>Bus-Listener Agent:tích hợp với dự án OpenStack Oslo </li>
 <li>Push Agent: đẩy dữ liệu lên Ceilometer, hỗ trợ phục hồi, có hiệu lục cao</li>
 <li>Polling Agent: thăm dò đối tượng và yêu cầu dữ liệu, hoàn thành trong lúc cấu hình, không hỗ trợ phục hồi
 </ul>
 <img src=http://2.bp.blogspot.com/-lKW1sHFMerU/VFcEQGe1m8I/AAAAAAAAAPA/9l9F2lCSw_E/s1600/ceilometer-workflow.jpg>
 <img src=http://2.bp.blogspot.com/-DpTb0y45Qcc/VFcEvJCh7rI/AAAAAAAAAPM/9hNPX2lldwE/s1600/ceilometer_dataRetrieval.png>
	
 - Đa xuất bản
 <ul>
 <img src=http://1.bp.blogspot.com/-CmY4SINTFr0/VFcHzrkPXDI/AAAAAAAAAPU/UO--BsUGssE/s1600/ceilometer_publisher.png>
 <li>Công bố thường xuyên:như một máy đo bạn dùng bao nhiêu trả bấy nhiêu, cập nhật mỗi 30 phút</li>
 <li>Vận chuyển:Trong trường hợp dữ liệu dành cho hệ thống giám sát mất một bản cập nhật hoặc không đảm bảo an ninh lúc đó đồng hồ sẽ cần cả an ninh và đảm bảo vận chuyển trong trường hợp các dữ liệu dành cho hệ thống đánh giá và thanh toán.</li>
 <li>notifier :	thông báo mà đẩy vào hàng đợi thông điệp</li>
 <li>rpc : RPC cơ bản và an toàn</li>
 <li>udp:xuất bản mẫu sử dụng các gói tin UDP.</li>
 <img src=http://4.bp.blogspot.com/-rnUgEP6iHCo/VFcIfM8kw4I/AAAAAAAAAPc/4z72VKQu8fw/s1600/ceilometer_multi-publish.png>
 
<li> Biểu đồ này cho thấy một mẫu duy nhất được gửi tới 2 phuong tiện vận chuyể là RPC và UDP mà lần lượt công bố các dữ liệu cùng với 2 mục tiêu khác nhau</li>
 </ul>
 
 - Cảnh báo:cho phép người dùng thiết lập báo động dựa trên đánh giá ngưỡng cho một bộ sưu tập các mẫu, có thể là một máy đo hoặc tổ hợp nhiều máy.
 <ul>
 <li>HTTPCallback:bạn đưa một URL khi báo động được đặt,tải trọng của yêu cầu có chứa tất cả các thông tin chi tiết về việc tại sao các báo động được kích hoạt.</li>
 <li>Log:chủ yếu là hữu ích để gỡ lỗi</li>
 </ul>
 
 

 

 

 

 
 
