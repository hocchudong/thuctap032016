#Báo cáo tìm hiểu Cloud Computing và Open Stack
##Mục lục
[I.Tổng quan về ảo hóa](#aohoa)

- [1.Khái niệm](#khainiem)

- [2.So sánh trước và sau ảo hóa](#sosanh)

- [3.Ưu điểm công nghệ ảo hóa](#uudiem)

- [4.Phân loại công nghệ ảo hóa](#phanloai)

- [5.Hường tiếp cận công nghệ ảo hóa](#huong)

II.Cloud Computing
<a name="aohoa"></a>
###I.Ảo hóa(Virtualization)
<a name="khainiem"></a>
####1.Khái niệm
- `Virtualization`(Ảo hóa) ra đời những năm 196x đề cập đến hành động phiên bảo `Virtual`(Ảo)của một cái gì đó 
bao gồm cả các máy tính ảo với nền tảng phần cứng, hệ ddieuf hành, thiết bị lưu trữ hoặc cả một tập tài nguyên về mạng máy tính,.. nhưng không bị hạn chế
(nguồn wiki)
<a name="sosanh"></a>
#####2.So sánh trước sau ảo hóa

|Trước ảo hóa|Sau ảo hóa|
|------------|----------|
|-Một hệ điều hành trên 1 máy|-Phần cứng độc lập với hệ điều hành và phần mềm|
|-Phần mềm và phần cứng gắn chặt nhăt|-Các máy ảo có thể được cung ứng từ mọi hệ thống|
|-Hạ tầng không linh hoạt, tốn kém,dễ xảy ra xung đột khi chạy nhiều ứng dụng trên cùng máy ảo|-Có thể quản lý hệ điều hành va ứng dụng như một đơn vị duy nhất biowr vì chúng được đóng gói vào một máy ảo
<a name="uudiem"></a>
#####3.Ưu điểm của `Virtualization`
<ul>
<li>Giảm thiểu chi phí bảo dưỡng</li>
<li>Tương thích với nhiều ứng dụng và hệ điều hành đòng thời</li>
<li>Tập trung cho kiểm soát và quản trị/li>
<li>Dễ dàng sao lưu và khôi phục</li>
<li>Khai thác nhiều hơn nữa về công suất hoạt động của phần cứng</li>
<li>Live Migration-"Chuyển đổi máy ảo kể cả khi đang hoạt đông"</li>
<li>Nâng cao độ sẵn sàng cho hệ thông</li>
</ul>

<a name="phanloai"></a>
#####4.Phân loại công nghệ ảo hóa
- Full `Virtualization`:
<ul>
<li>Open source:KVM, VirtualBox, KQEMU</li>
<li>Commercial:VMware,MS Hyper-VMware</li>
</ul>
- Para `Virtualization`: Xen,VMWare
- OS-Level `Virtualization`: OpenVc, Linux-VServer, Docker

<a name="huong"></a>
#####5.Hướng tiếp cận ảo hóa
- Host Architecture:
<ul>
<li>Được cài đặt và chạy như một ứng dụng</li>
<li>Dự vào một hệ điều hành của máy vật lý đẻ quanr lý tài nguyên và hỗ trợ thiết bị</li>
</ul>
- Bare-Metal(Hypervisor) Architecture
<li>Ảo hóa từ lõi-trong kernel</li>
<li>Cài đặt trực tiếp lên phần cứng</li>
</ul>

<a name="cloud"></a>
####II.Cloud Computing
#####1.Định nghĩa
>Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. This cloud model is composed of five essential characteristics, three service models, and four deployment models.
