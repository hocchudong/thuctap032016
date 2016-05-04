
#Vai trò và các thành phần trong các project trong OpenStack
=====================

###Mục lục:

[1. Keystone](#1)

[2. Nova](#2)

[3. Glance – Image Service](#3)

[4.Cinder – Block Storage Service](#4)

[5.Swift – Object Storage Service](#5)

[6. Neutron – Networking Service](#6)

[7. Horizon – Dashboard](#7)

[8. Heat - Block Orchestration](#8)

[9. Ceilometer - Bock Telemetry](#9)

[- 9.1 Telemetry Data Collection service](#9.1)

[- 9.2 Telemetry Alarming service](#9.2)

[10. Trove - Database Service](#10)

===============

<a name="1"></a>
###1. Keystone
- Cung cấp các dịch vụ nhận dạng và xác thực
- Theo dõi và cho phép người dùng
- Cung cấp một danh mục các dịch vụ sẵn có với endpoints

Người dùng có thể là:
```sh
Một người
Dịch vụ (ví dụ Nova, Cinder, Neutron ...)
Điểm cuối (một địa chỉ mạng có thể truy cập như một URL, RESTful API)
```
Các dịch vụ:

**Identity:**

- Dịch vụ nhận dạng, cung cấp xác nhận chứng chỉ, dữ liệu người dùng, nhóm...
- Basic case: Các dữ liệu được quản lý bới các dịch vụ, cho phép quản lý các CRUD kết hợp với các dữ liệu.
- Other cases: Dữ liệu được co giãn tùy từng mức độ bởi một dịch vụ phụ trợ. 
	
**Token**: Việc xác nhận dịch vụ Token và quản lý Tokens được dùng để xác thực yêu cầu một khi thông tin của người dùng đã được xác minh.
	
**Catalog**: Cung cấp một endpoint đăng ký để phát hiện các endpint.
		
**Policy**: Các dịch vụ Chính sách cung cấp nguyên tắc cho phép và giao diện quản lý quy tắc liên quan.
		
Các thành phần:

<ul>
<li>Key Value Store:  Một giao diện hỗ trợ tra cứu khóa chính, như một từ điển trong bộ nhớ</li>
<li>Memcached: Hệ thống phân phối bộ nhớ đệm bộ nhớ</li>
<li>Structured Query Language (SQL): Sử dụng SQLAlchemy (một bộ công cụ Python SQL và Object Relational Mapper) để lưu trữ dữ liệu liên tục</li>
<li>Pluggable Authentication Module (PAM): Sử dụng dịch vụ PAM hệ thống địa phương để xác thực</li>
<li>Lightweight Directory Access Protocol (LDAP): Kết nối thông qua LDAP vào một thư mục back-end, như Active Directory, để xác thực người sử dụng và có được thông tin vai trò</li>
</ul>

<a name="2"></a>
##2. Nova
- Là một module dùng để quản lý các trường máy ảo, nó là một lớp trừu tượng có giao diện và hỗ trợ siêu giám sát
- Hypervisors: KVM, ESx của VMware, Hyper-VMware

Các thành phần:
<ul>
<li>Nova-api service: Chấp nhận và phản hồi các yêu cầu API của người dùng cuối. Hỗ trợ Compute API, Amazon EC2 API, và API quản trị đặc biệt.</li>
<li>Nova-api-metadata service: Chấp nhận các yêu cầu siêu dữ liệu từ các trường. Dịch vụ được sử dụng ở chế độ đa máy chủ với nova-network.</li>
<li>Nova-compute service: Tạo và xóa máy ảo thông qua các API hypervisor
	XenAPI for XenServer/XCP
	libvirt for KVM or QEMU
	VMwareAPI for VMware</li>
<li>Nova-scheduler service: Lấy một yêu cầu về máy ảo ở hàng đợi và quyết định máy chủ sẽ chạy nó.
<li>Nova-conductor module: Là trung gian giữa nova-compute và dữ liệu. 
<li>Nova-cert module: Máy chủ phục vụ cho dịch vụ Nova Cert cho chứng thực X509. Tạo các giấy chứng nhận cho euca-bundle-image. Chỉ cần thiết cho EC2 API.
<li>Nova-network worker daemon: Chấp nhận nhiệm vụ kết nối mạng từ hàng đợi và vận hành mạng. Thực hiện thiết lập cầu nối giao diện hoặc thay đổi quy tắc IPtables.
<li>Nova-consoleauth daemon: 
<li>Nova-novncproxy daemon: Cung cấp một proxy để truy cập các trường hợp chạy qua một kết nối VNC. Hỗ trợ khách hàng novnc dựa trên trình duyệt.
<li>Nova-spicehtml5proxy daemon: Cung cấp một proxy để truy cập các trường hợp thông qua kết nối SPICE. Hỗ trợ khách hàng qua trình duyệt HTML5.
<li>Nova-xvpvncproxy daemon: Cung cấp một proxy để truy cập các trường hợp thông qua kết nối VNC. Hỗ trợ khách hàng qua OpenStack-specific Java.
<li>Nova-cert daemon: Chứng thực X509
<li>Nova client: Cho phép người dùng sử dụng commands như một quản trị hoặc người dùng cuối.
<li>The queue: Một vòng trung tâm để thông qua các tin nhắn giữa các daemon. Thường được thực hiện với RabbitMQ hoặc hàng đợi thông điệp AMQP như Zera MQ.
<li>SQL database: Chứa các build-time và run-time cho một cơ sở hạ tầng Cloud, bao gồm:
	Available instance types
	Instances in use
	Available networks
	Projects
Trên lý thuyết OpenStack Compute có thể hỗ trợ cơ sở dữ liệu SQL-Alchemy, SQLite3, MySQL và PostgreSQL.</li>

</ul>

<img src=http://i.imgur.com/YHTilCQ.png>

Message Queue và back-end database rất quan trọng để vận hành Nova.

Message Queue có thể là các nhóm tin AMPQ, nhưng sử dụng phổ biến là RabbitMQ, Apache Qpid (Red Hat OpenStack) và ZeroMQ. 

Back-end database: sqlite3, MySQL or PostgreSQL. 
	
<a name="3"></a>
##3. Glance – Image Service
- OpenStack Image Service cung cấp, thu hồi, lưu trữ và phân chia siêu dữ liệu cho các Images được dùng bơi Nova
- OpenStack Object Storage cho phép người dùng  lưu trữ và lấy hình ảnh thông qua một dịch vụ web đơn giản.
- Glance bắt tay với Nova để cung cấp hỗ trợ cho dự phòng máy ảo. Nó cũng có sự tương tác với Keystone để xác thực API.

Các thành phần:
<ul>
<li>Glance-api :  Chấp nhận các yêu cầu của Image API để phát hiện image, truy xuất là lưu trữ image.</li>
<li>Glance-registry : Lưu trữ, xử lý và lấy siêu dữ liệu về images( kích thước, loại...).</li>
<li>Glance database : Cơ sở dữ liệu lưu trữ siêu dữ liệu image.</li>
<li>A storage repository: Lưu trữ các file image thực, Glance hỗ trợ tập tin hệ thống bình thường, thiết bị khối RADOS, Amazon S3, HTTP, Swift.</li>
<li>Metadata definition service: API phổ biến cho các nhà cung cấp, quản trị, dịch vụ, người dùng... có ý nghĩa xác định siêu dữ liệu tùy chỉnh của riêng họ. Metadata có thể được sử dụng trên các loại khác nhau của các nguồn tài nguyên.</li>
</ul>
Danh sách định dạng disk và container được hỗ trợ:

Disk format: 
```sh
raw: Định dạng có cấu trúc
vhd: disk của máy ảo VMware, Xen....
vmdk: Hỗ trợ bởi nhiều máy ảo phổ biến
vdi: Hỗ trợ bởi VirtualBox,QEMU
iso: Định dạng lưu trữ dữ liệu của đĩa quang học
qcow2: Hỗ trợ bởi QEMU
aki: Amazon kernel image
ari: Amazon ramdisk image
ami: Amazon machine image
```
Container format: dùng để xem virtual machine image như một định dạng tập tin, nó có thể chứa siêu dữ liệu về máy ảo thực tế.
```sh	
bare: Không lưu trữ hoặc đóng gói siêu dữ liệu
ovf: Định dạng OVF
aki: Amazon kernel image
ari: Amazon ramdisk image
ami: Amazon machine image
ova: tập lưu trữ OVA tar
```
Glance API
```sh
API: có một vai trò quan trọng với Glance để xử lý hình ảnh.
Có 2 phiên bản của Glance API - Version 1 và Version 2. 
Glance API phiên bản 2 cung cấp tiêu chuẩn một số thuộc tính tùy chỉnh của image.
```

<a name="4"></a>	
##4.Cinder – Block Storage Service

Cinder là một dịch vụ lưu trữ khối(Block Storage service) cho OpenStack. Nó được thiết kế để cho phép sử dụng hoặc là một thực hiện tham chiếu (LVM) để trình bày tài nguyên lưu trữ cho người dùng có thể được sử dụng bởi OpenStack Compute Project (Nova). Các mô tả ngắn về Cinder là nó virtualizes pool các thiết bị lưu trữ khối và cung cấp cho người dùng cuối với một API tự phục vụ yêu cầu và tiêu thụ các nguồn tài nguyên mà không cần bất kỳ kiến ​​thức về nơi lưu trữ của họ được thực sự triển khai hoặc vào loại thiết bị.

Self service API được sử dụng để giao tiếp với các dịch vụ Cinder.

Kiến trúc Cinder

<img src= http://i.imgur.com/fRjaMgq.png>

**Cinder-api**

- Ứng dụng WSGI xác nhận và định tuyến yêu cầu cho các Block Storage service
- Yêu cầu được gửi tới cinder-scheduler để chuyển cho cinder-volumes thích hợp

**Cinder-scheduler**
<ul>
<li>Dựa vào việc yêu cầu thông điệp yêu cầu chuyển tới Cinder Volume Service thích hợp thông qua AMPQ (RabbitMQ or Qpid)</li>
<li>Có thể cấu hình để dùng round-robin.</li>
<li>Filter Scheduler là chế độ xác định mặc định nơi để gửi volume dựa trên năng lực, khu sẵn có, lại Volume, và khẳ năng bộ lịc tùy chỉnh.</li>
</ul>
**Cinder-volume**
<ul>
<li>Quản lý các khối lưu trữ back-end khác nhau.
<li>Tương tác trực tiếp với phần cứng hoặc phần mềm cung cấp các lưu trữ khối.</li>
<li>Cung cấp cái nhìn về volume cho người sử dụng.</li>
</ul>
**Cinder-backup**
<ul>
<li>Cung cấp dịch vụ sao lưu của Cinder volumes cho OpenStack Swift.</li>
</ul>
**Messaging queue**
<ul>
<li>Định tuyến thông tin giữa các tiến trình của Block Storage</li>
</ul>
	
Thành phần Cinder:

**Back-end Storage Devices**
<ul>
<li>Mặc định sử dụng LVM(Logical Volume Manager) trên nhóm local volume (cinder-volumes)</li>
<li>Hỗ trợ các thiết bị như mảng external RAID hoặc các thiết bị lưu trữ</li>
<li>Kích thước Block có thể điều chỉnh khi dùng KVM hoặc QEMU</li>
</ul>
**Users and Tenants/Projects**
<ul>
<li>Dùng Role-based Access Control (RBAC) cho nhiều người thuê</li>
<li>Sử dụng "policy.json" để duy trì các quy tắc cho mỗi vai trò</li>
<li>Volume truy cập là mỗi người dùng</li>
<li>Hạn ngạch để kiểm soát tiêu thụ tài nguyên trên tài nguyên phần cứng có sẵn đều là giá thuê</li>
<li>Hạn ngạch có thể được sử dụng để kiểm soát: số lượng volume và ảnh chụp mà có thể được tạo ra cũng như tổng số GBs phép cho mỗi người thuê</li>
</ul>
**Volumes, Snapshots and Backups**
<ul>
<li>Volumes: Phân bổ tài nguyên lưu trữ khối có thể được gắn liền với các trường hợp như lưu trữ thứ cấp hoặc chúng có thể được sử dụng như là các kho chứa gốc để khởi động các trường hợp. </li>
<li>Là thiết bị lưu trữ khối R/W gắn kết thường được gắn liền với các nút tính toán thông qua iSCSI.</li>
<li>Snapshots: Một điểm chỉ đọc trong thời gian sao chép của volume. Các snapshot có thể được tạo ra từ volume đang sử dụng hoặc có sẵn. Các snapshot  có thể được dùng để tạo ra volume mới.</li>
<li>Backups: Một bản sao lưu của volume được lưu trữ trong OpenStack Object Storage.</li>
</ul>

<a name="5"></a>
##5.Swift – Object Storage Service
Object Storage như là một nền tảng mạnh mẽ, khả năng mở rộng và lưu trữ chịu lỗi cho dữ liệu phi cấu trúc như các đối tượng. Đối tượng được lưu trữ bit, truy cập thông qua một giao diện dựa trên HTTP. Bạn không thể truy cập dữ liệu ở các khối hoặc tập tin cấp. Object Storage thường được sử dụng để lưu trữ và sao lưu dữ liệu, với trường hợp sử dụng trong virtual machine image, hình ảnh, video và âm nhạc.
	
Kiến trúc OpenStack Swift

<img src=http://i.imgur.com/PhHecut.png>

```sh
Proxy Nodes: Là điểm tương tác với "Swift clients" và xử lý các yêu cầu và tiến trình. 
Storage Nodes: Là điểm mà máy chủ lưu trữ các objects.
```

Các thành phần:
<ul>
<li>Proxy servers : Chấp nhận các OpenStack Object Storage API và các yêu cấu HTTP để upload dữ liệu, chỉnh sửa siêu dữ liệu, tạo các container.</li>
<li>Account servers : Quản lý các tài khoản của Object Storage.</li>
<li>Container servers : Quản lý kết nối của các container hoặc thư mục trong Object Storage.</li>
<li>Object servers: Quản lý đối tượng thực tế như các file trên các nút lưu trữ.</li>
<li>Various periodic processes: Thực hiện nhiệm vụ thu dọn trên các store dữ liệu lớn. </li>
<li>WSGI middleware: Xử lý xác thực, thường là OpenStack Identity. </li>
<li>Swift client: Cho phép user dùng trình lệnh để REST API thông qua command-line.</li>
<li>Swift-init: Các Script khởi tạo kiến trúc kết nối của file.</li>
<li>Swift-recon: Công cụ li để thu thập các dữ liệu khác nhau và các thông tin từ xa về một cụm đã được thu thập bởi các swift-recon trung gian.</li>
<li>Swift-ring-builder: Vòng lưu trữ xây dựng và tái cân bằng tiện ích.
</ul>

<a name="6"></a>	
##6. Neutron – Networking Service
<ul>
<li>Một dịch vụ độc lập thường triển khai một số quy trình qua một số nút. Các quá trình tương tác với nhau và với dịch vụ OpenStack khác.</li>
<li>Cung cấp dịch vụ về mạng.</li>
<li>Thay thế nova-network để hướng tới SDN trong OpenStack.</li>
<li>Có nhiều dịch vụ cao cấp: FWaas, LBaaS, VPNaaS.</li>
<li>Có cơ chế Plugin để làm việc với các hãng và giải pháp về network khác.</li>
</ul>	

Các thành phần của Neutron
<ul>
<li>Neutron server (neutron-server and neutron-*-plugin): Dịch vụ này chạy trên các nút mạng để phục vụ các  Networking API và phần mở rộng của nó. Nó cũng thực thi các mô hình mạng và địa chỉ IP của mỗi cổng
<li>Plugin agent (neutron-*-agent): Chạy trên mỗi nút tính toán để quản lý các cấu hình chuyển mạch ảo (vSwitch) địa phương
<li>DHCP agent (neutron-dhcp-agent): Cung cấp dịch vụ DHCP cho mạng người thuê. Thành phần này là như nhau trên tất cả các plug-in và chịu trách nhiệm cho việc duy trì cấu hình DHCP
<li>L3 agent (neutron-l3-agent): Cung cấp L3 / NAT chuyển tiếp để truy cập mạng bên ngoài của máy ảo trên mạng người thuê
<li>Network provider services (SDN server/services): Cung cấp các dịch vụ mạng bổ sung cho mạng lưới thuê. Những dịch vụ SDN có thể tương tác với các neutron-server, neutron-plugin, và / hoặc plugin-đại lý thông qua các API REST hoặc các kênh truyền thông khác.
</ul>

<img src=http://i.imgur.com/5Z6PnkK.png>

**Neutron API**

``Network`` - Một phân khúc L2 biệt lập, tương tự VLAN trong thế giới mạng vật lý

``Subnet`` - Một khối địa chỉ IP v4 hoặc v6 và trạng thái cấu hình liên quan

``Port`` - Một điểm kết nối để gắn một thiết bị duy nhất, chẳng hạn như các NIC của một máy chủ ảo, với một mạng ảo. Cũng mô tả các cấu hình mạng liên quan, chẳng hạn như MAC và địa chỉ IP được sử dụng trên cổng đó.
	
**Neutron Plug-ins**
	Plugin là giao diện giữa neutron và các công nghệ back-end như SDN, Cisco, VMware NSX.
	
plug-ins
```sh
	Open vSwitch
	Cisco UCS/Nexus
	Linux Bridge
	Nicira Network Virtualization Platform
	Ryu OpenFlow Controller
	NEC OpenFlow
```
Một plugin không liên quan trực tiếp đến các nhà cung cấp bên thứ 3 nhưng là một plugin rất quan trọng là ML2 (Modular Layer 2)
Nếu không có trình điều khiển ML2, Neutron chỉ có thể cung cấp một loại hình dịch vụ lớp 2 vì các hoạt động là độc lập.

<a name="7"></a>	
##7. Horizon – Dashboard
	Cung cấp một giao diện người dùng trên web tới các dịch vụ OpenStack bao gồm Nova, Swift, Keystone, vv
	Dashboard 

<a name="8"></a>	
##8. Heat - Block Orchestration
<ul>
<li>Dùng để triển khai các dịch vụ theo mẫu có sẵn</li>
<li>Khả năng tính toán, mở rộng hoặc thu hồi tài nguyên</li>
<li>Là tab "stack" ở trong Horizon</li>
</ul>

Các thành phần

<ul>
<li>Heat command-line client: CLI giao tiếp với Heat-Api để chạy AWS CloudFormation APIs.</li>
<li>Heat-api: Một OpenStack-native REST API xử lý các yêu cầu API bằng cách gửi chúng tới heat-engine qua Remote Procedure Call.</li>
<li>Heat-api-cfn: Một  AWS Query API tương thích với AWS CloudFormation. Nó xử lý yêu cầu API bằng cách gửi tới heat-engine.</li>
<li>Heat-engine: Cung cấp các mẫu và sự kiện lại cho người dùng API</li>
</ul>

<a name="9"></a>
##9. Ceilometer - Bock Telemetry

Cung cấp cở sở hạ tầng để thu thập mọi thông tin cần thiết liên quan tới OpenStack

3 nhiệm vụ chính của Ceilometer
<ul>
<li>Metering</li>
<li>Multi-Publishing</li>
<li>Alarming</li>
</ul>

<a name="9.1"></a>
**9.1 Telemetry Data Collection service**

Tính năng:

- Thu thập các dữ liệu liên quan tới dịch vụ OpenStack 
- Thu thập sự kiện, đo dữ liệu bằng cách giám sát các thông báo.
- Cung cấp các dữ liệu được thu thập cho các mục tiêu khác nhau gồm kho lưu trữ và hàng đợi tin nhắn.

Các thành phần:
<ul>
<li>A compute agent: Chạy trên các compute node và thống kê sử dụnh các nguồn lực.</li>
<li>A central agent: Chạy trên máy chủ quản lý tập trung để thống kê sử dụng các nguồn tài nguyên không gắn với các trường hợp hoặc các compute node.</li>
<li>A notification agent: Chạy trên máy chủ quản lý tập trung và sử dụng các thông điệp từ hàng đợi thông điệp để xây dựng sự kiện và định lượng dữ liệu.</li>
<li>An API server: Chạy trên một hoặc nhiều máy chủ quản lý để cung cấp truy cập dữ liệu từ kho dữ liệu. </li>
</ul>

<a name="9.2"></a>
**9.2 Telemetry Alarming service**

Dịch vụ báo động từ xa khi các quy định bị phá vỡ.

Các thành phần:
<ul>
<li>An API server (aodh-api): Cung cấp truy cập vào các thông tin báo động lưu trữ trong kho dữ liệu.</li>
<li>An alarm evaluator (aodh-evaluator):	</li>
<li>A notification listener (aodh-listener): Quyết định khi nào kich hoạt báo động.</li>
<li>An alarm notifier (aodh-notifier): Cho phép báo động được thiết lập dựa trên các ngưỡng đánh giá với mẫu thu thập.</li>
</ul>
<a name="10"></a>
##10. Trove - Database Service

<ul>
<li>Là một dịch vụ cho phép người dùng sử dụng cơ sở dữ liệu mà không cần quản lý cơ sở hạ tầng cơ sở dữ liệu.</li>
<li>Với nhiệm vụ đảm bảo khả năng mở rộng và độ tin cậy cơ sở dữ liệu đám mây. Có khả năng back up và hỗ trợ SQL/NoSQL.</li>
</ul>
Mô hình :

<img src=http://i.imgur.com/dq6y2Yc.png>

Các thành phần chính:  
<ul>
<li>Python-troveclient: CLI giao tiếp với các thành phần trove-api.</li>
<li>Trove-api: Cung cấp OpenStack-native RESTful API hỗ trợ JSON để cung cấp và quản lý các trường Trove. </li>
<li>Trove-conductor: Chạy trên máy chủ và nhận tin nhắn từ các trường khách muốn truy cập thông tin trên máy chủ.</li>
<li>Trove-taskmanager: Hỗ trợ các dự phòng các trường hợp, quản lý vòng đời và thực hiện các hoạt động trên các trường.</li>
<li>Trove-guestagent: Chạy trên trường khách. Quản lý và thực hiện các hoạt động trên cơ sở dữ liệu riêng của mình.</li>
</ul>
	
	
	
	
	
	
	 