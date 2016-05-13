# Mục Lục



<a name="I"></a>
## I. Openstack là gì?
- Openstack được định nghĩa là một nền tảng nguồn mở (Opensource Platform) để điều khiển một lượng lớn các hệ thống tính toán (compute), lưu trữ (storage) và các tài nguyên mạng trong một trung tâm dữ liệu. Tất cả các thao tác quản trị được quản lý qua một bảng điều khiển (dashboard) cho phép người quản trị vừa có thể điều khiển và có thể cung cấp cho người dùng các tài nguyên điện toán thông qua dashboard này.
- Openstack bao gồm nhiều thành phần (các project con) do các công ty, tổ chức, lập trình viên tự nguyện xây dựng đóng góp và phát triển. Có 3 nhóm chính tham gia là nhóm điều hành, nhóm phát triển và nhóm người dùng.  
- Openstack hoạt động theo hướng mở, công khai lộ trình phát triển và mã nguồn
- Openstack được sử dụng để triển khai các hệ thống Public cloud và Private cloud

<a name="II"></a>
## II. Mô hình của openstack:  
<img src="http://i.imgur.com/cq1W70E.png">  
- Phía dưới cùng là phần cứng, đã được ảo hóa để chia sẻ cho ứng dụng và người dùng
- Phía trên cùng là các ứng dụng của bạn, là phần mềm được triển khai trên nền tảng cloud để sử dụng cho nhiều mục đích khác nhau
- Openstack nằm giữa 2 phần trên. trong Openstack có nhiều module khác nhau, như trong hình có Compute, Networking, Storage DashBoard và các APIs


## III. Các service (Project) trong openstack
- Dashboard - Horizon
    - Cung cấp giao diện người dùng  tương tác cơ bản với openstack
    - Tương tác các APIs dịch vụ
    - Không đầy đủ chức năng để điều khiển openstack
- Openstack identity - Keystone:
    - Dịch vụ xác thực, ủy quyền
    - Quản lý tài khoản người dùng
    - Hỗ trợ kết hợp với CSDL SQL, LDAP, PAM...
- Compute - Nova
    - Lập lịch cho máy ảo (Instance) tạo, sửa, xóa...
    - Quản lý vòng đời, từ lúc spawn đến lúc delete
    - Nova tương đương với  EC2 của amazon
    - Hỗ trợ nhiều Hypervisor: VMWare, KVM, HyperV, Xen, docker...
    - Hỗ trợ nhiều backend storage: iSCSi, SAN...
- Disk-images service - GLANCE
    - Lưu trữ, truy vấn các máy mẫu được tạo sẵn.
    - Hỗ trợ nhiều định dạng Hypervisor vmdk, vhd...
    - Làm việc với các storage backend: Filesystem, swift
- Object Storage - SWIFT
    - Đọc ghi đối tượng (file) qua HTTP
    - Tương tự dịch vụ S3(Simple storage Service) của amazon
    - Dữ liệu trong Swift có khả năng tạo các bản sao(Replication)
    - Theo kiểu phân tán. có khả năng chống chịu lỗi, nhất quán
    - CÓ thể triển khai thành dịch vụ độc lập về lưu trữ (swift stack)
- Block Networking - NEUTRON
    - Cung cấp dịch vụ mạng
    - Thay thế Nova network hướng tới SDN trong openstack
    - Có nhiều dịch vụ  FWaaS, VPNaaS...
    - Cơ chế plugin để làm việc với các giải pháp network khác
- Block storage - CINDER
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