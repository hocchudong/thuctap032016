# Tìm hiểu về Cloud Computing và OpenStack
# Mục lục
<h3><a href="#cloud">1. Cloud Computing</a></h3>
<ul style="list-style: none">
<li><h4><a href="#virtual">1.1. Khái niệm ảo hóa</a></h4></li>
<li><h4><a href="#nist">1.2. Khái niệm Cloud Computing của NIST</a></h4></li>
<li><h4><a href="#arch">1.3. Giải thích kiến trúc cloud</a></h4></li>
<li><h4><a href="#543">1.4. 5-4-3 trong Cloud Computing</a></h4></li>
</ul>
<h3><a href="#stack">2. OpenStack</a></h3>
<ul style="list-style: none">
<li><h4><a href="#history">2.1. Lịch sử hình thành</a></h4></li>
<li><h4><a href="#feature">2.2. Tóm lược đặc điểm</a></h4></li>
<li><h4><a href="#os-arch">2.3. Kiến trúc</a></h4></li>
<li><h4><a href="#project">2.4. Các project thành phần</a></h4></li>
</ul>
---

<h3><a name="cloud">1. Cloud Computing</a></h3>
<ul style="list-style: none">
<li><h4><a name="virtual">1.1. Khái niệm ảo hóa</a></h4></li>
<ul>
<li>Kĩ thuật tạo ra phần cứng, thiết bị mạng, thiết bị lưu trữ ảo, etc.</li>
<li>Các khái niệm liên quan: Hardware Virtualization, Server Virtualization, Network virtualization, etc. Các máy ảo (virtual machine) có gần như đầy đủ các thành phần của máy thật, cài đặt được hệ điều hành, etc. Trong Network Virtualization có các khái niệm về router ảo, switch ảo, etc. Người dùng có thể khai thác, sử dụng các máy ảo, thiết bị mạng ảo này.</li>
</ul>
<li><h4><a name="nist">1.2. Khái niệm Cloud Computing của NIST</a></h4></li>
Cloud Computing  là mô hình cho phép truy cập qua mạng để lựa chọn và sử dụng tài nguyên  có thể được tính toán (ví dụ: mạng, máy chủ, lưu trữ, ứng dụng và dịch vụ) theo nhu cầu một cách thuận tiện và nhanh chóng; đồng thời cho phép kết thúc sử dụng dịch vụ, giải phóng tài nguyên dễ dàng, giảm thiểu các giao tiếp với nhà cung cấp”
<li><h4><a name="arch">1.3. Giải thích kiến trúc cloud</a></h4></li>
<h4><a name="node">Các phần tử cốt lõi của một node trong cloud</a></h4>
<img src="https://www.ibm.com/developerworks/vn/library/os-cloud-anatomy/figure1.gif"/>
<div>Hình trên là mô hình một node trong hệ thống cloud. Tầng dưới cùng là hạ tầng vật lý. Trên đó là tầng hypervisor - tầng quản lý tài nguyên ảo hóa. Tầng này tạo ra khả năng chạy đồng thời nhiều hệ điều hành (và các ứng dụng của chúng) trên một máy tính vật lý. Trên lớp hypervisor là các máy ảo chạy hệ điều hành và các ứng dụng cung cấp cho người dùng.</div> 
<h4><a name="icloud">Cơ sở hạ tầng cloud</a></h4>
<div>Khi kết hợp các node với cấu trúc như trên trong một mạng vật lý kết hợp với lưu trữ có chia sẻ, phối hợp quản lý trên toàn bộ cơ sở hạ tầng, cung cấp cân bằng tải ban đầu của các kết nối đến, etc. ta có được một cơ sở hạ tầng ảo gọi là "cloud" như mô tả ở hình bên dưới.</div>  
<img src="https://www.ibm.com/developerworks/vn/library/os-cloud-anatomy/figure2.gif" />
<li><h4><a name="543">1.4. 5-4-3 trong Cloud Computing</a></h4></li>
<img src="http://i.imgur.com/aiX8nWD.png?1"/>
<ul>
<li><h4>5 đặc tính của cloud computing</h4>
<ul>
<li>On-demand  self-service: Người dùng có khả năng tự phục vụ, tự dự phòng được  khả năng tính toán, như thời gian phục vụ và mạng lưu trữ, chủ động khởi tạo, tạm dừng dịch vụ mà không phải tương tác, phụ thuộc nhiều vào nhà cung cấp dịch vụ.
</li>
<li>Broad network access: khả năng hỗ trợ nhiều chuẩn mạng, hỗ trợ truy cập dịch vụ từ nhiều nền tảng thiết bị, nhiều hạ tầng vật lý (như: điện thoại di động, máy tính bảng, laptop, máy trạm, etc.)
</li>
<li>Resource pooling: Các tài nguyên tính toán của nhà cung cấp được gộp lại để cấp phát, chia sẻ tự động cho nhiều người dùng dựa theo nhu cầu.</li>
<li>Rapid elasticity: Khả năng thu hồi và cấp phát tài  nguyên nhanh chóng dựa theo nhu cầu người dùng.</li>
<li>Measured service:  Hệ thống cloud tự động hóa việc điều khiển và tối ưu tài nguyên được sử dụng bằng việc tận dụng khả năng đo lường, tính toán mức độ sử dụng dịch vụ, kiểm soát thời gian phục vụ, giám sát, điều khiển, báo cáo, etc. Từ đó có thể tính toán được chi phí của người sử dụng.</li>
</ul>
</li>
<li><h4>4 mô hình triển khai cloud computing</h4>
<ul>
<li>Private cloud: Nền tảng cloud được cung cấp cho nội bộ một tổ chức.</li>
<li>Community cloud: Nền tảng cloud cung cấp cho một nhóm các tổ chức có cùng chung mục đích, nhiệm vụ, chính sách, etc. Nó có thể được quản lý, vận hành bởi một hoặc nhiều tổ chức trong cộng đồng kết hợp quản lý với nhau.</li>
<li>Public cloud: là hệ thống cloud cumg cấp dịch vụ cho khách hàng sử dụng qua internet, có tính chất thương mại. Ví dụ: AWS của Amazon, Azue của Microsoft, Bluemix của IBM, etc.</li>
<li>Hybrid cloud: là nền tảng kết hợp giữa hai hay nhiều kiến trúc cloud (public, private  hoặc community cloud)</li>
</ul>
</li>
<li><h4>3 mô hình dịch vụ</h4>
<ul>
<li>Software  as  a  Service (SaaS): Mô hình cung cấp các dịch vụ về phần mềm, bán hoặc cho thuê. Nhà cung cấp sẽ quản lý toàn bộ về hạ tầng, hệ điều hành, lưu trữ, etc. do đó hạn chế người dùng về việc cấu hình đặc biệt cho các ứng dụng. Người dùng không phải quan tâm ứng dụng triển khai thế nào, chỉ việc thuê và sử dụng dịch vụ thông qua các phần mềm client (trình duyệt, mail client, etc.)</li>
<li>Platform as a Service (PaaS): cung cấp các dịch vụ về nền tảng, môi trường lập trình, database, etc. để khách hàng phát triển các ứng dụng của mình (thông thường nền tảng này cung cấp cho các developer). Ví dụ: AWS, GAE, Azue, Bluemix, OpenShift, etc.</li>
<li>Infrastructure  as  a  Service (IaaS):  Cung cấp các dịch vụ về hạ tầng, các máy chủ, tài nguyên tính toán (RAM, CPU), lưu trữ. Trên đó người dùng sẽ tạo các máy ảo với hệ điều hành, triển khai ứng dụng theo nhu cầu của mình.</li>
</ul>
</li>
</ul>
</ul>
<h3><a name="stack">2. OpenStack</a></h3>
<ul style="list-style: none">
<li><h4><a name="history">2.1. Lịch sử hình thành</a></h4>
<ul>
<li>OpenStack là phần mềm mã nguồn mở sử dụng để triển khai Cloud Computing (public và private cloud)</li>
<li>Ban đầu do NASA và Rackspace khởi xướng, giới thiệu lần đầu năm 2010. Hiện tại đang được phát triển bởi cộng đồng với sự tham gia của nhiều "ông lớn": AT&T, Ubuntu, IBM, RedHat, SUSE, Mirantis, etc.</li>
<img src="http://www.openstack.org/themes/openstack/images/software/openstack-software-diagram.png"/>
</ul>
</li>
<li><h4><a name="feature">2.2. Tóm lược đặc điểm</a></h4>
<ul>
<li>Thiết kế theo hướng module, OpenStack là một project lớn là sự kết hợp của các project thành phần: nova, swift, neutron, glance, etc.</li>
<li>Hoạt động theo hướng mở: công khai lộ trình phát triển, công khai mã nguồn, thiết kế, cộng đồng phát triển là cộng đồng mã nguồn mở, etc. </li>
<li>Chu kì 6 tháng phát hành phiên bản mới theo thứ tự bảng chữ cái: A, B, C...(Austin, Bexar, Cactus, etc.). Hiện tại OpenStack đã phát hành phiên bản thứ 13 - Mitaka.</li>
<li>Phần lớn mã nguồn của OpenStack là python</li>
</ul>
</li>
<li><h4><a name="os-arch">2.3. Kiến trúc</a></h4>
<ul>
<li>Kiến trúc mức khái niệm
<img src="https://camo.githubusercontent.com/bc18e1635965370feadce3e8dd327868a0ad7055/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f69643d30427739366652767139494c506546706655336c61566d5934596b6b"/>
</li>
<li>Kiến trúc mức logic (kiến trúc này tham khảo từ phiên bản Grizzly)
<img src="https://camo.githubusercontent.com/feb96392c1489c6235172383d5a182dc921e5889/68747470733a2f2f64726976652e676f6f676c652e636f6d2f75633f69643d30427739366652767139494c504d44463564556f79615578744e6b6b"/>
</li>
</ul>
</li>
<li><h4><a name="project">2.4. Các project thành phần</a></h4>
<div>Như đã giới thiệu ở trên, có thể coi OpenStack như một hệ điều hành cloud có nhiệm vụ kiểm soát các tài nguyên tính toán(compute), lưu trữ(storage) và networking trong hệ thống lớn datacenter, tất cả đều có thể được kiểm soát qua giao diện dòng lệnh hoặc một dashboard( do project horizon cung cấp). Ở thời điểm hiện tại, OpenStack có 6 core project và 13 project tùy chọn cài đặt theo nhu cầu. 6 core project của OpenStack bao gồm: NOVA, NEUTRON, SWIFT, CINDER, KEYSTONE, GLANCE. Sau đây là thông tin về một số project quan trọng của OpenStack.</div>
<ul>
<li><h4>NOVA - Compute service</h4>
 <ul>
<li>Quản lí các máy ảo trong môi trường OpenStack, chịu trách nhiệm khởi tạo, lập lịch, ngừng hoạt động của các máy ảo theo yêu cầu. </li>
<li>Starting, resizing, stopping và querying máy ảo</li>
<li>Gán và remove public IP</li>
<li>Attach và detach block storage</li>
<li>Show instance consoles (VNC)</li>
<li>Snapshot running instances</li>
<li>Nova hỗ trợ nhiều hypervisor: KVM, VMware, Xen, Docker, etc.</li>
</ul>
</li>
<li><h4>NEUTRON - Networking Service</h4>
<ul>
<li>Các phiên bản trước Grizzly tên là Quantum, sau đổi tên thành Neutron</li>
<li>Cung cấp kết nối mạng như một dịch vụ (Network-Connectivity-as-a-Service) cho các dịch vụ khác của OpenStack, thay thế cho nova-network.</li>
<li>Cung cấp API cho người dùng để họ tạo các network của riêng mình và attach vào server interfaces. </li>
<li>Kiến trúc pluggable hỗ trợ các công nghệ khác nhau của các nhà cung cấp networking phổ biến.</li>
<li> Ngoài ra nó cũng cung cấp thêm các dịch vụ mạng khác như: FWaaS (Firewall as a service), LBaaS (Load balancing as a servie), VPNaaS (VPN as a service),...</li>
</ul>
</li>
<li><h4>SWIFT - Object Storage Service</h4>
Cung cấp giải pháp lưu trữ và thu thập quy mô lớn dữ liệu phi cấu trúc thông qua RESTful API. Không giống như máy chủ tập tin truyền thống, giải pháp lưu trữ với Swift hoàn toàn là phân tán, lưu trữ nhiều bản sao của từng đối tượng để đạt được tính sẵn sàng cao cũng như khả năng mở rộng. Cụ thể hơn, Swift cung cấp các một số chức năng như:
<ul>
<li>Lưu trữ và thu thập các đối tượng (các files)</li>
<li>Thiết lập và chỉnh sửa metadata trên đối tượng(tags)</li>
<li>Đọc, ghi các đối tượng thông qua HTTP</li>
<li>etc.</li>
</ul>
</li>
<li><h4>CINDER - Block Storage Service </h4>
<ul>
<li>Cung cấp các khối lưu trữ bền vững (volume) để chạy các máy ảo (instances). </li>
<li>Kiến trúc pluggable driver cho phép kết nối với công nghệ Storage của các hãng khác.</li>
<li>Có thể attach và detach một volume từ máy ảo này gắn sang máy ảo khác, khởi tạo instance mới</li>
<li>Có thể sao lưu, mở rộng các volume</li>
</ul>
</li>
<li><h4>KEYSTONE - Identity Service</h4>
Cung cấp dịch vụ xác thực và ủy quyền cho các dịch vụ khác của OpenStack, cung cấp danh mục của các endpoints cho tất các dịch vụ trong OpenStack. Cụ thể hơn:
<ul>
<li>Xác thực user và vấn đề token để truy cập vào các dịch vụ</li>
<li>Lưu trữ user và các tenant cho vai trò kiểm soát truy cập(cơ chế role-based access control - RBAC)</li>
<li>Cung cấp catalog của các dịch vụ (và các API enpoints của chúng) trên cloud</li>
<li>Tạo các policy giữa user và dịch vụ </li>
<li>Mỗi chức năng của Keystone có kiến trúc pluggable backend cho phép hỗ trợ kết hợp với LDAP, PAM, SQL</li>
</ul>
</li>
<li><h4>GLANCE - Image Service</h4>
Lưu trữ và truy xuất các disk images của các máy ảo của người dùng và các cloud services khác. OpenStack compute sẽ sử dụng chúng trong suốt quá trình dự phòng instances. Các tính năng chính:
<ul>
<li>Người quản trị tạo sẵn template để user có thể tạo máy ảo nhanh chóng</li>
<li>Người dùng có thể tạo máy ảo từ ổ đĩa ảo có sẵn. Glance chuyển images tới Nova để vận hành instance</li>
<li>Snapshot từ các instance đang chạy có thể được lưu trữ, vì vậy máy ảo đó có thể được back up.</li>
</ul>
</li>
<li><h4>HORIZON - Dashboard Service</h4>
Cung cấp giao diện nền web cho người dùng cuối và người quản trị cloud để tương tác với các dịch vụ khác của OpenStack, ví dụ như vận hành các instance, cấp phát địa chỉ IP và kiểm soát cấu hình truy cập các dịch vụ. HORIZON viết dựa trên python django framework. Một số thông tin mà giao diện người dùng cung cấp cho người sử dụng: 
<ul>
<li>Thông tin về quota và cách sử dụng</li>
<li>Volume Management: điều khiển khởi tạo, hủy kết nối tới các block storage</li>
<li>Images and Snapshots: up load và điều khiển các virtual images, các virtual images được sử dụng để back up hoặc boot một instance mới</li>
<li>Addition:
<ul>
<li>Flavors: định nghĩa các dịch vụ catalog yêu cầu về CPU, RAM và BOOT disk storage</li>
<li>Project: cung cấp các group logic của các user</li>
<li>User: quản trị các user</li>
<li>System Info: Hiển thị các dịch vụ đang chạy trên cloud</li>
</ul>
</li>
</ul>
</li>
<li><h4>CEILOMETER - Telemetry Service</h4>
<ul>
<li>Giám sát và đo đạc các thông số của OpenStack, thống kê tài nguyên của người sử dụng cloud phục vụ mục đích billing, benmarking, thống kê và mở rộng hệ thống</li>
<li>Đáp ứng tính năng "Pay as you go" của Cloud Computing</li>
</ul>
</li>
<li><h4>HEAT - Orchestration Service</h4>
<ul>
<li>Triển khai các ứng dụng dựa trên các template dựng sẵn</li>
<li>Template sẽ mô tả cấu hình các thành phần compute, storagevaf networking để đáp ứng yêu cầu của ứng dụng.</li>
<li>Kết hợp với Ceilometer để có thể tự co dãn tài nguyên.</li>
<li>Tương thích với AWS Cloud Formation APIs</li>
</ul>
</li>
<li><h4>Các project khác:</h4>
<ul>
<li>Trove: Database as a service cung cấp MariaDB trong OpenVZ container theo yêu cầu</li>
<li>Ironic hỗ trợ sử dụng OpenStack để triển khai các bare metal server thay cho các các cloud instance đã ảo hóa.</li>
<li>Designate cung cấp DNS-as-a-service</li>
<li>Zaqar cung cấp dịch vụ multi-tenant message queuing cho các web và mobile dev.</li>
<li>etc.</li>
</ul>
</li>
<li>Một số các dịch vụ cài đặt trong hệ thống OpenStack (không phải project nhưng là thành phần cần thiết của hệ thống): MySQL (MariaDB) lưu trữ dữ liệu về hoạt động của các Project, trạng thái của các instance, hệ thống network, images, etc. ; Rabbit MQ - Message Broker sử dụng để lưu trữ, trao đổi các bản tin giữa các tiến trình trong hệ thống dùng giao thức AMQP (Advanced Message Queuing Protocol); etc.</li>
</ul>
</li>
</ul>





