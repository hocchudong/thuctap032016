#Báo cáo tìm hiểu về SSH

****
#Mục Lục : 
[I. Tổng quan về giao thức SSH] (#tongquan)
 <ul>
 <li>[1. SSH là gì?] (#whatisssh)</li>
 <li>[2. Lịch sử phát triển] (#history)</li>
 </ul>
[II. Các đặc điểm của SSH] (#dacdiem)
 <ul>
 <li>[1. Tính bí mật.] (#bimat)</li>
 <li>[2. Tính toàn vẹn.] (#toanven)</li>
 <li>[3. Chứng minh xác thực.] (#xacthuc)</li>
 <li>[4. Ủy quyền.] (#giayphep)</li>
 <li>[5. Chuyển tiếp.] (#chuyentiep)</li>
 </ul>
[III. SSH Architecture.] (#architecture)

[IV. Giao thức chứng thực SSH.] (#auth)
 <ul>
 <li>[1. Tiến trình yêu cầu chứng thực.] (#yeucau)</li>
 <li>[2. Tiến trình hồi đáp chứng thực.] (#hoidap)</li>
 <li>[3. Chứng thực khóa công khai.] (#public)</li>
 <li>[4. Xác thực password.] (#password)</li>
 <li>[5. Xác thực dựa trên host (hostbased)] (#hostbased)</li>
 </ul>
[V. Cài đặt SSH trên Ubuntu và cấu hình.] (#settingssh)
 <ul>
 <li>[1. Mô hình triển khai và cách cài đặt.] (#mohinh)</li>
 <li>[2. File cấu hình và ý nghĩa.] (#fileconfig)
  <ul>
  <li>[2.1. Cấu hình SSH chứng thực bằng mật khẩu.] (#authpass)</li>
  <li>[2.2. Cấu hình SSH chứng thực bằng Key.] (#authkey)</li>
  </ul>
 </li>
 </ul>

****
<a name="tongquan"></a>
##I. Tổng quan về giao thức SSH.
<a name="whatisssh"></a>
###1. SSH là gì?

- SSH (tiếng Anh: Secure Shell) là một giao thức mạng dùng để thiết lập kết nối mạng một cách bảo mật. SSH hoạt động ở lớp trên trong mô hình phân lớp TCP/IP. Các công cụ SSH (như là OpenSSH, PuTTy,…) cung cấp cho người dùng cách thức để thiết lập kết nối mạng được mã hoá để tạo một kênh kết nối riêng tư. Hơn nữa tính năng tunneling (hoặc còn gọi là port forwarding) của các công cụ này cho phép chuyển tải các giao vận theo các giao thức khác. Do vậy có thể thấy khi xây dựng một hệ thống mạng dựa trên SSH, chúng ta sẽ có một hệ thống mạng riêng ảo VPN đơn giản.

Mỗi khi dữ liệu được gửi bởi một máy tính vào mạng, SSH tự động mã hoá nó. Khi dữ liệu được nhận vào, SSH tự động giải mã nó. Kết quả là việc mã hoá được thực hiện trong suốt: người dùng có thể làm việc bình thường, không biết rằng việc truyền thông của họ đã được mã hoá an toàn trên mạng.
<a name="history"></a>
###2. Lịch sử phát triển.

- SSH1 và giao thức SSH-1 được trình bày năm 1995 bởi Tatu Ylõnen, một nhà nghiên cứu ở trường đại học kĩ thuật Helsinki của Phần Lan. Sau khi mạng trường đại học của ông ta là nạn nhân của một cuộc tấn công đánh cắp password vào đầu năm đó.
Tháng 7 năm 1995, SSH1 được phát hành rộng rãi dưới dạng một phần mềm miễn phí có source code, cho phép mọi người sao chép và sử dụng mà không thu phí. Vào cuối năm đó, ước tính có khoảng 20.000 người dùng trên 50 quốc gia đã sử dụng SSH1, và mỗi ngày Ylõnen nhận 150 mail yêu cầu hỗ trợ. Để đáp lại, Ylõnen đã thành lập SSH Communications Security (SCS, http://www.ssh.com) vào tháng 12 năm 1995 để duy trì, thương nghiệp hoá và tiếp tục phát triển SSH. 
Cũng trong năm 1995, Ylõnen soạn thảo giao thức SSH-1 còn gọi là Internet Engineering Task Force (IETF), nó diễn tả hoạt động cơ bản của phần mềm SSH1 trên thực tế. Nó là một giao thức có phần quảng cáo nhưng còn một số lỗi và giới hạn nhưng rất phổ biến. Năm 1996, SCS giới thiệu một phiên bản mới đó là phiên bản chính của giao thức, SSH 2.0 hay SSH-2, phiên bản này được kết hợp chặt chẽ những thuật toán mới và không hợp với SSH-1. Trong lúc đó, IETF thành lập một nhóm làm việc gọi là SECSH (Secure Shell) để chuẩn hoá giao thức và chỉ đạo sự phát triển của nó trên lợi ích chung. Nhóm làm việc SECSH đã trình bày bản phác thảo Internet đầu tiên đối với giao thức SSH-2 vào tháng 2 năm 1997.
Năm 1998, SCS phát hành sản phẩm phần mềm “SSH Secure Shell” (SSH2), dựa trên giao thức SSH-2. Tuy nhiên, SSH2 không thay thế SSH1 trong một số lĩnh vực, có 2 lí do. Thứ nhất, SSH2 không có một số tiện ích, các đặc điểm có ích và cấu hình tuỳ chọn như SSH1. Thứ hai, SSH2 có nhiều giới hạn về việc đăng kí. Bản chính SSH1 đã có sẵn miễn phí từ Ylõnen và trường đại học kĩ thuật Helsinki. Phiên bản mới hơn của SSH1 từ SCS vẫn có sẵn miễn phí cho hầu hết người dùng, thậm chí cả cấu hình thương mại cũng miễn phí chỉ cần phần mềm đó không được trực tiếp bán cho việc thu lợi nhuận hoặc được tặng như là một dịch vụ cho khách hàng. Vì thế, tuy SSH2 đã xuất hiện, nhưng hầu hết những người đang sử dụng SSH1 đều nhận ra vài ưu điểm của SSH1 so với SSH2 và tiếp tục sử dụng SSH1, ba năm sau khi SSH2 ra đời thì SSH1 vẫn là phiên bản được sử dụng phổ biến trên Internet và vượt qua cả SSH2 là giao thức tốt hơn và bảo mật hơn.
Tuy nhiên, SSH2 cũng có hai sự phát triển hưa hẹn, đó là một bản nới lỏng của SSH2 bản quyền và sự xuất hiện SSH-2 bổ sung. Năm 2000, SCS mở rộng SSH2 bản quyền để cho phép sử dụng khi làm việc riêng lẻ đối với các tổ chức hoạt động phi lợi nhuận. Nó cũng được mở rộng cho phép dùng miễn phí đối với Linux, NetBSD, FreeBSD và hệ điều hành OpenBSD. Cùng thời gian đó, OpenSSH (http://www.openssh.com) đã được phát triển nổi bật như là một SSH bổ sung, được phát triển dưới hoạt động của dự án OpenBSD (http://www.openbsd.org) và miễn phí sẵn bên dưới OpenBSD có đăng kí. OpenSH hỗ trợ cả SSH-1 và SSH-2 trong một chương trình. Tuy OpenSSH được phát triển trên nền OpenBSD nhưng nó cũng hoạt động được trên Linux, Solais, AIX và những hệ điều hành khác. Mặc dù OpenSSH tương đối mới và không có vài đặc điểm có trong SSH1 và SSH2 nhưng nó đang trên đà phát triển nhanh chóng và hứa hẹn trở thành bản SSH chính trong tương lai không xa.
<a name="dacdiem"></a>
##II. Các đặc điểm của SSH.

**Các đặc điểm chính của giao thức SSH là:**
- Tính bí mật (Privacy) của dữ liệu thông qua việc mã hoá mạnh mẽ
- Tính toàn vẹn (integrity) của thông tin truyền, đảm bảo chúng không bị biến đổi.
- Chứng minh xác thực (authentication) nghĩa là bằng chứng để nhận dạng bên gửi và bên nhận
- Giấy phép (authorization) :dùng để điều khiển truy cập đến tài khoản.
- Chuyển tiếp (forwarding) hoặc tạo đường hầm (tunneling) để mã hoá những phiên khác dựa trên giao thức TCP/IP
<a name="bimat"></a>
###1. Tính bí mật (Privacy).

- Tính bí mật có nghĩa là bảo vệ dữ liệu không bị phơi bày. Mạng máy tính bình thường không bảo đảm tính bí mật, bất cứ ai truy cập đến phần cứng của mạng hoặc đến những host kết nối với mạng đều có thể sẽ đọc được tất cả dữ liệu đi qua mạng. Mặc dù mạng chuyển mạch hiện đại đã giảm những vấn đề này trong mạng vùng cục bộ nhưng nó vẫn còn một vấn đề nghiêm trọng đó là mật khẩu dễ bị những kẻ xấu đánh cắp.
SSH cung cấp tính bí mật bằng việc mã hoá dữ liệu đi qua mạng. Đó là việc mã hoá hai đầu dựa trên khoá ngẫu nhiên (sinh ra để phục vụ cho một phiên kết nối và được huỷ đi khi phiên kết nối thành công). SSH hỗ trợ nhiều thuật toán mã hoá đối với phiên dữ liệu, đó là những thuật toán mã hoá chuẩn như: AES, ARCFOUR, Blowfish, Twofish, IDEA, DES và triple-DES (3DES).
<a name="toanven"></a>
###2. Tính toàn vẹn.

- Tính toàn vẹn nghĩa là bảo đảm dữ liệu được truyền từ một đầu này đến đầu kia của mạng không bị thay đổi. Giao thức SSH sử dụng phương pháp kiểm tra toàn vẹn mật mã, phương pháp này kiểm tra cả việc dữ liệu có bị biến đổi hay không và dữ liệu đến có đúng là do đầu kia gửi hay không. Nó sử dụng thuật toán băm khoá là MD5 và SHA-1.
<a name="xacthuc"></a>
###3. Chứng minh xác thực (authentication).

- Chứng minh xác thực là kiểm tra định danh của ai đó để xác định chính xác đúng là người đó hay không. Mỗi kết nối SSH bao gồm hai việc xác thực: client kiểm tra định danh của SSH server (server authentication) và server kiểm tra định danh của người sr dụng yêu cầu truy cập (user authentication). Server authentication chắc chắn rằng SSH server là chính xác và không phải là kẻ lừa đảo để đề phòng kẻ tấn công lại gửi kết nối mạng đến một máy khác. Server authentication cũng bảo vệ việc bị kẻ xấu ngồi ở giữa hai bên, lừa gạt cả hai bên nghĩa là kẻ xấu sẽ nói với server nó là client và nói với client nó là server để đọc được dữ liệu trao đổi giữa hai bên.
User authentication theo truyền thống là làm việc với mật khẩu. Để xác thực định danh của bạn, bạn phải đưa ra mật khẩu, và dễ bị lấy cắp. Thêm nữa, để dễ nhớ một mật khẩu, người ta thường đặt nó ngắn và có ý nghĩa nào đó nên dễ bị kẻ xấu đoán ra. Đối với mật khẩu dài hơn thì người ta thường chọn những từ hoặc câu trong ngôn ngữ bẩm sinh nên cũng dễ bị bẻ khoá.
SSH hỗ trợ xác thực bằng mật khẩu, mã hoá mật khẩu khi nó truyền đi trên mạng. Đây là sự cải thiện rất lớn so với những giao thức truy cập từ xa thông thường khác (Telnet, FTP) mà chúng gửi mật khẩu qua mạng dưới dạng clear text. Tuy nhiên, việc chứng thực như thế vẫn chỉ là chứng thực mật khẩu đơn giản vì thế SSH cung cấp cơ chế mạnh hơn và dễ sử dụng hơn: mỗi user có nhiều chữ kí khoá công cộng (per-user public-key signature) và một cải tiến rlogin-style xác thực với định danh host được kiểm tra bằng khoá công khai. Hơn nữa, những bản bổ sung khác nhau của SSH hỗ trợ vài hệ thống khác bao gồm Kerberos, RSA, mật khẩu S/Key one-time và PAM. Một SSH client và SSH server đàm phán với nhau để xác định cơ chế xác thực sẽ sử dụng dựa trên cấu hình của chúng và một server thậm chí có thể yêu cầu nhiều kiểu xác thực.
<a name="giayphep"></a>
###4. Giấy phép (authorization).

- Việc cấp giấy phép có tác dụng quyết định ai đó có thể hoặc không thể làm gì đó. Nó diễn ra sau khi xác thực, bởi vì bạn không thể chấp nhận một ai đó có quyền gì khi chưa biết đó là ai. SSH server có nhiều cách khác nhau để giới hạn hành động của client. Truy cập đến phiên đăng nhập tác động lẫn nhau như TCP port và X Window forwarding, key agent forwarding, … có thể tất cả đều được điều khiển mặc dù không phải tất các đặc điểm đều có sẵn trên tất cả các bản bổ sung SSH,và chúng không luôn luôn tống quát hoặc linh hoạt như bạn ý muốn. Giấy phép có thể được điều khiển tại một mức server rộng (ví dụ: /etc/ssh/sshd_config file đối với OpenSH) hoặc theo tài khoản phụ thuộc vào phương thức xác thực sử dụng.
<a name="chuyentiep"></a>
###5. Chuyển tiếp (forwarding) hoặc tạo đường hầm (tunneling).

- Chuyển tiếp hoặc tạo đường hầm là tóm lược dịch vụ dựa trên TCP khác như là Telnet hoặc IMAP trong một phiên SSH mang lại hiệu quả bảo mật của SSH đến với các dịch vụ dựa trên TCP khác. Ví dụ, một kết nối Telnet bình thường truyền username, password của bạn và phiên đăng nhập của bạn ở dạng clear text. Bằng cách chuyển tiếp telnet thông qua SSH, tất cả dữ liệu sẽ tự động được mã hoá và kiểm tra định danh và bạn có thể xác nhận dùng SSH tin cậy.
- SSH hỗ trợ 3 kiểu chuyển tiếp : 
 <ul>
 <li>v TCP port forwarding: SSH dùng TCP/IP làm cơ chế truyền, thường dùng port 22 trên máy server khi nó mã hoá và giải mã lưu lượng đi trên mạng. Ở đây chúng ta nói đến một đặc điểm mã hoá và giải mã lưu lựong TCP/IP thuộc về ứng dụng khác, trên cổng TCP khác dùng SSH. Tiến trình này gọi là port forwarding, nó có tính trong suốt cao va khá mạnh. Telnet, SMTP, NNTP, IMAP và những giao thức không an toàn khác chạy TCP có thể được bảo đảm bằng việc chuyển tiếp kết nối thông qua SSH. Port forwarding đôi khi được gọi là tunneling bởi vì kết nối SSH cung cấp một “đường hầm” xuyên qua để kết nối TCP khác có thể đi qua.
Giả sử bạn có một máy H ở nhà đang chạy IMAP và bạn muốn kết nối đến một IMAP server trên máy S để đọc và gửi mail. Bình thường thì việc kết nối này không đảm bảo an toàn, tài khoản và mật khẩu mail của bạn được truyền đi dưới dạng clear text giữa chương trình mail của bạn và server. Đối với SSH port forwarding, bạn có thể định tuyến lại trong suốt kết nối IMAP ( tìm cổng TCP 143 trên server S) để truyền đi thông qua SSH, mã hoá bảo đảm dữ liệu truyền đi trên kết nối. Máy IMAP server phải chạy một SSH server cho port forwarding để cung cấp việc bảo đảm đó.
Tuy nhiên, SSH port forwarding chỉ hoạt động trên giao thức TCP và không làm việc được trên các giao thức khác như UDP hay AppleTalk </li>
 <li>v X forwarding : X là một hệ thống window phổ biến đối với các trạm làm việc Unix, một trong những đặc điểm tốt nhất của nó là tính trong suốt. Sử dụng X bạn có thể chạy ứng dụng X từ xa để mở các cửa sổ của chúng trên màn hình hiển thị cục bộ của bạn</li>
 <li>v Agent forwarding : SSH client có thể làm việc với một SSH agent trên cùng một máy. Sử dụng một đặc trưng gọi là agent forwarding, client cũng có thể liên lạc với các agent trên những máy từ xa. Điều thuận lợi là nó cho phép client trên nhiều máy làm việc với một agent và có thể tránh vấn đề liên quan đến tường lửa.</li>
 </ul>
<a name="architecture"></a>
##III. SSH architecture.

![scr1](http://i.imgur.com/WOA7Lch.png)

**Các thành phần trong SSH**

- Server : Một chương trình cho phép đi vào kết nối SSH với một bộ máy, trình bày xác thực, cấp phép, … Trong hầu hết SSH bổ sung của Unix thì server thường là sshd.
- Client : Một chương trình kết nối đến SSH server và đưa ra yêu cầu như là “log me in” hoặc “copy this file”. Trong SSH1, SSH2 và OpenSSH, client chủ yếu là ssh và scp.
- Session : Một phiên kết nối giữa một client và một server. Nó bắt đầu sau khi client xác thực thành công đến một server và kết thúc khi kết nối chấm dứt. Session có thể được tương tác với nhau hoặc có thể là một chuyến riêng.
- Key : Một lượng dữ liệu tương đối nhỏ, thông thường từ mười đến một hoặc hai ngàn bit. Tính hữu ích của việc sử dụng thuật toán ràng buộc khoá hoạt động trong vài cách để giữ khoá: trong mã hoá, nó chắc chắn rằng chỉ người nào đó giữ khoá (hoặc một ai có liên quan) có thể giải mã thông điệp, trong xác thực, nó cho phép bạn kiểm tra trễ rằng người giữ khoá thực sự đã kí hiệu vào thông điệp. Có hai loại khóa: khoá đối xứng hoặc khoá bí mật và khoá bất đối xứng hoặc khóa công khai. Một khoá bất đối xứng hoặc khoá công khai có hai phần: thành phần công khai và thàn phần bí mật.
- SSH đề cập đến 4 kiểu khóa như hình :

![scr2](http://i.imgur.com/rNUn95y.png)

- User key : Là một thực thể tồn tại lâu dài, là khoá bất đối xứng sử dụng bởi client như một sự chứng minh nhận dạng của user ( một người dùng đơn lẻ có thể có nhiều khoá).
- Host key : Là một thực thể tồn tại lâu dài, là khoá bất đối xứng sử dụng bới server như sự chứng minh nhận dạng của nó, cũng như được dùng bởi client khi chứng minh nhận dạng host của nó như một phần xác thực đáng tin. Nếu một bộ máy chạy một SSH server đơn, host key cũng là cái duy nhất để nhận dạng bộ máy đó. Nếu bộ máy chạy nhiều SSH server, mỗi cái có thể có một host key khác nhau hoặc có thể dùng chung. Chúng thường bị lộn với server key.
- Server key : Tồn tại tạm thời, là khoá bất đối xứng dùng trong giao thức SSH-1. Nó đựợc tái tạo bởi server theo chu kỳ thường xuyên ( mặc định là mỗi giờ) và bảo vệ session key. Thường bị lộn với host key. Khoá này thì không bao giờ được lưu trên đĩa và thành phần bí mật của nó không bao giờ được truyền qua kết nối ở bất cứ dạng nào, nó cung cấp “perfect forward secrecy” cho phiên SSH-1.
- Session key : Là một giá trị phát sinh ngẫu nhiên, là khoá đối xứng cho việc mã hoá truyền thông giữa một SSH client và SSH server. Nó được chia ra làm 2 thành phần cho client và server trong một loại bảo bật trong suốt quá trình thiết lập kết nối SSH để kẻ xấu không phát hiện được nó.
- Key generator : Một chương trình tạo ra những loại khoá lâu dài( user key và host key) cho SSH. SSH1, SSH2 và OpenSSH có chương trình ssh-keygen.
- Agent : Một chương trình lưu user key trong bộ nhớ. Agent trả lời cho yêu cầu đối với khoá quan hệ hoạt động như là kí hiệu một giấy xác thực nhưng nó không tự phơi bày khoá của chúng. Nó là một đặc điểm rất có ích. SSH1, SSH2 và OpenSSH có agent ssh-agent và chương trình ssh-add để xếp vào và lấy ra khoá được lưu.
- Signer : Một chương trình kí hiệu gói chứng thực hostbased. 
- Random seed : Một dãy dữ liệu ngẫu nhiên đựoc dùng bởi các thành phần SSH để khởi chạy phần mềm sinh số ngẫu nhiên.
- Configuration file : Một chồng thiết lập để biến đổi hành vi của một SSH client hoặc SSH server. Không phải tất cả thành phần đều được đòi hỏi trong một bản bổ sung của SSH. Dĩ nhiên những server, client và khoá là bắt buộc nhưng nhiều bản bổ sung không có agent và thậm chí vài bản không có bộ sinh khoá.
<a name="auth"></a>

##IV. Gao thức chứng thực SSH (SSH_AUTH).
<a name="yeucau"></a>
###1. Tiến trình yêu cầu chứng thực.

- Quá trình chứng thực được client bắt đầu bằng yêu cầu chứng thực và server hồi đáp lại. Một yêu cầu chứng thực bao gồm những phần như sau:
 <ul>
 <li>Username U: là định danh giấy phép của client.</li>
 <li>Tên dịch vụ S: những việc mà client yêu cầu được truy cập, bắt đầu hoạt động thông qua kết nối SSH-TRANS sau khi chứng thực thành công. Có thể có nhiều dịch vụ có sẵn nhưng thông thường chỉ có một “ssh-connection” yêu cầu truy cập đến những dịch vụ cung cấp khác nhau thông qua giao thức</li>
 <li>SSH-CONN: đăng nhập, thi hành lệnh từ xa, chuyển tiếp cổng và tất cả những thứ khác mà người sử dụng muốn làm với SSH.</li>
 <li>Tên phương thức M, và phương thức dữ liệu cụ thể D : phương thức xác thực cụ thể được dùng trong yêu cầu là “pasword” hoặc “publickey” và phương thức dữ liệu cụ thể truyền bất cứ thứ gì cần thiết để bắt đầu trao đổi chứng thực rõ ràng, ví dụ, một mật khẩu được kiểm tra bởi server. Như là tên khoá trao đổi trong SSH-TRANS thì tên có cú pháp “@domain” có thể được dùng bởi bất cứ ai để thực hiện phương thức cục bộ, trong khi những tên không có @ phải được đăng kí tên toàn bộ các phương thức chứng thực SSH. Mỗi khi phương thức chứng thực bắt đầu, nó có thể bao gồm bất kỳ một số kiểu thông điệp chi tiết nào khác mà nó cần. Hoặc trong trường hợp đơn giản, dữ liệu mang bởi yêu cầu ban đầu cũng đã đủ và server có thể hồi đáp đúng như thể. Trong bất cứ trường hợp nào, sau khi yêu cầu và sau vài phương thức thông điệp theo sau đó thì server cấp phát một hồi đáp chứng thực.</li>
 </ul>
<a name="hoidap"></a>
###2. Tiến trình hồi đáp chứng thực.

- Một hồi đáp chứng thực có hai trạng thái: Thành công và thất bại. Một thông báo thành công không mang dữ liệu nào khác ngoài thông báo là xác thực đã thành công và dịch vụ yêu cầu đã được bắt đầu.
- Một thông báo lỗi có sẽ có cấu trúc như sau:
 <ul>
 <li>Một danh sách các phương thức chứng thực có thể tiếp tục</li>
 <li>Một cờ “ partial success” : Nếu cờ partial success không bật lên thì thông báo đó có nghĩa là những phương thức chứng thực trước đó đã bị lỗi. Nếu cờ partical được bật lên thì thông báo có nghĩa là phương thức đã thành công, tuy nhiên, server yêu cầu phải bổ sung những phương thức còn bị lỗi khác cho thành công trươc khi đồng ý cho truy cập.
</li>
 </ul>
<a name="public"></a>
###3. Chứng thực khóa công khai.

- Một yêu cầu chứng thực khoá công khai mang phương thức có tên là “publickey” và có thể có nhiều dạng khác nhau phụ thuộc vào một cờ được thiết lập. Một dạng của phương thức này là:

```sh
flag = FALSE
Tên thuật toán
Dữ liệu khoá
```

- Thuật toán khoá công khai có thể dùng là những thuật toán thiết lập trong SSH-TRANS và định dạng dữ liệu khoá phụ thuộc vào kiểu khoá như ssh-dss hay ssh-rsa.
- Với cờ thiết lập là FALSE, thông báo này chỉ đơn thuần là kiểm tra xác thực: nó yêu cầu server kiểm tra khoá này có được xác thực để truy cập như mong muốn của tài khoản hay không, nếu được thì gửi lại một thông báo cho biết. Nếu khoá không được xác thực, hồi đáp có giá trị FALSE đơn giản.
- Sau khi xác nhận khoá và gửi thông báo thành công, server cho biết đã chấp nhận truy cập và kết thúc phiên SSH-AUTH.
<a name="password"></a>
###4. Xác thực password.

- Phương thức mật khẩu thì rất đơn giản: nó tên là “password”. Phương thức này chỉ có trong một số bản bố sung của SSH2. Sau khi kiểm tra các tham số thích hợp, server sẽ gửi thông báo chấp nhận truy cập của client và nếu có giao thức này thì server sẽ gửi kết hợp password với thông báo đó để xác thực với client.
<a name="hostbaed"></a>
###5. Xác thực dựa trên host (hostbased).

- Cũng là một phương thức của một số bản bổ sung. Phương thức này dùng để server xác thực client mà nó đã nhận yêu cầu có đúng hay không dựa trên tên máy. Giả sử rằng bạn ở máy A gửi yêu cầu đến server nhưng không đi trực tiếp đến server mà trên đường truyền phải đi qua máy B thì server không kiểm tra máy B mà sẽ kiểm tra xem có phải bên gửi yêu cầu truy cập đến nó có phải là máy A hay không.
<a name="settingssh"></a>
##V. Cài đặt SSH trên Ubuntu và cấu hình dùng trên Putty.
<a name="mohinh"></a>
###1. Mô hình triển khai và cách cài đặt.

**Mô hình**

![scr3](http://i.imgur.com/bWCOqOj.png)

**Cách cài đặt.**

- Trước tiên chúng ta dùng câu lệnh `sudo apt-get -y update` để cập nhật các gói phần mềm.
- Dùng câu lệnh sau để tải về SSH : `sudo apt-get install -y ssh`.
<a name="fileconfig"></a>
###2. File cấu hình và ý nghĩa.

- Tất cả các file của SSH đều được lưu trong thư mục `/etc/ssh`

![scr4](http://i.imgur.com/5lgeORk.png)

- moduli: Chứa một nhóm Diffie-Hellman được sử dụng cho việc trao đổi khóa Diffie-Hellman, nó thực sự quan trọng để xây dựng một lớp bảo mật ở tầng vận chuyển dữ liệu.Khi các khóa được trao đổi với nhau bắt đấu ở một phiên kết nối SSH, một share secret value được tạo ra và không thể xác định bởi một trong hai bên kết nối, giá trị này sau đó sẽ được dùng để cung cấp chứng thực cho host.
- ssh_config: file cấu hình mặc định cho SSH client của hệ thống.
- sshd_config: File cấu hình cho sshd deamon.
- ssh_host_dsa_key: DSA private key được sử dụng với sshd deamon.
- ssh_host_dsa_key.pub: DSA public key được sử dụng bởi sshd deamon.
- ssh_host_key: RSA private key được sử dụng bởi sshd deamon cho phiên bản 1 của giao thức SSH.
- ssh_host_key.pub: RSA public key được sử dụng bởi sshd deamon cho phiên bản 1 của giao thức SSH.
- ssh_host_rsa_key: RSA private key được sử dụng bởi sshd deamon cho phiên bản 2 của giao thức SSH.
- ssh_host_rsa_key.pub: RSA public key được sử dụng bởi sshd deamon cho phiên bản 2 của giao thức SSH.
<a name="authpass"></a>
####2.1. Cấu hình SSH chứng thực bằng mật khẩu.

- Dùng trình soạn thảo vi để chỉnh sửa file sau `/etc/ssh/sshd_config` tìm và sửa các dòng sau thành : 

```sh
PermitRootLogin yes
PermitEmptyPasswords no
PasswordAuthentication yes
```

- Sau đó khởi động lại dịch vụ : 

```sh
service sshd restart 
```

- Sau đó dùng Putty để truy cập vào máy chủ :

![scr5](http://i.imgur.com/ssPVuMv.png)
<a name="authkey"></a>
####2.2. Cấu hình SSH xác thực bằng Key.

- Cấu hình file `/etc/ssh/sshd_config` sửa lại file cấu hình như hình sau :

![scr10](http://i.imgur.com/faCwtR5.png)

- Khởi động lại dịch vụ : 

```sh
service sshd restart
```

- Tạo khóa RSA bằng lệnh sau:

```sh
ssh-keygen -t rsa -b 1024
```
- Tại phần này mọi người có thể nhập password hoặc bỏ trống. Nếu nhập thì phải nhớ để còn mở khóa file id_rsa.

![scr9](http://i.imgur.com/qOmQ63G.png)

- Khi tạo xong chúng ta sẽ có 2 file private key(id_rsa) và public key(id_rsa.pub) cả 2 file này đều nằm ở /root/.ssh/
- Phân quyền cho 2 file /.ssh và id_rsa.pub.

```sh
chmod 700 /root/.ssh/
chmod 600 /root/.ssh/id_rsa.pub
```

- Sau đó copy file id_rsa cho máy client.
- Tại client Window chúng ta tải `puttygen` về. Tiếp theo các bạn chạy chương trình puttygen và vào Menu => Load private key sau đó chọn file id_rsa mà đã copy về máy.

![scr6](http://i.imgur.com/iPvIVrk.png)

- Các bạn mở chương trình putty lên. Các bạn chọn Conection => SSH và chọn 2 only nhé.

![scr7](http://i.imgur.com/PeQnZGb.png)

- Ở mục Conection => SSH => Auth các bạn Browse đến file .ppk mà các bạn đã lưu.

![scr8](http://i.imgur.com/fSnSuUA.png)

- Quay lại mục session các bạn điền IP server và bấm login nhé.
