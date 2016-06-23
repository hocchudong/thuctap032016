# Tìm hiểu OpenStack Nova
# Mục lục
<h3><a href="#sysarch">1. Giới thiệu Nova</a></h3>
<h3><a href="#services">2. Compute Services</a></h3>
<ul>
<li><a href="#srvarch">2.1. Kiến trúc Compute service</a></li>
<li><a href="#components">2.2. Các thành phần của Compute Service</a></li>
</ul>
<h3><a href="#nova">3. Nova, Libvirt và KVM</a></h3>
<ul>
<li><a href="#fundamental">3.1. Các khái niệm căn bản</a></li>
<li><a href="#integrated">3.2. Tích hợp Nova với Libvirt, KVM quản lý máy ảo</a>
<ul>
<li><a href="#workflow">3.2.1. Workflow của Nova Compute</a></li>
<li><a href="#spawn">3.2.2. Spawn</a></li>
<li><a href="#reboot">3.2.3. Reboot</a></li>
<li><a href="#suspend">3.2.4. Suspend</a></li>
<li><a href="#migration">3.2.5. Live Migration</a></li>
<li><a href="#resize">3.2.6. Resize/Migrate</a></li>
<li><a href="#snapshots">3.2.7. Snapshots</a></li>
</ul>
</li>
</ul>
<h3><a href="#ref">4. Tham khảo</a></h3>
---

<h2><a name="sysarch">1. Giới thiệu Nova</a></h2>
<div>
<ul>
<li>Nova bao gồm nhiều tiến trình trên server, mỗi tiến trình lại thực hiện một chức năng khác nhau.</li>
<li>Nova cung cấp REST API để tương tác với ứng dụng client phía người dùng, trong khi các thành phần bên trong Nova tương tác với nhau thông qua RPC.</li>
<li>Các API servers thực hiện các REST request, điển hình nhất là thao tác đọc, ghi vào cơ sở dữ liệu, với tùy chọn là gửi các bản tin RPC tới các dịch vụ khác của Nova. Các bản tin RPC dược thực hiện nhờ thư viện  <b>oslo.messaging</b> - lớp trừu tượng ở phía trên của các message queue. Hầu hết các thành phần của nova có thể chạy trên nhiều server và có một trình quản lý lắng nghe các bản tin RPC. Ngoại trừ <b>nova-compute</b>, vì dịch vụ <b>nova-compute</b> được cài đặt trên các máy compute - các máy cài đặt hypervisor mà <b>nova-compute</b> quản lý.</li>
<li>Nova cũng sử dụng một cơ sở dữ liệu trung tâm chia sẻ chung giữa các thành phần. Tuy nhiên, vì mục tiêu nâng cấp, các cơ sở dữ liệu được truy cập thông qua một lớp đối tượng dể đảm bảo các thành phần kiểm soát đã nâng cấp vẫn có thể giao tiếp với nova-compute ở phiên bản trước đó. Để thực hiện điều này, nova-compute ủy nhiệm các yêu cầu tới cơ sở dữ liệu thông qua RPC tới một trình quản lý trung tâm, chính là dịch vụ <b>nova-conductor</b>.</li>
</ul>
</div>


<h2><a name="services">2. Compute Services</a></h2>
<div>
<ul>
<li><h3><a name="srvarch">2.1. Kiến trúc Compute service</a></h3>
<br>
<img src="http://i.imgur.com/tMJ2NWN.png">
<br><br>
Các dịch vụ của nova được phân loại bao gồm:
<ul>
<li><b>API server</b>
<div>
API server là trái tim của cloud framework, nơi thực hiện các lệnh và việc kiểm soát hypervisor, storage, networking có thể lập trình được.
<br>
Các API endpoints về cơ bản là các HTTP web services thực hiện xác thực, ủy quyền và các lệnh căn bản, kiểm các các chức năng sử dụng giao diện API của Amazon, Rackspace, và các mô hình liên quan khác. Điều này cho phép các API tương thích với nhiều công cụ sẵn có, tương tác với các nhà cung cấp dịch vụ cloud khác. Điều này tạo ra để ngăn chặn vấn đề phụ thuộc vào nhà cung cấp dịch vụ.
</div>
</li>

<li><b>Message queue</b>
<div>
Message Broker cung cấp hàng đợi lưu bản tin tương tác giữa các dịch vụ, các thành phần như compute nodes, networking controllers(phần mềm kiểm soát hạ tầng mạng), API endpoints, scheduler(xác định máy vật lý nào được sử dụng để cấp phát tài nguyên ảo hóa), và các thành phần tương tự. 
</div>
</li>
<li><b>Compute worker</b>
<div>
Compute worker quản lý các tài nguyên tính toán của các máy ảo trên các Compute host. API  sẽ chuyển tiếp các lệnh tới compute worker để hoàn thành các nhiệm vụ sau:
<ul>
<li>Chạy các máy ảo</li>
<li>Xóa các máy ảo</li>
<li>Khởi động lại máy ảo</li>
<li>Attach các volume</li>
<li>Detach các volume</li>
<li>Lấy console output</li>
</ul>
</div>
</li>
<li><b>Network Controller</b>
<div>
Network Controller quản lý tài nguyên về network trên các máy chủ. API server sẽ chuyển tiếp các lệnh thông qua message queue, sau đó sẽ được xử lý bởi Network Controller. Các thao tác vận hành đặc biệt bao gồm:
<ul>
<li>Cấp phát các địa chỉ IP tĩnh</li>
<li>Cấu hình VLANs cho các project</li>
<li>Cấu hình mạng cho các compute nodes</li>
</ul>
</div>
</li>
</ul>
</li>

<li><h3><a name="components">2.2. Các thành phần của Compute Service</a></h3>
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
<li><b>nova-consoleauth </b>Ủy quyền tokens cho người dùng mà console proxies cung cấp. Dịch vụ này phải chạy với console proxies để làm việc.</li>
<li><b>nova-novncproxy </b>Cung cấp một proxy để truy cập máy ảo đang chạy thông qua kết nối VNC. Hỗ trợ các novnc client chạy trên trình duyệt.</li>
<li><b>nova-spicehtml5proxy </b>Cung cấp một proxy truy cấp máy ảo đang chạy thông qua kết nối SPICE. Hỗ trợ các client chạy trên trình duyệt hỗ trợ HTML5.</li>
<li><b>nova-xvpvncproxy </b>Cung cấp một proxy truy cập máy ảo đang chạy thông qua kết nối VNC.</li>
<li><b>nova client </b>Cho phép người dùng thực hiện tác vụ quản trị hoặc các tác vụ thông thường của người dùng cuối.</li>
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

<h2><a name="nova">3. Nova, Libvirt và KVM</a></h2>
<ul>
<li><h3><a name="fundamental">3.1. Các khái niệm căn bản</a></h3>
<div>
<ul>
<li><h3>KVM - QEMU</h3>
<div>
<ul>
<li>KVM - module của hạt nhân linux đóng vai trò tăng tốc phần cứng khi sử dụng kết hợp với hypervisor QEMU, cung cấp giải pháp ảo hóa full virtualization.</li>
<li>Sử dụng libvirt làm giao diện trung gian tương tác giữa QEMU và KVM</li>
</ul>
</div>
</li>
<li><h3>Libvirt</h3>
<ul>
<li>Thực thi tất cả các thao tác quản trị và tương tác với QEMU bằng việc cung cấp các API.</li>
<li>Các máy ảo được định nghĩa trong Libvirt thông qua một file XML, tham chiếu tới khái niệm "domain".</li>
<li>Libvirt chuyển XML thành các tùy chọn của các dòng lệnh nhằm mục đích gọi QEMU</li>
<li>Tương thích khi sử dụng với <b>virsh</b> (một công cụ quản quản lý tài nguyên ảo hóa giao diện dòng lệnh)</li>
</ul>
</li>
</ul>
</div>
</li>

<li><h3><a name="integrated">3.2. Tích hợp Nova với Libvirt, KVM quản lý máy ảo</a></h3>
<ul>
<li>
<h3><a name="workflow">3.2.1. Workflow của Nova Compute</a></h3>
<div>
<b>Compute Manager</b>
<ul>
<li>Cấu hình trong hai file: <b>nova/compute/api.py</b> và <b>nova/compute/manager.py</b></li>
<li>Các compute API tiếp nhận yêu cầu từ người dùng từ đó gọi tới compute manager. Compute manager lại gọi tới Nova libvirt driver. Driver này sẽ gọi tới API của libvirt thực hiện các thao tác quản trị.</li>
</ul>

<b>Nova Libvirt Driver</b>
<div>
Được cấu hình trong các file <b>nova/virt/libvirt/driver.py</b> và <b>nova/virt/libvirt/*.py</b> có vai trò tương tác với libvirt.
</div>

</div>
</li>

<li>
<h3><a name="spawn">3.2.2. Spawn</a></h3>
<div>
Đây là thao tác boot máy ảo, nova tiếp nhận lời gọi API từ người dùng mang đi xử lý qua các module như scheduler, compute manager và libvirt driver. Libvirt sẽ thực hiện tất cả các thao tác cần thiết để tạo máy ảo như cấp phát tài nguyên mạng, tài nguyên tính toán(ram, cpu), volume, etc.
<br>
Tiếp đó, tiến trình <b>spawn</b> này cũng tạo ra file đĩa bằng các thao tác sau:
<ul>
<li>Tải image từ glance đưa vào thư mục tương ứng chứa ảnh đĩa gốc bên máy compute được lựa chọn (nstance_dir/_base) và chuyển nó sang định dạng <b>RAW</b>.</li>
<li>Tạo file đĩa định dạng QCOW2 từ đĩa gốc ở trên. (instance_dir/uuid/disk)</li>
<li>Tạo 2 file đĩa định dạng QCOW2 là "disk.local" và "disk.swap". (instance_dir/uuid/disk.local và instance_dir/uuid/disk.swap, không nên sử dụng swap trong máy ảo)</li>
<li>Tạo ra file libvirt XML và tạo bản copy vào thư mục instance_dir (nstance_dir/libvirt.xml)</li>
<li>Thiết lập kết nối với volume(nếu boot từ volume). Thao tác vận hành này được thực thi như thế nào là phụ thuộc vào volume driver. 
<ul>
<li>iSCSI: kết nối thiets lập thông qua tgt hoặc iscsiadm.</li>
<li>RBD: tạo ra XML cho Libvirt, thực thi bên trong QEMU.</li>
</ul>
</li>
<li>Xây dựng hệ thống network hỗ trợ cho máy ảo:
<ul>
<li>Phụ thuộc vào driver sử dụng (nova-network hay neutron)</li>
<li>Thiết lập các bridges và VLANs cần thiết</li>
<li>Tạo Security groups (iptables) cho máy ảo</li>
</ul>
</li>
<li>Định nghĩa domain với libvirt, sử dụng file XML đã tạo. Thao tác này tương đương thao tác 'virsh define instance_dir/<uuid>/libvirt.xml' khi sử dụng virsh.</li>
<li>Bật máy ảo. Thao tác này tương đương thao tác 'virsh start <uuid>’ or ‘virsh start <domain name>' khi sử dụng virsh.</li>
</ul>
</div>
</li>

<li>
<h3><a name="reboot">3.2.3. Reboot</a></h3>
<div>
<ul>
<li>Có 2 loại reboot có thể thực hiện thông qua API: hard reboot và soft reboot. Soft reboot thực hiện hoàn toàn dựa vào guest OS và ACPI thông qua QEMU. Hard reboot thực hiện ở mức hypervisor và Nova cũng như các cấp độ phù hợp khác.</li>
<li>Hard reboot workflow:
<ul>
<li>Hủy domain. Tương đương với lệnh "virsh destroy", không hủy bỏ dữ liệu, mà kill tiến trình QEMU.</li>
<li>Tái thiết lập tất cả cũng như bất kỳ kết nối nào tới volume.</li>
<li>Tái tạo Libvirt XML</li>
<li>Kiểm tra và tải lại bất kỳ file nào bị lỗi ((instance_dir/_base)</li>
<li>"Cắm" lại các card mạng ảo (tái tạo lại các bridges, VLAN interfaces)</li>
<li>Tái tạo và áp dụng lại các iptables rules</li>
</ul>
</li>
</ul>
</div>
</li>

<li>
<h3><a name="suspend">3.2.4. Suspend</a></h3>
<div>
<ul>
<li>Tương ứng command: 'nova suspend'. Tương tự như thao tác 'virsh managed-save' khi sử dụng virsh</li>
<li>Thực sự tên hành động 'suspend' dễ gây hiểu lầm, vì bản chất lệnh này giống như thực hiện thao tác <b>hibernate</b> hệ thống vậy.</li>
<li>Khôi phục lại trạng thái của máy ảo đơn giản và tương tự như lệnh 'virsh start'.</li>
<li>Một số vấn đề đặt ra với trạng thái này:
<ul>
<li>Lưu lại trạng thái bộ nhớ tiêu thụ không gian đĩa bằng với bộ nhớ của máy ảo.</li>
<li>Không gian đĩa không bị giới hạn ở bất kỳ đâu</li>
<li>Cả hai giải pháp migration và live migration đều có những vấn đề đối với trạng thái này.</li>
<li>Cài đặt QEMU phiên bản khác nhau có thể có sự thay đổi giữa suspend và resume.</li>
</ul>
</li>

</ul>
</div>
</li>

<li>
<h3><a name="migration">3.2.5. Live Migration</a></h3>
<div>
<ul>
<li>Có hai loại live migration: normal migration và "block" migrations.</li>
<li>Normal live migration yêu cầu cả tài nguyên và hypervisor đều phải truy cập tới dữ liệu của máy ảo(trên hệ thống lưu trữ có chia sernhw NAS, SAN)</li>
<li>Block live migration không có yêu cầu đặc biệt gì đối với hệ thống lưu trữ. Các đĩa của máy ảo được migrated từng phần một trong tiến trình migration.</li>
<li>Live migration là một trong những thao tác vận hành mang tính nhạy cảm nhất liên quan đến phiên bản của QEMU đang chạy trên máy chủ nguồn và đích.</li>
<li>
Live Migration Workflow:
<ul>
<li>Xác nhận hệ thống lưu trữ backend có phù hợp với kiểu migration không:
<ul>
<li>Thực hiện kiểm tra hệ thống shared storage nếu thực hiện <b>normal live migration</b>
</li>
<li>Thực hiện kiểm tra các yêu cầu cho <b>block migrations</b></li>
<li>Việc kiểm tra được thực hiện trên cả nguồn và đích, điều phối thông qua các lời gọi RPC từ <b>scheduler</b></li>
</ul>
</li>
<li>Trên máy chủ đích:
<ul>
<li>Tạo các kết nối volume cần thiết</li>
<li>Nếu thực hiện <b>block migration</b>, tạo thư mục máy ảo, lưu lại các file bị mất. từ Glance và tạo đĩa máy ảo trống.</li>
</ul>
</li>
<li>Trên máy chủ nguồn, khởi tạo tiến trình migration.</li>
<li>Khi đã hoàn tất tiến trình live migration, tạo ra Libvirt XML và định nghĩa nó trên máy chủ đích.</li>
</ul>
</li>

</ul>
</div>
</li>

<li>
<h3><a name="resize"></a>3.2.6. Resize/Migrate</h3>
<div>
<ul>
<li>Resize/Migrate được nhóm lại với nhau bởi lẽ chúng sử dụng chung code.</li>
<li>Migrate khác với live migrate ở chỗ nó thực hiện migration khi tắt máy ảo (libvirt domain không chạy).</li>
<li>Yêu cầu SSH key pairs được triển khai cho các user đang chạy nova-compute với mọi hypervisors.</li>
<li>Resize không cho phép chia ổ đĩa, bởi vì điều đó không hề an toàn.</li>
<li>Resize/Migrate workflow:
<ul>
<li>Tắt máy ảo và ngắt các kết nối volume.
</li>
<li>Di chuyển thưc mục hiện tại của máy ảo ra ngoài. Tiến trình resize máy ảo sẽ tạo ra thư mục tạm.</li>
<li>Nếu sử dụng định dạng file QCOW2, convert image sang dạng raw.</li>
<li>Với hệ thống shared storage, chuyển thư mục <b>instance_dir</b> mới vào. Nếu không, copy toàn bộ dữ liệu thông qua SCP.</li>
</ul>
</li>

</ul>
</div>
</li>

<li>
<h3><a name="snapshots">3.2.7. Snapshots</a></h3>
<div>
<ul>
<li>2 kiểu snapshot hoàn toàn khác nhau: "live" snapshot và "cold" snapshot.</li>
<li>Hệ thống file hoặc dữ liệu bền vững có thể không được đảm bảo với mỗi kiểu snapshot khác nhau.</li>
<li>Live snapshot không có yêu cầu đặc biệt gì về cấu hình, Nova sẽ thực hiện tự động. Live snapshot workflow như sau:
<ul>
<li>Thực hiện kiểm tra xác định liệu hypervisor có đảm bảo yêu cầu cho live snapshot không.</li>
<li>Máy ảo cần ở trạng thái "running", trái lại ta thực hiện clod snapshots.</li>
<li>Tạo image QCOW2 rỗng trong thư mục tạm</li>
<li>Sử dụng libvirt thiết lập bản sao chép từ đĩa của máy ảo hiện tại sang đĩa rỗng đã tạo ở trên.</li>
<li>Thăm dò trạng thái của block cho tới khi không còn bytes dữ liệu nào để snapshots, khi đó ta có một bản sao của máy ảo đang chạy.</li>
<li>Sử dụng qemu-img, convert bản copy sang định raw image.</li>
<li>Tải image lên Glance</li>
</ul>
</li>
<li>Cold snapshot yêu cầu phải tắt máy ảo với workflow như sau:
<ul>
<li>Tắt hoàn toàn máy ảo</li>
<li>Khi đã tắt máy ảo, sử dụng qemu-img để convert, tạo ra bản copy của đĩa với cùng định dạng với image gốc tạo máy ảo từ Glance.</li>
<li>Trả lại trạng thái nguyên thủy của máy ảo.</li>
<li>Tải bản sao chép của image đã convert lên Glance</li>
</ul>
</li>

</ul>
</div>
</li>

</ul>
</li>
</ul>

<h2><a name="ref">4. Tham khảo</a></h2>
<div>
[1] - <a href="https://www.openstack.org/summit/openstack-summit-atlanta-2014/session-videos/presentation/under-the-hood-with-nova-libvirt-and-kvm">https://www.openstack.org/summit/openstack-summit-atlanta-2014/session-videos/presentation/under-the-hood-with-nova-libvirt-and-kvm</a>
<br>
[2] - <a href="https://www.openstack.org/assets/presentation-media/OSSummitAtlanta2014-NovaLibvirtKVM2.pdf">https://www.openstack.org/assets/presentation-media/OSSummitAtlanta2014-NovaLibvirtKVM2.pdf</a>
<br>
[3] - <a href="http://docs.openstack.org/developer/nova/architecture.html">http://docs.openstack.org/developer/nova/architecture.html</a>
</div>

