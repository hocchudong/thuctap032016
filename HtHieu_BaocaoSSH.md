#Báo cáo tìm hiểu giao thức SSH
##Mục lục

##Tổng quan và đặc điểm

- GIT – SSH (Secure Shell) là một giao thức mạng dùng để thiết lập kết nối mạng một cách bảo mật.
SSH hoạt động ở lớp trên trong mô hình phân lớp TCP/IP. Các công cụ SSH (như là OpenSSH, …) cung cấp cho người dùng cách thức để thiết lập kết nối mạng được mã hoá để tạo một kênh kết nối riêng tư. 

- SSH là một chương trình tương tác giữa máy chủ và máy khách có sử dụng cơ chế mã hoá đủ mạnh nhằm ngăn chặn các hiện tượng nghe trộm, đánh cắp thông tin trên đường truyền. 
Các chương trình trước đây: telnet, rlogin không sử dụng phương pháp mã hoá. Vì thế bất cứ ai cũng có thể nghe trộm thậm chí đọc được toàn bộ nội dung của phiên làm việc bằng cách sử dụng một số công cụ đơn giản. Sử dụng SSH là biện pháp hữu hiệu bảo mật dữ liệu trên đường truyền từ hệ thống này đến hệ thống khác.

- Mã hóa:nhằm mục đích để người khác không đọc nó
<ul>
<li>Shared secrets: dùng password để mã hóa hoặc giải mã ở cả hai bên</li>
<li>Public keys :có một cặp khóa để giải mã những thứ ở 2 bên, thông thường một cái sẽ bị ẩn còn 1 cái sẽ công khai</li>

- Phiên bản ssh:
<ul>
<li>Giao thức:Phiên bản 2 có nhiều tính năng đặc biệt là không dễ bị tổn thương khi có lỗi bảo mật như phiên bản 1</li>
<li>Triển khai:OpenSSH, F-Secure SSH, và SSH.com SSH. </li>
<li>UMBC:UMBC sử dụng SSH1 SSH.com, mà chỉ hỗ trợ phiên bản 1 của giao thức SSH</li>
</ul>

- Cách thức hoạt động: 
<ul>
<li>Định danh host - xác định định danh của hệ thống tham gia phiên làm việc SSH.</li>
<li>Mã hoá - thiết lập kênh làm việc mã hoá.</li>
<li>Chứng thực - xác thực người sử dụng có quyền đăng nhập hệ thống.</li>
</ul>

- Tính bí mật (Privacy):Tính bí mật có nghĩa là bảo vệ dữ liệu không bị phơi bày. Mạng máy tính bình thường không bảo đảm tính bí mật, bất cứ ai truy cập đến phần cứng của mạng hoặc đến những host kết nối với mạng đều có thể sẽ đọc được tất cả dữ liệu đi qua mạng. Mặc dù mạng chuyển mạch hiện đại đã giảm những vấn đề này trong mạng vùng cục bộ nhưng nó vẫn còn một vấn đề nghiêm trọng đó là mật khẩu dễ bị những kẻ xấu đánh cắp.
SSH cung cấp tính bí mật bằng việc mã hoá dữ liệu đi qua mạng. Đó là việc mã hoá hai đầu dựa trên khoá ngẫu nhiên (sinh ra để phục vụ cho một phiên kết nối và được huỷ đi khi phiên kết nối thành công). SSH hỗ trợ nhiều thuật toán mã hoá đối với phiên dữ liệu, đó là những thuật toán mã hoá chuẩn như: AES, ARCFOUR, Blowfish, Twofish, IDEA, DES và triple-DES (3DES)

- Tính toàn vẹn (Integrity):Tính toàn vẹn nghĩa là bảo đảm dữ liệu được truyền từ một đầu này đến đầu kia của mạng không bị thay đổi. Giao thức SSH sử dụng phương pháp kiểm tra toàn vẹn mật mã, phương pháp này kiểm tra cả việc dữ liệu có bị biến đổi hay không và dữ liệu đến có đúng là do đầu kia gửi hay không. Nó sử dụng thuật toán băm khoá là MD5 và SHA-1.

- Chứng minh xác thực (authentication):Chứng minh xác thực là kiểm tra định danh của ai đó để xác định chính xác đúng là người đó hay không. Mỗi kết nối SSH bao gồm hai việc xác thực: client kiểm tra định danh của SSH server (server authentication) và server kiểm tra định danh của người sr dụng yêu cầu truy cập (user authentication). Server authentication chắc chắn rằng SSH server là chính xác và không phải là kẻ lừa đảo để đề phòng kẻ tấn công lại gửi kết nối mạng đến một máy khác. Server authentication cũng bảo vệ việc bị kẻ xấu ngồi ở giữa hai bên, lừa gạt cả hai bên nghĩa là kẻ xấu sẽ nói với server nó là client và nói với client nó là server để đọc được dữ liệu trao đổi giữa hai bên.
User authentication theo truyền thống là làm việc với mật khẩu. Để xác thực định danh của bạn, bạn phải đưa ra mật khẩu, và dễ bị lấy cắp. Thêm nữa, để dễ nhớ một mật khẩu, người ta thường đặt nó ngắn và có ý nghĩa nào đó nên dễ bị kẻ xấu đoán ra. Đối với mật khẩu dài hơn thì người ta thường chọn những từ hoặc câu trong ngôn ngữ bẩm sinh nên cũng dễ bị bẻ khoá.
SSH hỗ trợ xác thực bằng mật khẩu, mã hoá mật khẩu khi nó truyền đi trên mạng. Đây là sự cải thiện rất lớn so với những giao thức truy cập từ xa thông thường khác (Telnet, FTP) mà chúng gửi mật khẩu qua mạng dưới dạng clear text. Tuy nhiên, việc chứng thực như thế vẫn chỉ là chứng thực mật khẩu đơn giản vì thế SSH cung cấp cơ chế mạnh hơn và dễ sử dụng hơn: mỗi user có nhiều chữ kí khoá công cộng (per-user public-key signature) và một cải tiến rlogin-style xác thực với định danh host được kiểm tra bằng khoá công khai. Hơn nữa, những bản bổ sung khác nhau của SSH hỗ trợ vài hệ thống khác bao gồm Kerberos, RSA, mật khẩu S/Key one-time và PAM. Một SSH client và SSH server đàm phán với nhau để xác định cơ chế xác thực sẽ sử dụng dựa trên cấu hình của chúng và một server thậm chí có thể yêu cầu nhiều kiểu xác thực.

- Việc cấp giấy phép:Việc cấp giấy phép có tác dụng quyết định ai đó có thể hoặc không thể làm gì đó. Nó diễn ra sau khi xác thực, bởi vì bạn không thể chấp nhận một ai đó có quyền gì khi chưa biết đó là ai. SSH server có nhiều cách khác nhau để giới hạn hành động của client. Truy cập đến phiên đăng nhập tác động lẫn nhau như TCP port và X Window forwarding, key agent forwarding, … có thể tất cả đều được điều khiển mặc dù không phải tất các đặc điểm đều có sẵn trên tất cả các bản bổ sung SSH,và chúng không luôn luôn tống quát hoặc linh hoạt như bạn ý muốn. Giấy phép có thể được điều khiển tại một mức server rộng (ví dụ: /etc/ssh/sshd_config file đối với OpenSH) hoặc theo tài khoản phụ thuộc vào phương thức xác thực sử dụng.

- Chuyển tiếp (forwarding) hoặc tạo đường hầm (tunneling):Chuyển tiếp hoặc tạo đường hầm là tóm lược dịch vụ dựa trên TCP khác như là Telnet hoặc IMAP trong một phiên SSH mang lại hiệu quả bảo mật của SSH đến với các dịch vụ dựa trên TCP khác. Ví dụ, một kết nối Telnet bình thường truyền username, password của bạn và phiên đăng nhập của bạn ở dạng clear text. Bằng cách chuyển tiếp telnet thông qua SSH, tất cả dữ liệu sẽ tự động được mã hoá và kiểm tra định danh và bạn có thể xác nhận dùng SSH tin cậy.
SSH hỗ trợ 3 kiểu chuyển tiếp:
<ul>
<li>v TCP port forwarding:SSH dùng TCP/IP làm cơ chế truyền, thường dùng port 22 trên máy server khi nó mã hoá và giải mã lưu lượng đi trên mạng. Ở đây chúng ta nói đến một đặc điểm mã hoá và giải mã lưu lựong TCP/IP thuộc về ứng dụng khác, trên cổng TCP khác dùng SSH. Tiến trình này gọi là port forwarding, nó có tính trong suốt cao va khá mạnh. Telnet, SMTP, NNTP, IMAP và những giao thức không an toàn khác chạy TCP có thể được bảo đảm bằng việc chuyển tiếp kết nối thông qua SSH. Port forwarding đôi khi được gọi là tunneling bởi vì kết nối SSH cung cấp một “đường hầm” xuyên qua để kết nối TCP khác có thể đi qua.Tuy nhiên, SSH port forwarding chỉ hoạt động trên giao thức TCP và không làm việc được trên các giao thức khác như UDP hay AppleTalk </li>
<li>v X forwarding:X là một hệ thống window phổ biến đối với các trạm làm việc Unix, một trong những đặc điểm tốt nhất của nó là tính trong suốt. Sử dụng X bạn có thể chạy ứng dụng X từ xa để mở các cửa sổ của chúng trên màn hình hiển thị cục bộ của bạn</li>
<li>v Agent forwarding:SSH client có thể làm việc với một SSH agent trên cùng một máy. Sử dụng mọt đặc trưng gọi là agent forwarding, client cũng có thể liên lạc với các agent trên những máy từ xa. Điều thuận lợi là nó cho phép client trên nhiều máy làm việc với một agent và có thể tránh vấn đề liên quan đến tường lửa.</li>

- Kiến trúc chung của giao thức SSH:
<ul>
<li>Server :Một chương trình cho phép đi vào kết nối SSH với một bộ máy, trình bày xác thực, cấp phép, … Trong hầu hết SSH bổ sung của Unix thì server thường là sshd.</li>
<li>Client :Một chương trình kết nối đến SSH server và đưa ra yêu cầu như là “log me in” hoặc “copy this file”. Trong SSH1, SSH2 và OpenSSH, client chủ yếu là ssh và scp.</li>
<li>Session :Một phiên kết nối giữa một client và một server. Nó bắt đầu sau khi client xác thực thành công đến một server và kết thúc khi kết nối chấm dứt. Session có thể được tương tác với nhau hoặc có thể là một chuyến riêng.</li>
<li>Key :Một lượng dữ liệu tương đối nhỏ, thông thường từ mười đến một hoặc hai ngàn bit. Tính hữu ích của việc sử dụng thuật toán ràng buộc khoá hoạt động trong vài cách để giữ khoá: trong mã hoá, nó chắc chắn rằng chỉ người nào đó giữ khoá (hoặc một ai có liên quan) có thể giải mã thông điệp, trong xác thực, nó cho phép bạn kiểm tra trễ rằng người giữ khoá thực sự đã kí hiệu vào thông điệp. Có hai loại khóa: khoá đối xứng hoặc khoá bí mật và khoá bất đối xứng hoặc khóa công khai. Một khoá bất đối xứng hoặc khoá công khai có hai phần: thành phần công khai và thàn phần bí mật.Các lạo key: </li>
<ul>
<li>User key :Là một thực thể tồn tại lâu dài, là khoá bất đối xứng sử dụng bởi client như một sự chứng minh nhận dạng của user ( một người dùng đơn lẻ có thể có nhiều khoá)</li>
<li>Host key :Là một thực thể tồn tại lâu dài, là khoá bất đối xứng sử dụng bới server như sự chứng minh nhận dạng của nó, cũng như được dùng bởi client khi chứng minh nhận dạng host của nó như một phần xác thực đáng tin. Nếu một bộ máy chạy một SSH server đơn, host key cũng là cái duy nhất để nhận dạng bộ máy đó. Nếu bộ máy chạy nhiều SSH server, mỗi cái có thể có một host key khác nhau hoặc có thể dùng chung. Chúng thường bị lộn với server key.</li>
<li>Server key :Tồn tại tạm thời, là khoá bất đối xứng dùng trong giao thức SSH-1. Nó đựợc tái tạo bởi server theo chu kỳ thường xuyên ( mặc định là mỗi giờ) và bảo vệ session key. Thường bị lộn với host key. Khoá này thì không bao giờ được lưu trên đĩa và thành phần bí mật của nó không bao giờ được truyền qua kết nối ở bất cứ dạng nào, nó cung cấp “perfect forward secrecy” cho phiên SSH-1</li>
<li>Session key :Là một giá trị phát sinh ngẫu nhiên, là khoá đối xứng cho việc mã hoá truyền thông giữa một SSH client và SSH server. Nó được chia ra làm 2 thành phần cho client và server trong một loại bảo bật trong suốt quá trình thiết lập kết nối SSH để kẻ xấu không phát hiện được nó.</li>
</ul>
</ul>


##Cài đặt SSH trên Ubuntuserver

