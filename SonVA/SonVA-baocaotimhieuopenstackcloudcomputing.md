# MỤC LỤC
[I. Ảo hóa (Virtualization)](#I)
* [1. Tổng quan ảo hóa](#1)
* [2. Cloud Computing](#2)
* [3. Lộ trình chuyển đổi từ virtualization sang cloud computing](#3)
* [4. Các platform triển khai cloud computing](#4)

[II. OpenStack](#II)
* [1. Giới thiệu](#2.1)
* [2. Đặc điểm](#2.2)
* [3. Sự phát triển và phiên bản](#2.3)
* [4. Kiến trúc](#2.4)
* [5. Chức năng các module chính](#2.5)
* [6. Cài đặt openstack](2.6)


<a name="I"></a>
## I. Ảo hóa (Virtualization)
<a name="1"></a>
### 1. Tổng quan ảo hóa
- Ra đời vào những năm 60 cho mainframe  
- Hardware, server, network, storage....+virtualization  
- Trước và sau ảo hóa:
 - Trước khi ảo hóa: Phần mềm và phần cứng phụ thuộc nhau, không linh hoạt, tốn kém, dễ xảy ra xung đột khi chạy nhiều ứng dụng
 - Sau khi ảo hóa: Phần cứng và phần mềm độc lập nhau, hệ điều hành và ứng dụng được đóng gói lại thành các đơn vị riêng biệt
- Cần phải ảo hóa để:  
 - Giảm chi phí bảo dưỡng
 - Dễ kiểm soát, sao lưu, khôi phục, chuyển đổi khi hoạt động
 - Giảm downtime, khai thác được công suất phần cứng
 - **Bước đệm để thực hiện điện toán đám mây**
- Các công nghệ ảo hóa:
 - Full virtualization (Ảo hóa toàn bộ)
   - Nguồn mở có: KVM, Virtualbox, KQEmu...
   - Thương mại có: VMware, Microsoft(Hyper-V miễn phí)
 - Para-Virtualization: Xen, VMware
 - Ảo hóa mức hệ điều hành (OS-Level Virtualization): OpenVZ, Linux Vserver, Docker
- Hướng tiếp cận: 
 - Hosted architecture: Cài đặt và chạy như ứng dụng, dùng OS máy host để quản lý tài nguyên máy ảo
 - Bare-metal architecture: Ảo hóa từ lõi, cài trực tiếp lên phần cứng  
 
 <a name="2"></a>
 ### 2. Cloud Computing:
 Cloud computing là một kiểu cấu trúc hệ thống nhằm tăng tính thuận tiện, có thể truy cập liên tục nhằm chia sẻ tài nguyên phần cứng có sẵn.(VD mạng, ổ đĩa, các dịch vụ v.v...) Những tài nguyên này có thể được cung cấp hoặc bỏ bớt mà không tốn nhiều công sức. Cloud computing bao gồm 5 đặc tính, 3 mô hình dịch vụ và 4 mô hình triển khai
 - 5 đặc tính:
    - **On-demand, self service:** Người dùng tự phục vụ (Khởi tạo, tạm dừng dịch vụ)
    - **Board network access:** Khả năng truy cập trên mọi nền tảng thiết bị, hạ tầng mạng
    - **Resource Pooling:** Gộp gom tài nguyên vật lý, rồi phân bố cho người sử dụng tùy nhu cầu
    - **Rapid elasticity:** cấp phát, thu hồi tài nguyên nhanh chóng, thuận tiện
    - **Mesure Service (Pay as you go):** Tính toán chi phí dựa trên mức độ sử dụng dịch vụ (Tài nguyên và thời gian mà người dùng đã dùng)
 - 4 mô hình triển khai
    - **Private cloud:** cung cấp cho nội bộ tổ chức, ít nhu cầu bảo mật, pháp lý
    - **Public cloud:** Cung cấp cho khách hàng sử dụng qua internet (Amazon, Google Cloud, Digital Ocean, RackSpaces...)
    - **Hibrid Cloud:** Kết hợp giữa public cloud và private cloud
    - **Community cloud** Kết hợp của nhiều nhà cung cấp dịch vụ cloud (CSP)
 - 3 mô hình Dịch vụ:
    - **IAAS**: Cung cấp dịch vụ hạ tầng, máy chủ tài nguyên, RAM, CPU, Storage. CUng cấp phần xác VM để người dùng tự cài ứng dụng (EC2 amazon)
    - **PAAS**: cung cấp nền tảng (cơ sở dữ liệu,..) môi trường để phát triển ứng dụng, (Google App Engine), Azure...
    - **SAAS**: Cung cấp dịch vụ phần mềm, bán và cho thuê. Email, collaboration, Dropbox...

Ưu điểm: Giá cả và tài nguyên linh động, nhiều lựa chọn hơn, chỉ phải trả cho những gì mình đã sử dụng  
Nhược điểm: Tính bảo mật, độ tin tưởng, khả năng điều khiển...
<a name="3"></a>
### 3. Lộ trình chuyển đổi từ virtualization sang cloud computing
Mức 1: Ảo hóa server  (Hợp nhất, cần chi phí vốn)  
Mức 2: Phân phối ảo hóa
Mức 3: Tạo các Private cloud
Mức 4: Tạo các Hibrid cloud (từng bước cung cấp dịch vụ ra ngoài)
Mức 5: Public cloud
<a name="4"></a>
### 4. Các platform triển khai cloud computing
- Openstack
- Cloud Stack
- Eucalyptus
- **Lựa chọn openstack vì:**
 - Trẻ và còn tiến hóa nhiều hơn nữa
 - Có sự ủng hộ của các ông lớn google, IBM, Cisco, VMware
 - Sử dụng ngôn ngữ duy nhất Python (99.99%)
 - Mọi thứ đều mở, triển khai quy mô lớn, thiết kế dạng module
 - CUng cấp toàn bộ APIs

<center><img src="https://www.openstack.org/themes/openstack/images/openstack-logo-vert.png"></center>

<a name="II"></a>
## II. OpenStack
<a name="2.1"></a>
### 1. Giới thiệu: 
Là nền tảng mã nguồn mở. được sử dụng để xây dựng private cloud và public cloud
<img src="http://i.imgur.com/qxPsXs2.png">

Được sáng lập bởi NASA và RackSpace năm 2010  
Nasa đóng góp dự án Nebula -> NOVA ngày nay
Rackspace đóng góp dự án lưu trữ file -> SWIFT

<a name="2.2"></a>
### 2. Đặc điểm:
- Thiết kế mở theo hướng module
- 6 tháng 1 phiên bản mới 
- 99,99% mã nguồn là Python 2x
- Tên phiên bản đánh theo kí tự (Giống kiểu android :)) )
- Tên-mã dự án: Compute - NOVA, Network - NEUTRON

Cách tổ chức trong openstack Foundation:
- Technical committee: Nhóm phụ trách kĩ thuật
- Board of director: Ban giám đốc
- User committee:  Nhóm người sử dụng

<a name="2.3"></a>
### 3. Sự phát triển và phiên bản
Đến 05/2014 có 139 quốc gia và 16567 người tham gia vào openstack
Các phiên bản
- Autin, 10/2010 ,NOVA & SWIFT
- Bexa, 02/2011, Bổ sung thêm GLANCE
- Cactus, 4/2011, Giữ nguyên 3 project ở bản Bexa Nhưng cải tiến
- Diablo, 09/2011, Giữ nguyên 3 project ở bản Bexa Nhưng cải tiến
- Essex, 04/2012, Bổ sung thêm: KEYSTONE & HORIZON
- Folsom, 09/2012, Bổ sung thêm: CINDER & QUANTUM
- Grizzly, 04/2013, Giữ nguyên 7 dự án, đổi QUANTUM thành NEUTRON
- Havana, 10/2014, Bổ sung thêm: HEAT & CEILOMETER
- Icehouse, 04/2014, Bổ sung thêm: TROVE  
ICE House hiện gồm 10 project NOVA - SWIFT - GLANCE - CINDER - KEYSTONE
HORIZON - NEUTRON - HEAT - CEILOMETER - TROVE

<a name="2.4"></a>
### 4. Kiến trúc
Kiến trúc ý niệm
<center><img src="http://i.imgur.com/K5DBXPv.png"></center>

Kiến trúc mức logic
<center><img src="http://i.imgur.com/yXzA6EZ.png"></center>

Thiết kế :
<center><img src="http://i.imgur.com/QFnKK1C.png"></center>
- Thiết kế theo từng module
- Có thể lựa chọn module để triển khai
- Có thể tích hợp kĩ thuật khác với từng project
- Các dịch vụ mở rộng theo chiều ngang
- Tất cả các project đều có API mở

<a name="2.5"></a>
### 5. Chức năng các module chính
- Horizon
    - CUng cấp giao diện người dùng  tương tác cơ bản với openstack
    - Tương tác các APIs dịch vụ
    - Không đầy đủ chức năng để điều khiển openstack
- Openstack identity - Keystone:
    - Dịch vụ xác thực, ủy quyền
    - Quản lý tài khoản người dùng
    - Hỗ trợ kết hợp với CSDL SQL, LDAP, PAM...
-Nova
    - Lập lịch cho máy ảo (Instance) tạo, sửa, xóa...
    - Quản lý vòng đời, từ lúc spawn đến lúc delete
    - Nova tương đương với  EC2 của amazon
    - Hỗ trợ nhiều Hypervisor: VMWare, KVM, HyperV, Xen, docker...
    - Hỗ trợ nhiều backend storage: iSCSi, SAN...
- Diskimage service GLANCE
    - Lưu trữ, truy vấn các máy mẫu được tạo sẵn.
    - Hỗ trợ nhiều định dạng Hypervisor vmdk, vhd...
    - Làm việc với các storage backend: Filesystem, swift
- SWIFT
    - Đọc ghi đối tượng (file) qua HTTP
    - Tương tự dịch vụ S3(Simple storage Service) của amazon
    - Dữ liệu trong Swift có khả năng tạo các bản sao(Replication)
    - Theo kiểu phân tán. có khả năng chống chịu lỗi, nhất quán
    - CÓ thể triển khai thành dịch vụ độc lập về lưu trữ (swift stack)
- NEUTRON
    - Cung cấp dịch vụ mạng
    - Thay thế Nova network hướng tới SDN trong openstack
    - Có nhiều dịch vụ  FWaaS, VPNaaS...
    - Cơ chế plugin để làm việc với các giải pháp network khác
- CINDER
    - Thay thế Nova Volume, cấp block storage cắm vào máy ảo
    - Cung cấp các ổ đĩa gắn vào máy ảo, có thể khởi tạo các máy từ volume
    - Có plugin để kết nối đến storage của các hãng
    - Có thể sao lưu mở rộng
- Block Orchestration - Heat
    - Triển khai các ứng dụng dựa vào template có sẵn
    - Tự động tính toán sử dụng các tài nguyên
    - là tab stack trong horizon
- Block Telemetry - Ceilometer
    - Tính năng Pay As you go
    - Thống kê tài nguyên người dùng sử dụng, đo lường tính chi phí

- Openstack Database service
    - Là dịch vụ về cơ sở dữ liệu.
    - Cung cấp DB ko cần thông qua người quản trị
    - Có khả năng tự backup, đảm bảo an toàn, hỗ trợ SQL và NoSQL

<a name="2.6"></a>
### 6. Cài đặt OPENSTACK
Xác định thành phần core:  Horizone, keystone, nova, glance
Cài đặt theo doc từ trang chủ openstack
VD Mô hình topo 3 node:

<img src="http://i.imgur.com/SUsH0IM.png">

