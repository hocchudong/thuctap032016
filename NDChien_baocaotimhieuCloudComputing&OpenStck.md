#Tìm hiểu Cloud Computing và OpenStack

**Mục lục:**

[1. Cloud Computing](#1)

[1.1 Đặc điểm khái quát](#1.1)

[1.2 Mô tả dịch vụ](#1.2)

[1.3 Mô hình triển khai](#1.3)

[1.4 Ưu, nhược điểm](#1.4)

[2. OpenStack](#2)

[2.1 Khái niệm và đặc điểm](#2.1)

[2.2 Các thành phần của OpenStack](#2.2)

[2.3 Một vài chú ý khi cài đặt OpenStack](#2.3)

[2.4 Các nhà phân phối](#2.4)

[2.5 Một vài chú ý khi cài đặt OpenStack](#2.5)

<a name="1"></a>
##1. Cloud Computing

**Cloud Computing**: Điện toán đám mây, còn gọi là điện toán máy chủ ảo, là mô hình điện toán sử dụng các công nghệ máy tính và phát triển dựa vào mạng Internet.
Thuật ngữ "đám mây" ở đây là lối nói ẩn dụ chỉ mạng Internet, và như một liên tưởng về độ phức tạp của các cơ sở hạ tầng chứa trong nó. 

Mọi khả năng liên quan đến công nghệ thông tin đều được cung cấp dưới dạng các "dịch vụ", cho phép truy cập các dịch vụ công nghệ từ một nhà cung cấp nào đó 
"trong đám mây" mà không cần phải có các kiến thức, kinh nghiệm về công nghệ đó,cũng như không cần quan tâm đến các cơ sở hạ tầng phục vụ công nghệ đó. 

Đại bộ phận hạ tầng cơ sở của điện toán đám mây hiện nay là sự kết hợp của những dịch vụ đáng tin cậy được phân phối thông qua các trung tâm dữ liệu (data center) 
được xây dựng trên những máy chủ với những cấp độ khác nhau của các công nghệ ảo hóa.

Mô hình điện toán đám mây bao gồm năm đặc điểm thiết yếu, ba mô hình dịch vụ, và bốn mô hình triển khai.

<a name="1.1"></a>
**1.1 Đặc điểm khái quát**

- `On-demand self-service`: Khả năng tự phục vụ của người dùng, chủ động khởi tạo, tạm dừng dịch vụ...
- `Broad network access`: Khả năng try cập trên mọi nền tảng thiết bị, mọi loại hạ tầng về mạng, khu vực địa lý.
- `Resource pooling`: Khả năng gộp- gom tài nguyên vật lý, sau đó phân bổ một cách tự động cho người dùng dựa vào nhu cầu.
- `Rapid elasticity`: Khả năng cấp phát và thu hồi tài nguyên một cách nhanh chóng, thuận tiện.
- `Measured elasticity(Pay as you go)`: Khả năng đo lường dịch vụ để kiểm soát thời gian sử dụng, từ đó tính toán chi phí theo mức dộ sử dụng dịch vụ.

<a name="1.2"></a>
**1.2 Mô hình dịch vụ**
* `IaaS (Infrastructure as a services)`: 
- Cung cấp dịch vụ về hạ tầng, các máy chủ, tài nguyên: Ram, CPU. Storage..
- Cung cấp phần xác của Virtual Machine. người dùng chủ động cài đặt ứng dụng.
* `PaaS (Platform as a Services)`
- Cung cấp dịch vụ về nền tảng(Platfform) như: Database. môi trường để phát triển chương trình.
- Máy chủ có sẵn các môi trường để phát triển ứng dụng.
* `SaaS (Software as a Services)`
-  Cung cấp các dịch vụ về phần mềm, bán hoặc cho thuê lâu dài.
- Nhà cung câp dịch vụ triển khai gần như toàn bộ.
-	Các phần mềm về ERP, Email.....

<a name="1.3"></a>
**1.3 Mô hình triển khai**
* **Private Cloud**

 Các cơ sở hạ tầng được cấp phép cho sử dụng độc quyền bởi một tổ chức bao gồm nhiều người. Ít có nhu cầu bảo mật và tính pháp lý so với Public Cloud.
* **Public Cloud**

	Các cơ sở hạ tầng điện toán đám mây được cấp phép cho sử dụng mở. Nó có thể được sở hữu, quản lý và điều hành bởi một doanh nghiệp hoặc các tổ chức chính phủ, 
	hoặc một số sự kết hợp của họ. Nó tồn tại trên cơ sở của các nhà cung cấp điện toán đám mây. Thường là thương mại hóa.
* **Community Cloud**

	Các cơ sở hạ tầng điện toán đám mây được kết hợp bởi nhiều CSP (Cloud service provider). 
	Nó có thể được sở hữu, quản lý, và điều hành bởi một hoặc nhiều tổ chức, một bên thứ ba, hoặc một số sự kết hợp của họ.
* **Hybrid cloud**

	Các cơ sở hạ tầng điện toán đám mây là một thành phần của hai hoặc nhiều hơn những cơ sở hạ tầng điện toán đám mây (tư nhân, cộng đồng, hoặc công cộng)
	mà vẫn thực thể duy nhất, nhưng đang bị ràng buộc với nhau bằng công nghệ tiêu chuẩn hóa hoặc độc quyền cho phép dữ liệu và ứng dụng di động. Nó là sự kết
	hợp của Private Cloud và Public Cloud.

<a name="1.4"></a>
**1.4 Ưu, nhược điểm**
* Ưu điểm:
- Sử dụng các tài nguyên tính toán động (Dynamic computing resources): Các tài nguyên được cấp phát cho doanh nghiệp đúng như những gì doanh nghiệp muốn một cách 
tức thời.
- Giảm chi phí mua bán cài đặt bảo trì tài nguyên.
- Tăng khả năng sử dụng tài nguyên tính toán.
- Giảm độ phức tạp trong cơ cấu của doanh nghiệp.
* Nhược điểm:
- Các thông tin người dùng và dữ liệu được chứa trên điện toán đám mây có đảm bảo được quyền riêng tư, và liệu các thông tin đó có bị sử dụng vì mục đích khác mà chủ nhân nó không hề biết.
- Các dịch vụ của đám mây có thể bị “treo” bất ngờ.
- Một vài dịch vụ lưu trữ dữ liệu trực tuyến trên đám mây bất ngờ ngừng hoạt động hoặc không tiếp tục cung cấp dịch vụ, khiến cho người dùng phải sao lưu dữ liệu của họ.
Một vài trường hợp, vì một lý do nào đó, dữ liệu người dùng bị mất và không thể phục hồi được.
- Tính di động của dữ liệu và quyền sở hữu: Liệu người dùng có thể chia sẻ dữ liệu từ dịch vụ đám mây này sang dịch vụ của đám mây khác? Hoặc trong trường hợp 
không muốn tiếp tục sử dụng dịch vụ cung cấp từ đám mây, liệu có thể sao lưu toàn bộ dữ liệu của họ từ đám mây? Và làm cách nào để người dùng có thể chắc chắn 
rằng các dịch vụ đám mây sẽ không hủy toàn bộ dữ liệu của họ trong trường hợp dịch vụ ngừng hoạt động.
- Việc tập trung dữ liệu trên đám mây nhằm mục đích tăng cường sự bảo mật, tuy nhiên nó cũng là nguyên nhân cho sự tấn công đánh cắp dữ liệu của các tin tặc.

<a name="1.5"></a>
**1.5 Nghĩa vụ của người dùng**
- Chấp nhận các chính sách: Không lưu trữ các  nội dung bất hợp pháp.
- Phần mềm được cấp phép: Các phần mềm bên thứ ba đang chạy trên đám mây phải phù hợp với điều khoản cấp phép của phần mềm.
- Thanh toán kịp thời các chi  phí phát sinh.

<a name="2"></a>
##2. OpenStack

<a name="2.1"></a>
**2.1 Khái niệm và đặc điểm**

**OpenStack** là một nền tảng `mã nguồn mở` hỗ trợ quản trị các tài nguyên trong mô hình `điện toán đám mây`, dùng để xây dựng mô hình Private Cloud và Public Cloud. 
Nó cung cấp cơ sở hạ tầng như một `dịch vụ`. 
OpenStack được sáng lập bởi **NASA** và **Rackspace Hosting**.

Mô hình OpenStack

<img src=http://i.imgur.com/TPJmm2o.png>

Các phiên bản OpenStack:

<img src=http://i.imgur.com/udL4Gi0.png>

Đặc điểm:
- Thiết kế theo hướng Modun.
- Tình mở về: Thiết kế, phát triển, cộng đồng, mã nguồn.
- Có thể tích hợp các kỹ thuật khác với từng project.
- Tất cả các project đều có có APIs mở.
- Chu kỳ 6 tháng một phiên bản mới.
- Hầu hết là mã nguồn Python.

<a name="2.2"></a>
**2.2 Các thành phần của OpenStack**

OpenStack có một kiến trúc Modun với tên mã khác nhau cho các thành phần của nó.

* OpenStack Dashboard- Horizon
	- Cung cấp giao diện cho người dùng, tương tác cơ bản với OpenStack.
	- Tương tác với APIs của các dịch vụ.
	- Không đấy đủ chức năng để điều khiển OpenStack.
* OpenStack Idenity- Keystone
	- Dịch vụ xác thực và ủy quyền trong OpenStack.
	- Quản lý, sửa, xóa tài khoản.....
	- Hỗ trợ và có thể kếp hợp với LDAP, PAM, SQL...
* OpenStack Compute- Nova
	- Lập lịch cho các máy ảo. Tạo, sửa, xóa máy ảo...
	- Quản lý vòng đời máy ảo.
	- Tương đương với EC2 của AWS.
	- Hỗ trợ nhiều Hypervisor: KVM, VMWare, Hyper-V...
	- Hỗ trợ nhiều backend storage: iCSL, SAN.........
* OpenStack Image Service- Glance
	- Lưu trữ, truy vấn các disk image.
	- Hỗ trợ nhiều định dạng của Hypervisor: vmdk,vhd,pcow....
	- Làm việc với các storage backend: Filesystem, Swift, Amazon S3.
* OpenStack Object Storage- Swift
	- Đọc và ghi các đối tượng thông qua http.
	- Tương tự dịch vụ S3 của AWS( Lưu trữ File).
	- Dữ liệu trong Swift có khả nâng tạo các bản sao.
	- Có thể triển khai thành dịch vụ độc lập để lưu trữ.
	- Tính phân tán, khả năng chống chịu lỗi.
* OpenStack Network- Neutron
	- Cung cấp dịch vụ về mạng.
	- Thay thế nova-network để hướng tới SDN trong OpenStack.
	- Có nhiều dịch vụ cao cấp: FWaas, LBaaS, VPNaaS.
	- Có cơ chế Plugin để làm việc với các hãng và giải pháp về network khác.
* OpenStack Block Storage- Cinder
	- Cấp các Block Storage gắn vào máy ảo.
	- Cung cấp các volume(ổ đĩa) gắn vào máy ảo.
	- Có thể khởi tạo các máy từ Volume.
	- Có các Plugin để kết nối với các Storage của hãng khác.
	- Có thể sao lưu, mở rộng các volume.
* OpenStack Block Orchestration- Heat
	- Dùng triển khai các ứng dụng dựa vào template được dựng sẵn.
	- Tự động tính toán và sử dụng các tài nguyên.
	- Là tab "stack" ở trong Horizon.
* OpenStack Block Telemetry- Ceilometer
	- Đáp ứng tính năng "Pay as you go" của Cloud Computing.
	- Dùng để thống kê các tài nguyên mà người dùng sử dụng.
	- Giám sát mức độ sử dụng tài nguyên.
	- Tích hợp trong Horizon với quyền Admin.
* OpenStack Database Service- Trove
	- Dịch vụ về cơ sở dữ liệu, có trên phiên bản OpenStack Icehouse.
	- Cung cấp các Database ko cần thông qua người quản trị.
	- Có khả năng tự động backup và đảm bảo an toàn.
	- Hỗ trợ SQL và NoSQL.
	
<a name="2.3"></a>
**2.3 Mô hình triển khai**

- OpenStack-based Public Cloud: Một nhà cung cấp cung cấp một hệ thống điện toán đám mây công cộng dựa trên dự án OpenStack.	
- On-premises distribution: Trong mô hình này, một khách hàng tải và cài đặt một phân phối OpenStack trong mạng nội bộ của họ. Xem các Distributions.
- Hosted OpenStack Private Cloud: Một nhà cung cấp tổ chức một đám mây riêng OpenStack dựa trên: bao gồm cả phần cứng cơ bản và các phần mềm OpenStack.
- OpenStack-as-a-Service: Một chủ nhà cung cấp phần mềm quản lý OpenStack (không có bất kỳ phần cứng) như một dịch vụ. Khách hàng đăng ký dịch vụ và 
	ghép nối nó với máy chủ nội bộ, lưu trữ và mạng lưới của họ để có được một đám mây tư nhân hoạt động đầy đủ.	
- Appliance based OpenStack: Nebula là một nhà cung cấp chuyên bán các thiết bị có thể được cài đặt vào một mạng lưới triển khai OpenStack.

<a name="2.4"></a>
**2.4 Các nhà phân phối (Distributions)**
- Bright Computing
- Canonical
- HP
- IBM
- Mirantis
- Oracle OpenStack for Oracle Linux, or O3L[97]
- Platform9 Managed OpenStack
- Red Hat
- SUSE

<a name="2.5"></a>
**2.5 Một vài chú ý khi cài đặt OpenStack**

- Xác định các thành phần core trong OpenStack:
		Horizon
		Keystone
		Nova
		Glance
- Xác định network và use case cho network khi sử dụng Network.
- Xác định distro cài đặt OpenStack: Ubuntu, Centos.
- Cài đặt theo docs, theo scrip có sẵn hay công cụ tự động.
- Hiểu về các bước thực hiện và có chuẩn bị kiến thức về Linux.

Một vài hướng dẫn cài đặt:
- http://www.server-world.info/en/note?os=CentOS_6&p=openstack_havana&f=1
- http://discoposse.com/2014/01/26/openstack-havana-all-in-one-lab-on-vmware-workstation/
- http://www.andrewklau.com/getting-started-with-multi-node-openstack-rdo-havana-gluster-backend-neutron/
- https://github.com/vietstacker/openstack-liberty-multinode
- https://github.com/congto/OpenStack-Mitaka-Scripts/blob/master/DOCS-OPS-Mitaka/Caidat-OpenStack-Mitaka.md
