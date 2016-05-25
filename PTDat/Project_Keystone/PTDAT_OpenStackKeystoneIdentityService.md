##OpenStack Keystone Identity Service.

### Keystone architecture.

- Keystone được tổ chức như một nhóm các dịch vụ nội bộ tiếp xúc trên một hoặc nhiều thiết bị đầu cuối.
 <ul>
 <li><Identity : các dịch vụ cung cấp xác thực xác nhận chứng chỉ và dữ liệu về người sử dụng, các tenant và role, cũng như bất kì matadata nào liên quan./li>
 <li>Token : Xác nhận dịch vụ và quản lý sử dụng cho các Token. Thẩm định yêu cầu một khi thông tin người dùng đã được xác minh.</li>
 <li>Catalog : dịch vụ catalog cung cấp một enpoint registry sử dụng cho các enpoint discovery. </li>
 <li>Policy : Các dịch vụ chính sách cung cấp một động cơ cho phép dựa trên nguyên tắc.</li>
 </ul>
- Mỗi dịch vụ có thể được cấu hình để sử dụng một backend, cho phép Keystone phù hợp với một hay nhiều môi trường  và nhu cầu. Các backend cho mỗi dịch vụ được quy đinh tại file `keystone.conf`
 <ul>
 <li>KVS backend : một giao diện backend đơn giản có nghĩa là để được tiếp tục phụ trợ về bất cứ điều gì bạn có thể tra cứu khóa chính.</li>
 <li>SQL backend : một SQL dựa trên backend sử dụng SQLAlchemy để lưu trữ dữ liệu liên tục.</li>
 <li>PAM backend : backend sử dụng PAM của hệ thống hiện tại của dịch vụ để xác thực, cung cấp một mối quan hệ một - một giữa người sử dụng và người thuê.</li>
 <li>LDAP backend : Các LDAP backend lưu trữ user và
tenents riêng biệt ở các subtrees</li>
 <li>Templated backend : Một mẫu đơn giản dùng để cấu hình Keystone.</li>
 </ul> 

![scr4](http://i.imgur.com/H2esq3h.png)

![scr5](http://i.imgur.com/vOz0YRV.png)

###Keystone flowchart

![scr6](http://i.imgur.com/c2tOWip.png)

####Quản lý user Keystone


- 3 khái niệm chính của quản lý Identity user là :
 <ul>
 <li>User : Một người sử dụng đại diện cho một người sử dụng của con người, và đã liên kết các thông tin như username, password và email.</li>
 <li>Tenants : Một tenant được coi như là một dự án, nhóm hoặc tổ chức. Bất cứ khi nào bạn thực hiện yêu cầu đến OpenStack service bạn phải chỉ định một tenant.</li>
 <li>Roles: Một vai trò quy định những gì hoạt động của người dùng được phép thực hiện trong một tenant.</li>
 </ul>

- Keystone cũng hoạt động như một cửa hàng dịch vụ để cho hệ thống OpenStack khác biết nơi các API enpoint có liên quan tồn tại cho dịch vụ OpenStack. Hai khái niệm chính về quản lý dịch vụ nhận dạng là :
 <ul>
 <li>Services</li>
 <li>Enpoints</li>
 </ul>
- Các dịch vụ nhận dạng cũng duy trì một người sử dụng tương ứng cho mỗi dịch vụ (ví dụ : một người dùng có tên nova cho các compute service) một tenant sercvice đặc biệt được gọi là dịch vụ.

###Cài đặt và cấu hình cho Keystone.

  Tạo database cài đặt các gói và cấu hình keystone
- Đăng nhập vào MariaDB

	```sh
	mysql -u root -p
	```

- Tạo user, database cho keystone

	```sh
	CREATE DATABASE keystone;
	GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost'  IDENTIFIED BY 'Welcome123';
	GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' IDENTIFIED BY 'Welcome123';
	FLUSH PRIVILEGES;
	
	exit;
	```

Cài đặt và cấu hình `keystone`
- Không cho `keystone` khởi động tự động sau khi cài

	```sh
	echo "manual" > /etc/init/keystone.override
	```
- Cài đặt gói cho `keystone`

	```sh
	apt-get -y install keystone apache2 libapache2-mod-wsgi
	```

- Sao lưu file cấu hình của dịch vụ keystone trước khi chỉnh sửa.

	```sh
	cp /etc/keystone/keystone.conf /etc/keystone/keystone.conf.orig
	```

- Dùng lệnh `vi` để mở và sửa file `/etc/keystone/keystone.conf`.

 - Trong section `[DEFAULT]` khai báo dòng
 
	```sh
	admin_token = Welcome123
	```
	
 - Trong section `[database]` thay dòng `connection = sqlite:////var/lib/keystone/keystone.db` bằng dòng dưới
 
		```sh
		connection = mysql+pymysql://keystone:Welcome123@10.10.10.40/keystone
		```
	
 - Sửa file `[token]`
 
		```sh
		provider = fernet
		```
	
- Đồng bộ database cho keystone
	```sh
	su -s /bin/sh -c "keystone-manage db_sync" keystone
	```
	- Lệnh trên sẽ tạo ra các bảng trong database có tên là keysonte

- Thiết lập `Fernet` key

	```sh
	keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone
	```

- Cấu hình apache cho `keysonte`

 - Dùng `vi` để mở và sửa file `/etc/apache2/apache2.conf`. Thêm dòng dưới ngay sau dòng `# Global configuration`

	 ```sh
	 # Global configuration
	 ServerName controller
	 ```

- Sử dụng `vi` để tạo file `/etc/apache2/sites-available/wsgi-keystone.conf` chứa nội dung dưới

```sh
Listen 5000
Listen 35357

<VirtualHost *:5000>
	WSGIDaemonProcess keystone-public processes=5 threads=1 user=keystone group=keystone display-name=%{GROUP}
	WSGIProcessGroup keystone-public
	WSGIScriptAlias / /usr/bin/keystone-wsgi-public
	WSGIApplicationGroup %{GLOBAL}
	WSGIPassAuthorization On
	<IfVersion >= 2.4>
	  ErrorLogFormat "%{cu}t %M"
	</IfVersion>
	ErrorLog /var/log/apache2/keystone.log
	CustomLog /var/log/apache2/keystone_access.log combined

	<Directory /usr/bin>
		<IfVersion >= 2.4>
			Require all granted
		</IfVersion>
		<IfVersion < 2.4>
			Order allow,deny
			Allow from all
		</IfVersion>
	</Directory>
</VirtualHost>

<VirtualHost *:35357>
	WSGIDaemonProcess keystone-admin processes=5 threads=1 user=keystone group=keystone display-name=%{GROUP}
	WSGIProcessGroup keystone-admin
	WSGIScriptAlias / /usr/bin/keystone-wsgi-admin
	WSGIApplicationGroup %{GLOBAL}
	WSGIPassAuthorization On
	<IfVersion >= 2.4>
	  ErrorLogFormat "%{cu}t %M"
	</IfVersion>
	ErrorLog /var/log/apache2/keystone.log
	CustomLog /var/log/apache2/keystone_access.log combined

	<Directory /usr/bin>
		<IfVersion >= 2.4>
			Require all granted
		</IfVersion>
		<IfVersion < 2.4>
			Order allow,deny
			Allow from all
		</IfVersion>
	</Directory>
</VirtualHost>
```

- Tạo link để cấu hình virtual host cho dịch vụ `keysonte` trong `apache`

```sh
ln -s /etc/apache2/sites-available/wsgi-keystone.conf /etc/apache2/sites-enabled
```

- Khởi động lại `apache`
	```sh
	service apache2 restart
	```

- Xóa file database mặc định của `keysonte` 
	```sh
	rm -f /var/lib/keystone/keystone.db
	```


Tạo endpoint và các service cho `keystone`


- Khai báo sử dụng `token` để xác thực.

	```sh
	export OS_TOKEN=Welcome123
	export OS_URL=http://controller:35357/v3
	export OS_IDENTITY_API_VERSION=3
	```

- Tạo các service và endpoint cho `keysonte`
	```sh
	openstack service create \
	  --name keystone --description "OpenStack Identity" identity
	```

- Tạo các endpoint
	```sh
	openstack endpoint create --region RegionOne identity public http://controller:5000/v3
	  
	openstack endpoint create --region RegionOne identity internal http://controller:5000/v3
	  
	openstack endpoint create --region RegionOne identity admin http://controller:35357/v3
	```

 
Tạo domain, projects, users, and roles

- Tạo domain

	```sh
	openstack domain create --description "Default Domain" default
	```

- Tạo `admin` project

	```sh
	openstack project create --domain default  --description "Admin Project" admin
	```

- Tạo user `admin`
	```sh
	openstack user create admin --domain default --password Welcome123
	```

- Tạo role `admin`
	```sh
	openstack role create admin
	```

- Gán user `admin` vào role `admin` thuộc project `admin`
	```sh
	openstack role add --project admin --user admin admin
	```

- Tạo project có tên là `service` để chứa các user service của openstack
	```sh
	openstack project create --domain default --description "Service Project" service
	```

- Tạo project tên là `demo`
	```sh
	openstack project create --domain default --description "Demo Project" demo
	```

- Tạo user tên là `demo`
	```sh
	openstack user create demo --domain default --password Welcome123
	```

- Tạo role tên là `user`
	```sh
	openstack role create user
	```

- Gán tài khoản `demo` có role là `user` vào project `demo`
	```sh
	openstack role add --project demo --user demo user
	```


Kiểm chứng lại các bước cài đặt `keysonte`


- Vô hiệu hóa cơ chế xác thực bằng token tạm thời trong `keysonte` bằng cách xóa `admin_token_auth` trong các section `[pipeline:public_api]`,  `[pipeline:admin_api]`  và `[pipeline:api_v3]` của file `/etc/keystone/keystone-paste.ini`

- Bỏ thiết lập trong biến môi trường của `OS_TOKEN` và `OS_URL` bằng lệnh
	```sh
	unset OS_TOKEN OS_URL
	```

- Gõ lần lượt 2 lệnh dưới sau đó nhập mật khẩu
	```sh
	openstack --os-auth-url http://controller:35357/v3 \
	--os-project-domain-name default --os-user-domain-name default \
	--os-project-name admin --os-username admin token issue

	và 

	openstack --os-auth-url http://controller:5000/v3 \
	--os-project-domain-name default --os-user-domain-name default \
	--os-project-name demo --os-username demo token issue
	```


###Keystone Workflow.

![scr7](http://i.imgur.com/1o2wFpV.png)

