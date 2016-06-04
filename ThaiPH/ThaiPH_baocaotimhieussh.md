# Tìm hiểu giao thức SSH
# Mục lục
<h4><a href="#concept">1. Khái niệm SSH</a></h4>
<h4><a href="#other">2. Một số khái niệm xung quanh SSH</a></h4>
<ul>
<li><h4><a href="#encryption">2.1. Encryption</a></h4></li>
<li><h4><a href="#access">2.2. Truy cập máy tính từ xa</a></h4></li>
<li><h4><a href="#ver">2.3. Các phiên bản ssh</a></h4></li>
</ul>

<h4><a href="#basic">3. Basic SSH</a></h4>
<ul>
<li><h4><a href="#standard">3.1. Standard case</a></h4></li>
<li><h4><a href="#host">3.2. Host keys</a></h4></li>
<li><h4><a href="#usr">3.3. User names</a></h4></li>
<li><h4><a href="#scp">3.4. SCP</a></h4></li>
</ul>

<h4><a href="#intermediate">4. Intermediate SSH</a></h4>
<ul>
<li><h4><a href="#remote">4.1. Remote commands</a></h4></li>
<li><h4><a href="#x11">4.2. X11 forwarding</a></h4></li>
<li><h4><a href="#config">4.3. Config files</a></h4></li>
</ul>

<h4><a href="#advanced">5. Advanced SSH</a></h4>
<ul>
<li><h4><a href="#rsa">5.1. RSA authentication</a></h4></li>
<li><h4><a href="#agent">5.2. ssh-agent</a></h4></li>
<li><h4><a href="#port">5.3. Port forwarding</a></h4></li>
</ul>

---

<h3><a name="concept">1. Khái niệm SSH</a></h3>
<div>
<ul>
<li>SSH (Secure Shell) là giao thức mạng dùng để thiết lập kết nối mạng một cách bảo mật. SSH hoạt động ở lớp ứng dụng của phân lớp TCP/IP. </li>
<li>Các công cụ SSH (như OpenSSH, PuTTy, etc.) cung cấp cho người dùng cách thức để thiết lập kết nối mạng được mã hóa để tạo kênh kết nối riêng tư.</li>
<li>Tính năng tunneling (port forwarding) cho phép chuyển tải các giao vận theo các giao thức khác.</li>
</ul>
</div>

<h3><a name="other">2. Một số khái niệm xung quanh SSH</a></h3>
<ul>
<li><h4><a name="encryption">2.1. Encryption</a></h4>
<ul>
<li><b>a. Shared secrets</b>
<div>Khái niệm chỉ sự chia sẻ thông tin bí mật, trường hợp thường thấy là sử dụng "password" ở cả 2 phía để mã hóa và giải mã.</div>
</li>
<li><b>b. Public keys</b>
<div>Thực chất có một cặp keys. Thông tin bị mã hóa với một key nhưng có thể giải mã với một key khác. Thông thường một key sẽ giữ bí mật trong khi key kia sẽ được phân tán công khai.
<ul>
<li><b>Public key authentication</b>
<div>Nếu bạn có public key, bạn có thể sử dụng để kiểm tra liệu các đầu cuối khác có đang giữa private key không</div>
</li>

<li><b>Fingerprints </b>
<div>
Khi nhận được một public key, ta không biết được nó có thuộc về người mà ta muốn "nói chuyện" hay không. Phương thức để xác nhận keys ở đây là thông qua fingerprints. Nếu có được fingerprint ahead của key, ta có thể kiểm tra lại lần nữa key đang giữ. 
</div>
</li>
</ul>
</div>
</li>
</ul>
</li>

<li><h4><a name="access">2.2. Truy cập máy tính từ xa</a></h4>
<ul>
<li><b>a. Truy cập cục bộ</b>
<div>
Thực hiện các command trực tiếp trên shell mọi thứ ta gõ lên terminal
</div>
</li>
<li><b>b. Telnel:</b> mô phỏng tương tự như truy cập cục bộ nhưng thông qua mạng. Mọi thứ ta gõ đều có thể lấy được, gửi qua mạng và gửi tới shell trên máy remote. Telnet gửi mọi thứ thông qua mạng và mọi người đều có thể thấy được chính xác những gì ta đã gõ, bao gồm cả việc ta thấy gì trên màn hình (ví dụ password)</li>
<li><b>c. SSH:</b> ý tưởng tương tự telnet, lấy những gì ta gõ và gửi qua mạng tới shell trên máy remote, truy nhiên thông tin trước khi gửi đi được mã hóa. Mọi người theo dõi phiên ssh trên mạng sẽ chỉ thấy những ký tự vô nghĩa</li>
</ul>
</li>


<li><h4><a name="ver">2.3. Các phiên bản ssh</a></h4>
<ul>
<li><b>a. Protocol</b>
<div>Phiên bản 2 có nhiều tính năng hay, bao gồm cả các bản vá lỗ hổng bảo mật ở phiên bản đầu</div>
</li>
<li><b>b. Implementations</b>
<div>Có 3 hướng triển khai ssh: OpenSSH, F-Secure SSH, SSH.com SSH</div>
</li>
<li><b>c. UMBC</b>
<div>UMBC sử dụng phiên bản SSH phiên bản 1 theo hướng SSH.com</div>
</li>
</ul>
</li>
</ul>

<h3><a name="basic">3. Basic SSH</a></h3>
<ul>
<li><h4><a name="standard">3.1. Standard case</a></h4>
Trường hợp cơ bản, ssh được sử dụng giống telnet, ta có thể ssh tới một host, nhập mật khẩu chính xác là đăng nhập được. Ví dụ:
<pre>
<code>
ssh 10.10.10.130
thaiph@10.10.10.130's password: [not shown]
10.10.10.130$
</code>
</pre>
</li>

<li><h4><a name="host">3.2. Host keys</a></h4>
ssh sử dụng mã hóa với public key để khởi tạo kết nối tới host
<ul>
<li><b>a. Tính hữu dụng của PKI</b>
<ul>
<li><b>Encryption</b>
<br>
Public keys sử dụng khá chậm, do đó ssh client sẽ gửi một password đã mã hóa với public key của server.
</li>
<li><b>Authentication</b>
Để tránh tấn công MITM, client sử dụng host key để xác nhận host có chính xác không. Do private key của host được giữ bí mật nên MITM không thể giả mạo được.
</li>
</ul>
</li>
<li><b>b. Thực hành</b>
<div>Khi ssh tới một host chưa bao giờ "nói chuyện" trước đó, nó sẽ gửi lại cho bạn một public key. Đây có khả năng sẽ trở thành lỗ hổng bảo mật vì host giải mạo có thể gửi lại bạn key của nó thay vì key của host.</div>
<ul>
<li><b>Ví dụ</b>
<br><br>
<img src="http://i.imgur.com/pBySF7h.png"/>
<br><br>
</li>
<li><b>Giải thích</b>
<div>ssh cảnh báo bạn chưa từng giao tiếp với host này. Nó sẽ chỉ ra hostname và địa chỉ IP để bạn chắc chắn được kết nối tới host chính xác không. Nó cũng đưa ra fingerprint để kiểm tra, nếu không phù hợp thì sẽ hủy yêu cầu.</div>
</li>
<li><b>Thay đổi host key</b>
Trường hợp thay đổi host key khi phát hiện có tấn công MITM, ví dụ như sau:
<br><br>
<img src="http://i.imgur.com/BBJTnct.png"/>
</li>
</ul>
</li>
</ul>
</li>

<li><h4><a name="usr">3.3. User names</a></h4>
ssh giả định rằng username trên remote computer giống với username trên máy cục bộ đang ssh tới.
<ul>
<li><b>a. Username khác:</b>
<pre>
<code>
C:\Users\thaiph>ssh thaihust@10.10.10.136
thaihust@10.10.10.136's password:
Welcome to Ubuntu 16.04 LTS (GNU/Linux 4.4.0-21-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Mon May 16 08:53:37 ICT 2016

  System load:    0.05              Processes:            206
  Usage of /home: 0.2% of 15.17GB   Users logged in:      1
  Memory usage:   17%               IP address for ens33: 172.16.69.133
  Swap usage:     0%                IP address for ens34: 10.10.10.136

  Graph this data and manage this system at:
    https://landscape.canonical.com/

22 packages can be updated.
0 updates are security updates.


*** System restart required ***
Last login: Mon May 16 01:42:09 2016
thaihust@u1604:~$
</code>
</pre>
<img src="http://i.imgur.com/ACIvapL.png"/>
<br><br>
</li>
<li><b>b. Giải thích:</b>
<div>Ta có thể chỉ định username trên command line nếu nó khác với username trên máy cục bộ, hoặc cũng có thể chỉ định trong file config</div>
</li>
</ul>
</li>

<li><h4><a name="scp">3.4. SCP</a></h4>
scp là một chương trình sao chép file qua mạng dựa trên giao thức ssh. Nó mã hóa mọi thứ, cả password và dữ liệu.
<pre>
<code>
[2016-05-16 09:15.09]  ~/Desktop
[thaiph.thaiph-PC] ➤ scp usr.png thaihust@10.10.10.136:/home/thaihust/
usr.png                                       100%   88KB  87.7KB/s   00:00
</code>
</pre>
<img src="http://i.imgur.com/jc7Xml4.png"/>
<br><br>
</li>
</ul>

<h3><a name="intermediate">4. Intermediate SSH</a></h3>
<ul>
<li><h4><a name="remote">4.1. Remote commands</a></h4>
Ta không cần kết nối tới shell trên remote computer, chỉ cần nói với ssh để thực hiện một command từ xa và lấy kết quả trả về.
<pre>
<code>
[2016-05-16 09:33.36]  ~/Desktop
[thaiph.thaiph-PC] ➤ ssh thaihust@10.10.10.136 'ls -l; echo "----REMOTE COMMAND----"; whoami'                                                                        total 176
-rwxrwx--- 1 thaihust thaihust 89839 May 16 09:14 Desktop
-rwxrwx--- 1 thaihust thaihust 89839 May 16 09:15 usr.png
----REMOTE COMMAND----
thaihust                                                                                                                                                                   
</code>
</pre>
<img src="http://i.imgur.com/Xdk92tx.png"/>
<br><br>
Một số chương trình chạy trực tiếp trên terminal như 'vi' là những chương trình có tính tương tác. Tuy nhiên khi sử dụng ssh remote command, cần phải sử dụng tùy chọn -t để sử dụng terminal giả lập để chạy các phần mềm đó. Ví dụ:
<br><br>
<img src="http://i.imgur.com/swq6f6V.png"/>
</li>
<li><h4><a name="x11">4.2. X11 forwarding</a></h4>
Chương trình đồ họa sử dụng giao thức X Window để hiển thị lên màn hình của bạn. Với X, bạn có thể chạy một chương trình trên remote computer và hiển thị nó lên máy cục bộ. Thông thường X sẽ không mã hóa qua mạng. Với tùy chọn -X, bạn có thể sử dụng kết nối mã hóa với chương trình đồ họa. Ví dụ:
<pre>
<code>
[2016-05-16 09:56.59]  ~/Desktop
[thaiph.thaiph-PC] ➤ ssh -X -f thaihust@10.10.10.136 xclock
</code>
</pre>
<img src="http://i.imgur.com/beDxs1V.png"><br><br>
</li>
<li><h4><a name="config">4.3. Config files</a></h4>
File config ssh (~/.ssh/config) chứa nhiều thông tin cấu hình trước khi kết nối với remote host.
<ul>
<li><b>a. Host <foo></b>
<br>
File config được tách thành nhiều phần bởi chỉ thị "Host". Mọi cấu hình sau dòng Host được áp dụng cho host đó. 
<br>
Chỉ thị "Host *" là chỉ thị đặc biệt, ký tự "*" đại diện cho mọi host. 
</li>
<li><b>b. HostName <name></b>
<br>
Sử dụng chỉ thị "HostName <name>" để chỉ định host với tên cụ thể. SSH sẽ kết nối tơi host đó thay thì host chỉ định trên command line 
</li>
<li><b>c. User <username></b>
<br>
Chỉ định người dùng khi kết nối tới host, tương ứng với "<username>@" khi thực hiện ssh trên command line. Ví dụ:
<pre>
<code>
thaihust@u1604:~/.ssh$ ls
config  known_hosts
thaihust@u1604:~/.ssh$ cat config
Host 10.10.10.128
HostName mininet-vm
User mininet
thaihust@u1604:~/.ssh$ ssh 10.10.10.128
mininet@mininet-vm's password:
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.13.0-85-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Sun May 15 21:00:04 PDT 2016

  System load:  0.0               Processes:           84
  Usage of /:   52.5% of 6.76GB   Users logged in:     1
  Memory usage: 9%                IP address for eth0: 10.10.10.128
  Swap usage:   0%                IP address for eth1: 172.16.69.134

  Graph this data and manage this system at:
    https://landscape.canonical.com/
Last login: Sun May 15 21:00:05 2016 from 10.10.10.136
mininet@mininet-vm:~$
</code>
</pre>
<img src="http://i.imgur.com/PjBPFly.png"/><br><br>
</li>
<li><b>d. Compression <yes or no></b>
<br>
Thiết lập "Compression yes" nếu muốn nén dữ liệu khi truyền dữ liệu.
</li>
<li><b>d. Lots of rthers</b>
Ngoài các tùy chọn trên còn nhiều tùy chọn khác có thể cấu hình trong file config. Đọc thêm SSH book hoặc tra man page để tìm hiểu thêm.
</li>
</ul>
</li>
</ul>

<h3><a name="advanced">5. Advanced SSH</a></h3>
<ul>
<li><h4><a name="rsa">5.1. RSA authentication</a></h4>
ssh có thể sử dụng một số phương thức xác thực để kết nối tới remote host. Password là tùy chọn mặc định. Tuy nhiên hướng tiếp cận linh hoạt hơn là sử dụng RSA keys. Cách này sẽ tương tự như việc ssh sử dụng host key của server để xác thực danh tính của remote computer.
<ul>
<li><b>a. Versions</b>
Sử dụng chuẩn SSH1 của SSH.com và OpenSSH.
</li>
<li><b>b. Lợi thế</b>
<ul>
<li>Không thể thỏa thuận kết nối từ xa. Server sẽ không bao giờ thấy được private key của bạn, do vậy kể cả nếu đã thỏa thuận kết nối, attacker cũng không thể đánh cắp mật khẩu của bạn từ host khác.</li>
<li>Có thể sử dụng một agent để giữ key. Nếu bạn có ssh-agent cục bộ với key đã được load, ssh sẽ sử dụng nó thay vì hỏi lại bạn password mỗi lần kết nối. Điều này sẽ thuận tiện hơn trong khi vẫn đảm bảo bí mật.</li>
<li>Có thể hạn chế các key để thực hiện một số command đặc biệt. Điều này thực hiện bằng cách thêm dòng <code>command="<program>"</code> ở dòng đầu của key trong file <code>~/.ssh/authorized_keys</code>, mọi việc xác thực với key đó sẽ tự động chạy chương trình mang tên <program></li>
</ul>
</li>
<li><b>c. Tạo key</b>
<br>
Sử dụng ssh-keygen với tùy chọn '-t rsa' để tạo RSA key, sử dụng phiên bản 2 của giao thức SSH.
<br>
Tạo keygen:
<pre>
<code>
thaihust@u1604:~$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/thaihust/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/thaihust/.ssh/id_rsa.
Your public key has been saved in /home/thaihust/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:Sls3ZO0TvguWAgYXQzy7M9nXAS1LJJW7t4c8L0qs+ys thaihust@u1604
The key's randomart image is:
+---[RSA 2048]----+
|     o+ .ooo     |
|      oo .=..    |
|    . .o .o=o    |
|     o.  ooo..   |
|      ++S oo+.   |
|     o==.ooooo   |
|      oo..*o.o   |
|        E= .*..  |
|        o++o.=.  |
+----[SHA256]-----+
thaihust@u1604:~$
</code>
</pre>
</li>
<li><b>d. Cho phép đăng nhập thông qua key đó</b>
<br>
Trên remote host, thêm nội dung trong file <code>~/<user>/.ssh/id_rsa.pub</code> vào file ~/.ssh/authorized_keys.
<br>
Copy file id_rsa.pub lên host:
<pre>
<code>
thaihust@u1604:~/.ssh$ scp id_rsa.pub 10.10.10.128:/home/mininet
mininet@mininet-vm's password:
id_rsa.pub                                                                                                         100%  396     0.4KB/s   00:00
</code>
</pre>
Thêm nội dung file *.pub vào file authorized_keys và thử ssh lại để kiểm tra:
<pre>
<code>
mininet@mininet-vm:~$ ls -l id_rsa.pub
-rw-r--r-- 1 mininet mininet 396 May 15 21:47 id_rsa.pub
mininet@mininet-vm:~$ cat id_rsa.pub >> ~/.ssh/authorized_keys
mininet@mininet-vm:~$ cat ~/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQChwTthxzEKbUaNEQcdY/Z3T04wWIBgxAc39P9VJ+fEUurh2F3uTS6ycCp+gqof7XNnbeOJQBNlrh2uhuOlgYHgdiEuCitqrOx6w9ZEZgdzADBt8nJ0ySVTv1Ps
hzNm3fNcud3CQxWPlXEjqVzkWnl3scl5rtJoeAOCtw5RdrGURp+hUMHlsbpwMh/mTW6KxbacqK7dkVGbaZ/w/Ji1Luw/mt1C8y8TNtBDJMMmpXcWFcS315CO78BfLIZMu7pxTF/+u4AH5lgTdk77fmM+uCy0b1j9
2qhVnhYnSmouVx+eP+QjfZkEETSENyJpcNBewOSzr8HGZb2ny7mKRcdWkbyn thaihust@u1604
mininet@mininet-vm:~$ clear

mininet@mininet-vm:~$ exit
logout
Connection to mininet-vm closed.
thaihust@u1604:~/.ssh$ clear

thaihust@u1604:~/.ssh$ ssh 10.10.10.128
Enter passphrase for key '/home/thaihust/.ssh/id_rsa':
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.13.0-85-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Sun May 15 21:47:36 PDT 2016

  System load:  0.0               Processes:           87
  Usage of /:   52.5% of 6.76GB   Users logged in:     1
  Memory usage: 10%               IP address for eth0: 10.10.10.128
  Swap usage:   0%                IP address for eth1: 172.16.69.134

  Graph this data and manage this system at:
    https://landscape.canonical.com/
Last login: Sun May 15 21:47:37 2016 from 10.10.10.136
mininet@mininet-vm:~$
</code>
</pre>
</li>
<li><b>e. Hoàn thành</b>
<br>Như vậy bạn đã có thể ssh tới remote host sử dụng rsa key.
</li>
</ul>
</li>

<li><h4><a name="agent">5.2. ssh-agent</a></h4>
Một ssh-agent là một chương trình giữ một bản sao của key của bạn trong bộ nhớ để chương trình ssh sử dụng, nhờ đó khi thực hiện kết nối ssh, ssh sẽ không phải hỏi lại bạn mà vẫn đảm bảo tính bảo mật. Tuy nhiên vẫn tồn tại một số vấn đề như sau.
<ul>
<li><b>a. Các vấn đề bảo mật</b>
<ul>
<li><b>Việc sử dụng agent khi vắng mặt</b>
<br>
Trong trường hợp bạn rời khỏi máy tính mà có người khác sử dụng máy tính của bạn, học có thể thực hiện ssh thay bạn. Giải pháp là trước khi rời máy tính, bạn hãy khóa màn hình hoặc gỡ key khỏi agent.
</li>
<li><b>Lừa gạt agent</b>
<br>
Nếu ai đó trên máy tính có thể thao tác với vai trò như bạn(ví dụ quyền root), học có thể đưa dữ liệu vào agent và thực thi nó khi bạn hỏi tới. Giải pháp: không sử dụng agent trên một máy tính mà bạn không tin tưởng người quản trị máy tính đó. 
</li>
<li><b>Đánh cắp key</b>
Ai đó vkhi truy cập vào bộ nhớ máy tính có thể thông qua dữ liệu của agent mà lấy được bản copy của key và có thể kết nối tới host bất hợp pháp. Giải pháp tương tự như trên.
</li>
</ul>
</li>
<li><b>b. Bắt đầu một agent</b>
<pre>
<code>
thaihust@u1604:~/.ssh$ eval `ssh-agent -s`
Agent pid 27797
thaihust@u1604:~/.ssh$
</code>
</pre>
</li>
<li><b>c. Thêm và gỡ keys</b>
<ul>
<li><b>Thêm keys</b>
<pre>
<code>
thaihust@u1604:~$ ssh-add ~/.ssh/id_rsa
Enter passphrase for /home/thaihust/.ssh/id_rsa:
Identity added: /home/thaihust/.ssh/id_rsa (/home/thaihust/.ssh/id_rsa)
</code>
</pre>
</li>
<li><b>Liệt kê danh sách các key đã add và agent</b>
<pre>
<code>
thaihust@u1604:~$ ssh-add -l
2048 SHA256:Sls3ZO0TvguWAgYXQzy7M9nXAS1LJJW7t4c8L0qs+ys /home/thaihust/.ssh/id_rsa (RSA)
</code>
</pre>
</li>
<li><b>Gỡ bỏ keys</b>
<pre>
<code>
thaihust@u1604:~$ ssh-add -d ~/.ssh/id_rsa
Identity removed: /home/thaihust/.ssh/id_rsa (thaihust@u1604)
</code>
</pre>
</li>
</ul>
</li>
<li><b>d. Sử dụng agent</b>
<br> Khi key đã load và ssh-agent, ta có thể ssh tới host mà không cần nhập mật khẩu(ssh không hỏi lại nữa).
<pre>
<code>
thaihust@u1604:~$ ssh-add -l
2048 SHA256:Sls3ZO0TvguWAgYXQzy7M9nXAS1LJJW7t4c8L0qs+ys /home/thaihust/.ssh/id_rsa (RSA)
thaihust@u1604:~$ ssh 10.10.10.128
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.13.0-85-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Sun May 15 21:54:04 PDT 2016

  System load:  0.0               Processes:           87
  Usage of /:   52.5% of 6.76GB   Users logged in:     1
  Memory usage: 10%               IP address for eth0: 10.10.10.128
  Swap usage:   0%                IP address for eth1: 172.16.69.134

  Graph this data and manage this system at:
    https://landscape.canonical.com/
Last login: Sun May 15 21:54:05 2016 from 10.10.10.136
</code>
</pre>
</li>
<li><b>e. Thiết lập trên nhiều shell</b>
<br>
Mặc định agent chỉ được thiết lập để làm việc với một shell. Để có thể sử dụng ssh-agent trên nhiều shell sử dụng cùng một agent, thực hiện sao chép biến môi trường $SSH_AUTH_SOCK từ shell này sang shell khác.
<pre>
<code>
thaihust@u1604:~$ echo $SSH_AUTH_SOCK
/tmp/ssh-paEbY3EkK05J/agent.27796
thaihust@u1604:~$ export SSH_AUTH_SOCK=/tmp/ssh-paEbY3EkK05J/agent.27796
</code>
</pre>
</li>
<li><b>f. Thoát khỏi agent</b>
<pre>
<code>
thaihust@u1604:~$ unset SSH_AUTH_SOCK
thaihust@u1604:~$ eval `ssh-agent -k`
Agent pid 27797 killed
</code>
</pre>
</li>
</ul>
</li>
<li><h4><a name="port">5.3. Port forwarding</a></h4>
Chương trình ssh có thể lắng nghe trên port tùy ý lên cả local và remote computer, chuyển tiếp bất kỳ dữ liệu nào thông qua kết nối đã được mã hóa, gửi từ đầu cuối này sang đầu cuối khác.
<ul>
<li><b>a. Một số ví dụ cụ thể</b>
<ul>
<li><b>Kịch bản</b>
Bạn có một web proxy trên remote computer.  Bạn muốn trình duyệt trên máy mình sử dụng một kết nối mã hóa tới máy tính đó để sử dụng proxy. Như vậy, ssh sẽ lắng nghe trên cổng cụ bộ, chuyển tiếp dữ liệu qua kết nối đã mã hóa và gửi nó tới proxy trên remote computer. Trình duyệt của bạn lúc này sẽ được sử dụng một port trên trình duyệt cục bộ giống như proxy của nó
</li>
<li><b>Số hiệu cổng</b>
<div>
Quy định remote computer là "somehost". Máy cục bộ là "localhost". Proxy lắng nghe trên cổng 5865 trên remote host. SSH trên máy cục bộ sử dụng port 5001.
</div>
</li>
<li><b>Commands</b>
<pre>
<code>
$ ssh -L 5001:somehost:5865 somehost 
user@somehost's password: [not shown] 
somehost$ 
</code>
</pre>
</li>
<li><b>Giải thích</b>
<div>Tùy chọn -L nhằm mục đích để ssh lắng nghe trên máy cục bộ và chuyển tiếp tới remote host. (sử dụng tùy chọn -R trong trường hợp ngược lại). Sối liệu đầu tiên là cổng lắng nghe trên máy cục bộ - port 5001. Giá trị thứ hai là tên máy mà dữ liệu sẽ chuyển tới thông qua kết nối đã mã hóa. Con số cuối cùng là giá trị cổng mà dữ liệu sẽ được gửi tới trên máy đích. Trong trường hợp này là 5865, nơi mà web proxy lắng nghe. Lúc này ta sẽ thiết lập trình duyệt trên máy cụ bộ sử dụng "localhost:5001" như một HTTP proxy. Đường hầm này sẽ duy trì miễn là thực hiện kết nối qua ssh.</div>
</li>
</ul>
</li>
<li><b>b. Lắng nghe máy tính không cục bộ</b>
<div>Nếu muốn sử dụng máy tính khác trên cùng mạng sử dụng đường hầm đã mã hóa, bạn phải thêm tùy chọn -g khi thực hiện ssh.</div>
</li>
<li><b>c. Tunnel mà không sử dụng terminal</b>
<div>OpenSSH sử dụng tùy chọn -N để tạo tunnel mà không mở bất kỳ shell nào trên remote computer. Tunnel này sẽ luôn mở cho tới khi ssh client ngừng hoạt động.</div></li>
</ul>
</li>
</ul>

