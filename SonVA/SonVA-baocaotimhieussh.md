# Mục Lục
[I. Một vài khái niệm](#I)  
- [a. mã hóa](#I.a)
- [b. Truy cập từ xa](#I.b)
- [c. Các phiên bản SSH](#I.c)  

[II.Basic SSH](#II)
- [a.Trường hợp thông thường](#II.a)
- [b. Hostkey](#II.b)
- [c. SCP](#II.c)  

[III. Intermediate SSH](#III)
- [a. Remote command](#III.a)
- [b. X11 Forwarding](#III.b)
- [c. Chỉnh sửa config file](#III.c)  

[IV. Advance SSH](#IV)
- [a. Dùng khóa RSA xác thực](#IV.a)
- [b. SSH agent](#IV.b)
- [c. Port Forwarding](#IV.c)


<a name="I"></a>
## I. Một vài khái niệm
<a name="I.a"></a>
### a. Mã hóa 
- Chia sẻ khóa dùng chung để mã hóa/giải mã dữ liệu ở cả hai nơi
- Sử dụng Public Key (Khóa công cộng): là cặp khóa gồm 2 khóa: Public và Private key. Dữ liệu được mã hóa bởi khóa Public key chỉ có thể giải mã bởi Private key. Private key được giữ bí mật trong khi Public key được phân phối rộng rãi.
    - Public key authentication: Nếu như có Public key có thể kiểm tra xem ai đó có thực sự đang nắm giữ private key hay không
    - fingerprint: khi bạn nhận một public key, chưa chắc nó đã thuộc về người đưa Publickey đó cho bạn, nếu bạn có một chuỗi fingerprint, bạn có thể kiểm tra key đó.

<a name="I.b"></a>
### b. Truy cập từ xa
- Local access: Khi bạn ngồi máy bạn và thực hiện trực tiếp những dòng lệnh trên máy bạn.
- Telnet: thông qua mạng, khi bạn gõ những gì ở dưới máy bạn thì nó sẽ được truyền qua mạng và gửi tới Shell của một máy khác. Tuy nhiên những gì bạn gõ khi truyền qua mạng sẽ vẫn giữ nguyên ở dưới dạng text bình thường mà bất cứ ai theo dõi trên đường mạng cũng có thể đọc được những gì bạn gửi đi, kể cả mật khẩu
- SSH: Cũng như telnet, nhưng dữ liệu bạn nhập vào khi gửi đến shell của máy remote thì được mã hóa và không ai có thể xem được nó thông qua đường truyền giữa bạn và remote host

<a name="I.c"></a>
### c. Các phiên bản của SSH
Giao thức SSH hiện tại có 2 phiên bản chính và có 3 bản cải tiến kế thừa từ nó: OpenSSH, F-sercure SSH, SSH.com SSH

<a name="II"></a>
## II. SSH cơ bản

<a name="II.a"></a>
### a. Trường hợp thông thường:
Nếu bạn muốn telnet, gõ ssh tới host, sau đó nhập mật khẩu
```
ssh user@host
user@host's password:
host$
```


Nếu như bạn gõ ssh user@host thì sẽ truy cập ssh dưới user gõ vào, còn nếu chỉ ```ssh host``` thì sẽ truy cập với user giống như user trên local

<a name="II.b"></a>
### b. Host key
SSH sử dụng public key để mã hóa dữ liệu truyền và nhận. vì public key không nhanh do mất thời gian mã hóa, SSH sẽ  gửi mật khẩu được mã hóa bằng public key của server  
Để phòng chống tấn công theo kiểu Man-in-the-middle, client sẽ sử dụng hostkey để xác thực truy nhập vào host. Chừng nào prvate key không bị lộ thì kiểu tấn công Man-in-the-middle không thể thực hiện được.
- Khi bạn kết nối đến một host mà trước đó bạn chưa từng SSH đến, host đó sẽ gửi bạn  một public key, đây có thể là lỗ hổng bảo mật nếu như có một host giả mạo lấy key này của bạn.
```
ssh ***.edu.vn
The authenticity of host '***.edu.vn (***.***.43.35)' can't be established.
RSA key fingerprint is 92:ef:64:7a:82:6a:d8:96:a8:55:1f:11:6a:b4:ca:2a.
Are you sure you want to continue connecting (yes/no)
```
<img src="http://i.imgur.com/rkkE5pM.png">  
SSH cảnh báo rằng chưa từng kết nối đến host này trước đó, SSH sẽ hiển thị hostname và IP và server fingerprint string. Thường thì cũng an toàn khi mà bạn chấp nhận sử dụng key này.
- Nếu như hostkey bị change thì sẽ có cảnh báo
```
 ssh somehost 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @ 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY! 
Someone could be eavesdropping on you right now (man-in-the-middle attack)! 
It is also possible that the RSA host key has just been changed. 
The fingerprint for the RSA key sent by the remote host is 
90:9c:46:ab:03:1d:30:2c:5c:87:c5:c7:d9:13:5d:75. 
Please contact your system administrator. 
Add correct host key in /home/user/.ssh/known_hosts to get rid of this message. 
Offending key in /home/user/.ssh/known_hosts:1 
Password authentication is disabled to avoid man-in-the-middle attacks. 
Agent forwarding is disabled to avoid man-in-the-middle attacks. 
X11 forwarding is disabled to avoid man-in-the-middle attacks. 
Permission denied (publickey,password,keyboard-interactive). 
$ 
```
<a name="II.c"></a>
### c. SCP
SCP là chương trình giúp copy dữ liệu qua mạng. các kết nối trong quá trình chạy SCP cũng được mã hóa để tránh rò rỉ thông tin.
```
$ scp test.html 192.168.128.10:public_html/ 
user@somehost's password: [not shown] 
localfile            100% |*****************************|  2048 KB 00:03 
$ scp test@192.168.128.10:public_html/index.html ~/public_html/ 
test@192.168.128.10's password: [not shown] 
index.html           100% |*****************************| 10198 KB 00:05 
$
```
<a name="III"></a>
## III. Intermediate SSH
<a name="III.a"></a>
### a. remote command:
Bạn có thể gửi kèm command để chạy trên remote computer qua lệnh truy cập ssh
``` 
$ hostname 
ubuntu
$ ssh root@192.168.128.10 hostname 
root@192.168.128.10's password: [not shown] 
ubuntu 
$ 
```
Bạn có thể chạy các ứng dụng trên remote computer qua lệnh truy cập SSH
```
ssh -t sweetlove@192.168.232.128 nano
```

<a name="III.b"></a>
### b. X11 forwarding
Một vài chương trình đồ họa đặc biệt có thể chạy trên remote computer và hiển thị dưới dạng đồ họa dưới máy của bạn. SSH giúp mã hóa kết nối của ứng dụng qua đường truyền.
```
ssh -X -f sweetlove@192.168.232.128 xclock
```
-f có tác dụng ẩn ssh chạy background sau khi nhập password. VD trên chạy xclock. ta thu được  
<img src="http://i.imgur.com/I5b9Hyt.png">

<a name="III.c"></a>
### c. Config file
Config file nằm tại etc/ssh/ssh_config. Dấu * sau Host là chỉ định áp dụng option này cho tất cả các host  
<img src="http://i.imgur.com/D17dodL.png">  
Nếu như hostname được khai báo thì chỉ cần ssh dùng hostname
```
----- 
Host moo 
  HostName supercalifragilisticexpialidocious 
----- 
$ host moo 
moo does not exist 
$ host supercalifragilisticexpialidocious 
supercalifragilisticexpialidocious is 192.168.1.2 
$ ssh moo 
user@moo's password: [not shown] 
supercalifragilisticexpialidocious$ 
```

nếu như tên người dùng được khai báo ở đây, SSH sẽ dùng nó để connect dưới dạng ```tennguoidung@sshsrv```  
Khai báo nén kết nối để cải thiện truy cập: sửa Compression  thành YES

<a name="IV"></a>
## IV. Advance SSH

<a name="IV.a"></a>
### a. RSA Auth.
ssh có nhiều phương pháp để xác thực kết nối giữa bạn và remote srv. Bạn có thể dùng khóa RSA (RSA key) để xác thực truy cập.
Ưu điểm:
- SSH srv không thể thấy được private key nên attacker không thể đánh cắp password và giả mạo truy cập
- Nếu local có ssh-agent hỗ trợ truy cập bằng key (Putty) thì ssh sẽ dùng key để xác thực, ko hỏi mật khẩu
- nếu bạn thêm 'command="<program>" ' vào trong /.ssh/authorized_keys thì khi dùng khóa để truy cập sẽ chỉ chạy được lệnh tương ứng  

Các bước làm:
- Chạy lệnh ```ssh-keygen -t rsa``` để generate cặp key RSA. nhập mật khẩu để khóa key. PuTTYgen cũng đùng để tạo key
- Thiết lập cho phép đăng nhập bằng key này: 
copy dòng public key trong ```/home/user/.ssh/id_rsa.pub``` vào ~/.ssh/authorized_keys
<a name="IV.b"></a>
### b. ssh-agent
ssh-agent copy key của bạn vào bộ nhớ để ssh sử dụng. khi kết nối thì bạn chỉ cần ssh hostname là truy cập được (phải nhập passphrase của key lúc generate ở bên trên)
!!! Cảnh báo bảo mật: nếu như ai đó điều khiển máy tính của bạn có thể dùng key để login vào remote computer trực tiếp hoặc đánh cắp cặp key của bạn nếu như có quyền.

Thêm key:
```
$ ssh-add ~/.ssh/id_rsa 
Enter passphrase for /home/user/.ssh/id_rsa: [not shown] 
Identity added: /home/user/.ssh/id_rsa (/home/user/.ssh/id_rsa) 
$ 
```

Liệt kê key:
```
$ ssh-add -l 
1024 75:a4:2c:9b:b1:58:8f:9c:96:d8:99:77:fc:01:0d:8a /home/user/.ssh/id_rsa (RSA) 
$ 
```

xóa key

```
$ ssh-add -d ~/.ssh/id_rsa 
Identity removed: /home/user/.ssh/id_rsa (/home/user/.ssh/id_rsa.pub) 
$ 
```

<a name="IV.c"></a>
### c. Port forwarding:

```
$ ssh -L 5001:localhost:5865 remotehost 
user@somehost's password: [not shown] 
somehost$ 
```

-L dùng để listen từ localhost chuyển tới remote host
-R làm ngược lại

Open SSH có một option -N dùng để tạo một đường hầm kết nối giữa máy trạm và máy remote, đường hầm này vẫn còn kể cả khi client SSH proc. bị killed

