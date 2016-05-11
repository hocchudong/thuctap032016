# Tìm hiểu các distro linux
## Mục lục
<ul style="list-style: none; font-size: 18px">
<li><h3><a href="#intro">1. Giới thiệu hệ điều hành linux</a></h3></li>
<li><h3><a href="#distro">2. Các loại distro linux</a></h3>
<ul style="list-style: none">
<li><h4><a href="#debian">a. Debian và các distro Debian-based</a></h4></li>
<li><h4><a href="#rpm">b. Các distro RPM-based</a></h4></li>
<li><h4><a href="#pacman">c. Các distro Pacman-based</a></h4></li>
<li><h4><a href="#arm">d. Các distro dành cho kiến trúc ARM</a></h4></li> 
<li><h4><a href="#em">e. Các distro dành cho hệ thống nhúng</a></h4></li> 
</ul>
</li>
</ul>

---

<ul style="list-style: none; font-size: 18px">
<li><h3><a name="intro">1. Giới thiệu hệ điều hành linux</a></h3>
	<p style="text-align: justify">
    	Linux là một hệ điều hành máy tính dựa trên Unix được phát triển và phân phối qua mô hình phần mềm tự do mã nguồn mở. Thành phần cơ bản tạo nên Linux đó là nhân linux, một nhân hệ điều hành ra đời bản đầu tiên vào tháng 8 năm 1991 bởi Linus Torvalds. Nhiều người gọi Linux là GNU/Linux, lý do là bản thân linux chỉ là phần nhân hệ điều hành. Rất nhiều phần mềm, ứng dụng khác như hệ thống đồ họa, trình biên dịch, soạn thảo, các công cụ phát triển cũng cần được gắn vào nhân để tạo nên một HĐH hoàn chỉnh. Hầu hết những phần mềm này được phát triển bởi cộng đồng GNU.
    	<br>
        Linux có rất nhiều bản phân phối khác nhau(distro), có cả các bản phát hành chính thức hoặc do người dùng tự build nên. Một bản phân phối linux (distro) là khái niệm chỉ hệ điều hành được xây dựng nên từ Linux kernel và hệ thống quản lý gói phần mềm (package management), cũng như các thư viện và các gói phần mềm. Ta có thể phân chia các distro linux thành một số loại được trình bày dưới đây.
    </p>
</li>
<li><h3><a name="distro">2. Các loại distro linux</a></h3>
<ul style="list-style: none">
<li><h4><a name="debian">a. Debian và các distro Debian-based</a></h4>
<ul style="list-style: circle">
<li>Các distro tiêu biểu: Debian, Ubuntu, Knoppix, Linux Mint, Kali, etc.</li>
<li>Debian là một trong các distro phổ biến, có ảnh hưởng lớn tới nhiều distro khác. Một số thông tin cơ bản về Debian và các bản phân phối Debian-based: 
<ul list-style="square">
<li>Công ty/Nhà phát triển: Debian Project</li>
<li>Họ: Unix, Linux</li>
<li>Kiểu mã nguồn: Phần mềm tự do</li>
<li>Phát hành lần đầu: 16 tháng 8, 1993</li>
<li>Phương thức cập nhật và cài đặt phần mềm: APT (Advanced Package Tool)</li>
<li>Quản lý gói cài đặt: dpkg</li>
<li>Nền tảng hỗ trợ: i386, amd64, PowerPC, SPARC, DEC Alpha, ARM, MIPS, PA-RISC, S390, IA-64</li>
<li>Kiểu nhân: Đơn khối (nhân Linux, FreeBSD, NetBSD), Micro (Hurd)</li>
<li>Giao diện người dùng mặc định: GNOME, KDE, Xfce, và LXDE</li>
<li>Giấy phép: Chủ yếu là GNU GPL và các giấy phép khác</li>
<li>Phạm vi áp dụng: dành cho cả người dùng desktop và server (tùy vào bản phân phối)</li>
</ul>
Có nhiều distro Linux được phát triển dựa trên Debian (các bản phân phối thứ cấp), như: Ubuntu, Knoppix, Linux Mint, Kali, Matriux,...
</li>
</ul>
</li>
<li><h4><a name="rpm">b. Các distro RPM-based</a></h4>
<ul style="list-style: circle">
<li>Các distro tiêu biểu: Red Hat, Fedora, CentOS,  Mandriva, SUSE</li>
<li>Một số thông tin cơ bản về các distro RPM-based
<ul style="list-style: square">
<li>Phương thức cài đặt và cập nhật: yum, dnf (RedHat, Fedora, CentOS),   Zypper và  YaST (SUSE)</li>
<li>Quản lý gói cài đặt: rpm</li>
<li>Phạm vi sử dụng: desktop, server</li>
<li>Giao diện người dùng; GNOME, KDE, Cinamon, Xfce, etc.</li>
</ul>
</li>
</ul>
</li>
<li><h4><a name="pacman">c. Các distro Pacman-based</a></h4>
<ul style="list-style: circle">
<li>Các distro đại diện: Arch Linux, Antergos, ArchBang, Chakra, etc.</li>
<li>Quản lý gói cài đặt: pacman</li>
<li>Giao diện người dùng: OpenBox, Xfce4</li>
<li>Arch Linux và một số distro tương tự sử dụng pacman là các hệ thống phát hành quay vòng (rolling release), trong đó các gói phần mềm sẽ được cập nhật liên tục version mới nhất từ nhà sản xuất (upstream), khác với các distro deb-base và rpm-base có repo bị đóng băng theo từng phiên bản.</li>
</ul>
</li>
<li><h4><a name="arm">d. Các distro dành cho kiến trúc ARM</a></h4>
<ul style="list-style: circle">
     <li>Các distro tiêu biểu: Raspbian, Arch Linux ARM</li>
     <li>Các distro dạng này khá "nhẹ", vì chủ yếu áp dụng cho các kit phát triển cấu hình thấp như Rasspberry PI để phục vụ lập trình phần cứng, xử lý ảnh, xây dựng hệ thống IoT, etc.</li>
</ul>
</li> 
<li><h4><a name="em">e. Các distro dành cho hệ thống nhúng</a></h4>
<ul style="list-style: circle">
     <li>Các distro tiêu biểu: Android, Firefox OS, Ubuntu Touch, Sailfish OS</li>
</ul>
</li> 
</ul>
</li>
</ul>
