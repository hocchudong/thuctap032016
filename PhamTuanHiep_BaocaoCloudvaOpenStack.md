#Tìm hiểu Cloud computing và Open stack
----
#Mục Lục
* [1.Cloud computing] (#cloud)
  * [1.1 Định nghĩa về Cloud computing.] (#1.1)
  * [1.2 Các đặc tính cốt lõi của cloud computing.] (#1.2)
  * [1.3 Các mô hình dịch vụ của cloud computing.] (#1.3)
  * [1.4 Các mô hình triển khai của cloud computing.] (#1.4)
* [2.Open stack] (#openstack)
  * [2.1 Định nghĩa về OpenStack. ] (#2.1)
  * [2.2 Một số đặc điểm và các phiên bản của OpenStack. ] (#2.2)
  * [2.3 Vị trí của OpenStack trong mô hình thực tế. ] (#2.3)

----
<a name="cloud"></a>
##1. Cloud computing.
<a name="1.1"><a>
###1.1 Định nghĩa về Cloud computing.
* **Cloud computing** là mô hình cho phép truy cập mạng theo nhu cầu, thuận tiện và phổ biến tới các tài nguyên tính toán có khả năng đồng bộ ( ví dụ như mạng, server, lưu trữ, ứng dụng và dịch vụ ). Những tài nguyên này được cung cấp và giải phóng một cách nhanh chóng với chi phí quản lý nhỏ, giảm thiểu tương tác với nhà cung cấp dịch vụ. Mô hình này được gồm 5 đặc tính cốt lõi, 3 mô hình dịch vụ, 4 mô hình ứng dụng.

----
<a name="1.2"><a>
###1.2 Năm đặc tính cốt lõi của cloud computing.
* **Cloud computing là dịch vụ tự phục vụ theo nhu cầu**. Một cách chi tiết hơn, một khách hàng có thể đơn phương cung cấp các khả năng tính toán, ví dụ như: thời gian máy chủ, lưu trữ mạng, một cách tự động mà không cần tới tương tác giữa họ với nhà cung cấp dịch vụ
* **Khả năng truy cập qua các mạng chuẩn**. Các khả năng của cloud có sẵn trên mạng và được truy cập thông qua các chuẩn cơ học, cái hỗ trợ cho cảc nền tảng máy khác mỏng hoặc day (thin or thick), ví dụ như điện thoại thông minh, máy tính bảng,...
* **Chia sẻ tài nguyên**. Các tài nguyên của nhà cung cấp được tổng hợp để phục vụ cho đa khách hàng sử dụng mô hình đa thuê (multi-tenant), 
với các tài nguyên ảo và vật lý khác nhau để phục vu, gán cho từng nhu cầu của từng khách hàng. Khách hàng có thể không biết chính xác vị trí tài nguyên của các dịch vụ mà được cung cấp nhưng họ có thể biết những thông tin ở mức cao như nước, bang nơi cung cấp tài nguyên.
* **Tính đàn hồi cao**. Các khả năng tính toán có thể được cung cấp và giải phóng một cách đàn hồi để mở rộng nhanh chóng ra ngoài và bên trong tương ứng với nhu cầu. Đối với khách hàng, các khả năng có sẵn thường xuất hiện không bị giới hạn và thích hợp với mọi số lượng ở bất kỳ thời 
điểm nào.
* **Dịch vụ được đo đạc được** Hệ thống cloud có thể tự động điều khiển và tối ưu hóa tài nguyên ở một số level của tài nguyên dịch vụ như: lưu trữ xử lý, băng thông và kích hoạt tài khoản. Lưu lượng sử dụng tài nguyên có thể được quản lý, điều khiển, báo cáo cho cả nhà cung cấp và khách hàng sử dụng dịch vụ.

----
<a name="1.3"><a>
###1.3 Ba mô hình cung cấp dịch vụ.
* **Software as a service**: Khả năng được cung cấp cho khách hàng là sử dụng các ứng dụng của nhà cung cấp chạy trên kiến trúc hạ tầng cloud.Các ứng dụng này có thể truy cập thì nhiều loại thiết bị phía máy khách thông qua hoặc các giao diện trực quan phía máy khách như trình duyệt 
web hoặc các giao diện ứng dụng. Khách hàng không quản lý hoặc điều khiển kiến trúc hạ tầng cloud bao gồm mạng, máy chủ, hệ điều hành, lưu trữ và thậm chí khả năng ứng dụng riêng biệt.
* **Platform as a Service**: Khả năng được cung cấp tới khách hàng là triển khai hạ tầng tạo bởi khách hàng hoặc hạ tầng mà ứng dung cần. Khách hàng không quản lý hoặc điều khiển hạ tầng cloud nhưng có khả năng điều khiển trên các ứng dụng mình triển khai trên cload và có thể đồng bộ cài đặt cho môi trường quản lý ứng dụng.
* **Infrastructure as a Service**: Khả năng được cung cấp cho khách hàng là khả năng cung cấp xử lý, lưu trữ, mạng và các tài nguyên tính toán khác nơi mà khách hàng có thể triển khai và chạy trên phần mềm độc lập, bao gốm hệ điều hành và các ứng dụng. Khách hàng không quản lý hoặc điều khiển hạ tầng cloud nhưng có thể điều khiển trên hệ điều hành, lưu trữ và các ứng dụng được triển khai và có thể quản lý hạn chế việc lựa chọn các thành phần mạng.

----
<a name="1.4"><a>
###1.4 Bốn mô hình triển khai.
* **cloud riêng tư**: Đây là hạ tầng cloud được cung cấp cho các tổ chức đơn gồm đa khách hang. Nó được sở hữu, quản lý và điều hành bở tổ chức, là bên thứ ba.
* **cloud cộng đồng**: Đây là hạ tầng cloud được cung cấp cho việc sử dụng của cộng đồng khách hàng từ nhiều tổ chức mà có những thứ liên quan tới nhau như nhiệm vụ, yêu cầu bảo mật, chính sách). Nó có thể quản lý, sở hữu bởi một hoặc nhiều tổ chức trong cộng đồng, bên thứ ba, hoặc phối hợp giữa các tổ chức đó.
* **cloud công cộng**: Đây là hạ tầng cloud được cung cấp cho việc sử dụng của toàn bộ mọi người. Nó có thể sở hữu, quản lý, điều hành bởi các tổ chức doanh nghiệp, học thuật hay chính phủ hoặc phối hợp giữ chúng.
* **cloud hỗ hợp**: Đây là hạ tầng cloud được phối hợp 2 hoặc nhiều hạ tầng cloud riêng biêt. Những hạ tầng này vẫn giữ tính đặc điểm riêng biệt nhưng có thể phối hợp cùng nhay bởi việc được chuẩn hóa hoặc công nghệ phù hợp cái mà cho phép dữ liệu tính di động của dữ liệu và ứng dụng.

----
<a name="openstack"></a>
##2. OpenStack.
<a name="2.1"></a>
* **2.1 Định nghĩa**: 
* OpenStack là một hệ điều hành cloud giúp điều khiển tập lớn các tính toán, lưu trữ và cả tài nguyên mạng thông qua một trung tâm dữ liệu, tất cả được quản lý thông qua một dashboard. Dashboar này giúp người quản trị điều khiển trong khi trao quyền cho các tài khoản của họ để cung cấp tài nguyên thông qua giao diện web.
* OpenStack là một dự án  mã nguồn mở  dùng để triển khai private cloud và public cloud, nó bao gồm nhiều thành phần (tài liệu tiếng anh gọi là project con) do các công ty, tổ chức ,lập trình viên tự nguyện xây dựng và phát triển. Có 3 nhóm chính tham gia: Nhóm điều hành, nhóm phát triển và nhóm người dùng.

----
<a name="2.2"></a>
* **2.2 Một số đặc điểm của và phiên bản của OpenStack.**
* OpenStack hoạt động theo hướng mở: (Open) Công khai lộ trình phát triển, (Open) công khai mã nguồn. Tháng 10/2010 Racksapce và NASA công bố phiên bản đầu tiên của OpenStack, có tên là OpenStack Austin, với 2 thành phần chính ( project con) : Compute (tên mã là Nova) và Object Storage (tên mã là Swift)
* Các phiên bản OpenStack có chu kỳ 6 tháng. Tức là 6 tháng một lần sẽ công bố phiên bản mới với các tính năng bổ sung.
* Tính đến nay có 9 phiên bản của OpenStack bao gồm: Austin, Bexar, Cactus, Diablo, Essex, Folsom, Grizzly, Havana.Tên các phiên bản được bắt đầu theo thứ tự A, B, C, D …trong bảng chữ cái.
* Tính đến thời điểm viết bài này phiên bản hiện tại là OpenStack Havana (công bố tháng 10/2013) . Tham khảo thêm tại đây về các phiên bản ,
* Các thành phần (project con) có tên và có mã dự án đi kèm, với Havana gồm 9 thành phần sau:
   Compute (code-name Nova)
   Networking (code-name Neutron)
   Object Storage (code-name Swift)
   Block Storage (code-name Cinder)
   Identity (code-name Keystone)
   Image Service (code-name Glance)
   Dashboard (code-name Horizon)
   Telemetry (code-name Ceilometer)
   Orchestration (code-name Heat)

----
<a name="2.3"></a>
* **2.3 Vị trí OpenStack trong thực tế.**
* Hình sau sẽ minh họa cho vị trí của OpenStack:

![](https://www.openstack.org/themes/openstack/images/software/openstack-software-diagram.png)
* Trong đó :
  * Phía dưới là phần cứng của, đã được ảo hóa để chia sẻ cho ứng dụng, người dùng
  * Trên cùng là các ứng dụng của bạn, tức là các phần mềm mà bạn sử dụng
  * Và OpenStack là phần ở giữa 2 phần trên, trong OpenStack có các thành phần, module khác nhau nhưng trong hình minh họa các thành phần cơ bản: Dashboard, Compute, Networking, API, Storage …
  
----
