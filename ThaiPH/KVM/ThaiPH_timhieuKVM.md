# Tìm hiểu KVM (Kernel-based Virtual Machine)
# Mục lục
<h3><a href="#concept">1. Khái niệm</a></h3>
<h3><a href="#arch">2. KVM Stack</a></h3>
<h3><a href="#kvm-qemu">3. KVM - QEMU</a></h3>
<h3><a href="#features">4. Các tính năng của KVM</a></h3>
<ul>
<li><a href="#sec">4.1. Security</a></li>
<li><a href="#memmgr">4.2. Memory Management</a></li>
<li><a href="#storage">4.3. Storage</a></li>
<li><a href="#migrate">4.4. Live migration</a></li>
<li><a href="#perf">4.5. Performance and scalability</a></li>
</ul>
<h3><a href="#ref">5. Tham khảo</a></h3>

---

<h2><a name="concept">1. Khái niệm</a></h2>
<div>
KVM (Kernel-based virtual machine) là giải pháp ảo hóa cho hệ thống linux trên nền tảng phần cứng x86 có các module mở rộng hỗ trợ ảo hóa (Intel VT-x hoặc AMD-V). 
<br>
Về bản chất, KVM không thực sự là một hypervisor có chức năng giải lập phần cứng để chạy các máy ảo. Chính xác KVM chỉ là một module của kernel linux hỗ trợ cơ chế mapping các chỉ dẫn trên CPU ảo (của guest VM) sang chỉ dẫn trên CPU vật lý (của máy chủ chứa VM). Hoặc có thể hình dung KVM giống như một driver cho hypervisor để sử dụng được tính năng ảo hóa của các vi xử lý như Intel VT-x hay AMD-V, mục tiêu là tăng hiệu suất cho guest VM. 
</div>

<h2><a name="arch">2. KVM Stack</a></h2>
<div>
<img src="http://i.imgur.com/dUhDP88.png"/>
Trên đây là KVM Stack bao gồm 4 tầng:
<ul>
<li><b>User-facing tools:</b> Là các công cụ quản lý máy ảo hỗ trợ KVM. Các công cụ có giao diện đồ họa (như virt-manager) hoặc giao diện dòng lệnh như (virsh)</li>
<li><b>Management layer:</b> Lớp này là thư viện <b>libvirt</b> cung cấp API để các công cụ quản lý máy ảo hoặc các hypervisor tương tác với KVM thực hiện các thao tác quản lý tài nguyên ảo hóa, vì tự thân KVM không hề có khả năng giả lập và quản lý tài nguyên như vậy.</li>
<li><b>Virtual machine:</b> Chính là các máy ảo người dùng tạo ra. Thông thường, nếu không sử dụng các công cụ như <b>virsh</b> hay <b>virt-manager</b>, KVM sẽ sử được sử dụng phối hợp với một hypervisor khác điển hình là <b>QEMU</b>.</li>
<li><b>Kernel support:</b> Chính là KVM, cung cấp một module làm hạt nhân cho hạ tầng ảo hóa (kvm.ko) và một module kernel đặc biệt hỗ trợ các vi xử lý VT-x hoặc AMD-V (kvm-intel.ko hoặc kvm-amd.ko)</li>
</ul>
</div>

<h2><a name="kvm-qemu">3. KVM - QEMU</a></h2>
<div>
Hệ thống ảo hóa KVM hay đi liền với QEMU. Về mặt bản chất, QEMU đã là một hypervisor hoàn chỉnh và là hypervisor loại 2. QEMU có khả năng giả lập tài nguyên phần cứng, trong đó bao gồm một CPU ảo. Các chỉ dẫn của hệ điều hành tác động lên CPU ảo này sẽ được QEMU chuyển đổi thành chỉ dẫn lên CPU vật lý nhờ một <b>translator</b> là <b>TCG(Tiny Core Generator)</b>. Các hypervisor loại 2 khác như VMWare cũng có các bộ chuyển đổi tương tự, và bản thân các bộ dịch này hiệu suất không lớn. 
<br>
Do KVM hỗ trợ ánh xạ CPU vật lý sang CPU ảo, cung cấp khả năng tăng tốc phần cứng cho máy ảo và hiệu suất của nó nên QEMU sử dụng KVM làm <b>accelerator</b> tận dụng tính năng này của KVM thay vì sử dụng TCG.
</div>
<h2><a name="features">4. Các tính năng của KVM</a></h2>
<ul>
<li><h3><a name="sec">4.1. Security</a></h3>
<div>
<br><br>
<img src="http://www.ibm.com/developerworks/cloud/library/cl-hypervisorcompare-kvm/figure6.gif"/>
<br><br>
Trong kiến trúc KVM, máy ảo được xem như các tiến trình Linux thông thường, nhờ đó nó tận dụng được mô hình bảo mật của hệ thống Linux như SELinux, cung cấp khả năng cô lập và kiểm soát tài nguyên.
<br>
Bên cạnh đó còn có SVirt project - dự án cung cấp giải pháp bảo mật MAC (Mandatory Access Control - Kiểm soát truy cập bắt buộc) tích hợp với hệ thống ảo hóa sử dụng SELinux để cung cấp một cơ sở hạ tầng cho phép người quản trị định nghĩa nên các chính sách để cô lập các máy ảo. Nghĩa là SVirt sẽ đảm bảo rằng các tài nguyên của máy ảo không thể bị truy cập bởi bất kì các tiến trình nào khác; việc này cũng có thể thay đổi bởi người quản trị hệ thống để đặt ra quyền hạn đặc biệt, nhóm các máy ảo với nhau chia sẻ chung tài nguyên.
</div>
</li>

<li><h3><a name="memmgr">4.2. Memory Management</a></h3>
<div>
KVM thừa kế tính năng quản lý bộ nhớ mạnh mẽ của Linux. Vùng nhớ của máy ảo được lưu trữ trên cùng một vùng nhớ dành cho các tiến trình Linux khác và có thể swap. KVM hỗ trợ NUMA (Non-Uniform Memory Access - bộ nhớ thiết kế cho hệ thống đa xử lý) cho phép tận dụng hiệu quả vùng nhớ kích thước lớn.
<br>
KVM hỗ trợ các tính năng ảo của mới nhất từ các nhà cung cấp CPU như EPT (Extended Page Table) của Microsoft, Rapid Virtualization Indexing (RVI) của AMD để giảm thiểu mức độ sử dụng CPU và cho thông lượng cao hơn.
<br>
KVM cũng hỗ trợ tính năng <b>Memory page sharing</b> bằng cách sử dụng tính năng của kernel là Kernel Same-page Merging (KSM).
</div>
</li>
<li><h3><a name="storage">4.3. Storage</a></h3>
<div>
KVM có khả năng sử dụng bất kỳ giải pháp lưu trữ nào hỗ trợ bởi Linux để lưu trữ các Images của các máy ảo, bao gồm các ổ cục bộ như IDE, SCSI và SATA, Network Attached Storage (NAS) bao gồm NFS và SAMBA/CIFS, hoặc SAN thông qua các giao thức iSCSI và Fibre Channel.
<br>
KVM tận dụng được các hệ thống lưu trữ tin cậy từ các nhà cung cấp hàng đầu trong lĩnh vực Storage.
<br>
KVM cũng hỗ trợ các images của các máy ảo trên hệ thống tệp tin chia sẻ như GFS2 cho phép các images có thể được chia sẻ giữa nhiều host hoặc chia sẻ chung giữa các ổ logic.
</div>
</li>
<li><h3><a name="migrate">4.4. Live migration</a></h3>
<div>
KVM hỗ trợ <b>live migration</b> cung cấp khả năng di chuyển ác máy ảo đang chạy giữa các host vật lý mà không làm gián đoạn dịch vụ. Khả năng <b>live migration</b> là trong suốt với người dùng, các máy ảo vẫn duy trì trạng thái bật, kết nối mạng vẫn đảm bảo và các ứng dụng của người dùng vẫn tiếp tục duy trì trong khi máy ảo được đưa sang một host vật lý mới. KVM cũng cho phép lưu lại trạng thái hiện tại của máy ảo để cho phép lưu trữ và khôi phục trạng thái đó vào lần sử dụng tiếp theo.
</div>
</li>
<li><h3><a name="perf">4.5. Performance and scalability</a></h3>
<div>
KVM kế thừa hiệu năng và khả năng mở rộng của Linux, hỗ trợ máy ảo với 16 CPUs ảo, 256GB RAM và hệ thống máy host lên tới 256 cores và trên 1TB RAM. 
</div>
</li>
</ul>
<h2><a name="ref">5. Tham khảo</a></h2>
<div>
[1] - <a href="http://www.ibm.com/developerworks/cloud/library/cl-hypervisorcompare-kvm/">http://www.ibm.com/developerworks/cloud/library/cl-hypervisorcompare-kvm/</a>
<br>
[2] - <a href="https://www.ibm.com/developerworks/library/l-using-kvm/">https://www.ibm.com/developerworks/library/l-using-kvm/</a>
<br>
[3] - <a href="https://manthang.wordpress.com/2014/06/18/kvm-qemu-do-you-know-the-connection-between-them/">https://manthang.wordpress.com/2014/06/18/kvm-qemu-do-you-know-the-connection-between-them/</a>
</div>

