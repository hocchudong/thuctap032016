#Cloud Computing và Openstack
##Mục lục:
###[I.Tổng quan về Cloud Computing](#cloud)
####[1.Khái niệm Cloud Computing theo NIST](#khainiem)
####[2.5 đặc tính của cloud computing](#5dactinh)
####[3.4 mô hình triển khai](#mohinh)
####[4.3 mô hình dịch vụ](#dichvu)
####[5.Nền tảng Openstack để triển khai cloud computing](#nentang)
###[II.Openstack](#openstack)
####[1.Khái niệm.](#khainiemopenstack)
####[2.Tóm tắt lược điểm](#tomtat)
####[3.Kiến trúc trong Openstack](#kientruc)
####[4.Chức năng và vai trò của các project](#chucnang)
#####<li>[4.1.Horizon]</li>
#####<li>[4.2.Keystone]</li>
<a name="cloud"></a>
###I.Tổng quan về cloud computing:
<a name="khainiem"></a>
####1.Khái niệm Cloud Computing theo NIST:
Cloud Computing là 1 mô hình cho phép trao đổi 1 cách thuận tiện về nhu cầu truy cập mạng vào 1 nơi để chia sẻ tài nguyên máy tính (mạng, máy chủ, lưu trữ, các ứng dụng dịch vụ...) . Mô hình điện toán đám mây này bao gồm năm đặc điểm thiết yếu, ba mô hình dịch vụ, và bốn mô hình triển khai.
<a name="5dactinh"></a>
####2.5 đặc tính của cloud computing:
<ul>
<li>On-demand self-service: Khả năng tự phục vụ người dùng.</li>
<li>Broad network access: Khả năng truy cập trên mọi nền tảng</li>
<li>Resource pooling: Gom gộp tài nguyên vật lý và phân bổ 1 cách tự động cho người dùng</li>
<li>Rapid elasticity: Khả năng co giãn, đàn hồi tài nguyên 1 cách nhanh chóng. Có thể cấp phát và thu hồi 1 cách nhanh chóng.</li>
<li>Measured service: Khả năng đo lường dịch vụ để kiểm soát thời gian sử dụng, từ đó tính toán chi phí theo mức độ sử dụng dịch vụ.</li>
</ul>
<a name="mohinh"></a>
####3.4 mô hình triển khai:
<ul>
<li>Private cloud: Được cung cấp cho nội bộ tổ chức, ít nhu cầu bảo mật và tính pháp lý so với public cloud</li>
<li>Public cloud: Là dịch vụ cung cấp cho khách hàng sử dụng thông qua internet</li>
<li>Hybrid cloud: Là sự kết hợp giữa private cloud và public cloud</li>
<li>Community cloud: Sự kết hợp giữa nhiều cloud service provider</li>
</ul>
<a name="dichvu"></a>
####4.3 mô hình dịch vụ:
<ul>
<li>Infracstructure as a service</li>
<li>Platform as a service</li>
<li>Soft as a service</li>
</ul>
<a name="nentang"></a>
####5.Nền tảng openstack để triển khai cloud computing:
#####Lựa chọn openstack bởi vì:
<ul>
<li>Openstack là 1 công nghệ mới và còn phát triển hơn nữa trong tương lai</li>
<li>Được các công ty lớn ủng hộ như: IBM, Cisco, Google..</li>
<li>Sử dụng 1 ngôn ngữ duy nhất (99% python)</li>
<li>Triển khai quy mô lớn</li>
<li>Mọi thứ đều mở</li>
</ul>
<a name="openstack"></a>
###II.Openstack:
<a name="khainiemopenstack"></a>
####1.Khái niệm Openstack:
Là nền tảng mã nguồn mở, được sử dụng để xây dựng mô hình private cloud và public cloud.
<a name="tomtat"></a>
####2.Tóm tắt lược điểm:
#####Các đặc điểm:
<ul>
<li>Thiết kế theo hướng mô-đun.</li>
<li>Mở về thiết kế,phát triển, cộng đồng, mã nguồn.</li>
<li>Cứ 6 tháng sẽ có 1 phiên bản mới.</li>
<li>Sử dụng ngôn ngữ python.</li>
</ul>
<a name="kientruc"></a>
####3.Kiến trúc trong Openstack:
<ul>
<li>Kiến trúc theo ý niệm:
<img src="http://docs.openstack.org/juno/install-guide/install/apt/content/figures/1/a/common/figures/openstack_havana_conceptual_arch.png">
<li>Kiến trúc theo logic</li>
<img src="http://docs.openstack.org/icehouse/training-guides/content/figures/5/a/figures/openstack-arch-havana-logical-v1.jpg">
</ul>
#####Tóm lược thiết kế:
<ul>
<li>Openstack được thiết kế theo từng mô-đun</li>
<li>Có thể chọn lựa mô-đun để triển khai</li>
<li>Có thể tích hợp kĩ thuật với từng project</li>
<li>Các dịch vụ mở theo chiều ngang</li>
<li>Tất cả các project đều có APIs mở</li>
</ul>
<a name="chucnang"></a>
####4.Chức năng và vai trò của project:
#####4.1.Horizon
<ul>
<li>Cung cấp giao diện tương tác với người dùng.</li>
<li>Tương tác với APIs của các dịch vụ.</li>
<li>Không đầy đủ chức năng để điều khiển Openstack</li>
</ul>
#####4.2.Keystone:
<ul>
<li>Dịch vụ xác thực và ủy quyền trong Openstack</li>
<li>Tạo, sửa, xóa tài khoản và nhóm người dùng</li>
<li>Hỗ trợ và có thể kết hợp với LDAP, PAM, SQL..</li>
</ul>






















 

