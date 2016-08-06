# Software-defined Networking và OpenFlow
# Mục lục
<h3><a href="#sdn">1. Software-defined Networking (SDN)</a></h3>
<ul>
    <li><a href="#sdnconcept">1.1 Định nghĩa SDN</a></li>
    <li><a href="#sdnarch">1.2. Kiến trúc hệ thống của SDN</a></li>
</ul>
<h3><a href="#openflow">2. OpenFlow Protocol</a></h3>
<h3><a href="#ref">3. Tham khảo</a></h3>

---

<h2><a name="sdn">1. Software-defined Networking (SDN)</a></h2>
<ul>
    <li><h3><a name="sdnconcept">1.1. Định nghĩa SDN</a></h3>
    Software-Defined Networking (SDN) là kiến trúc mạng linh động, dễ dàng quản lý, hiệu quả về chi phí, có khả năng đáp ứng cao, lý tưởng cho các ứng dụng đòi hỏi băng thông lớn và có tính năng động cao. Kiến trúc này tách biệt hai cơ chế đang tồn tại trong kiến trúc mạng hiện tại là cơ chế điều khiển (control plane) và cơ chế chuyển tiếp (dataplane), cho phép phần điều khiển có khả năng lập trình được và hạ tầng bên dưới trở nên trừu tượng với các ứng dụng và các dịch vụ mạng. Các đặc tính trong kiến trúc của SDN: 
    <ul>
        <li><b>Khả năng lập trình trực tiếp: </b>Việc điều khiển network được lập trình trực tiếp bởi nó đã được tách biệt với các chức năng chuyển tiếp</li>
        <li><b>Nhanh chóng: </b>Việc tách biệt các chức năng điều khiển và chức năng chuyển tiếp cho phép các nhà quản trị linh hoạt trong việc điều chỉnh luồng lưu lượng của network khi có yêu cầu thay đổi</li>
        <li><b>Quản lý tập trung: </b>Việc điều khiển tập trung được thực hiện bởi SDN Controller(một phần mềm) duy trì khung nhìn toàn cục về mạng</li>
        <li><b>Việc cấu hình lập trình được: </b>SDN cho phép người quản lý mạng cấu hình, quản lý, thiết lập bảo mật, tối ưu hóa tài nguyên mạng nhanh chóng nhờ có các chương trình hỗ trợ SDN đã tự động hóa, những chương trình đó hoàn toàn có thể tự lập trình được mà không phụ thuộc vào phần mềm.</li>
        <li><b>Cung cấp các tiêu chuẩn mở: </b>Khi triển khai thông qua các tiêu chuân mở, SDN đã đơn gian hóa việc thiết kế mạng và vận hành bởi vì các chỉ dẫn được cung cấp bởi SDN controller thay vì các giao thức hay các thiết bị chuyên biệt của các nhà cung cấp.</li>
    </ul>
    <br><br>
    <img src="https://www.opennetworking.org/images/stories/sdn-resources/meet-sdn/sdn-3layers.gif">
    <br><br>
    </li>

    <li><h3><a name="sdnarch">1.2. Kiến trúc hệ thống của SDN</a></h3>
    <br><br>
    <img src="http://www.cisco.com/c/dam/en_us/about/ac123/ac147/images/ipj/ipj_16-1/161_sdn_fig01_sm.jpg">
    <br><br>

    Theo Open Networking Foundation, kiến trúc của SDN bao gồm bao lớp tách biệt truy cập thông qua các APIs mở:
    <ul>
        <li><b>Lớp ứng dụng: </b>bao gồm các ứng dụng của người dùng cuối sử dụng các dịch vụ truyền thông qua SDN. Ranh giới giao tiếp giữa lớp ứng dụng và lớp điều khiển được thực hiện bởi northbound API.</li>
        <li><b>Lớp điều khiển (SDN control plance): </b>cung cấp chức năng quản lý tập trung làm nhiệm vụ quản lý việc chuyển tiếp trong mạng thông các các open interfaces. Các chức năng này bao gồm: định tuyến, khai báo tên, chính sách và thực hiện kiểm tra vấn đề bảo mật.</li>
        <li><b>Lớp cơ sở hạ tầng (SDN data plane): </b>bao gồm các thiết bị mạng cung cấp chức năng chuyển mạch và forward các gói tin.</li>

    </ul>
    SDN Controller định nghĩa nên các luồng dữ liệu trong SDN Data plane. Mỗi luồng đi qua mạng trước hết phải lấy thông tin về quyền hạn trên controller, để chứng thực các giao tiếp được phép thực hiện quy định bởi network policy. Nếu controller cho phép một luồng đi qua mạng, nó sẽ tính toán đường đi cho luồng dữ liệu này, và bổ sung một entry tương ứng với flow đó trong mỗi switch trên đường đi đã tính toán. Nhờ có controller xử lý rất nhiều các chức năng phức tạp, các switch đơn giản hơn trong việc quản lý các flow tables mà các entry của các table này chỉ được tính toán bởi controller. Việc truyền thông giữa controller và các switch sử dụng một giao thức chuẩn (Openflow) và southbound API.
    <br>
    Kiến trúc SDN nổi bật về sự linh hoạt, nó có thể vận hành với nhiều loại switch và nhiều lớp giao thức khác nhau. Các SDN Controller và các switch có thể được triển khai cho các Switch layer 2, các router, chuyển mạch giao vận hoặc chuyển mạch và định tuyến lớp ứng dụng.
    <br>
    </li>

</ul>

<h2><a name="openflow">2. OpenFlow</a></h2>
<div>
    Khái niệm SDN đặt ra 2 vấn đề khi triển khai thực tế:
    <ul>
        <li>Cần phần có một kiến trúc logic chung cho tất cả các switch, router và các thiết bị mạng khác được quản lý bởi SDN Controller. Kiến trúc này có thể được triển khai bằng nhiều cách khác nhau trên các thiết bị của các nhà cung cấp khác nhau và phụ thuộc vào nhiều loại thiết bị mạng, miễn là SDN controller thấy được chức năng chuyển mạch thống nhất</li>
        <li>Một giao thức chuẩn, bảo mật để giao tiếp giữa SDN controller và các thiết bị mạng</li>
    </ul>
    OpenFlow được đưa ra để giao quyết cả hai vấn để đó.
    <ul>
        <li><h3><a name="" ="">2.1. Kiến trúc logical của OpenFlow Switch</a></h3>
                <br><br>
        <img src="http://www.cisco.com/c/dam/en_us/about/ac123/ac147/images/ipj/ipj_16-1/161_sdn_fig03_sm.jpg">
        <br><br>
        Mỗi switch kết nối với các OpenFlow switch khác và kết nối với các thiết bị của người dùng cuối là nguồn và đích của luồng dữ liệu. 
        Một OpenFlow switch bao gồm ít nhất ba thành phần:
        <ul>
            <li><b>Flow table: </b> có trách nhiệm "nói chuyện" với switch để chỉ ra rằng phải xử lý flow ra sao, mỗi hành động tương ứng với 1 <b>flow-entry.</b></li>
            <li><b>Secure Channel: </b> kết nối switch với controller sử dụng giao thức OpenFlow chạy qua Secure Sockets Layer (SSL), để gửi các <b>commands</b> và các <b>packets</b>.</li>
            <li><b>OpenFlow Protocol</b></li>
        </ul>
        <br>      
        <h4>Flow table</h4>  .
        Có ba loại tập hợp các flow tables:
        <ul>
            <li>Một <b>flow table</b> sẽ ghép các gói tin tới với một flow nhất định và chỉ định các chức năng được thực hiện trên các gói tin đó. Có thể có nhiều flow tables vận hành trong một pipeline.  </li>
            <li>Một flow table có để chuyển một luồng vào một <b>Group Table</b>, tại đó có thể kích hoạt cùng một lúc nhiều hành động ảnh hưởng tới một hoặc nhiều flow.</li>
            <li>Một <b>Meter Table</b> có thể kích hoạt nhiều hành động liên quan tới hiệu năng trên một flow.</li>
        </ul>
        <i>Chú ý: Khái niệm <b>flow</b> không được định nghĩa trong đặc tả của OpenFlow. Hiểu một cách đơn giản, một flow là một chuỗi các gói tin đi qua một mạng mà có chung một tập các giá trị trường header. Ví dụ, một flow có thể bao gồm tất cả các gói tin với cùng địa chỉ nguồn và địa chỉ đích, hoặc tất cả các gói tin có cùng VLAN id.</i>
        <h4>Flow-entry</h4>
        <div>
            Mỗi <b>flow-entry</b> trong <b>flow table</b> có một hành động tương ứng với nó và gồm 3 trường:
            <ul>
                <li><b>Packet header</b> định nghĩa nên flow</li>
                <li><b>Hành động (Action)</b> định nghĩa cách mà gói tin sẽ được xử lý</li>
                <li><b>Thống kê (Statistics)</b> giữ thông tin theo dõi về số lượng gói tin và kích thước theo bytes của mỗi flow, thời gian kể từ lúc gói tin cuối đưa vào flow (nhằm mục đích loại bỏ các flow đã ngừng hoạt động).</li>
            </ul>
            Mỗi <b>flow-entry</b> có một hành động tương ứng với nó, và có ba loại hành động cơ bản:
            <ul>
                <li>Chuyển các gói tin của một flow tới port (hoặc các port) đã chỉ định. Điều này cho phép các gói tin được định tuyến qua mạng.</li>
                <li>Đóng gói và chuyển tiếp các gói tin của flow tới controller. Gói tin sẽ được đưa tới <b>Secure Channel</b>, tại đó nó được đóng gói và gửi tới controller. Điển hình như gói tin đầu tiên của mỗi flow mới sẽ được gửi tới controller để được quyết định xem liệu flow có được đưa vào trong <b>flow table</b> hay không.</li>
                <li>Hủy các gói tin của flow. Hành động này được sử dụng nhằm mục đích bảo mật, như tấn công từ chối dịch vụ (DoS).</li>
            </ul>
        </div>
        </li>

        <li><h3><a name="ofp">2.2. OpenFlow Protocol</a></h3>
        Giao thức OpenFlow mô tả bản tin trao đổi giữa OpenFlow Controller và một OpenFlow switch. Giao thức này được triển khai trên Secure Socket Layer (SSL) hoặc Transport Layer Security (TLS), cung cấp kênh OpenFlow bảo mật. Giao thức OpenFlow cho phép controller thực hiện các thao tác bổ sung, cập nhật và xóa các hành động vào các flow entry trong các flow tables. Nó hỗ trợ 3 loại bản tin:
        <ul>
            <li>
                <h4>Controller-to-Switch</h4>
                Các bản tin này được khởi tạo bởi controller, có thể yêu cầu hoặc không yêu cầu phản hồi từ switch. Lớp bản tin này cho phép controller quản lý các trạng thái logic của switch, bao gồm cấu hình và chi tiết về các flow entry trong flow table hoặc group table. Ngoài ra, nó cũng bao gồm các bản tin Packet-out (bản tin đi tới một port nhất định trên switch). Bản tin này được sử dụng khi switch gửi một packet tới controller và controller sẽ quyết định không hủy gói nhưng sẽ chuyển hướng tới một output port của switch.
            </li>

            <li>
                <h4>Asynchronous</h4>
                Các bản tin loại này được gửi mà không có yêu cầu từ controller. Lớp các bản tin này bao gồm nhiều bản tin trạng thái khác nhau gửi tới controller. Ngoài ra lớp này còn bao gồm các bản tin packet-in - các packet không phù hợp với flow table nào, và như vậy các bản tin đó sẽ được gửi tới controller để xử lý.
            </li>

            <li>
                <h4>Symmetric</h4>
                Các bản tin này được gửi đi mà không có yêu cầu cả từ controller và switch, bao gồm các bản tin:
                <ul>
                    <li><b>Hello: </b>là bản tin trao đổi giữa switch và controller dựa trên kết nối đã được đã được thiết lập.</li>
                    <li><b>Echo: </b>các bản tin <b>echo request/reply</b> có thể được gửi từ switch hoặc controller, và chúng sẽ phải trả về một bản tin echo reply.</li>
                    <li><b>Experimenter: </b>Các bản tin cho các chức năng bổ sung</li>
                </ul> 
            </li>
        </ul> 
        Giao thức OpenFlow cho phép controller quản lý cấu trúc logic của switch mà không liên quan tới chi tiết việc switch triển khai kiến trúc OpenFlow ra sao.
        </li>
    </ul>
</div>

<h2><a name="ref">3. Tham khảo</a></h2>
<div>
    [1] - <a href="http://www.cisco.com/c/en/us/about/press/internet-protocol-journal/back-issues/table-contents-59/161-sdn.html">http://www.cisco.com/c/en/us/about/press/internet-protocol-journal/back-issues/table-contents-59/161-sdn.html</a>
    <br>
    [2] - <a href="https://www.opennetworking.org/sdn-resources/sdn-definition">https://www.opennetworking.org/sdn-resources/sdn-definition</a>
</div>