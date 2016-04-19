#Báo Cáo Thực Tập : Tìm Hiểu Về Cloud Computing và Open Stack.

****
##Mục Lục
[A. Ảo hóa và Cloud Computing.] (#ahcc)
 <ul>
 <li>[I. Ảo hóa.] (#ah)
  <ul>
  <li>[1. Ảo hóa là gì?] (#ahlg)</li>
  <li>[2. Lợi ích của ảo hóa] (#liah)</li>
  <li>[3. Các loại ảo hóa.] (#clah)</li>
  <li>[4. Hướng tiếp cận ảo hóa.] (#htcah)
   <ul>
   <li>[4.1. Hosted Architecture.] (#ha)</li>
   <li>[4.2. Bare-Metal.] (#bm)</li>
   </ul>
  </li>
  </ul>
 </li>
 <li>[II. Điện toán đám mây (Cloud Computing).] (#dtdm)
  <ul>
  <li>[1. Điện toán đấm mây (Cloud Computing) là gì?] (#dtdmlg)</li>
  <li>[2. Lợi ích của điện toán đám mây.] (#lidtdm)</li>
  <li>[3. Mô hình triển khai.] (#mhtk)
   <ul>
   <li>[3.1. Public Cloud.] (#pc)</li>
   <li>[3.2. Private Cloud.] (#prc)</li>
   <li>[3.3. Hybrid Cloud.] (#hc)</li>
   <li>[3.4. Community Cloud.] (#cc)</li>
   </ul>
  </li>
  <li>[4. Mô hình dịch vụ.] (#mhdv)
   <ul>
   <li>[4.1. Infrastructure as a Service (IaaS).] (#iaas)</li>
   <li>[4.2. Platform as a Service (PaaS).] (#paas)</li>
   <li>[Software as a Services (SaaS).] (#saas)</li>
   </ul>
  </li>
  </ul>
 </li>
 </ul>
[B. OpenStack.] (#openstack)
 <ul>
 <li>[I. Tổng quan về Openstack.] (#tqos)
  <ul>
  <li>[1. Giới thiệu về Openstack.] (#gtos)</li>
  <li>[2. Openstack được sử dụng như thế nào trong môi trường điện toán đám mây.] (#oshow)</li>
  </ul>
 </li>
 <li>[II. Các thành phần của OpenStack.] (#tpos)
  <ul>
  <li>[1. NOVA.] (#nova)</li>
  <li>[2. Swift.] (#swift)</li>
  <li>[3. Cinder.] (#cinder)</li>
  <li>[4. Neutron.] (#neutron)</li>
  <li>[5. Horizon.] (#horizon)</li>
  <li>[6. Keystone.] (#keystone)</li>
  <li>[7. Glane.] (#glane)</li>
  <li>[8. Cilometer.] (#cilometer)</li>
  <li>[9. Heat.] (#heat)</li>
  </ul>
 </li>
 <li>[III. Lợi ích và hạn chế khi sử dụng OpenStack.] (#lihc)
  <li>[1. Lợi ích.] (#lios)</li>
  <li>[2. Hạn chế.] (#hcos)</li>
 </li>
 </ul>



****

<a name="ahcc"></a>
##A. Ảo hóa và Cloud Computing.
<a name="ah"></a>
###I. Ảo hóa.
<a name="ahlg"></a>
###1. Ảo hóa là gì?

- Ảo hóa là tạo ra một phiên bản ảo của một thứ gì đó trong máy tính. Có rất nhiều thứ để có thể được ảo hóa, từ tạo ổ đĩa ảo, RAM ảo, ổ cứng ảo, máy chủ ảo và cho đến hệ điều hành.
<a name="liah"></a>
###2. Lợi ích của ảo hóa.

- Giúp giảm thiểu chi phí bảo dưỡng.
- Tương thích với nhiều ứng dụng và hệ điều hành đồng thời.
- tập chung cho kiểm soát và quản trị.
- Dễ dàng trong sao lưu và khôi phục.
- Khai thác nhiều hơn về công suất hoạt động của phần cứng.
- Chuyển đổi các máy ảo kể cả khi đang hoạt động.
- Nâng cao độ sẵn sàng cho hệ thống.
- Là bước đệm để thực hiện điện toán đám mây.
<a name="clah"></a>
###3. Các loại ảo hóa.

- Hệ điều hành ảo (tạo máy ảo).
- Ảo hóa phần cứng.
 <ul>
 <li>Ảo hóa toàn phần (KVM, VITUALBOX,KQEMU).</li>
 <li>Ảo hóa một phần.</li>
 <li>Ảo hóa song song (Xen, VMWare).</li>
 <li>CPU hỗ trợ ảo hóa</li>
 </ul>
- Ổ đĩa ảo.
- Desktop ảo.
- RAM ảo.
- Máy chủ ảo.
- Ảo hóa phần mềm (OS-level vitualization : OpenVZ, Linux-VServer, Docker)
<a name="htcah"></a>
###4. Hướng tiếp cận ảo hóa.
<a name="ha"></a>
####4.1. Hosted Architecture.
####4.1.a. Tổng quan.

- Trong kiến trúc này, một hệ thống điều hành cơ sở (như Windows) được cài đặt trước. Một phần của phần mềm được gọi là Hypervisor hoặc màn hình máy ảo (VMM) được cài đặt trên hệ điều hành máy chủ và cho phép người sử dụng chạy các hệ điều hành khác nhau trong cửa sổ ứng dụng riêng của họ. Các sản phẩm thông thường sử dụng kiến trúc này là VMWare workstation.

![scr1](http://i.imgur.com/cWsLOzK.png)

####4.1.b. Lợi ích và hạn chế.

- Lợi ích: Một lợi ích của việc sử dụng một kiến trúc ảo hóa lưu trữ trên máy là dễ dàng cài đặt và cấu hình.

- Hạn chế:
 <ul>
 <li>Tổ chức kiến trúc ảo hóa không có khả năng cạnh tranh hoặc cung cấp so với tổ chức kiến trúc có chạy qua nhiều PCI thiết bị I/O.</li>
 <li>Thiếu sự hỗ trợ cho hệ điều hành thời gian thực.</li>
 </ul>

####4.1.c. Use Cases.

- Nó thường sử dụng trong các phần mềm thử nghiệm hoặc để chạy các ứng dụng. Ảo hóa lưu trữ trên máy cũng hỗ trợ nhanh chóng cho chạy các hệ điều hành khác nhau trên một máy tính.
<a name="bm"></a>
###4.2. Bare-Metal.
####4.2.a. Tổng quan.

- Trong kiến trúc này, một VMM (còn gọi là hypervisor) được cài đặt giao trực tiếp với hệ thống phần cứng hơn là dựa trên một hế điều hành máy chủ.

![scr2](http://i.imgur.com/5zUxFiR.png)

####4.2.b. Lợi ích và hạn chế.

- Lợi ích: 
 <ul>
 <li>Hiệu suất I/O được cải thiện tốt hơn khi phân vùng.</li>
 <li>Có sự hỗ trợ của hệ điều hành thời gian thực.</li>
 </ul>

- Hạn chế:
 <ul>
 <li>Bất kì trình điều khiển cần thiết để hỗ trợ các nền tảng phần cứng khác nhau phải được bao gồm trong các hypervisor, ngoài trình điều khiển cho các thiết bị này sẽ được chia sẻ cho những máy ảo.</li>
 <li>Khó khăn hơn trong việc cài đặt và cấu hình hơn là một phải pháp lưu trữ.</li>
 </ul>

####4.2.c. Use Cases.

- Thực sự hữu ích khi sử dụng  trong trường hợp các ứng dụng triển khai có sử dụng nhiều hệ điều hành. Cụ thể các ứng dụng phải cung cấp xử lí dữ liệu thời gian thực và cung cấp truy cập đến các dịch vụ hệ điều hành thông dụng có thể được hưởng lợi từ Bare-Metal vitualization.
<a name="dtdm"></a>
###II. Điện toán đám mây (Cloud Computing).

- Cloud Computing hay còn gọi là "công nghệ điện toán đám mây" hiện nay được ứng dựng rất nhiều trong công nghệ thông tin điện tử viễn thông. Với những tính năng ưu việt và những ứng dụng nổi bật của nó mà hiện nay công nghệ này được ưa chuộng và được sử dụng rất nhiều.

- Trong vài năm gần đây, điện toán đám mây đã tạo ra một cuộc cách mạng trong nghành công nghiệp máy tính, thay đổi cơ bản cách thức sử dụng nguồn tài nguyên, cơ cấu vận hành cũng như việc lưu trữ, phân phối và xử lí thông tin. Đa số chúng ta đều đã và đang sử dụng một hoặc nhiều các dịch vụ ứng dụng công nghệ điện toán đấm mây trong đời sống hằng ngày cũng như trong quản lí doanh nghiệp.
<a name="dtdmlg"></a>
####1. Điện toán đấm mây (Cloud Computing) là gì?

- Là mô hình điện toán cho phép truy cập qua mạng để lựa chọn và sử dụng tài nguyên tính toán theo nhu cầu một cách thuận tiện và nhanh chóng, đồng thời cho phép kết thúc sử dụng dịch vụ, giải phóng tài nguyên dễ dàng, giảm thiểu các giao tiếp với nhà cung cấp.

- Điện toán đấm mây đơn giản chỉ là một tập hợp các tài nguyên máy tính gộp lại và cung cấp dịch vụ trên các kênh web. Khi chúng ta biểu đồ mối quan hệ giữa tất cả các yếu tố thì chúng tương tự như một đám mây.

![scr3](http://i.imgur.com/prFxtWL.png)
<a name="lidtdm"></a>
####2. Lợi ích của điện toán đám mây.

- Sử dụng các tài nguyên tính toán động.
- Giảm thiểu chi phí.
- Giảm độ phức tạp trong cơ cấu của doanh nghiệp.
- Tằng khả năng sử dụng tài nguyên tính toán.
<a name="mhtk"></a>
####3. Mô hình triển khai.

![scr4](http://i.imgur.com/5UwtJC2.png)
<a name="pc"></a>
####3.1. Public Cloud.

![scr5](http://i.imgur.com/adCg7J1.png)

- Là các dịch vụ đám mây được một bên thứ 3 cung cấp. Chúng tồn tại bên ngoài tường lửa của công ty.
- Các Public Cloud cố gắng cung cấp cho người tiêu dùng với các phần tử công nghệ thông tin tốt nhất. Cho dù đó là phần phềm, cơ sở hạ tầng ứng dụng hay là cơ sở hạ tầng vật lý. Nhà cung cấp chịu trách nhiệm về cài đặt, quản lí, cung cấp và bảo trì.
- Ví dụ : Amazon, Digital Ocean, Rackspaces,...
<a name="prc"></a>
####3.2. Private Cloud.

![scr6](http://i.imgur.com/Qcq6LcZ.png)

- Các Private Cloud là các dịch vụ đám mây được cung cấp trong doanh nghiệp. Những Cloud này thường nằm trong tường lửa của công ty và được doanh nghiệp quản lý.
- Các Cloud Private đưa ra nhiều lợi thế hơn so với các Cloud Public. Việc kiểm soát chi tiết hơn trên các tài nguyên khác nhau đe, lại cho công ty tất cả các tùy chọn cấu hình có sẵn. Việc sử dụng Private Cloud cũng đem lại sự bảo mật và quản lý tốt hơn.
- Một Private Cloud là sự lựa chọn rõ ràng khi:
 <ul>
 <li>Việc kinh doanh của doanh nghiệp gắn với dữ liệu và ứng dụng của doanh nghiệp. Vì vậy việc kiểm soát và bảo mật chiếm phần lớn công việc.</li>
 <li>Việc kinh doanh của doanh nghiệp là một phần của nghành công nghiệp phải phù hợp với an ninh nghiêm ngặt và các vấn đề bảo mật dữ liệu.</li>
 <li>Doanh nghiệp là đủ lớn để chạy một dữ liệu trung tâm điện toán đám mây có hiệu quả.</li>
 </ul>
- Ví dụ : Data center của HP.
<a name="hc"></a>
####3.3. Hybrid Cloud.

![scr7](http://i.imgur.com/pj9jcjd.png)


- Hybrid Cloud là sự kết hợp giữa các đám mây của Private Cloud và Public Cloud. Những đám mây này thường được các doanh nghiệp tạo ra và các trách nhiệm quản lý sẽ được phân chia giữa doanh nghiệp và nhà cung cấp Public Cloud.
- Một vài tình huống mà sử dụng Hybrid Cloud là tốt nhất:
 <ul>
 <li>Doanh nghiệp muốn sử dụng một ứng dụng SaaS nhưng quan tâm về bảo mật.</li>
 <li>Doanh nghiệp cung cấp dịch vụ được thay đổi cho các thị trường khác nhau.</li>
 </ul>
<a name="cc"></a>
####3.4. Community Cloud.

![scr8](http://i.imgur.com/HkVKpsy.png)

- Community Cloud là các đám mây được chia sẻ bởi một số tổ chức và hỗ trợ một cộng đồng cụ thể có mỗi quan tâm chung. Nó có thể được quản lý bởi bên phía tổ chức hoặc bên thứ 3.
<a name="mhdv"></a>
####4. Mô hình dịch vụ.
<a name="iaas"></a>
####4.1. Infrastructure as a Service (IaaS).

- Cung cấp dịch vụ về hạ tầng, các máy chủ, tài nguyên là : RAM, CPU, Storage,...
- Cung cấp phần "xác" của VM, người dùng chủ động cài đặt ứng dụng.
- Ví dụ: EC2 của Amazon, RackSpace,....
<a name="paas"></a>
####4.2. Platform as a Service (PaaS).

- Cung cấp dịch vụ về nền tảng (Platform) như : Database, môi trường để phát triển chương trình.
- Máy chủ có sẵn các môi trường để phát triển ứng dụng.
- Ví dụ: Google's AppEngine, Microsoft Azure.
<a name="saas"></a>
####4.3. Software as a Services (SaaS).

- Cung cấp các dịch vụ về phần mềm, bán hoặc cho thuê lâu dài.
- Nhà cung cấp dịch vụ triển khai gần như toàn bộ.
- Các phần mềm về ERP, Email,.... 
- Ví dụ : SalesFore.com, Webex, Gmail, Dropbox.

****
<a name="os"></a>
##B. Openstack.
<a name="tqos"></a>
###I. Tổng quan về Openstack.
<a name="gtos"></a>
####1. Giới thiệu về Openstack.

- Openstack cho phép người dùng triển khai các máy ảo và các trường hợp khác mà xử lý các nhiện vụ khác nhau, để quản lý một môi trường điện toán đám mây đang bay.
- Openstack là phần mềm mã nguồn mở, bất cứ ai cũng có thể truy cập và mã nguồn, thực hiện bất kì thay đổi hay sửa đỏi nào họ cần và tự do chia sẻ những thay đổi này ra một cộng đồng lớn.
<a name="oshow"></a>
####2. Openstack được sử dụng như thế nào trong môi trường điện toán đám mây.

- Openstack được coi là một cơ sở hạ tầng 
như một dịch vụ (IaaS).
- Cung cấp cơ sở hạ tầng có nghĩa là OpenStack làm cho nó dễ dàng cho người sử dụng để nhanh chóng thêm trường hợp mới khi các hạ tầng đám mây khác có thể chạy.
<a name="tpos"></a>
###II. Các thành phần của OpenStack.

![scr9](http://i.imgur.com/I8EDkQe.png)
<a name="nova"></a>
####1. NOVA.

- Là công cụ tính toán chính đằng sau OpenStack.
- Nó được sử dụng để triển khai và quản lý số lượng các máy ảo và các trường hợp khác xử lý các tác vụ tính toán.
- Hỗ trợ nhiều công nghệ ảo hóa : Xen, KVM, QEMU,....
<a name="swift"></a>
####2. Swift.

- Là một hệ thống lưu trữ cho các đối tượng và tập tin.
- Cung cấp khả năng sao lưu mở rộng, dự phòng, phân tán.
<a name="cinder"></a>
####3. Cinder.

- Là một thành phần lưu trữ khối.
- Có khả năng mở rộng và phân tán.
<a name="neutron"></a>
####4. Neutron.

- Cung cấp khả năng kết nối mạng cho OpenStack.
- Nó đảm bảo rằng mỗi thành phần của một triển khai OpenStack có thể giao tiếp với nhau một cách nhanh chóng và hiệu quả.
<a name="horizon"></a>
####5. Horizon.

- Là bảng điều khiển phái sau OpenStack.
- Là một ứng dụng chạy web và chạy trên nền của Apache.
- Cung cấp giao diện đồ họa để Adminstrator để quản lý các dịch vụ khác của OpenStack.
<a name="keystone"></a>
####6. Keystone.

- Cung cấp dịch vụ nhận dạng cho OpenStack.
- Nó cung cấp nhiều phương tiện truy cập, có nghĩa là nhà phát triển có thể dễ dàng khoanh vùng phương pháo truy cập người dùng hiện có của họ chống lại Keystone.
<a name="glane"></a>
####7. Glane.

- Là dịch vụ lưu trữ và truy xuất ổ đĩa ảo.
- Hỗ trợ nhiều định dạng.
- Có 3 tính năng chính.
 <ul>
 <li>Người quản trị tạo sẵn Template để User có thể tạo máy ảo nhanh chóng.</li>
 <li>Người dùng có thể tạo máy ảo từ ổ đĩa ảo có sẵn.</li>
 <li>Sao lưu máy ảo nhanh chóng bằng tính năng Snapshots.</li>
 </ul>
<a name="cilometer"></a>
####8.Cilometer.

- Cung cấp các dịch vụ từ xa.
- Là dịch vụ giám sát và thống kê.
- Có khả năng tính toán và sử dụng báo cáo.
<a name="heat"></a>
####9. Heat.

- Cung cấp những Template cho những ứng dụng phổ biến.
- Template sẽ mô tả cấu hình các thành phần compute, storage và networking để đáp ứng nhu cầu của ứng dụng.
- Kết hợp với Cilometer để có thể tự điều phối tài nguyên.
<a name="lihc"></a>
###III. Lợi ích và hạn chế khi sử dụng OpenStack.
<a name="lios"></a>
####1. Lợi ích.

- Tiết kiệm chi phí.
- Hiệu suất cao.
- Nền tảng mở.
- Mềm dảo trong việc tương tác.
- Khả năng phát triển và mở rộng cao.
<a name="hcos"></a>
####2. Hạn chế.

- Độ ổn định chưa cao.
- Hỗ trợ đa ngôn ngữ chưa tốt.
- Chỉhỗ trợ kỹ thuật qua chat và Email.

#Nguồn:

- http://www.gensys.com.vn/vi/giai-phap-ao-hoa.html
- http://www.ni.com/white-paper/8709/en/#toc1
-  http://www.ni.com/white-paper/9629/en/
-  http://novaonidc.vn/en/tim-hieu-cong-nghe-dien-toan-dam-may/
-  http://kenhgiaiphap.vn/Detail/880/Cac-mo-hinh-trien-khai-Cloud-Computing.html
-  https://opensource.com/resources/what-is-openstack
-  http://kipalog.com/posts/OpenStack-la-gi-va-de-lam-gi
