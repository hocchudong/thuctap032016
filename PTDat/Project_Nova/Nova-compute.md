#Nova Compute

- Openstack Compute bao gồm những thành phần chính như sau:
 <ul>
 <li>Cloud controller : Đại diện cho global state tương tác với các thành phần khác . API server hoạt động như một web services front end cho cloud controller. Compute controller cung cấp nguồn compute server và cũng thườg bao gồm Compute services.</li>
 <li>Object store là một thành phần tùy chọn cung cấp dịch vụ lưu trữ; chúng ta cũng có thể sử dụng Openstack Oject Storage để thay thế.</li>
 <li>Một thành phần khác đó là `auth manager` cung cấp xác thực và ủy quyền cho các services khi sử dụng với Compute system; chúng ta cũng có thể sử dụng Openstack identity giống như một dịch vụ xác thực riêng biệt để thay thế.</li>
 <li>`Volume controller` cung cấp lưu trữ khối nhanh chóng và vĩnh viễn cho compute servers.</li>
 <li>`Network controller` : Cung cấp vitual network để cho phép compute server tương tác với các thành phần khác và với public network. Chúng ta cũng có thể sử dụng Openstack Networking để thay thế.</li>
 <li>`Scheduler` : Được sử dụng để lựa chọn những compute controller thích hợp nhất cho instance.</li>
 </ul>

##Hypervisors.

- Compute controls hypervisor thông qua một API server. Lựa chọn những hypervisor tốt nhất để sử dụng, có thể rất khó khăn để lựa chọn, và bạn phải có ngân sách, các tài nguyên về nguồn lực, hỗ trợ các tính năng, và yêu cầu về kỹ thuật. Tuy nhiên , phần lớn sự phát triển của hệ thống Openstack sử dụng KVM và Xen-based hypervisor.
- Chúng ta có thể sắp xếp cloud sử dụng multiple hypervisor. Compute hỗ trợ những hypervisor như sau :
 <ul>
 <li>Baremetal</li>
 <li>Docker</li>
 <li>Hyper-V</li>
 <li>Kernel-based Vitual Machine (KVM)</li>
 <li>Linux Containers (LXC)</li>
 <li>Quick Emulator (QEMU)</li>
 <li>User Mode Linux (UML)</li>
 <li>VMware vSphere</li>
 <li>Xen</li>
 </ul>

##Compute service architecture.

**API server**
- API server là trái tim của cloud framework, nơi thực hiện các lệnh và việc kiểm soát hypervisor, storage, networking có thể lập trình được. 
- Các API endpoints về cơ bản là các HTTP web services thực hiện xác thực, ủy quyền và các lệnh căn bản, kiểm các các chức năng sử dụng giao diện API của Amazon, Rackspace, và các mô hình liên quan khác. Điều này cho phép các API tương thích với nhiều công cụ sẵn có, tương tác với các nhà cung cấp dịch vụ cloud khác. Điều này tạo ra để ngăn chặn vấn đề phụ thuộc vào nhà cung cấp dịch vụ.

**Message queue**

- Message Broker cung cấp hàng đợi lưu bản tin tương tác giữa các dịch vụ, các thành phần như compute nodes, networking controllers(phần mềm kiểm soát hạ tầng mạng), API endpoints, scheduler(xác định máy vật lý nào được sử dụng để cấp phát tài nguyên ảo hóa), và các thành phần tương tự.

**Compute worker**

- Compute worker quản lý các tài nguyên tính toán của các máy ảo trên các Compute host. API sẽ chuyển tiếp các lệnh tới compute worker để hoàn thành các nhiệm vụ sau:
 <ul>
 <li>Chạy các máy ảo.</li>
 <li>Xóa các máy ảo.</li>
 <li>Khởi động lại máy ảo.</li>
 <li>Attach các volume.</li>
 <li>Detach các volume</li>
 <li>Lấy các console output.</li>
 </ul>

**Network controller**

- Network controller quản lý tài nguyên mạng trên host machines. Các máy chủ API gửi command thông qua hàng đợi , sau đó được xử lý bởi độ điều khiển mạng. Các hoạt động cụ thể bao gồm.
 <ul>
 <li>Phân bố địa chỉ IP cố định.</li>
 <li>Cấu hình VLANs cho các project.</li>
 <li>Cấu hình network cho các compute node.</li>
 </ul>