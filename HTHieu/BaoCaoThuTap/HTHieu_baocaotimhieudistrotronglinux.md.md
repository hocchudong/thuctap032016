#Báo cáo tìm hiểu các loại Distro trên Linux
##Mục lục
[I.Tổng quan](#tq)

[II. Ubuntu](#ubuntu)

===============
<a name="tq"></a>
## I.Tổng quan

`Linux` là tên hệ điểu hành và cũng là tên hạt nhân của nó, ví dụ nổi tiếng của phần mềm tự do và mã nguồn mở
được viết bởi `Linus Torvalds` vào năm 1991. Hiện nay `Linux` làm hệ điều hành cho các siêu máy tính, máy chủ, để phát triển web, dịch vụ đám mây...
`Linux` có nhiều phiên bản khác nhau gọi là `Distro` hiện nay tính đến 5/9/2015

<img src=http://i.imgur.com/KQAYzEs.png>


- Phân loại các `distro Linux` chủ yếu dự trên 2 tiêu chí:
<ul>
<li>Thị trường mà `distro` muốn nhắm đến ví dụ: máy chủ, doanh nghiệp hay cá nhân</li>
<li>Tùy thuộc vào triết lí phần mềm của từng distro mà những người phát triển quyết định gắn bó lâu dài với distro đó hay không.</li>
</ul>

- Các `distro` phổ biến hiện và phát triển bền vững hiện nay có thể chia làm 4 nhóm:
<ul>
<li> (1) Arch (archlinux.org), Gentoo (gentoo.org), Slackware (slackware.com): Các distro nhắm vào người dùng am hiểu về hệ thống Linux. 
Hầu hết phương thức xây dựng và cấu hình hệ thống đều phải thực hiện qua môi trường dòng lệnh.</li>
<li> (2) Debian (debian.org), Fedora (fedoraproject.org): Các distro cũng nhắm vào những người dùng am hiểu hệ thống, tuy nhiên cung cấp nhiều công cụ hơn cho những người chưa thật sự hiểu rõ hoàn toàn về Linux. 
Nhóm này tương đối thân thiện với người dùng mới bắt đầu hơn nhóm (1). 
Tuy nhiên, các distro nhóm này lại có một quy trình phát triển và kiểm tra chất lượng các gói phần mềm cực kì khắt khe so với các distro còn lại. 
Để trở thành một lập trình viên chính thức của Debian hay Fedora cần phải có thời gian đóng góp khá dài, và phải được chứng nhận bởi các lập trình viên khác. 
Do vậy, môi trường để lập trình và nghiên cứu ở 2 distro này khá tốt.</li>
<li> (3) Centos (centos.org), RHEL (redhat.com/rhel), SUSE EL (novell.com/linux): Các distro này chủ yếu nhắm vào thị trường doanh nghiệp, cơ quan, thị trường máy chủ… Các dòng distro này có nhiều đặc tính phù hợp cho mảng thị trường đòi hỏi sự ổn định cao như: thời gian ra phiên bản mới thường khá lâu (3 - 5 năm tùy distro); dịch vụ hỗ trợ thương mại cho các công ty, tổ chức sử dụng sản phẩm; ít sử dụng các công nghệ mới nhất (thường kém ổn định) mà tập trung phát triển trên các công nghệ lâu đời và đáng tin cậy hơn.</li>
<li> (4) Ubuntu (ubuntu.com), Open SUSE (opensuse.org): Nhóm các distro nhắm đến người dùng đầu cuối và người mới bắt đầu sử dụng Linux. Đặc tính của các distro này là thời gian phát hành ngắn, ứng dụng liên tục các công nghệ mới với nhiều công cụ đồ họa để cấu hình hệ thống, thiết kế với mục đích dễ dùng, dễ làm quen, không cần đọc tài liệu đối với người mới. </li>
</ul>

- Triết lí phần mềm (`software philosophy`): nó chỉ đơn giản là bộ các quy tắc, định hướng, mục tiêu mà những người phát triển một phần mềm đặt ra hay đi theo triết lí do người khác đặt ra để phát triển sản phẩm của mình nhưng phải tuân thủ theo các triết lí đó. 
Ví dụ triết lí của Microsoft Windows là dễ sử dụng, ít cấu hình thì triết lí của Mac OS X lại là bóng bẩy, thanh lịch... 
Các distro Linux cũng có những triết lí riêng ví dụ: Nhóm (1) là cấu trúc gọn nhẹ, uyển chuyển để có thể xây dựng một hệ thống hoàn toàn tuân theo ý của mình. 
Nhóm (2) lại nhắm đến việc chuẩn hóa, chuyên môn hóa quá trình phát triển phần mềm nhằm tạo ra một hệ thống hoạt động nhịp nhàng, ăn khớp và hạn chế lổ hỗng bảo mật.
Nhóm (3) phát triển theo hướng bền vững, chuyên nghiệp, cung cấp dịch vụ hỗ trợ dài hạn, cung cấp sản phẩm có vòng đời kéo dài (lên tới 7 năm). 
Nhóm (4) cung cấp những công nghệ mới nhất, những hiệu ứng đồ họa bắt mắt ngay sau khi cài đặt, không cần phải cấu hình nhiều…

<a name="ubuntu"></a>
## II.Ubuntu
 
- `Ubuntu`là một trong những `Distro Linux` phổ biến nhất hiện nay phát triển dựa trên một `distro` khác là `Debian GNU/Linux` để tận dụng hệ thống quản lý gói APT của `Debian`. `Ubuntu` do `Mark Shuttleworth` cùng cộng đồng sáng lập và do công ty Canonical tài trợ.

- `Ubuntu`là một hệ điều hành mã nguồn mở nhắm đến người dùng đầu cuối và người mới bắt đầu sử dụng Linux có nghĩa là người dùng tự do sao chép, nghiên cứu, thay đổi, cải tiến theo diều khoản giấy phép GNU GPL, hoàn toàn miễn phí, là `distro` phổ biến nhất hiện nay

- `Ubuntu`có tinh bảo mật cao, nhanh nhẹ, có giao diện đẹp, thân thiên, dễ dùng, có kho phần mềm phong phú, ổn dịnh, dễ cài đặt, cập nhật thường xuyên cho người dùng

- Phiên bản thông thường của `Ubuntu` đặt tên theo dạng dạng YY.MM (tên), trong đó Y tương ứng với năm phát hành, và MM tương ứng với tháng phát hành.

 Mỗi phiên bản Ubuntu thông thường được hỗ trợ trong vòng 9 tháng, chúng cũng được phát hành định kỳ 6 tháng 1 lần và việc nâng cấp lên phiên bản mới hoàn toàn miễn phí. Người dùng được khuyến khích nâng cấp lên phiên bản mới để có thể sử dụng các tính năng mới nhất mà ứng dụng cung cấp. Phiên bản Ubuntu chính thức mới nhất hiện tại là Ubuntu 15.04 (Vivid Vervet), phát hành tháng 4 năm 2015.

- Phiên bản hỗ trợ lâu dài của `Ubuntu` cũng có những phiên bản hỗ trợ dài hạn "Long Term Support", hỗ trợ trong vòng 3 năm đối với máy tính để bàn và 5 năm đối với máy chủ

- Ngoài ra `Ubuntu` còn một nhánh khác  tên mã là `Grumpy Groundhog`. Nó luôn là nhánh phát triển và kiểm tra các bản không ổn định, kết thúc việc kiểm duyệt mã nguồn của nhiều phần mềm và ứng dụng để sau đó chúng được phân phối như một phần của `Ubuntu`. Điều này cho phép những người dùng có khả năng và các nhà phát triển kiểm tra các phiên bản mới nhất của từng phần mềm riêng lẻ khi chúng vừa xuất hiện trong ngày, mà không cần phải tự tạo các gói; việc này giúp đưa ra những cảnh báo sớm về lỗi đóng gói trên một số kiến trúc nền. Bản Grumpy Groundhog chưa bao giờ được công bố.

- `Ubuntu` còn các phân phối cả chình thức và không chính thức :
<ul>
<li>Chính thức:</li>
<ul>
<li>`Kubuntu`, bản phân phối Ubuntu sử dụng môi trường làm việc `KDE`.</li>
<li>`Lubuntu`, phiên bản gọn nhẹ, được khuyên dùng cho các máy tính cũ, có cấu hình không cao. Lubuntu sử dụng `LXDE`.</li>
<li>`Xubuntu`, bản phân phối với giao diện mặc định là `Xfce`.</li>
<li>`Mythubuntu` dành cho hệ thống `MythTV`, thích hợp cho giải trí gia đình.</li>
<li>`Ubuntu Studio` phục vụ cho việc chỉnh sửa video và âm thanh chuyên nghiệp, bao gồm nhiều phần mềm chỉnh sửa đa phương tiện.</li>
</ul>
<li>Không chính thức:</li>
<ul>
<li>Nhờ tính thân thiện và dễ sử dụng mà `Ubuntu` đã được dùng làm cơ sở cho rất nhiều bản phân phối Linux khác nhau. Trong đó, được sử dụng rộng rãi nhất là `Linux Mint`, một bản phân phối hướng tới người mới làm quen với hệ điều hành `Linux`, sử dụng hai môi trường làm việc truyền thống là `Cinnamon` và `MATE` trong phiên bản chính. Ngoài ra, còn có nhiều bản phân phối với các lựa chọn phần mềm, giao diện đồ hoạ khác nhau như `elementary OS, Netrunner, Moon OS, Peppermint OS, Trisquel`...</li>
</ul>
</ul>

- `Ubuntu` có thể cài từ đĩa cứng hay bản mềm iso hay thậm chí chạy thẳng không cần cài đặt trên các thiết bị lưu thữ ngoài có lưu phần cài đặt như `usb`,...



