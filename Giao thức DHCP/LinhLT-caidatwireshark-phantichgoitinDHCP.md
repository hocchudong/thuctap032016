#Wireshark - Thực hành bắt và phân tích gói tin.

#Mục lục
* [1. Tìm hiểu Wireshark](#wireshark)
	* [1.1. Giới thiệu](#gioi_thieu)
	* [1.2. Một số tính năng nâng cao của Wireshark](#tinh_nang_nang_cao)
	* [1.3 Hướng dẫn sử dụng wireshark](#su_dung)
* [2. Dùng wireshark để bắt gói tin DHCP](#wireshak_bat_goi_tin)
	* [2.1 Mô hình](#mo_hinh)
	* [2.2 Cấu hình máy tính nhận ip động.](#ip_dong)
	* [2.3 Sử dụng wireshark bắt gói tin.](#bat_goi_tin)
	* [2.4 Phân tích gói tin.](#phan_tich_goi_tin)
		* [2.4.1 Lọc gói tin DHCP](#loc_goi_tin)
		* [2.4.2. Gói tin DHCP Release](#dhcp_release)
		* [2.4.3. Gói tin DHCP discovery](#dhcp_discorery)
		* [2.4.4 Gói tin DCHP offer](#dhcp_offer)
		* [2.4.5 Gói tin DHCP Request](#dhcp_request)
		* [2.4.6 Gói tin DHCP ACK](#dhcp_ack)
* [3. Tài liệu tham khảo](#tham_khao)

<a name="wireshark"></a>
#1. Tìm hiểu Wireshark

<a name="gioi_thieu"></a>
##1.1. Giới thiệu:
* Wireshark là một công cụ kiểm tra, theo dõi và phân tích thông tin mạng.
* Các tính năng cơ bản của wireshark
	* Wireshark thân thiện với người dùng: wireshark có cửa sổ giao diện rất dễ sử dụng.
	* Wireshark là một phần mềm hoàn toàn miễn phí và mã nguồn mở.
	* Wireshark hỗ trợ hầu hết các hệ điều hành hiện nay.
	* Wireshark hỗ trợ hầu hết các giao thức hiện nay, kể cả những giao thức đặc biệt như apple talk hay bit torrent.

<a name="tinh_nang_nang_cao"></a>
##1.2. Một số tính năng nâng cao của Wireshark:
* Giao diện tổng quát: có 5 phần chính

![](https://farm8.staticflickr.com/7579/16011145562_eae3b825fc_o.png)

	* Các Tùy chỉnh nằm ở phía trên của cửa sổ. Mối quan tâm của chúng ta hiện nay là các tập tin và Capture. Các menu File cho phép bạn lưu dữ liệu gói tin bị bắt hoặc mở một tập tin có chứa các gói dữ liệu bị bắt từ trước, và thoát khỏi ứng dụng Wireshark. Menu Capture cho phép bạn bắt đầu bắt gói tin.
	* Cửa sổ danh sách gói tin hiển thị một bản tóm tắt một dòng cho mỗi gói tin bị bắt, tại thời điểm mà các gói tin bị bắt, nguồn và địa chỉ đích của gói tin, các loại giao thức, và thông tin giao thức cụ thể có trong các gói tin. Danh sách này có thể được sắp xếp theo tùy chỉnh của mỗi loại bằng cách nhấp vào một tên cột. Các loại trường giao thức liệt kê các giao thức cấp cao nhất mà gửi hoặc nhận được gói tin này.
	* Cửa sổ chi tiết gói tin cung cấp chi tiết về các gói lựa chọn. Những chi tiết này bao gồm thông tin về các khung Ethernet (giả sử các gói đã được gửi/nhận trên một cổng Ethernet) và IP gói tin. Số lượng Ethernet và IP lớp chi tiết hiển thị có thể được mở rộng hoặc giảm thiểu bằng cách nhấp vào biểu tượng cộng hoặc trừ bên trái của khung Ethernet hoặc IP trong cửa sổ chi tiết gói tin. Nếu gói dữ liệu đã được thực hiện trên TCP hoặc UDP, chi tiết về TCP hoặc UDP cũng sẽ được hiển thị, tương tự mà có thể mở rộng hoặc thu nhỏ. Cuối cùng, chi tiết về các giao thức cấp cao nhất mà gửi hoặc nhận được gói tin này cũng được cung cấp.
	* Cửa sổ nội dung gói tin: hiển thị toàn bộ nội dung của khung hình chụp, trong cả hai định dạng mã ASCII và định dạng mã Hex.
	* Phía trên cùng của giao diện người dùng đồ họa Wireshark, là màn hình hiển thị kỹ thuật lọc gói tin, mà trong đó một tên giao thức hoặc các thông tin khác có thể được nhập vào đặt để lọc các thông tin hiển thị trong cửa sổ (và do đó các gói tiêu đề và gói nội dung cửa sổ).

* Name Resolution: 
    * Dữ liệu truyền trong mạng thông qua một vài hệ thống địa chỉ, các địa chỉ này thường dài và khó nhớ (Ví dụ: MAC). Phân giải điạ chỉ là quá trình mà một giao thức sử dụng để chuyển đổi một địa chỉ loại này thành một địa chỉ loại khác đơn giản hơn.
	* Các kiểu công cụ phân giải tên trong Wireshark: có 3 loại
		* MAC Name Resolution: phân giải địa chỉ MAC tầng 2 sang địa chỉ IP tầng 3.
    	* Network Name Resolution: chuyển đổi địa chỉ tầng 3 sang một tên DNS dễ đọc như là MarketingPC1.
    	* Transport Name Resolution: chuyển đổi một cổng sang một tên dịch vụ tương ứng với nó, ví dụ: cổng 80 là http.
* Protocol Dissection: 
	* Một protocol dissector cho phép Wireshark phân chia một giao thức thành một số thành phần để phân tích.
	* Wireshark sử dụng đồng thời vài dissector để phiên dịch mỗi gói tin.
	* Nó quyết định dissector nào được sử dụng bằng cách sử dụng phân tích lôgic đã được cài đặt sẵn và thực hiện việc dự đoán.

* Following TCP Streams: 
	* Một trong những tính năng hữu ích nhất của Wireshark là khả năng xem các dòng TCP như là ở tầng ứng dụng.
	* Tính năng này cho phép bạn phối hợp tất cả các thông tin liên quan đến các gói tin và chỉ cho bạn dữ liệu mà các gói tin này hàm chứa giống như là người dùng cuối nhìn thấy trong ứng dụng.
	* Để sử dụng tính năng này, bạn click chuột phải vào 1 gói packet, chọn Follow TCP Stream

	![](http://ksec.info/attachments/tcpfollow1-png.454)

* Cửa sổ thống kê phân cấp giao thức
	* Khi bắt được một file có kích thước lớn, chúng ta cần biết được phân bố các giao thức trong file đó, bao nhiêu phần trăm là TCP, bao nhiêu phần trăm là IP và DHCP là bao nhiêu phần trăm,... Thay vì phải đếm từng gói tin để thu được kết quả, chúng ta có thể sử dụng cửa sổ thống kê phân cấp giao thức của Wireshark.
	* Để sử dụng tính năng này, bạn chọn menu Statistics > Protocol Hierarchy
	![](http://ksec.info/attachments/tcpfollow-png.455)

* Xem các Endpoints
	* Một Endpoint là chỗ mà kết nối kết thúc trên một giao thức cụ thể. Ví dụ, có hai endpoint trong kết nối TCP/IP: các địa chỉ IP của các hệ thống gửi và nhận dữ liệu, 192.168.1.5 và 192.168.0.8.
	* Để sử dụng tính năng này, bạn chọn menu Statistics > Endpoint List và chọn một giao thức để hiển thị.
	![](http://ksec.info/attachments/picture1-png.457)

* Cửa số đồ thị IO
	* Cách tốt nhất để hình dung hướng giải quyết là xem chúng dưới dạng hình ảnh. Cửa sổ đồ thị IO của Wireshark cho phép bạn vẽ đồ thị lưu lượng dữ liệu trên mạng.
	* Để sử dụng tính năng này, bạn chọn menu Statistics > IO Graph

	![](http://ksec.info/attachments/picture2-png.458)

<a name="su_dung"></a>
##1.3 Hướng dẫn sử dụng wireshark
* Wireshark là một phần mềm hoàn toàn miễn phí, có thể tải về tại http://wireshark.org.
* Để bắt được gói tin, Wireshark phải được cài đặt trên máy tính có kết nối mạng(LAN, mạng ảo, Internet…) đang hoạt động và Wireshark phải chạy trước, trước khi quá trình trao đổi dữ liệu diễn ra.
* Để bắt một gói tin với wireshark. Tại màn hình chính, chọn menu Capture > Interface hoặc nhấn tổ hợp phím Ctrl + I.

![](http://ksec.info/attachments/picture3-png.460)

* Chọn card mạng mà bạn muốn bắt gói tin và nhấn start.

![](http://ksec.info/attachments/picture4-png.461)

* Cửa sổ hiển thị các gói tin gồm 3 phần:

![](http://ksec.info/attachments/picture5-png.462)

    * Phần danh sách các gói tin: hiển thị tất cả các gói tin đã bắt được, kèm theo thông tin vắn tắt của mỗi gói tin.
    * Phần “Các phần của gói tin đang chọn” sẽ hiển thị các giao thức, các trường của mỗi giao thức. Các trường được tổ chức theo cấu trúc cây, có thể mở rộng hoặc thu gọn cấu trúc cây để tiện quan sát.
    * Khi bấm vào mỗi gói tin trong phần “Danh sách các gói tin”, nội dung của gói tin dưới dạng hệ số16 sẽ được hiển thị tại phần “Nội dung dạng hex của gói tin”.

* Để kết thúc quá trình bắt gói tin, bạn nhấn vào nút stop trên thanh công cụ hoặc vào menu Capture > Stop.

<a name="wireshark_bat_goi_tin"></a>
#2. Dùng wireshark để bắt gói tin DHCP

<a name="mo_hinh"></a>
##2.1 Mô hình

![](http://i.imgur.com/MFNLds4.jpg)

* Router đồng thời là Wifi access point, đóng vai trò dhcp server, kết nối đến nhà cung cấp dịch vụ internet.
* Laptop đóng vai trò dhcp client, kết nối với router thông qua sóng wifi.
* Địa chỉ mạng: 192.168.1.0/24.
* Địa chỉ router: 192.168.1.1/24.

<a name="ip_dong"></a>
##2.2 Cấu hình máy tính nhận ip động.

![](http://i.imgur.com/FbzrVR8.png)

<a name="bat_goi_tin"></a>
##2.3 Sử dụng wireshark bắt gói tin.
* Chạy wireshark với quyền admin.

![](http://i.imgur.com/BnTpoAt.png)

* Chọn card mạng để bắt gói tin.

![](http://i.imgur.com/NACUwDZ.png)

* Giải phóng địa chỉ IP.

![](http://i.imgur.com/bUMfyrF.png)

* Yêu cầu cấp địa chỉ IP.

![](http://i.imgur.com/PDIOtsY.png)


<a name="phan_tich_goi_tin"></a>
##2.4 Phân tích gói tin.

<a name="loc_goi_tin"></a>
###2.4.1 Lọc gói tin DHCP: Gõ `bootp` vào ô filter.

![](http://i.imgur.com/7I5t0RY.png)

<a name="dhcp_release"></a>
###2.4.2. Gói tin DHCP Release

![](http://i.imgur.com/g07mCHU.png)

<a name="dhcp_discovery"></a>
###2.4.3. Gói tin DHCP discovery

![](http://i.imgur.com/ihuSC2P.png)

Đây là gói tin broadcast gửi từ client đến các servers.

* Trong đó:
	* 1: Card mạng nguồn, địa chỉ MAC nguồn, MAC đích
	* 2: Là tin broadcast. địa chỉ ip nguồn (0.0.0.0) và địa chỉ ip đích (255.255.255.255)
	* 3: Cổng nguồn (68) và cổng đích (67).
	* 4: Địa chỉ IP client trong gói header.
	* 5: Địa chỉ MAC nguồn.
	* 6: IP được client yêu cầu cấp phát.

<a name="dhcp_offer"></a>
###2.4.4 Gói tin DCHP offer

![](http://i.imgur.com/8zFTgxu.png)

![](http://i.imgur.com/k3lmWoO.png)

Đây là gói tin unicast gửi từ server đến client

* Trong đó: 
	* 1: Card mạng nguồn, địa chỉ MAC nguồn, MAC đích
	* 2: Là tin broadcast. địa chỉ ip nguồn (192.168.1.1) và địa chỉ ip đích (192.168.1.45)
	* 3: Cổng nguồn (67) và cổng đích (68).
	* 4: Địa chỉ IP client trong gói header.
	* 5: Định danh dhcp server:chính là ip của server
	* 6: Thời gian cho client thuê
	* 7: Địa chỉ subnetmask.
	* 8: Địa chỉ broadcast.
	* 9: Địa chỉ defalut gateway.
	* 10: Địa chỉ DNS server.

<a name="dhcp_request"></a>
###2.4.5 Gói tin DHCP Request

![](http://i.imgur.com/jM3FiXE.png)

Đây là gói tin broadcast gửi từ client đến các servers.Nó có thêm trường Client Fully Qualified Domain Name trong dhcp header

<a name="dhcp_ack"></a>
###2.4.6 Gói tin DHCP ACK
![](http://i.imgur.com/bGEB7gG.png)

Đây là gói tin unicast gửi từ server đến client để xác nhận lại các thông tin đã cấp cho client

<a name="tham_khao"></a>
#3. Tài liệu tham khảo

* https://github.com/kieulam141/DHCP/blob/master/Capture_wireshark.md
* http://documents.tips/documents/tuan52minh-hoa-phan-tich-goi-tin-dhcp.html
* http://www.conmaz.net/kien-thuc/phan-mem-wireshark.html#
* http://ksec.info/threads/wireshark-bat-va-phan-tich-goi-tin.575/
