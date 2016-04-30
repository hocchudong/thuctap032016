# Các project trong OpenStack
# Mục lục
<h4><a href="#architecture">A. Kiến trúc của OpenStack</a></h4> 
<ul>
<li><a href="#concept">I - Kiến trúc mức khái niệm</a>
</li>
<li><a href="#logical">II - Kiến trúc mức logic</a>

</li>
</ul>

<h4><a href="#project">B. Các project trong OpenStack</a></h4>
<ul>
<li><a href="#keystone">I - Keystone - Identity Service</a></li>
<li><a href="#nova">II - Nova - Compute Service</a></li>
<li><a href="#glance">III - Glance - Image Service</a></li>
<li><a href="#cinder">IV - Cinder - Block Storage Service</a></li>
<li><a href="#cinder">V - Swift - Object Storage Service</a></li>
<li><a href="#neutron">VI - Neutron - Networking Service</a></li>
<li><a href="#horizon">VII - Horizon - Dashboard Service</a></li>
<li><a href="#heat">VIII - Heat - Orchestration Service</a></li>
<li><a href="#ceilometer">IX - Ceilometer - Monitoring and Metering Service</a></li>
<li><a href="#trove">X - Trove - Database Service</a></li>
<li><a href="#queue">XI - Messaging and Queuing System in OpenStack</a></li>
</ul>

---

<h3><a name="architecture">A. Kiến trúc của OpenStack</a></h3> 
<hr>
<ul>
<li><h4><a name="concept">I - Kiến trúc mức khái niệm</a></h4>
<hr>
Kiến trúc mức khái niệm hể hiện mối quan hệ giữa các dịch vụ trong OpenStack, như sơ đồ dưới đây.
<img src="http://docs.openstack.org/admin-guide/_images/openstack_kilo_conceptual_arch.png"/>
</li>
<li><h4><a name="logical">II - Kiến trúc mức logic</a></h4>
<hr>
Kiến trúc mức logic thể hiện rõ ràng mối quan hệ giữa các tiến trình trong mỗi project và quan hệ của chúng với tiến trình của các project khác trong OpenStack. Người quản trị cloud OpenStack muốn thiết kế, triển khai, cấu hình hệ thống của mình cần phải hiểu sơ đồ này. Dưới đây là kiến trúc mức logic của một cloud OpenStack. (Cập nhật theo phiên bản Mitaka). 
<img src="http://docs.openstack.org/admin-guide/_images/openstack-arch-kilo-logical-v1.png"/>
</li>
</ul>
---
<h3><a name="project">B. Các project trong OpenStack</a></h3>
<hr>
<ul>
<li><h4><a name="keystone">I - Keystone - Identity Service</a></h4>
<hr>
<ul>
<li>Cung cấp dịch vụ xác thực cho toàn bộ hạ tầng OpenStack
<ul>
<li> Theo dõi người dùng và quyền hạn của họ</li>
<li>Cung cấp một catalog của các dịch vụ đang sẵn sàng với các API endpoints để truy cập các dịch vụ đó</li>
</ul>
</li>
<li>
Về mặt bản chất, Keystone cung cấp chức năng xác thực và ủy quyền cho các phần tử trong OpenStack. Người dùng khai báo chứng thực với Keystone  
và dựa trên kết quả của tiến trình xác thực, nó sẽ gán "role" cùng với một token xác thực cho người dùng. "Role" này mô tả quyền hạn cũng như vai trò trong thực hiện việc vận hành OpenStack.
</li>
<li>"User" trong Keystone có thể là:
<ul>
<li>Con người</li>
<li>Dịch vụ (Nova, Cinder, neutron, etc.)</li>
<li>Endpoint (là địa chỉ có khả năng truy cập mạng như URL, RESTful API, etc.)</li>
</ul>
</li>

<li>
Keystone gán một tenant và một role cho user. Một user có thể có nhiều role trong các tenants khác nhau. Tiến trình xác thực có thể biểu diễn như sau:
<img src="http://2.bp.blogspot.com/-bPiAf5VkWiM/VEoB4XbZRpI/AAAAAAAAAFs/ABl9iaxnyhQ/s1600/Keystone_identityMgr-diagram.png"/>
</li>

<li>
Keystone được tổ chức theo nhóm các nội dịch vụ (internal services)tương tác với một hoặc nhiều endpoints. Các nội dịch vụ đó là:
<ul>
<li> Identity: 
<ul>
<li>Cung cấp dịch vụ chứng thực và dữ liệu về Users, Groups, Projects, Domains Roles, metadata, etc.</li>
<li>Về cơ bản, tất cả các dữ liệu này được quản lý bởi dịch vụ, cho phép các dịch vụ quản lý các thao tác CRUD (Create - Read - Update - Delete) với dữ liệu</li>
<li>Trong nhiều trường hợp khác, dữ liệu bị thu thập từ các dịch vụ backend được ủy quyền khác như LDAP</li>
</ul>
 </li>
<li>Token: Xác nhận và quản lý các tokens được sử dụng để xác thực yêu cầu khi thông tin của người dùng đã được xác minh</li>
<li>Catalog: cung cấp một endpoint registry sử dụng để phát hiện endpoint</li>
<li>Policy: cung cấp engine để ủy quyền dựa trên rule và kết nối với giao diện quản lý rule</li>
</ul>
</li>

<li>
 Mỗi dịch vụ này có thể được cấu hình để sử dụng một dịch vụ back-end. Một số back-end service điển hình:
 <ul>
<li>Key Value Store: cung cấp giao diện hỗ trợ tìm kiếm theo khóa</li>
<li>Memcached: Là hệ thống phân phối và lưu trữ bộ nhớ đệm (cache) và chứa dữ liệu trên RAM. (lưu tạm thông tin những dữ liệu hay sử dụng và bộ nhớ RAM)</li>
<li>SQL: sử dụng SQLAlchemy để lưu trữ dữ liệu bền vững</li>
<li>Pluggable Authentication Module (PAM): sử dụng dịch vụ PAM của hệ thống cục bộ cho việc xác thực</li>
<li>LDAP: kết nối thông qua LDAP tới một thư mục back-end, như Active Directory để xác thực các user và lấy thông tin về role </li>
</ul>
</li>

<li>
Từ bản Juno, Keystone có tính năng mới là federation of identity service. Nghĩa là thay vì việc xác thực tập trung, việc xác thực sẽ phân tán trên Internet, hay còn gọi là Identity Providers(IdPs). Lợi ích của việc sử dụng IdPs:
<ul>
<li>Không cần phải dự phòng các user entries trong Keystone (các bản ghi về người dùng), bởi vì các user entries đã được lưu trữ trong cơ sở dữ liệu của các IdPs</li>
<li>Không cần phải xây dựng mô hình xác thực trong Keystone, bởi vì các IdPs chịu trách nhiệm xác thực cho người dùng sử dụng bất kỳ công nghệ nào phù hợp. Do đó có thể kết hợp nhiều công nghệ xác thực khác nhau</li>
<li>Nhiều tổ chức hợp tác có thể chia sẻ chung các dịch vụ cloud bằng cách mỗi tổ chức sẽ sử dụng IdP cục bộ để xác thực người dùng của họ</li>
</ul>
</li>
</ul>
</li>


<li><h4><a name="nova">II - Nova - Compute Service</a></h4>
<hr>
<ul style="list-style: decimal">
<li>Chức năng
<ul>
<li>Thực hiện quản lý vòng đời các máy ảo, cung cấp abstract layer tương tác với hypervisors được hỗ trợ: Hyper-V, VMware, XenServer, Xen via libvirt, KVM (libvirt/QEMU)</li>
<li>Nova phân lại hypervisors thành 3 nhóm dựa trên số lượng các bài kiểm thử thành công với các driver tương tác với hypervisors:
<ul>
<li>GROUP A: libvirt (qemu/KVM on x86). Các drivers này được hỗ trợ hoàn toàn. Các bài kiểm tra bao gồm: unit test và functional testing </li>
<li>GROUP B: Hyper-V, VMware, XenServer. Các drivers này được hỗ trợ ở mức trung bình. Các bài test bao gồm: unit test và functional testing cung cấp bởi một hệ thống bên ngoài. </li>
<li>GROUP C: baremetal, docker, Xen via libvirt, LXC via libvirt. Các driver này được thực hiện một số bài kiểm thử nhỏ và có thể hoạt động không ổn định. Việc sử dụng chúng là mạo hiểm. Các bài test bao gồm: unit tests và các bài test chức năng không public</li>
</ul>
</li>
</ul>
</li>

<li>Các thành phần - gồm 7 thành phần chính:
<ul>
<li>Cloud Controller: đại diện cho trạng thái toàn cục và tương tác với các component khác</li>
<li>API Server: có thể coi như các Web services cho cloud controller</li>
<li>Compute Controller: cung cấp tài nguyên máy chủ tính toán</li>
<li>Object Store: cung cấp dịch vụ lưu trữ</li>
<li>Auth Manager: cung cấp dịch vụ xác thực và ủy quyền</li>
<li>Volume Controller: cung cấp các khối lưu trữ bền vững và nhanh chóng cho các computer server</li>
<li>Network controller: cung cấp mạng ảo cho phép các compute server tương tác với nhau và với public network</li>
<li>Scheduler lựa chọn compute controller phù hợp nhất để host một instance (máy ảo)</li>
</ul>
</li>

<li>Mối quan hệ giữa các thành phần
<ul>
<li>Sơ đồ: 
<img src="http://2.bp.blogspot.com/-bYd9cxoncgs/VErn5ECWjZI/AAAAAAAAAF8/gYMkUCD51FQ/s1600/Nova_architecture.png"/>
<i> Chú ý: Message Queue và các back-end database rất quan trọng trong khi vận hành Nova</i>
</li>
<li> Message Queue có thể là bất kì một AMQP message queue nào. Trong OpenStack đó là RabbitMQ, Apache Qpid và ZeroMQ</li>
<li>Back-end database thông thường là sqlite3, MySQL và PostgreSQL</li>
<li>Mô tả ngắn gọn về Nova:
<img src="http://3.bp.blogspot.com/-NcY-3pbZbcY/VErtbVISE9I/AAAAAAAAAGM/6r7MVm78qLk/s1600/nova-logical_KenPepple.gif"/>
<ul>
<li> End users (DevOps, Dev, hoặc có thể là các thành phần khác trong OpenStack) sẽ "nói chuyện" với nova-api để tương tác với OpenStack Nova</li>
<li>Các OpenStack Nova daemons trao đổi thông tin qua queue (lưu trữ các actions) và database (infomation) để thực hiện các API requests</li>
<li>OpenStack Glance giao tiếp với OpenStack Nova interfaces thông qua Glance API</li>
<li>Nova-networking vẫn được sử dụng trong một số use cases. Người dùng có thể lựa chọn nova-networking hoặc Neutron</li>
</ul>
</li>
</ul>

</li>

</ul>
</li>


<li><h4><a name="glance">III - Glance - Image Service</a></h4>
<hr>
<ul>
<li>OpenStack Image Service cung cấp dịch vụ quản lý các disk image của các máy ảo. Dịch vụ này cung cấp dịch vụ tìm kiếm, đăng ký, chuyển các disk image tới Compute service và cũng dùng vào mục đích dự phòng các máy ảo.
<img src="http://4.bp.blogspot.com/-8BGR7XSvuSw/VEr6NqccUKI/AAAAAAAAAGc/PP4yLwUYzpI/s1600/glance.png"/>
</li>

<li>Danh sách các tiến trình của Images Service và chức năng của chúng:
<ul>
<li>glance-api: nó tiếp nhận lời gọi Image API để thực hiện tìm kiếm, thu thập và lưu trữ các images</li>
<li> glance-registry: lưu trữ, thực thi và thu thập metadata về các image (size, type, etc.)</li>
<li>glance-database: là cơ sở dữ liệu lưu trữ metadata của các image</li>
<li>storage repository: là các image files. Glance hỗ trợ hệ thống file thông thường như: RADOS block devices, Amazon S3, HTTP và Swift</li>
</ul>
Glance tiếp nhận các API request về images (hoặc metadata của images) từ người dùng cuối hoặc các Nova component và có thể lưu trữ các file ổ đĩa trong object storage service, Swift hoặc các storage repo khác.
</li>

<li>Danh sách các định dạng ổ đĩa và container được hỗ trợ bao gồm:
<ul>
<li>Disk Format: Disk format của một image máy ảo là định dạng của disk image, bao gồm:
<ul>
<li>raw: là định dạng ảnh đĩa phi cấu trúc</li>
<li>vhd: là định dạng ảnh đĩa chung sử dụng bởi các công nghệ VMware, Xen, Microsoft, VirtualBox, etc.</li>
<li>vmdk: định dạng ảnh đĩa chung hỗ trợ bởi nhiều công nghệ ảo hóa khác nhau (điển hình là VMware)</li>
<li>vdi: định dạng ảnh đĩa hỗ trợ bởi VirtualBox và QEMU emulator</li>
<li>iso: định dạng cho việc lưu trữ dữ liệu của ổ đĩa quang</li>
<li>qcow2: hỗ trợ bởi QEMU và có thể ở rộng động, hỗ trợ copy on write</li>
<li>aki, ari, ami</li>
</ul>
</li>

<li>Container Format:
<ul>
<li>bare: định dạng này xác định rằng không có container cho image</li>
<li>ovf: định dạng OVF container</li>
<li>aki: xác định Amazon kernel image lưu trữ trong Glance </li>
<li>ami: Xác định Amazon ramdisk image lưu trữ trong Glance</li>
<li>ova: xác định file OVA tar lưu trữ trong Glance</li>
</ul>
</li>
</ul>
 </li>

<li>oVirt tích hợp với Glance: oVirt (Open Virtualization Manager) từ Red Hat là project cho phép oVirt user sử dụng, trích xuất và share images với Glance. Glance sẽ được coi như một External Provider cho oVirt 3.3.
<br>Bên cạnh việc import và export ác image tới Glance, việc tích hợp oVirt cho phép oVirt thực hiện tìm kiếm image và liệt kê nội dung của Glance trên giao diện của oVirt
<br><br>
<img src="http://1.bp.blogspot.com/-8_hta2MsdqE/VEvpGcz_n1I/AAAAAAAAAGs/ekV15QqyzWo/s1600/discovery_glance_provider_small.png"/>

<br><br>Tính năng hữu ích khác khi tích hợp oVirt với Glance đó là oVirt có thể "discover" kích thước của image định dạng QCOW2 bằng cách tìm kiếm trong QCOW2 header. Glance metadata không cung cấp kích thước của image.

</li>

<li> Glance API: API đóng vai trò quan trọng trong việc xử lý image của Glance. Glance API có 2 version 1 và 2. Glance API ver2 cung cấp tiêu chuẩn của một số thuộc tính tùy chỉnh của image.
<br>Glance phụ thuộc vào Keystone và OpenStack Identity API để thực hiện việc xác thực cho client. Bạn phải có được token xác thực từ Keystone và gửi token đó đi cùng với mọi API requests tới Glance thông qua X-Auth-Token header. Glance sẽ tương tác với Keystone để xác nhận hiệu lực của token và lấy được các thông tin chứng thực 
</li>

</ul>

</li>


<li><h4><a name="cinder">IV - Cinder - Block Storage Service</a></h4>
<hr>
<ul>
<li>Sơ lược về Cinder
<ul>
<li>Tương tự như Amazon Web Services S3 (Simple Storage Service) cung cấp khối lưu trữ bền vững (persistent block storage) để vận hành các máy ảo.</li>
<li>Cinder cung cấp dịch vụ Block Storage. Một cách ngắn gọn, Cinder thực hiện ảo hóa pool các khối thiết bị lưu trữ và cung cấp cho người dùng cuối API để request và sử dụng tài nguyên mà không cần biết khối lưu trữ của họ thực sự lưu trữ ở đâu và loại thiết bị là gì. Cũng như các dịch vụ khác trong OpenStack, self service API được sử dụng để tương tác với dịch vụ Cinder.</li>
<li>Ý tưởng chính của Cinder là cung cấp một lớp abstract cho người dùng cuối đối với các khối thiết bị lưu trữ. Người dùng Cinder không cần phải biết chi tiết hay quản lý khối thiết bị lưu trữ vật lý, chỉ cần sử dụng khối lưu trữ được cung cấp.</li>
</ul>
<br>
</li>

<li>Các thành phần của Cinder <br>
<img src="http://4.bp.blogspot.com/-onbO2eMISfk/VEwBuGLkOvI/AAAAAAAAAHM/ryp2OhRTcBE/s1600/cinder_architecture.png"/>
<br><br>
<ul>
<li>Cinder-api:
<ul>
<li>Một ứng dụng WSGI có vai trò xác thực và chuyển request trong toàn bộ dịch vụ Block Storage</li>
<li>Request được gửi tới cinder-scheduler rồi điều hướng tới cinder-volumes thích hợp</li>
</ul>
</li>
<li>Cinder-scheduler:
<ul>
<li>Dựa trên request được điều hướng tới, cinder-scheduler chuyển request tới Cinder Volume Service thông qua giao thức AMQP (lưu trữ bản tin điều hướng trong Queue của RabbitMQ hoặc Qpid)</li>
<li>Có thể được cấu hình để sử dụng cơ chế round-robin</li>
<li>Filter Scheduler là mode mặc định xác định nơi để gửi volume dựa trên Capacity, Avalability Zone, Volume Types, Capabilities cũng các bộ lọc tùy biến</li>
</ul>
</li>
<li>Cinder-volume:
<ul>
<li>Quản lý các công nghệ lưu trữ back-ends khác nhau</li>
<li>Tương tác trực tiếp với phần cứng hoặc phần mềm cung cấp khối lưu trữ</li>
<li>Cung cấp khung nhìn của volume cung cấp cho người dùng</li>
</ul>
</li>
<li>Cinder-backup: Cung cấp dịch vụ backups của Cinder volumes cho OpenStack Swift</li>
</ul>
</li>

<li>Một số khái niệm quan trọng trong Cinder
<ul>
<li>Back-end Storage Devices
<ul>
<li>Mặc định là LVM (Logical Volume Manager) trên nhóm các volume cục bộ - "cinder-volumes"</li>
<li>Hỗ trợ các thiết bị khác như RAID ngoài hoặc các thiết bị lưu trữ</li>
<li> Kích thước khối lưu trữ được điều chỉnh sử dụng hypervisor như KVM hoặc QEMU </li>
</ul>
</li>
<li>Users và Tenants/Projects
<ul>
<li>Sử dụng cơ chế Role-based Access Control (RBAC) cho multi-tenants</li>
<li>Sử dụng file "policy.json" để duy trì rule cho mỗi role</li>
<li>Volume truy cập bởi mỗi người dùng riêng biệt</li>
<li>Định ra Quotas để kiểm soát mức độ tiêu tốn tài nguyên thông qua tài nguyên phần cứng sẵn sàng cho mỗi tenants</li>
<li>Quota có thể được sử dụng để kiểm soát: số lượng volume và snapshots có thể tạo ra cũng như tổng dung lượng (theo GBs) cho phép đối với mỗi tenants</li>
</ul>
</li>
<li>Volumes, Snapshots và Backups:<br>
Tài nguyên mà dịch vụ Block Storage service cung cấp là volumes và snapshots:
<ul>
<li>Volumes: Cấp phát các khối lưu trữ có thể attach vào các instance như một khối lưu trữ thứ hai hoặc có thể sử dụng đẻ boot các instances. Volume là các khối lưu trữ đọc/ghi bên vững được attach trên compute node thông qua iSCSI</li>
<li>Snapshots: có thể được khởi tạo từ 1 volume đang sử dụng (bằng việc sử dụng tùy chọn --force True) hoặc trong trạng thái sẵn sàng. Snapshot sau đó có thể sử dụng để tạo volume mới.</li>
<li> Backups: là bản dự phòng của 1 volume lưu trữ trong OpenStack Object Storage</li>
</ul>
Lưu trữ vật lý hỗ trợ Cinder có thể là ổ vật lý HDD hoặc SSD. NÓ cũng có thể là hệ thống lưu trữ ngoài cung cấp bởi giải pháp lưu trữ của bên thứ ba như NetApp hoặc EMC 
</li>
</ul>
</li>
</ul>
</li>


<li><h4><a name="cinder">V - Swift - Object Storage Service</a></h4></li>
<hr>

<li><h4><a name="neutron">VI - Neutron - Networking Service</a></h4>
<hr>
<ul>
<li>NEUTRON - Networking Service
<ul>
<li>Ban đầu khi OpenStack mới ra mắt, dịch vụ network được cung cấp trong Nova - nova-networking.  Sau này, khi OpenStack ngày càng trưởng thành, yêu cầu đặt ra là phải có module networking mạnh mẽ và khả chuyển (powerful & flexible). </li>
<li>Nova-networking bị hạn chế trong các network topo, và gần như không hỗ trợ các giải pháp của bên thứ ba. Nova-network chỉ có thể sử dụng Linux-bridge, hạn chế network type và iptable để cung cấp dịch vụ mạng cho hypervisor trong Nova. Do đó project network thay thế nova-networking ra đời - ban đầu đặt tên Quantum sau đổi tên lại thành Neutron</li>
</ul>
</li>

<li>Các thành phần của neutron
<ul>
<li>neutron server (neutron-server là neutron-*-plugin)<br>
Dịch vụ này chạy trên các network node để phục vụ Networking API và các mở rộng của nó. Nó cũng tạo ra network model và đánh địa chỉ IP cho mỗi port. neutron-server và các plugin agent yêu cầu truy cập vào database để lưu trữ thông tin
lâu dài và truy cập vào message queue (RabbitMQ) để giao tiếp nội bộ (giữa các tiến trình và với các tiến trình của các project khác)</li>
<li>plugin agent (neutron-*-agent)<br>
Chạy trên các Compute node để quản lý cấu hình các switch ảo cục bộ (vSwitch). Các plugin này xác định xem những agent nào đang chạy. Dịch vụ này yêu cầu truy cập vào message queue.</li>
<li>DHCP agent (neutron-dhcp-agent)<br>
Cung cấp dịch vụ DHCP cho tenant networks. Agent này chịu trách nhiệm duy trì cấu hình DHCP. neutron-dhcp-agent yêu cầu truy cập message queue</li>
<li> L3 agent (neutron-l3-agent)<br>
Cung cấp kết nối ra mạng ngoài (internet) cho các VM trên các tenant networks nhờ L3/NAT forwarding. </li>
<li>network provider service (SDN server/services)<br>
Cung cấp dịch vụ mạng nâng cao cho tenant network. Các dịch vụ SDN này có thể tương tác với neutron-server, neutron-plugin, plugin-agents thông qua REST APIs hoặc các kênh kết nối khác.
 <img src="http://1.bp.blogspot.com/-Y2nFB5BI5Xw/VEyH2C5MaZI/AAAAAAAAAIU/ZbkJ2LEexbo/s1600/Neutron-PhysNet-Diagram.png"/>
</li>
</ul>
 </li>

<li> Neutron API: cho phép người dùng định nghĩa:
<ul>
<li> Network: người dùng có thể tạo ra một L2 segment tách biệt, tương tự như VLAN </li>
<li>Subnet: người dùng có thể định nghĩa ra được một tập các địa chỉ IP v4 hoặc v6 và các tham số cấu hình liên quan</li>
<li>Port: là điểm kết nối cho phép attach  một thiết bị đơn lẻ (ví dụ như card mạng của server ảo) vào mạng ảo (Virtual network) cũng như các thông số cấu hình network liên quan như địa chỉ MAC và IP được sử dụng trên port đó.</li>
</ul>
 </li>

<li>Neutron API extension<br>
 Với API extension. user có thể định nghĩa nên các chức năng mạng bổ sung thông qua Neutron plugins. Sơ đồ dưới đây biểu diễn mối quan hệ giữa Neutron API, Neutron API extension và Neutron plugin - plugin interface để giao tiếp với SDN Controller - OpenDaylight.
 <img src="http://2.bp.blogspot.com/-pKluO0upSZw/VEyI9UaO5CI/AAAAAAAAAIc/iNJb13K9de8/s1600/SDN-diagram.jpg"/>
 </li>
<li>Neutron plugins<br>
 Là giao diện kết nối giữa Neutron và các công nghệ back-end như SDN, Cisco, VMware NSX. Nhờ đó người dùng Neutron có thể tận dụng được các tính năng nâng cao của các thiết bị mạng hoặc phần mềm mạng của bên thứ ba.
 Các plugin này bao gồm: Open vSwitch, Cisco UCS/Nexus, Linux Bridge, Nicira Network Virtualization Platform,  Ryu OpenFlow Controller, NEC OpenFlow.
 <br>
 Một trong các plugin không trực tiếp liên quan tới công nghệ bên thứ ba nhưng là 1 plugin quan trọng đó là ML2 (Modular Layer 2) plugin. Plugin này cho phép hoạt động đồng thời của nhiều công nghệ mạng hỗn hợp trong Neutron.<br><br>
 <img src="http://2.bp.blogspot.com/-USeyydbptFo/VFp8P06ST_I/AAAAAAAAAQo/uBz-go8sVz4/s1600/neutron_ML2.jpg"/><br>
 Không có ML2 driver, Neutron chỉ có thể cung cấp dịch vụ lớp 2. Hai khái niệm về driver trong ML2 là Type và Mechanism:
 <ul>
<li>Type Manager: GRE, VLAN, VXLAN</li>
<li>Mechanism Manager: Cisco APIC, Cisco Nexus, Linux Bridge, OvS  </li>
</ul>
 </li>
</ul>

</li>


<li><h4><a name="horizon">VII - Horizon - Dashboard Service</a></h4>
<hr>
Cung cấp giao diện nền web cho người dùng cuối và người quản trị cloud để tương tác với các dịch vụ khác của OpenStack, ví dụ như vận hành các instance, cấp phát địa chỉ IP và kiểm soát cấu hình truy cập các dịch vụ. Một số thông tin mà giao diện người dùng cung cấp cho người sử dụng:
<ul>
<li>Thông tin về quota và cách sử dụng</li>
<li>Instances để vậy hành các máy ảo cloud</li>
<li>Volume Management điều khiển khởi tạo, hủy kết nối tới các block storage</li>
<li>Images and Snapshots để up load và điều khiển các virtual images, các virtual images được sử dụng để back up hoặc boot một instance mới</li>
<li>Mục addition cũng cung cấp giao diện cho hệ thống cloud:
<ul>
<li>Project: cung cấp các group logic của các user</li>
<li>User: quản trị các user</li>
<li>System Info: Hiển thị các dịch vụ đang chạy trên cloud</li>
<li>Flavors: định nghĩa các dịch vụ catalog yêu cầu về CPU, RAM và BOOT disk storage</li>
</ul>

</li>
</ul>

</li>


<li><h4><a name="heat">VIII - Heat - Orchestration Service</a></h4></li>
<hr>


<li><h4><a name="ceilometer">IX - Ceilometer - Monitoring and Metering Service</a></h4></li>
<hr>


<li><h4><a name="trove">X - Trove - Database Service</a></h4>
<hr>
<ul>
<li>Giới thiệu Trove
<br>
Trove là dịch vụ cho phép người dùng sử dụng database quan hệ hoặc phi quan hệ (Relational database và Non-Relational database - NoSQL) mà không cần quan tâm tới hạ tầng database. Nó tạo ra lớp abstract giữa người dùng và database, thực hiện dự phòng, mở rộng và quản lý database trên hạ tầng OpenStack.
</li>
<li>Kiến trúc của Trove
<br><br>
<img src="http://2.bp.blogspot.com/-MuunxQO3w-0/VE8kV7B-Z0I/AAAAAAAAAK0/XCAJBVPuF04/s1600/trove_arch.jpg"/>
<br><br>
Trove tương tác với các thành phần khác trong OpenStack để cung cấp dịch vụ Database
<br><br>
<img src="http://3.bp.blogspot.com/-DnAwBEIXMr0/VE8nnAZ_pLI/AAAAAAAAALA/bg1wKms9VrU/s1600/trove_arch2.png"/>
<br><br>
</li>
<li>Các thành phần của Trove
<br>
Các thành phần chủ đạo của Trove:
<ul>
<li>API server</li>
<li>Message Bus</li>
<li>Task Manager</li>
<li>Guest Agent</li>
<li>Conductor</li>
</ul>
Cụ thể hơn:
<ul>
<li>Trove-api service là một WSGI thực hiện REST API mà dựa vào đó người dùng có thể dự phòng database instance, để mở rộng tài nguyên cpu và memory của databas instance cũng như không gian lưu trữ.
API cũng có thể sử dụng để quản lý các database instance. Như hình vẽ trên, một database (có thê là MySQL hoặc PosgreSQL) và một Message Bus(RabbitMQ, Qpid) được sử dụng cho trove api server để giao tiếp với trove-taskmanager - tại đó mọi hành động sẽ được thực thi.</li>
<li>Trove-taskmanager nói chuyện với Nova, Cinder, Glance khi database image được lưu trữ. Khi database instance chạy, Guest Agent - một thành phần của database instance sẽ thực hiện health check và tương tác trở lại với health status của database instance thông qua trove-conductor</li>
<li>Trove cũng tương tác với Keystone để xác thực cũng như Neutron để sử dụng dịch vụ mạng</li>
<li>Trove hỗ trợ các hệ quản trị csdl sau: MySQL, MongoDB, Cassandra, Redis, CouchDB, PostgreSQL</li>
</ul>

</li>
</ul>

</li>


<li><h4><a name="queue">XI - Messaging and Queuing System in OpenStack</a></h4></li>
<hr>
</ul>
