#Ansible up and running.


##I. Introduction.
###1. What is it Good for?

- Ansible thường xuyên được mô tả như một CM tool, và được để cập đến như là chef, puppet, và salt. khi chúng ta nói về CM, chúng ta phải nói về một số loại trạng thái mô tả cho hệ thống của chúng ta, và sau đó sử dụng tool để thực hiện cho các máy chủ, Thật đúng như vậy , ở state : những package đúng được cài đặt , cấu hình files chứa những giá trị mà ta mong muốn và có phân quyền cho chúng, những service đúng sẽ được chạy. Giống như những CM tools khác , ansible cũng chu chúng ta thấy được nó là một `Domain Specific Languge` (DSL) , đó là cái mà chúng ta sử dụng để mô tả trạng thái của hệ thống.
- Có một số tools cũng có thể sử dụng cho việc deverlopment rất tốt. Ansible cũng như vậy, Ansible là một công cụ rất tốt để dành cho việc deverlopment cũng như CM. Sử dụng một tool dành cho cả 2 công việc là Dever và CM khiến cuộc sống của chúng ta trở nên đơn giản hơn cho việc folks reponsible cho hệ thống.

###2. How Ansible Works?

- Một số trường hợp cần sử dụng đến Ansible. Cấu hình r web-server trên Ubuntu chạy Nghinx . Chúng ta sử dụng ansible và viết một Ansible script gọi là `webservers.yml` Trong ansible một script được gọi là `play-book`. Một `play-book` mô tả đó là hosts (Những gì mà Ansible gọi là remote servers) để cấu hình, và một danh sách được công việc được thực hiện trên nhiều hosts. Ví dụ ở đây chúng ta cài đặt web1, web2 và web3 , và công việc cụ thể là : 
 <ul>
 <li>Install Nghinx</li>
 <li>Tạo ra một file cấu hình nghinx</li>
 <li>Sao chép dựa trên sercurity certificate</li>
 <li>Bắt đầu nghinx service</li>
 </ul>

- Ansible sẽ thực hiện kết nối SSH song song tới web1 , web 2 và web 3. Nó sẽ thực hiện công việc đầu tiên trên list đồng thời trên cả 3 hosts. Trong ví dụ công việc đầu tiên sẽ là cài đặt Nginx apt package (Kể từ khi Ubuntu sử dụng apt package để quản lý), cho nên công việc trong playbook sẽ được thực hiện như :

```sh
name: install nginx
apt: name=nghinx
```

- Ansible sẽ : 
 <ul>
 <li>Tạo ra một script bằng Python dùng để cài đặt nghinx package.</li>
 <li>Coppy script tới web1, web2, web3</li>
 <li>Thực thi script trên web1, web2, web3.</li>
 <li>CHờ cho Script thực thi hoàn tất trên tất cả các hosts.</li>
 </ul>

- Ansible sau đó sẽ di chuyển tới công việc tiếp theo trong list, và đi thông qua 4 bước .Những chú ý quan trọng :
 <ul>
 <li>Ansible chạy mỗi công việc song song trên tất cả các hosts.</li>
 <li>Ansible chờ tới khi tới cả hosts đã hoàn tất công việc trước khi chuyển tiếp đến công việc mới trong list.</li>
 <li>Ansible chạy những công việc đã được xác định rõ ràng trong order list.</li>
 </ul>

![Screenshot_1.png](http://www.upsieutoc.com/images/2016/06/24/Screenshot_1.png)

- Trên là mô hình chạy một Ansible playbook để cấu hình 3 web-server.

**Có gì tốt từ Ansible?**

- Có nhiều sự lựa chọn Open Sources cho CM cụ thể ở đây là Ansible.

**Dễ dàng đọc cú pháp**

- Nhắc lại rằng Ansible CM scripts được gọi là playbooks. Cú pháp của Ansible playbook được xây dựng treeb top của YAML, đó là một định dạng ngôn ngữ được thiết kế dễ dàng cho người đọc cũng như viết nó. Ở đây YAML là một JSON [chưa dịch].
- Có thể chúng ta sẽ có suy nghĩ rằng Ansible playbook là một tài liệu hướng dẫn thực thi. Nó giống như README file, nơi mô tả dòng lệnh triển khai phần mềm của chúng ta, ngoại trừ cấu trúc sẽ không bao giờ go out-of-date bởi vig họ không code để thực thi trực tiếp.

**Nothing to Install on the Remote hosts**

- Để quản lý một hệ thống với Ansible, hệ thống cần phải có SSH và python 2.5 hoặc cài đặt sau đó, hoặc Python 2.4 với thư viện Python `simplejson` đã được cài đặt. Không cần cài đặt trước agent hoặc bất kỳ phần mềm nào khác trên host.
- COntrol machine (Một cách mà bạn có thể điều khiển các máy từ xa) cần phải được cào đặt Python 2.6 sau đó.

**Push-Based**

- Một số hệ thống CM sử dụng nhiều agent, giống như chef và puppet, là "Pull-Based" mặc định. Agent được cài đặt trên nhiều server, kiểm tra định kỳ với một service trung tâm và pull down thông tin cấu hình từ service. CM thay đổi từ các server một số việc giống như :
 <ul>
 <li>Bạn : làm thay đổi CM script.</li>
 <li>Bạn : Push những thay đổi về CM lên service trung tâm.</li>
 <li>Agent trên server : Được khởi động sau thời gian cháy định kỳ.</li>
 <li>Agent trên server : Kết nối tới CM service trung tâm.</li>
 <li>Agent trên server : Download những CM script mới.</li>
 <li>Agent trên server : Thực thi CM script cục bộ đó là làm thay đổi server state.</li>
 </ul>

- Ở chiều ngược lại, Ansible là "push-based" mặc định. làm thay đổi hệ thống gống như sau :
 <ul>
 <li>Bạn : Làm thay đổi một playbook. </li>
 <li>Bạn : Chạy mới một playbook.</li>
 <li>Ansible : Kết nối tới những server và thực thi modules, đó là thay đổi sercer state.</li>
 </ul>

- Ngay sau khi chúng ta chạy lệnh ansible-playbook, Ansible kết nối để remote server và làm việc của nó.
-  Push-Based giúp chúng ta tiếp cận và có thể có được lợi thế đáng kể : Chúng ta có thể điều khiển khi thay đổi xảy ra trên servers. Chúng ta không cần đợi xung quanh đến hết thời gian hiệu lực. Những người ủng hộ tiếp cận push-based yêu cầu pull với cấp cao hơn để có thể nhân rộng một số lượng lớn hơn các server và có thể đối phó với các servers mới có thể online bất kì thời gian nào. Ansible đã sử dụng thành công sản suất hàng nghìn nodes, và hỗ trợ tuyệt vời cho nhiều môi trường nơi mà server có thể được thêm vào hoặc dời đi.
-  Nếu chúng ta sẵn sàng sử dụng pull-based model, Ansible chính thức hỗ trợ cho pull mode , sử dụng một tool vận chuyển với ansible-pull.

```sh
+ Pull-based model: mô hình kéo
+ Push-based model: mô hình đẩy
```

**Ansible Scales down**

- Thật vậy, Ansible có thể được sử dụng để quản lý hàng trăm hoặc thậm chí là hàng nghìn nodes. Nhưng chúng ta sẽ nối scales down như thế nào. Sử dụng Ansible để cấu hình một node riêng lẻ là dễ dàng; chúng ta đơn giản viết một playbook đơn. Ansible tuân theo châm ngôn của `Alan Kay` đó là : Những điều đơn giản nên hãy làm cho nó trở nên đơn giản hơn, những điều phức tạp hãy làm cho nó có thể.

**Xây dựng Modules**

- Chúng ta cí thể sử dụng Ansible để thực thi lệnh SHELL bất kỳ trên server remote của chúng ta, nhưng sức mạnh thực sự của Ansible đến từ các Modules được ship đi cùng. Bạn sử dụng modules để thực hiện công việc giống như cài đặt một package, khởi động lại một service hoặc có thể là sao chép lại file cấu hình.
- Tất cả những thứ đó chúng ta sẽ được thấy sau, Ansible modules là khai báo; chúng ta sử dụng chúng để mô tả state (trạng thái) mà chúng ta muốn máy chủ đạt được. Một ví dụ : chúng ta muốn gọi ra user module như là đảm bảo có một account named "deploy"ở trong "web" group :

```sh
user: name=deploy group=web
```

- Modules cũng là "idempotent". Nếu "deloy" user không tồn tại , sau đó Ansible sữ tạo ra nó. Nếu nso tồn tại, Ansible không làm bất cứ cái gì. Idempotence là một thuộc tính rất tốt bởi vì nó nghĩa là nó sẽ chạy an toàn một ansible playbook nhiều thời gian trước khi chạy lại trên một server. Đó là một cả thiện lớn so với Shell script. Shell script chạy lần thứ 2 đã có thể khác nhau.

**Very thin layer of Abstraction**

- Một vài tools CM cung cấp một layer của absstraction cho nên bạn có thể sủ dụng giống như CM script để quản lý những máy chủ chạy khác hệ điều hành. 
- Một ví dụ : thay vì phải xử lý những package như là yum hay apt, CM tools có một "package" absstraction để cho chúng ta sử dụng thay cho những package kia.
- Ansible không giống điều đó. Chúng ta có thể sử dụng apt module để cài đặt các package trên hệ thống apt-based và yum module để cài đặt các package trên các hệ thống yum-based.
- Mặc dù điều này có vẻ như là một bất lợi trong thực tế. Chúng ta có thể dễ dàng thấy điều đó trong khi làm việc với Ansible. Ansible không yêu cầu chúng ra phải học cách để thiết lập mới một abstraction, giấu đi những thứ khác nhau giữa các hệ thống. Điều này làm cho Ansible trở lên nhỏ gọn hơn. Có rất ít thứ chúng ta cần biết trước khi chúng ta muốn bắt đầu viết một playbooks.
- Nếu chúng ta muốn , chúng ta có thể viết Ansible playbooks của chúng ta hoạt động khác nhau, tùy vào hệ thống mà chúng ta remote. Nhưng chúng ta phải cố gắng tránh khi chúng ta có thể và thay vì chúng ta tập chung viết playbooks chúng ta nên thiết kế chạy trên một HĐH cụ thể như là Ubuntu.
- Các đơn vị chính tái sử dụng Ansible community là module. Bởi vì phạm vi của một module là nhỏ và có thể là một hệ điều hành , nó trực tiếp chuyển tiếp đến implement well-defined, có thẻ chia sẻ các module. Ansible project luôn mở cửa để để đón nhận  những đóng góp từ cộng đồng.
**Is Ansible Too Simple?**

- Có một số người nói rầng "Ansible" là một vòng SSH. Nếu như bạn đang muốn có một công cụ CM vào thời điểm này có lẽ Ansible là công cụ có thể đáp ứng được nhu cầu thiết yếu của bạn.
- Như chúng ta đã tìm hiểu thì ANsible cung caaso nhiều chức năng hơn so với Shell Scripts. Điều đó nhắc nhở rằng, Module của Ansible cung cấp idempotence, và hơn thế nữa Ansible hỗ trợ thêm các template, cũng như Ansible có thể hỗ trợ các biến ở phạm vi khác nhau. Mọi người vẫn nghĩ rằng Ansible làm việc giống Shell Script, nhưng không Ansible chưa bao giờ phải duy trì một chương trình bình thường viết bằng Shell.

**What DO I Need to Know**

- Để có thể viết ra được các playbook với Ansible, chúng ta cần hiểu biết về các kiến thức về các công việc của linux system adminstrator. Ansible làm nó trở nên dễ dàng hơn trong việc tự động hóa các công việc của bạn, nhưng nó không thuộc loại công cụ "automagically" đủ thông minh để hiểu được cần phải làm nếu như không có bạn.
- Dưới đây là những gì mà cuốn sách này đem lại cho bạn.
 <ul>
 <li>Connect to a remote machine using SSH</li>
 <li>Interact with the bash command-line shell</li>
 <li>Install package</li>
 <li>Use the sudo command</li>
 <li>Check and set file permisssions</li>
 <li>Start and stop services</li>
 <li>Set environment variables</li>
 <li>Write scripts</li> 
 </ul> 

- Chúng ta không cần có các kiến thức về các ngôn ngữ lập trình cụ thể nào đó. Dành cho máy chủ, chúng ta không cần biết Python để sử dụng Ansible trừ khi bạn muốn viết một module cho riêng bạn.
- Ansible sử dụng định dạng YAML file sử dụng Jinja2 templating languages, cho nên bạn sẽ cần học YAML và Jinja2 để sử dụng Ansible, nhưng cả 2 công nghệ này rất dễ để có thể học.

**Vargant**

14 (32 of 332)


**Playbook Beginning**
