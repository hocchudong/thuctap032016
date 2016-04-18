#Tìm hiểu Cloud computing và Openstack

#Mục lục
* [1. Virtualization (ảo hóa)](#ao_hoa)
	* [1.1. Khái niệm Ảo hóa](#khai_niem_ao_hoa)
	* [1.2 thành phần của một hệ thống ảo hóa](#thanh_phan_ao_hoa)
	* [1.3. Các kiến trúc ảo hóa](#kien_truc_ao_hoa)
		* [1.3.1. Kiến trúc ảo hóa Hosted-based](#hosted_based)
		* [1.3.2. Kiến trúc ảo hóa Hypervisor-based](#hypervisor_based)
			* [1.3.2.1. Monolithic Hypervisor](#monolithic_hypervisor)
			* [1.3.2.2. Microkernelized Hypervisor](#microkernelized_hypervisor)
		* [1.3.3. Kiến trúc ảo hóa Hybrid](#hybrid)
	* [1.4. Các công nghệ ảo hóa.](#cong_nghe_ao_hoa)
		* [1.4.1. Ảo hóa toàn phần - Full Virtualization.](#ao_hoa_toan_phan)
		* [1.4.2. Paravirtualization - Ảo hóa song song](#ao_hoa_song_song)
		* [1.4.3.Ảo hóa hệ điều hành.](#ao_hoa_he_dieu_hanh)
		* [1.4.4. Ảo hóa ứng dụng.](#ao_hoa_ung_dung)
* [2. Cloud Computing (điện toán đám mây)](#dien_toan_dam_may)
	* [2.1. 5 đặc điểm](#dac_diem)
	* [2.2: 4 mô hình dịch vụ (mô hình sản phẩm)](#mo_hinh_dich_vu)
	* [2.3: 3 mô hình triển khai](#mo_hinh_trien_khai)
* [3. OpenStack](#openstack)
	* [3.1. Một vài thông tin vắn tắt về OpenStack](#thong_tin_openstack)

<a name="ao_hoa"></a>
#1. Virtualization (ảo hóa)

<a name="khai_niem_ao_hoa"></a>
##1.1. Khái niệm Ảo hóa
Ảo hóa máy chủ là một công nghệ được ra đời nhằm khai thác triệt để khả năng làm việc của các phần cứng trong một hệ thống máy chủ. 
Ý tưởng của công nghệ ảo hóa máy chủ là từ một máy vật lý đơn lẻ có thể tạo thành nhiều máy ảo độc lập.

* Ảo hóa cho phép tạo nhiều máy ảo trên một máy chủ vật lý, mỗi một máy ảo cũng được cấp phát tài nguyên phần cứng như máy thật gồm có Ram, CPU, Card mạng, ổ cứng, các tài nguyên khác và hệ điều hành riêng.

* Các bộ xử lý có ứng dụng ảo hóa thường là Intel VT(Virtual Technology) hoặc AMD Pacifica.

* **Ảo hóa cứng** còn được gọi là phân thân máy chủ. Dạng ảo hóa này cho phép tạo nhiều máy ảo trên môt máy chủ vật lý. Mỗi máy ảo chạy hệ điều hành riêng và được cấp phát các tài nguyên phần cứng như số xung nhịp CPU, ổ cứng và bộ nhớ.

* **Ảo hóa mềm** còn gọi là phân thân hệ điều hành. Nó thực ra chỉ là sao chép bản sao của một hệ điều hành chính làm nhiều hệ điều hành con và cho phép các máy ảo ứng dụng có thể chạy trên nó.

<a name="thanh_phan_ao_hoa"></a>
##1.2. Các thành phần của một hệ thống ảo hóa.

![](http://voer.edu.vn/media/transforms/20140306-214626-tong-quan-ve-ao-hoa-may-chu/Picture%203.png)

* Tài nguyên vật lý (host machine, host hardware): cung cấp tài nguyên mà các máy ảo sẽ sử dụng tới: ổ đĩa cứng, ram, card mạng,...
* Các phần mềm ảo hóa (virtual software) cung cấp và quản lý môi trường làm việc của các máy ảo.
* Máy ảo (virtual machine): Các máy được cài trên phần mềm ảo hóa.
* Hệ điều hành: Là hệ điều hành được cài trên máy ảo.

<a name="kien_truc_ao_hoa"></a>
##1.3. Các kiến trúc ảo hóa.

<a name="hosted_based"></a>
###1.3.1. Kiến trúc ảo hóa Hosted-based (hosted hypervisor).
* Kiến trúc này sử dụng một lớp hypervisor chạy trên nền tảng hệ điều hành, sử dụng các dịch vụ được hệ điều hành cung cấp để phân chia tài nguyên tới các máy ảo.
* Một số hệ thống hypervisor dạng Hosted-base có thể kể đến như Vmware Server,Microsoft Virtual PC, máy ảo Java ..

![](http://voer.edu.vn/media/transforms/20140306-214626-tong-quan-ve-ao-hoa-may-chu/Picture%201.png)

<a name="hypervisor_based"></a>
###1.3.2. Kiến trúc ảo hóa Hypervisor-based (bare-metal hypervisor)

* Trong mô hình này, lớp phần mềm hypervisor chạy trực tiếp trên nền tảng phần cứng của máy chủ, không thông qua bất kì một hệ điều hành hay một nền tảng nào khác.
* Qua đó, các hypervisor này có khả năng điều khiển, kiểm soát phần cứng của máy chủ. Đồng thời, nó cũng có khả năng quản lý các hệ điều hành chạy trên nó. Nói cách khác, các hệ điều hành sẽ chạy trên một lớp nằm phía trên các hypervisor dạng bare-metal.

![](http://voer.edu.vn/media/transforms/20140306-214626-tong-quan-ve-ao-hoa-may-chu/Picture%205.png)

* Một số ví dụ về các hệ thống Bare-metal hypervisor như là: Oracle VM, Vmware ESX Server, IBM's POWER Hypervisor (PowerVM), Microsoft's Hyper-V (xuất xưởng tháng 6 năm 2008), Citrix XenServer…
* Mô hình Hypervisor - Base có 2 dạng là Monothic Hypervisor và Microkernel Hypervisor.

<a name="monolithic_hypervisor"></a>
####1.3.2.1. Monolithic Hypervisor.

* Monolithic Hypervisor là một hệ điều hành máy chủ. Nó chứa những trình điều khiển (Driver) hoạt động phần cứng trong lớp Hypervisor để truy cập tài nguyên phần cứng bên dưới.
* Khi các hệ điều hành chạy trên các máy ảo truy cập phần cứng thì sẽ thông qua lớp trình điều khiển thiết bị của lớp hypervisor.

![](http://voer.edu.vn/media/transforms/20140306-214626-tong-quan-ve-ao-hoa-may-chu/Picture%206.png)

<a name="microkernelized_hypervisor"></a>
####1.3.2.2. Microkernelized Hypervisor.

* trình điều khiển thiết bị phần cứng bên dưới được cài trên một máy ảo và được gọi là trình điều khiển chính, trình điều khiển chính này tạo và quản lý các trình điều khiển con cho các máy ảo.

![](http://voer.edu.vn/media/transforms/20140306-214626-tong-quan-ve-ao-hoa-may-chu/Picture%207.png)

<a name="hybrid"></a>
###1.3.3. Kiến trúc ảo hóa Hybrid.
* Hybrid là một kiểu ảo hóa mới hơn và có nhiều ưu điểm.
* Trong đó lớp ảo hóa hypervisor chạy song song với hệ điều hành máy chủ
* Tuy nhiên trong cấu trúc ảo hóa này, các máy chủ ảo vẫn phải đi qua hệ điều hành máy chủ để truy cập phần cứng nhưng khác biệt ở chỗ cả hệ điều hành máy chủ và các máy chủ ảo đều chạy trong chế độ hạt nhân. 

![](http://voer.edu.vn/media/transforms/20140306-214626-tong-quan-ve-ao-hoa-may-chu/Picture%208.png)

<a name="cong_nghe_ao_hoa"></a>
##1.4. Các công nghệ ảo hóa. 

<a name="ao_hoa_toan_phan"></a>
###1.4.1. Ảo hóa toàn phần - Full Virtualization.
* Đây là loại ảo hóa mà ta không cần chỉnh sửa hệ điều hành khách (guest OS) cũng như các phần mềm đã được cài đặt trên nó để chạy trong môi trường hệ điều hành chủ (host OS).
* Các phần mềm hỗ trợ: KVM, VirtualBox, KQEMU, Vmware, Microsoft,...

<a name="ao_hoa_song_song"></a>
###1.4.2. Paravirtualization - Ảo hóa song song
* Thay vì mô phỏng một môi trường phần cứng hoàn chỉnh, phần mềm ảo hóa này là một lớp mỏng, dồn các truy cập các hệ điều hành máy chủ vào tài nguyên máy vật lý cơ sở.
* Sử dụng môt kernel đơn để quản lý các Server ảo và cho phép chúng chạy cùng một lúc (có thể ngầm hiểu, một Server chính là giao diện người dùng được sử dụng để tương tác với hệ điều hành).
* Các phần mềm hỗ trợ: Xen, Vmware,...
![](http://voer.edu.vn/media/transforms/20140306-214626-tong-quan-ve-ao-hoa-may-chu/paravirtualization.png)

<a name="ao_hoa_he_dieu_hanh"></a>
###1.4.3.Ảo hóa hệ điều hành.

* Một hệ điều hành được vận hành ngay trên một hệ điều hành chủ đã tồn tại và có khả năng cung cấp một tập hợp các thư viện tương tác với các ứng dụng, khiến cho mỗi ứng dụng truy xuất tài nguyên phần cứng cảm thấy như truy xuất trực tiếp máy chủ vật lý. 
* Các phần mềm hỗ trợ: OpenVZ, Linux-VServer, Docker,...

<a name="ao_hoa_ung_dung"></a>
###1.4.4. Ảo hóa ứng dụng.

* Một ứng dụng được ảo hóa sẽ không được cài đặt lên máy tính một cách thông thường, mặc dù ở góc độ người sử dụng, ứng dụng vẫn hoạt động một cách bình thường.
* Ảo hóa ứng dụng sẽ giúp tách rời sự phụ thuộc giữa nền tảng phần cứng, hệ điều hành và ứng dụng với nhau.

<a name="dien_toan_dam_may"></a>
#2. Cloud Computing (điện toán đám mây)
* Cloud Computing là mô hình cho phép truy cập qua mạng để lựa chọn và sử dụng tài nguyên có thể được tính toán (ví dụ: mạng, máy chủ, lưu trữ, ứng dụng và dịch vụ) theo nhu cầu một cách thuận tiện và nhanh chóng;
* đồng thời cho phép kết thúc sử dụng dịch vụ, giải phóng tài nguyên dễ dàng, giảm thiểu các giao tiếp với nhà cung cấp”

<a name="dac_diem"></a>
##2.1. 5 đặc điểm
* Khả năng thu hồi và cấp phát tài nguyên (Rapid elasticity)
* Truy nhập qua các chuẩn mạng (Broad network access)
* Dịch vụ sử dụng đo đếm được (Measured service,) hay là chi trả theo mức độ sử dụng pay as you go.
* Khả năng tự phục vụ (On-demand self-service).
* Chia sẻ tài nguyên (Resource pooling).

<a name="mo_hinh_dich_vu"></a>
##2.2: 4 mô hình dịch vụ (mô hình sản phẩm)
* Public Cloud: Đám mây công cộng (là các dịch vụ trên nền tảng Cloud Computing để cho các cá nhân và tổ chức thuê, họ dùng chung tài nguyên).
* Private Cloud: Đám mây riêng (dùng trong một doanh nghiệp và không chia sẻ với người dùng ngoài doanh nghiệp đó)
* Community Cloud: Đám mây cộng đồng (là các dịch vụ trên nền tảng Cloud computing do các công ty cùng hợp tác xây dựng và cung cấp các dịch vụ cho cộng đồng. Tôi cũng chưa rõ FB có phải là một dạng này không, cần xác nhận lại.
* Hybrid Cloud : Là mô hình kết hợp (lai) giữa các mô hình Public Cloud và Private Cloud (không rõ có Community Cloud nữa không … :D)

<a name="mo_hinh_trien_khai"></a>
##2.3: 3 mô hình triển khai: tức là triển khai Cloud Computing để cung cấp:
* Hạ tầng như một dịch vụ (Infrastructure as a Service)
* Nền tảng như một dịch vụ (Platform as a Service)
* Phần mềm như một dịch vụ (Software as a Service)

<a name="openstack"></a>
#3. OpenStack
* OpenStack là một phần mềm mã nguồn mở, dùng để triển khai Cloud Computing, bao gồm private cloud và public cloud.
* Mô hình cụ thể:

![](https://vietstack.files.wordpress.com/2014/02/openstack-software-diagram.png?w=756&h=313)

Trong đó: 
	* Standard Hardware: phần cứng của bạn, đã được ảo hóa để chia sẻ cho ứng dụng, người dùng.
	* Your Applicaions: Trên cùng là các ứng dụng của bạn, tức là các phần mềm mà bạn sử dụng
	* OpenStack là phần ở giữa 2 phần trên. Trong OpenStack có các thành phần, module khác nhau nhưng trong hình minh họa các thành phần cơ bản: Dashboard, Compute, Networking, API, Storage …

<a name="thong_tin_openstack"></a>
##3.1. Một vài thông tin vắn tắt về OpenStack
* OpenStack là một dự án  mã nguồn mở  dùng để triển khai private cloud và public cloud, nó bao gồm nhiều thành phần, do các công ty, tổ chức ,lập trình viên tự nguyện xây dựng và phát triển. Có 3 nhóm chính tham gia: Nhóm điều hành, nhóm phát triển và nhóm người dùng.
* OpenStack hoạt động theo hướng mở: (Open) Công khai lộ trình phát triển, (Open) công khai mã nguồn …
* Tháng 10/2010 Racksapce và NASA công bố phiên bản đầu tiên của OpenStack, có tên là OpenStack Austin, với 2 thành phần chính: Compute (tên mã là Nova) và Object Storage (tên mã là Swift)
* Các phiên bản OpenStack có chu kỳ 6 tháng. Tức là 6 tháng một lần sẽ công bố phiên bản mới với các tính năng bổ sung.
* Tính đến nay có 9 phiên bản của OpenStack bao gồm: Austin, Bexar, Cactus, Diablo, Essex, Folsom, Grizzly, Havana.
* Tên các phiên bản được bắt đầu theo thứ tự A, B, C, D …trong bảng chữ cái.
* Các thành phần (project con) có tên và có mã dự án đi kèm, với Havana gồm 9 thành phần sau:
	* Compute (code-name Nova)
	* Networking (code-name Neutron)
	* Object Storage (code-name Swift)
	* Block Storage (code-name Cinder)
	* Identity (code-name Keystone)
	* Image Service (code-name Glance)
	* Dashboard (code-name Horizon)
	* Telemetry (code-name Ceilometer)
	* Orchestration (code-name Heat)
