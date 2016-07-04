# MỤC LỤC
[I. GIỚI THIỆU VỀ LDAP](#I)  
- [1. Dịch vụ thư mục (Dicrectory Service) là gì ?](#I.1)  
- [2. LDAP là gì?](#I.2)  
- [3. Phương thức hoạt động của LDAP](#I.3)  
- [4.Database backend của LDAP](#I.4)  
- [5. Lưu trữ thông tin của LDAP](#I.5)  

[II. Mô hình LDAP](#II)
- [1. Mô hình thông tin Ldap (LDAP information model)](#II.1)
- [2. Mô hình đặt tên Ldap (LDAP naming model)](#II.2)
- [3. Mô hình chức năng Ldap (LDAP function model)](#II.3)
- [4. Mô hình bảo mật Ldap (LDAP Security model)](II.4)

[III. Xác thực trong LDAP](#III)

<img src="http://i.imgur.com/wHqJbVR.png">
<a name="I"></a>
# I. GIỚI THIỆU VỀ LDAP

<a name="I.1"></a>
## 1. Dịch vụ thư mục (Dicrectory Service) là gì ?
Thư mục (Directory) là một phần của cuộc sống con người :  
```
Danh bạ điện thoại  
TV Guide  
Catalog sản phẩm  
Thẻ thư viện....  
```  
 ==> Offline Directory  
Thư mục giúp chúng ta tìm kiếm thông tin bằng cách tổ chức và mô tả thành phần bên trong : Từ sđt cho đến kênh TV, từ đồ ăn cho đến tài liệu tham khảo...  
Khái niệm thư mục trong IT cũng tương tự nhưng có một số khác biệt khá quan trọng. ==> Online Directory  

Online Directories khác Offline Directories ở :  
- Thư mục online là động (Dynamic)
- Thư mục online linh hoạt hơn (Flexible)
- Thư mục online an toàn hơn (Sercurity)
- Thư mục online riêng tư hơn (Personalized)  

Dựa vào mục đích, chúng ta có thể phân chia Directory thành 4 loại :  
- Application-specific directories: Chúng thường đi kèm hoặc nhúng vào ứng dụng mà đôi khi chúng ta hoàn toàn không nhận ra. Ví dụ : IBM/Lotus Notes Name and Address book, Microsoft Exchange, file aliases trong MTA
- Network operating system (NOS)–based directories: Những thư mục như Novell's eDirectory (NDS), Sun Microsystems Network Information Service (NIS),Banyan's StreetTalk được thiết kế để đáp ứng nhu cầu của một HĐH mạng  
- Purpose-specific directories : Tuy không đi kèm với ứng dụng nhưng những thư mục này thường thiết kế cho mục đích cố định, chuyên hóa. Ví dụ hệ thống DNS, Switchboard.. 
- General-purpose, standards-based directories : Dạng thư mục được phát triển để phục vụ một lượng lớn các ứng dụng khác nhau. (Ví dụ LDAP, X.500)  

Như ta đã trình bày ở trên, theo một cách ngắn gọn và dễ hiểu, thư mục là một loại CSDL đặc biệt.  
**Vậy dịch vụ thư mục (Directory Service) là gì ?**
```
  Đó là một tập hợp các phần mềm, phần cứng, tiến trình, chính sách, thủ tục quản trị nhằm mục đích cung cấp nội dung thư mục của bạn đến cho người dùng
```
Dịch vụ thư mục gồm các yếu tố sau :

- Thông tin chứa trong thư mục
- Phần mềm Server tổ chức thông tin
- Phần mềm Client đóng vai trò người dùng truy xuất các thông tin này
- Phần cứng cho Server và Client
- Phần mềm hỗ trợ (Ví dụ HĐH, Driver..)
- Hạ tầng mạng cho phép kết nối Server-Client, và các kết nối khác.
- Chính sách quản lý (Ai truy cập, cập nhật thông tin thư mục ? Cái gì được lưu trữ...)
- Các thủ tục duy trì và giám sát dịch vụ thư mục
- Các phần mềm dùng để giám sát, duy trì..  
<img src="http://i.imgur.com/ZVLtwmk.png">  

Khi nói tới dịch vụ thư mục , chúng ta không thể không nhắc tới chuẩn X.500  
Vào giữa những năm 1980s, có 2 chuẩn dành cho dịch vụ thư mục do 2 cơ quan quốc tế độc lập ban hành :  
- International Telegraph and Telephone Consultative Committee (CCITT) sau này là International Telecommunication Union (ITU) → Tìm kiếm SĐT và email
- International Organization for Standardization (ISO) → Cung cấp một name service chạy trên 2 lớp network và application trong OSI  

Chuẩn X.500 lần đầu tiên được phê duyệt vào năm 1988 và công bố vào năm 1990 bởi CCITT, liên tục được cập nhật vào 1993,1997, 2001 và tới hôm nay.  
Các đặc điểm kĩ thuật được định nghĩa theo loạt tiêu chuẩn sau :
- X.501 : The models
- X.509: Authentication Framework
- X.511: Abstract Service Definition
- X.518: Procedures for Distributed Operation
- X.519: Protocol Specifications
- X.520: Selected Attribute Types.
- X.525: Replication
- X.530: Systems Management  

Khi được công bố , X.500 là một chuẩn có khá nhiều đặc tính mới :  
- Là một hệ thống dịch vụ thư mục đầu tiên có mục đích chung, nhằm phục vụ yêu cầu của một loạt ứng dụng.
- Cung cấp hệ thống tìm kiếm phong phú và hỗ trợ nhiều cấu trúc truy vấn khác nhau.
- X.500 được thiết kế như là một hệ thống phân phối dịch vụ cao cấp với hệ thống máy chủ, client và admin có thể trải dài toàn cầu.
- X.500 là một tiêu chuẩn mở, không phụ thuộc vào bất cứ hãng phần mềm hay thiết bị nào.  

<img src="http://i.imgur.com/EudsHvx.png">  

<a name="I.2"></a>
## 2. LDAP là gì?
Sớm chấp nhận rằng X.500 (DAP) là giao thức nặng nề , phức tạp và không phù hợp với máy tính để bàn ngày nay. Những người triển khai X.500 đã tìm đường đi để tránh tiếp cận một giao thức DAP kiểu heavyweight.  
Vào khoảng năm 1990, có 2 nhóm độc lập đã phát triển giao thức tương tự, cạnh tranh với DAP, dễ dàng triển khai trên máy tính để bàn thông thường.  
- Client dùng giao thức này để gửi yêu cầu tới máy chủ trung gian qua TCP/IP
- Máy chủ trung gian này sẽ triển khai yêu cầu tới một máy chủ DAP  

Đó là 2 giao thức mang tên Directory Assistance Service (DAS) và Directory Interface to X.500 Implemented Efficiently (DIXIE)  
<img src="http://i.imgur.com/Cq57io2.png">  
Như vậy , LDAP là gì ?   
- LDAP (Lightweight Directory Access Protocol) - Giao thức truy cập nhanh các dịch vụ thư mục : Là một chuẩn mở rộng của giao thức truy cập dịch vụ thư mục (DAP – X.500)
- LDAP là một giao thức chạy trên nền TCP/IP (TCP:389,UDP:389) dưới dạng kết nối Client-Server.
- LDAP là một dạng giao thức Lightweight , tức là một giao thức có tính hiệu quả, đơn giản và dễ dàng cài đặt (trái với Heavyweight như X.500)
- LDAP đã phát triển với v2 và LDAP v3.  
<img src="http://i.imgur.com/jdfLsxl.png">

LDAP tối ưu và đơn giản hóa DAP (tức X.500) ở 4 phương diện :  
- Chức năng (Functionally): LDAP cung cấp hầu hết các chức năng của DAP với chi phí thấp hơn. Các chức năng dự phòng, ít sử dụng bị loại bỏ, đơn giản hóa việc triển khai lên client và server
- Trình diễn dữ liệu (Data Representation): Trong LDAP, phần lớn yếu tố dữ liệu được thực hiện dưới dạng chuỗi văn bản, nhằm đơn giản và tăng cường hiệu suất (tuy nhiên để hiệu quả thì các chuỗi văn bản được gói trong các thông điệp mã hóa nhị phân) 
- Mã hóa (Encoding) : Một tập con các quy tắc mã hóa của X.500 được dùng để mã hóa thông điệp LDAP . Qua đó đơn giản giản hóa việc triển khai.
- Truyền tải (Transport): LDAP chạy trực tiếp trên TCP thay vì yêu cầu một hệ thống phức tạp và khó sử dụng như OSI. Việc thực hiện được đơn giản đi nhiều, hiệu suất được tăng lên, sự phụ thuộc vào OSI bị loại bỏ do đó tối ưu hóa việc triển khai thư mục LDAP  

LDAP qua các thời kỳ :  
<img src="http://i.imgur.com/YbUTxOr.png">
<img src="http://i.imgur.com/7hIOPWs.png">
<img src="http://i.imgur.com/fS26q6B.png">  
**CÁC MÔ HÌNH HOẠT ĐỘNG CHÍNH CỦA LDAP :**  
Ngoài vai trò là một giao thức mạng thì LDAP còn định nghĩa ra 4 mô hình (model) cho phép linh động trong việc tổ chức sắp xếp thư mục :
- LDAP Information : Định nghĩa các loại dữ liệu chứa trong thư mục .
- LDAP Naming : Định nghĩa cách sắp xếp và tham chiếu đến thư mục.
- LDAP Functional : Định nghĩa cách truy cập và cập nhật thông tin trong thư mục
- LDAP Security : Định nghĩa cách mà thư mục được bảo vệ, tránh các truy cập trái phép  

LDAP định nghĩa định dạng file trao đổi dữ liệu LDIF (LDAP Data Interchange Format) dưới dạng văn bản dùng để mô tả thông tin về thư mục.  
LDAP chỉ là giao thức, không hỗ trợ xử lý như cơ sở dữ liệu. Mà nó cần một nơi lưu trữ backend và xử lý dữ liệu tại đó. Vì vậy mà LDAP client kết nối tới LDAP server theo mô hình sau:  
<img src="http://i.imgur.com/Wuzu29G.gif">  
LDAP là giao thức truy cập vì vậy nó theo mô hình dạng cây (Directory Information Tree). LDAP là giao thức truy cập dạng client/server.  
<img src="http://i.imgur.com/bek7M6V.png">

<a name="I.3"></a>
## 3. Phương thức hoạt động của LDAP
LDAP hoạt động theo mô hình client-server. Một hoặc nhiều LDAP server chứa thông tin về cây thư mục (Directory Information Tree – DIT). Client kết nối đến server và gửi yêu cầu. Server phản hồi bằng chính nó hoặc trỏ tới LDAP server khác để client lấy thông tin. Trình tự khi có kết nối với LDAP:  
- Connect (kết nối với LDAP): client mở kết nối tới LDAP server
- Bind (kiểu kết nối: nặc danh hoặc đăng nhập xác thực): client gửi thông tin xác thực
- Search (tìm kiếm): client gửi yêu cầu tìm kiếm
- Interpret search (xử lý tìm kiếm): server thực hiện xử lý tìm kiếm
- Result (kết quả): server trả lại kết quả cho client
- Unbind: client gửi yêu cầu đóng kết nối tới server
- Close connection (đóng kết nối): đóng kết nối từ server  
<img src="http://i.imgur.com/d4yQwZW.png">  

<a name="I.4"></a>
## 4.Database backend của LDAP
Slapd là một “LDAP directory server” có thể chạy trên nhiều platform khác nhau. Bạn có thể sử dụng nó để cung cấp những dịch vụ của riêng mình. Những tính năng mà slapd cung cấp:  
- LDAPv3: slapd hỗ trợ LDAP cả IPv4, IPv6 và Unix IPC.
- Simple Authentication and Security Layer: slapd hỗ trợ mạnh mẽ chứng thực và bảo mật dữ liệu dịch vụ bằng SASL
- Transport Layer Security: slapd hỗ trợ sử dụng TLS hay SSL.
2 database mà SLAPD sử dụng để lưu trữ dữ liệu hiện tại là bdb và hdb. BDB sử dụng Oracle Berkeley DB để lưu trữ dữ liệu. Nó được đề nghị sử dụng làm database backend chính cho SLAPD thông thường. HDB là cũng tương tự như BDB nhưng nó sử dụng database phân cấp nên hỗ trợ cơ sỡ dữ liệu dạng cây. HDB thường được mặc định cấu hình trong SLAPD hiện nay.

<a name="I.5"></a>
## 5. Lưu trữ thông tin của LDAP
Ldif (LDAP Data Interchange Format) là một chuẩn định dang file text lưu trữ thông tin cấu hình LDAP và nội dung thư mục. File LDIF thường dùng để import dữ liệu mới vào trong directory hoặc thay đổi dữ liệu đã có. Dữ liệu trong file LDIF phải tuân theo quy luật có trong schema của LDAP.  
Schema là loại dữ liệu được định nghĩa từ trước. Mọi thành phần được thêm vào hoặc thay đổi trong directory của bạn sẽ được kiểm tra lại trong schema để đảm bảo chính xác.

### 5.1 Cấu trúc tập tin LDIF  

Thông thường file LDIF sẽ có mẫu sau:  
 - Mỗi tập entry khác nhau được phân cách bởi dòng trắng
 - “tên thuộc tính: giá trị”
 - Một tập chỉ dẫn cú pháp để làm sao xử lý thông tin

Những yêu cầu khi khai báo LDIF:
- Lời chú thích được gõ sau dấu # trong 1 dòng
- Thuộc tính được liệt kê bên trái dấu “:” và giá trị được biểu diễn bên phải.
- Thuộc tính dn định nghĩa duy nhất cho một DN xác định trong entry đó.

Ví dụ: thông tin của OU, people, các thư mục bên trong Distinguished Name test.com Thông tin LDAP thể hiện theo dạng cây o: test.com

----------------File LDIF lưu thông tin: ----------------------------------------------  
dn: o=test
objectclass: top
objectclass: organization
o: test.com
dn: ou=People,o=test.com
objectclass: organizationalUnit
ou: People
dn: ou=Server, o=test.com
objectclass: organizationalUnit
ou: Server
dn: ou=IT, ou=People, o=test.com
objectclass: organizationalUnit
ou: IT
dn: cn=sonva, ou=IT, ou=People, o=test.com
objectclass: top
objectclass: organizationalPerson
cn: sonva
sn: vu
givenname: son
uid: sonva
ou: IT

### 5.2 Entry là gì?
Một entry là tập hợp của các thuộc tính, từng thuộc tính này mô tả một nét đặt trưng tiêu biểu của một đối tượng. Một entry bao gồm nhiều dòng  
- DN : distinguished name - là tên của entry thư mục, tất cả được viết trên một dòng.
- Sau đó lần lượt là các thuộc tính của entry, thuộc tính dùng để lưu giữ dữ liệu. Mỗi thuộc tính trên một dòng theo định dạng là “kiểu thuộc tính : giá trị thuộc tính”.  

Một số các thuộc tính cơ bản trong file Ldif:  

|STT|Tên|Mô tả                                 | 
|---|---|---------------------------------------|
|1  |dn |Distinguished Name, tên gọi phân biệt |   
|2	|c	|country – 2 kí tự viết tắt tên của một nước| 
|3	|o	|organization – tổ chức|
|4	|ou	|organization unit – đơn vị tổ chức|
|5	|objectClass|	Mỗi giá trị objectClass hoạt động như một khuôn mẫu cho các dữ liệu được lưu giữ trong một entry. Nó định nghĩa một bộ các thuộc tính phải được trình bày trong entry (Ví dụ: entry này có giá trị của thuộc tính objectClass là eperson, mà trong eperson có quy định cần có các thuộc tính là tên, email, uid ,…thì entry này sẽ có các thuộc tính đó)|
|6	|givenName|	Tên|
|7	|uid	|id người dùng|
|8	|cn	|common name – tên thường gọi|
|9	|telephoneNumber	|số điện thoại|
|10	|sn	|surname – họ|
|11	|userPassword	|mật khẩu người dùng|
|12	|mail	|địa chỉ email|
|13	|facsimileTelephoneNumber	|số phách|
|14	|createTimestamp	|thời gian tạo ra entry này|
|15	|creatorsName	|tên người tạo ra entry này|
|16	|pwdChangedTime	|thời gian thay đổi mật khẩu|
|17	|entryUUID	|id của entry|

<a name="II"></a>
# II. Mô hình LDAP
LDAP chia ra 4 mô hình:  
- Mô hình LDAP information - xác định cấu trúc và đặc điểm của thông tin trong thư mục.
- Mô hình LDAP Naming - xác định cách các thông tin được tham chiếu và tổ chức.
- Mô hình LDAP Functional - định nghĩa cách mà bạn truy cập và cập nhật thông tin trong thư mục của bạn.
- Mô hình LDAP Security - định nghĩa ra cách thông tin trong thư mục của bạn được bảo vệ tránh các truy cập không được phép.  

<a name="II.1"></a>
## 1. Mô hình thông tin Ldap (LDAP information model)
Khái niệm:  
Mô hình LDAP Information định nghĩa ra các kiểu dữ liệu và các thành phần thông tin cơ bản mà bạn có thể chứa trong thư mục. Hay nó mô tả cách xây dựng ra các khối dữ liệu mà chúng ta có thể sử dụng để tạo ra thư mục.  
<img src="http://i.imgur.com/l3RWkaU.png">  

<a name="II.2"></a>
## 2. Mô hình đặt tên Ldap (LDAP naming model)
Khái niệm:  
- Mô hình LDAP Naming định nghĩa ra cách để chúng ta có thể sắp xếp và tham chiếu đến dữ liệu của mình.
- Mô hình này mô tả cách sắp xếp các entry vào một cấu trúc có logic, và mô hình LDAP Naming chỉ ra cách để chúng ta có thể tham chiếu đến bất kỳ một entry thư mục nào nằm trong cấu trúc đó.
- Mô hình LDAP Naming cho phép chúng ta có thể đặt dữ liệu vào thư mục theo cách mà chúng ta có thể dễ dàng quản lý nhất.  

Cách sắp xếp dữ liệu:  
- Ví dụ như chúng ta có thể tạo ra một container chứa tất cả các entry mô tả người trong một tổ chức(o), và một container chứa tất cả các group của bạn, hoặc bạn có thể thiết kế entry theo mô hình phân cấp theo cấu trúc tổ chức của bạn. Việc thiết kế tốt cần phải có những nghiên cứu thoả đáng.
- Ta có thể thấy rằng entry trong thư mục có thể đồng thời là tập tin và là thư mục.  
<img src="http://i.imgur.com/cCLODrA.png">

Một phần thư mục LDAP với các entry chứa thông tin:  
- Giống như đường dẫn của hệ thống tập tin, tên của một entry LDAP được hình thành bằng cách nối tất cả các tên của từng entry cấp trên (cha) cho đến khi trở lên root.
- Như hình trên ta thấy node có màu đậm sẽ có tên là uid=mlin, ou=people, dc=imagenie, dc=com, nếu chúng ta đi từ trái sang phải thì chúng ta - có thể quay ngược lại đỉnh của cây, chúng ta thấy rằng các thành phần riêng lẽ của cây được phân cách bởi dấu “,”.
- Với bất kỳ một DN, thành phần trái nhất được gọi là relative distingguished name (RDN), như đã nói DN là tên duy nhất cho mỗi entry trên thư mục, do đó các entry có cùng cha thì RDN cũng phải phân biệt.  
<img src="http://i.imgur.com/FWXDIvB.png">  
Ví dụ như hình trên, mặc dù hai entry có cùng RDN cn=son nhưng hai entry ở hai nhánh khác nhau.  

**Bí danh (Aliases) – cách tham chiếu đến dữ liệu**  
- Những entry bí danh (Aliases entry) trong thư mục LDAP cho phép một entry chỉ đến một entry khác.
- Để tạo ra một alias entry trong thư mục trước tiên bạn phải tạo ra một entry với tên thuộc tính là aliasedOjecctName với giá trị thuộc tính là DN của entry mà chúng ta muốn alias entry này chỉ đến.
- Hình dưới đây cho ta thấy được một aliases entry trỏ đến một entry thật sự.  
<img src="http://i.imgur.com/2pRSfUB.png">  

**LDAP với Alias entry**  
Không phải tất cả các LDAP Directory Server đều hổ trợ Aliases. Bởi vì một alias entry có thể chỉ đến bất kỳ một entry nào, kể cả các entry LDAP server khác. Và việc tìm kiếm khi gặp phải một bí danh có thể phải thực hiện tìm kiếm trên một cây thư mục khác nằm trên các server khác, do đó làm tăng chi phi cho việc tìm kiếm, đó là lý do chính mà các phần mềm không hổ trợ alias.  

<a name="II.3"></a>
## 3. Mô hình chức năng Ldap (LDAP function model)
Khái niệm  
- Đây là mô hình mô tả các thao tác cho phép chúng ta có thể thao tác trên thư mục.
- Mô hình LDAP Functional chứa một tập các thao tác chia thành 3 nhóm:
 - Thao tác thẩm tra (interrogation) cho phép bạn có thể search trên thư mục và nhận dữ liệu từ thư mục.
 - Thao tác cập nhật (update): add, delete, rename và thay đổi các entry thư mục.
 - Thao tác xác thực và điều khiển (authentiaction and control) cho phép client xác định mình đến chỗ thư mục và điều kiển các hoạt động của phiên kết nối.
 - Với version 3 giao thức LDAP ngoài 3 nhóm thao tác trên, còn có thao tác LDAP extended, thao tác này cho phép nghi thức LDAP sau này có thể mở rộng một cách có tổ chức.
 
**Mô tả các thao tác**
### 3.1. Thao tác thẩm tra (LDAP Interrogation)
- Cho phép client có thể tìm và nhận lại thông tin từ thư mục.
- Thao tác tìm kiếm (LDAP search operation) yêu cầu 8 tham số (Ví dụ: search (“ou=people,dc=framgia,dc=com”,”base”,”derefInsearching”,10,60,attrOnly=true,Filter,ArrayAttribute)
- Tham số đầu tiên là đối tượng cơ sở mà các thao tác tìm kiếm thực hiện trên đó, tham số này là DN chỉ đến đỉnh của cây mà chúng ta muốn tìm.
- Tham số thứ hai là phạm vi cho việc tìm kiếm, chúng ta có 3 phạm vi thực hiện tìm kiếm:
    - Phạm vi “base” chỉ ra rằng bạn muốn tìm ngay tại đối tượng cơ sở.
    - Phạm vi “onelevel” thao tác tìm kiếm diễn ra tại cấp dưới (con trực tiếp của đối tượng cơ sở)
    - Phạm vi “subtree” thao tác này thực hiện tìm hết trên cây mà đối tượng cơ sở là đỉnh.

<img src="http://i.imgur.com/N3phMmU.png">  
VD phạm vi base  
<img src="http://i.imgur.com/6Bhryz4.png">  
VD phạm vi one level  
<img src="http://i.imgur.com/dEYoSQ3.png">  
VD phạm vi subtree  

- Tham số thứ ba derefAliases , cho server biết rằng liệu bí danh aliases có bị bỏ qua hay không khi thực hiện tìm kiếm, có 4 giá trị mà derefAliases có thể nhận được:  
"nerverDerefAliases" - thực hiện tìm kiếm và không bỏ qua bí danh (aliases) trong lúc thực hiện tìm kiếm và áp dụng với cả đối tượng cơ sở.  
"derefInsearching" - bỏ qua các aliases trong trong các entry cấp dưới của đối tượng cơ sở, và không quan tâm đến thuộc tính của đối tượng cơ sở.  
"derefFindingBaseObject" - tìm kiếm sẽ bỏ qua các aliases của đối tượng cơ sở, và không quan tâm đến thuộc tính của các entry thấp hơn đối tượng cơ sở.  
"derefAlways" - bỏ qua cả hai nếu việc tìm kiếm thấy đối tượng cơ sở hay là các entry cấp thấp là các entry aliases.
- Tham số thứ bốn cho server biết có tối đa bao nhiêu entry kết quả được trả về.
- Tham số thứ năm qui định thời gian tối đa cho việc thực hiện tìm kiếm.
- Tham số thứ sáu: attrOnly – là tham số kiểu bool, nếu được thiết lập là true, thì server chỉ gởi các kiểu thuộc tính của entry cho client, nhưng sever không gởi giá trị của các thuộc tính đi
- Tham số thứ bảy là bộ lọc tìm kiếm (search filter) đây là một biểu thức mô tả các loại entry sẽ được giữ lại.
- Tham số thứ tám: danh sách các thuộc tính được giữ lại với mỗi entry.

### 3.2. Thao tác cập nhật (update)
Chúng ta có 4 thao tác cập nhật đó là add, delete, rename (modify DN), và modify  
- Add: tạo ra một entry mới với tên DN và danh sách các thuộc tính truyền vào, khi thực hiện add một entry mới vào thư mục phải thoả các điều kiện sau :  
    - Entry là nút cha của entry mới phải tồn tại
    - Chưa tồn tại một entry nào có cùng tên DN với entry mới trên thư mục
- Delete: thao tác xóa chỉ cần truyền vào tên của entry cần xóa và thực hiện thao tác nếu:
    - Entry tồn tại
    - Entry bị xóa không có entry con bên trong
- Rename: sử dụng để đổi tên hay di chuyển các entry trong thư mục
- Update: cập nhật với tham số DN và tập hợp các thay đổi được áp dụng nếu:
    - Entry với DN phải tồn tại
    - Tất cả thuộc tính thay đổi đều thành công
    - Các thao tác cập nhật phải là các thao tác được phép
    
### 3.3. Thao tác xác thực và điều khiển (authentiaction and control)
Thao tác xác thực gồm: thao tác bind và unbind:
- Bind : cho phép client tự xác định được mình với thư mục, thao tác này cung cấp sự xác nhận và xác thực chứng thưc
- Unbind : cho phép client huỷ bỏ phân đoạn làm việc hiện hành

Thao tác điều kiển chỉ có abandon:
- Abandon : cho phép client chỉ ra các thao tác mà kết quả client không còn quan tâm đến nữa.

### 3.4. Các thao tác mở rộng
Ngoài 9 thao tác cơ bản, LDAP version 3 được thiết kế mở rộng thông qua 3 thao tác :
- Thao tác mở rộng LDAP (LDAP extended operations)
    - Đây là một thao tác mới. Trong tương lai nếu cần một thao tác mới, thì thao tác này có thể định nghĩa và trở thành chuẩn mà không yêu cầu ta phải xây dựng lại các thành phần cốt lõi của LDAP.
    - Ví dụ một thao tác mở rộng là StarTLS, nghĩa là báo cho sever rằng client muốn sử dụng transport layer security (TLS) để mã hoá và tuỳ chọn cách xác thực khi kết nối.
- LDAP control
    - Là những phần của thông tin kèm theo cùng với các thao tác LDAP, thay đổi hành vi của thao tác trên cùng một đối tượng.
- Xác thực đơn giản và tầng bảo mật (Simple Authentication and Security Layer - SASL)
    - Là một mô hình hổ trợ cho nhiều phương thức xác thực.
    - Bằng cách sử dụng mô hình SASL để thực hiện chứng thực, LDAP có thể dễ dàng thích nghi với các phương thức xác thực mới khác.
    - SASL còn hổ trợ một mô hình cho client và server có thể kết nối trên hệ thống bảo mật diễn ra ở các tầng thấp (dẫn đến độ an toàn cao).

<a name="II.4"></a>
## 4. Mô hình bảo mật Ldap (LDAP Security model)
Vấn đề cuối cùng trong các mô hình LDAP là việc bảo vệ thông tin trong thư mục khỏi các truy cập không được phép. Khi thực hiện thao tác bind dưới một tên DN hay một người vô danh (anonymous) thì với mỗi user có một số quyền thao tác trên thư mục entry. Và những quyền nào được entry chấp nhận tất cả những điều trên gọi là truy cập điều khiển (access control). Hiện nay LDAP chưa định nghĩa ra một mô hình Access Control, các điều kiện truy cập này được thiết lập bởi các nhà quản trị hệ thống bằng các server software.

<a name="III"></a>
# III. Chứng thực trong LDAP
- Việc xác thực trong một thư mục LDAP là một điều cần thiết và không thể thiếu. Quá trình xác thực được sử dụng để thiết lập quyền của khách hàng cho mỗi lần sử dụng.
- Tất cả các công việc như tìm kiếm, truy vấn, vv… được sự kiểm soát bởi các mức uỷ quyền của người được xác thực.
- Khi xác nhận một người dùng của LDAP cần tên người dùng được xác định như là một DN (ví dụ cn = cuongtv,o = it,dc = framgia,dc = com) và mật khẩu tương ứng với DN đó.
Một số phương thức xác thực người dùng: 
- Xác thực người dùng nặc danh (Anonymous Authentication)
    - Xác thực người dùng nặc danh là một xử lý ràng buộc đăng nhập vào thư mục với một tên đăng nhập và mật khẩu là rỗng. Cách đăng nhập này rất thông dụng và đuợc thường xuyên sử dụng đối với ứng dụng client.
- Xác thực nguời dùng đơn giản (Simple Authtication)
    - Đối với xác thực nguời dùng đơn giản, tên đăng nhập trong DN được gửi kèm cùng với một mật khẩu dưới dạng clear text tới máy chủ LDAP.
    - Máy chủ sẽ so sánh mật khẩu với giá trị thuộc tính userPassword hoặc với những giá trị thuộc tính đã được định nghĩa truớc trong entry cho DN đó.
    - Nếu mật khẩu được lưu dưới dạng bị băm (mã hoá), máy chủ sẽ sử dụng hàm băm tương ứng để biến đối mật khẩu đưa vào và so sánh giá trị đó với giá trị mật khẩu đã mã hoá từ trước.
    - Nếu cả hai mật khẩu trùng nhau, việc xác thực client sẽ thành công.
- Xác thực đơn giản qua SSL/TLS
    - LDAP sẽ mã hóa trước khi thực hiện bất cứ hoạt động kết nối nào. Do đó, tất cả thông tin người dùng sẽ được đảm bảo (ít nhất là trong session đó)