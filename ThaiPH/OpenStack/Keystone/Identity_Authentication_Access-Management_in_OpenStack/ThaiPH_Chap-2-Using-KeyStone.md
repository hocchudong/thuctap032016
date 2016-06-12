#Chương 2: Sử dụng Keystone

#Mục lục
<h4><a href="#devstack">2.1. Cài đặt OpenStack với DevStack</a></h4>
<h4><a href="#cli">2.2. Sử dụng OpenStack client (CLI) vận hành Keystone</a></h4>
<ul>
<li><h5><a href="#1">2.2.1. Lấy token</a></h5></li>
<li><h5><a href="#2">2.2.2. Liệt kê danh sách các user</a></h5></li>
<li><h5><a href="#3">2.2.3. Liệt kê các project</a></h5></li>
<li><h5><a href="#4">2.2.4. Liệt kê các group</a></h5></li>
<li><h5><a href="#5">2.2.5. Liệt kê các role</a></h5></li>
<li><h5><a href="#6">2.2.6. Liệt kê các domain</a></h5></li>
<li><h5><a href="#7">2.2.7. Tạo domain mới</a></h5></li>
<li><h5><a href="#8">2.2.8. Tạo project trong domain</a></h5></li>
<li><h5><a href="#9">2.2.9. Tạo người dùng trong domain</a></h5></li>
<li><h5><a href="#10">2.2.10. Gán role cho người dùng trong một project</a></h5></li>
<li><h5><a href="#11">2.2.11. Xác thực với tài khoản người dùng mới</a></h5></li>
</ul>
<h4><a href="#horizon">2.3. Sử dụng OpenStack client trên Horizon vận hành Keystone</a></h4>
<ul>
<li><h5><a href="#231">2.3.1. Các thao tác vận hành Keystone sẵn sàng thông qua horizon</a></h5></li>
<li><h5><a href="#232">2.3.2. Truy cập các thao tác vận hành Identityr</a></h5></li>
<li><h5><a href="#233">2.3.3. List, Set, Delete, Create, View as Project</a></h5></li>
<li><h5><a href="#234">2.3.4. List, Set, Delete, Create, View as User</a></h5></li>
</ul>
<h4><a href="#tip">2.4. Tips, Trouleshooting</a></h4>

---

<i>Nội dung: Sử dụng Keystone trong môi trường phát triển (dev và test), sử dụng DevStack. Bắt đầu từ bước triển khai OpenStack với DevStack, sau đó thử vận hành Keystone sử dụng OpenStack client (CLI), sau đó thực hiện các thao tác vận hành tương tự sử dụng Horizon. Ngoài ra còn giải pháp thay thế sử dụng cURL command.</i>

<ul>
<li><h3><a name="devstack">2.1. Cài đặt OpenStack với DevStack</a></h3>
Sử dụng VMware hoặc VirtualBox cài Ubuntu 64 bit. Sau đó thực hiện việc cài đặt OpenStack sử dụng DevStack. Trước hết tải mã nguồn DevStack về: 
<pre>
<code>
cd ~
sudo apt-get install git curl
git clone https://github.com/openstack-dev/devstack/
cd devstack
</code>
</pre>
Trong thư mục devstack tạo file local.conf để chỉ ra những project nào muốn cài đặt (Keystone, Nova, Glance, Cinder, Horizon), một số cấu hình liên quan. Nội dung file local.conf như sau:
<pre>
<code>
[[local|localrc]]
RECLONE=yes
# Credentials
DATABASE_PASSWORD=openstack
ADMIN_PASSWORD=openstack
SERVICE_PASSWORD=openstack
SERVICE_TOKEN=openstack
RABBIT_PASSWORD=openstack
# Services
ENABLED_SERVICES=rabbit,mysql,key
ENABLED_SERVICES+=,horizon
ENABLED_SERVICES+=,n-api,n-crt,n-obj,n-cpu,n-cond,n-sch,n-novnc,n-cauth
ENABLED_SERVICES+=,n-net
ENABLED_SERVICES+=,g-api,g-reg
ENABLED_SERVICES+=,cinder,c-api,c-vol,c-sch,c-bak
# Enable Logging
LOGFILE=/opt/stack/logs/stack.sh.log
VERBOSE=True
LOG_COLOR=True
SCREEN_LOGDIR=/opt/stack/logs
</code>
</pre>

Cuối dùng thực thi file stack.sh để bắt đầu quá trình cài đặt:
<pre>
<code>
./stack.sh
</code>
</pre>

Sau khi cài đặt xong, kết quả trả về sẽ tương tự như sau:
<pre>
<code>
This is your host IP address: 10.0.2.15
This is your host IPv6 address: ::1
Horizon is now available at http://10.0.2.15/
Keystone is serving at http://10.0.2.15:5000/
The default users are: admin and demo
The password: openstack
</code>
</pre>

</li>

<li><h3><a name="cli">2.2. Sử dụng OpenStack client (CLI) vận hành Keystone</a></h3>
Trước hết thiết lập biến môi trường cho máy ảo Ubuntu 14.04. Chú ý các giá trị hostname và IP phải tùy chỉnh lại cho phù hợp. Ví dụ như sau:
<pre>
<code>
export OS_IDENTITY_API_VERSION=3
export OS_AUTH_URL=http://10.0.2.15:5000/v3
export OS_USERNAME=admin
export OS_PROJECT_NAME=admin
export OS_USER_DOMAIN_NAME=Default
export OS_PASSWORD=openstack
export OS_PROJECT_DOMAIN_NAME=Default
</code>
</pre>
<br>
Để kiểm tra biến môi trường đã thiết lập chưa, dùng lệnh sau:
<br>
<pre>
<code>
$ env | grep OS
OS_IDENTITY_API_VERSION=3
OS_AUTH_URL=http://10.0.2.15:5000/v3
OS_USERNAME=admin
OS_PROJECT_NAME=admin
OS_USER_DOMAIN_NAME=Default
OS_PASSWORD=openstack
OS_PROJECT_DOMAIN_NAME=Default
</code>
</pre>

<ul>
<li><h3><a name="1">2.2.1. Lấy Token</a></h3><br>
<b>Sử dụng OpenStack client</b>
<br>
Nếu đã thiết lập dữ liệu xác thực và ủy quyền dữ liệu như các biến môi trường, sử dụng lệnh sau để tạo ra một token:
<pre>
<code>
$ openstack token issue
+------------+----------------------------------+
| Field      | Value                            |
+------------+----------------------------------+
| expires    | 2015-08-27T21:45:41.712853Z      |
| id         | d219ca63fd2548f685fea48623b22a10 |
| project_id | 92841d1c386643a08c697c833ed840af |
| user_id    | 82d7e61f128b4e398bb165f278f45569 |
+------------+----------------------------------+
</code>
</pre>
<b>Sử dụng cURL</b>
<br>
Khi sử dụng cURL để lấy token, payload trong request xác thực phải bao gồm các thông tin về user và project

<pre>
<code>
$ curl -i -H "Content-Type: application/json" -d '
{ "auth": {
"identity": {
"methods": ["password"],
"password": {
"user": {
"name": "admin",
"domain": { "name": "Default" },
"password": "openstack"
}
}
},
"scope": {
"project": {
"name": "admin",
"domain": { "name": "Default" }
}
}
}
}' http://localhost:5000/v3/auth/tokens
HTTP/1.1 201 Created
Date: Thu, 27 Aug 2015 21:57:56 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Subject-Token: 2511aaa898ff42158addea8c90ba2622
Vary: X-Auth-Token
x-openstack-request-id: req-ab469b0e-6990-4cca-9b1a-98780ae4108a
Content-Length: 5276
Content-Type: application/json
{"token": {"methods": ["password"], "roles": [{"id": "2d357899bd5c430988772eb861f
b7a68", "name": "admin"}], "expires_at": "2015-08-27T22:57:58.249918Z",
"project": {"domain": {"id": "default", "name": "Default"}, "id": "ed50269971bc41
ef9f25ce2c7e9b9d11", "name": "admin"}, "catalog": [{"endpoints": [{"region_id":
"RegionOne", "url": "http://10.0.2.15:35357/v2.0", "region": "RegionOne",
"interface": "admin", "id": "19dfab5f51b24dbe8cfc0e7d5f4677a7"}, {"region_id":
"RegionOne", "url": "http://10.0.2.15:5000/v2.0", "region": "RegionOne",
"interface": "internal", "id": "763fef84e9bd43b58733813d5b1f29bb"}, {"region_id":
"RegionOne", "url": "http://10.0.2.15:5000/v2.0", "region": "RegionOne",
"interface": "public", "id": "d210b05177b24733b40146f7dcafdb90"}], "type":
"identity", "id": "8ae94fc3bb534ef2ae5bc16979e28eaf", "name": "keystone"}],
"extras": {}, "user": {"domain": {"id": "default", "name": "Default"}, "id":
"9644330bc62542c491179895c6a6d228", "name": "admin"}, "audit_ids": ["2h1Ass48TvKn
Oa4u3LR3HA"], "issued_at": "2015-08-27T21:57:58.249944Z"}}
</code>
</pre>

</li>

<li><h3><a name="2">2.2.2. Liệt kê danh sách các user</a></h3><br>
<b>Sử dụng OpenStackClient</b>
<br>
Sau khi chạy DevStack, nhiều user sẽ tự động được tạo ra trong đó có các service account cho các dịch vụ của OpenStack (Cinder, Glance, Nova), một tài khoản quản trị(admin) và một tài khoản không phải tài khoản quản trị(demo)
<br>
<pre>
<code>
$ openstack user list
+----------------------------------+--------+
| ID                               | Name   |
+----------------------------------+--------+
| 05a77e13219949c59368b99047b6be4b | cinder |
| 4da7bd7e25f34ea4aca792055f715fb8 | admin  |
| 8e30d2d495eb467b8b673fbdfb8be6c7 | glance |
| ae760d23927b467e910146e4e9f400c0 | nova   |
| f6ddb1f6568942cbb85fdbf441c45c05 | demo   |
+----------------------------------+--------+
</code>
</pre>

<b>Sử dụng cURL</b>
<br>
<pre>
<code>
$ curl -s -H "X-Auth-Token: $OS_TOKEN" \
http://localhost:5000/v3/users | python -mjson.tool
{
"links": {
"next": null,
"previous": null,
"self": "http://localhost:5000/v3/users"
},
"users": [
{
"domain_id": "default",
"enabled": true,
"id": "0aa473010af04acb86018125ef71a65e",
"links": {
"self": "http://localhost:5000/v3/users/0aa473010a...125ef71a65e"
},
"name": "glance"
},
{
"domain_id": "default",
"enabled": true,
"id": "9644330bc62542c491179895c6a6d228",
"links": {
"self": "http://localhost:5000/v3/users/96443...91179895c6a6d228"
},
"name": "admin"
},
{
"domain_id": "default",
"enabled": true,
"id": "ab7ab1f3fe2745fd91b3d62fd3b7309b",
"links": {
"self": "http://localhost:5000/v3/users/ab7a...d91b3d62fd3b7309b"
},
"name": "cinder"
},
{
"domain_id": "default",
"email": "demo@example.com",
"enabled": true,
"id": "c88b8fa1414e44be918e9e129f04147d",
"links": {
"self": "http://localhost:5000/v3/users/c88b8fa...8e9e129f04147d"
},
"name": "demo"
},
{
"domain_id": "default",
"enabled": true,
"id": "cf15631f360c4db18fc95fe95da827f2",
"links": {
"self": "http://localhost:5000/v3/users/cf1563...fc95fe95da827f2"
},
"name": "nova"
}
]
}
</code>
</pre>

</li>

<li><h3><a name="3">2.2.3. Liệt kê các project</a></h3><br>
<b>Sử dụng OpenStackClient</b>
<br>
<pre>
<code>
$ openstack project list
+----------------------------------+--------------------+
| ID                               | Name               |
+----------------------------------+--------------------+
| 10bc96bf62c14d44b02bb5ad8aef57d3 | admin              |
| 241d8b116a164bcb9c63d75117ed3894 | demo               |
| 81dc6de893924fbbbf16f272bdfba38d | invisible_to_admin |
| ebad3ef327c143bb8e79a52b9b0324e8 | service            |
+----------------------------------+--------------------+
</code>
</pre>
<b>Sử dụng cURL</b>
<br>
<pre>
<code>
$ curl -s -H "X-Auth-Token: $OS_TOKEN" \
http://localhost:5000/v3/projects | python -mjson.tool
{
"links": {
"next": null,
"previous": null,
"self": "http://localhost:5000/v3/projects"
},
"projects": [
{
"description": "",
"domain_id": "default",
"enabled": true,
"id": "5f198c74b0984566b0a6da26440c5f85",
"is_domain": false,
"links": {
"self": "http://localhost:5000/v3/projects/5f1...0a6da26440c5f85"
},
"name": "demo",
"parent_id": null
},
{
"description": "",
"domain_id": "default",
"enabled": true,
"id": "9457bf6cb940453ab92a88219a40a3f7",
"is_domain": false,
"links": {
"self": "http://localhost:5000/v3/projects/9457bf6cb9...9a40a3f7"
},
"name": "service",
"parent_id": null
},
{
"description": "",
"domain_id": "default",
"enabled": true,
"id": "dcd882c878bd43188f9758831676559a",
"is_domain": false,
"links": {
"self": "http://localhost:5000/v3/projects/dcd882c878...1676559a"
},
"name": "invisible_to_admin",
"parent_id": null
},
{
"description": "",
"domain_id": "default",
"enabled": true,
"id": "ed50269971bc41ef9f25ce2c7e9b9d11",
"is_domain": false,
"links": {
    "self": "http://localhost:5000/v3/projects/ed5026997...c7e9b9d11"
},
"name": "admin",
"parent_id": null
}
]
}    
</code>
</pre>

</li>

<li><h3><a name="4">2.2.4. Liệt kê các group</a></h3><br>
<b>Sử dụng OpenStackClient</b>
<br>
<pre>
<code>
$ openstack group list
+----------------------------------+-----------+
| ID                               | Name      |
+----------------------------------+-----------+
| a95873d6a7f54dae90e53de3044b0964 | nonadmins |
| e27d8f1c492441888ea4b0a7e836a835 | admins    |
+----------------------------------+-----------+
</code>
</pre>

<b>Sử dụng cURL</b>
<br>
<pre>
<code>
$ curl -s -H "X-Auth-Token: $OS_TOKEN" \
http://localhost:5000/v3/groups | python -mjson.tool
{
"groups": [
{
"description": "openstack admin group",
"domain_id": "default",
"id": "5553cf58254746c8ba615b671dcdc5b2",
"links": {
"self": "http://localhost:5000/v3/groups/5553cf582...1dcdc5b2"
},
"name": "admins"
},
{
"description": "non-admin group",
"domain_id": "default",
"id": "8a2e550b2edc4f76bae608e578becf5c",
"links": {
"self": "http://localhost:5000/v3/groups/8a2e550b2...8e578becf5c"
},
"name": "nonadmins"
}
],
"links": {
"next": null,
"previous": null,
"self": "http://localhost:5000/v3/groups"
}
}
</code>
</pre>
</li>

<li><h3><a name="5">2.2.5. Liệt kê các role</a></h3><br>
<b>Sử dụng OpenStackClient</b>
<br>
<pre>
<code>
$ openstack role list
+----------------------------------+---------------+
| ID                               | Name          |
+----------------------------------+---------------+
| 03bdd6d46c2c4f99818bc855872a909e | service       |
| 4684cf02622f49dd82458852c62f4135 | Member        |
| 8a5dbcef99274f688effa338db6bf928 | anotherrole   |
| a22b737940ed4e7588639f1bcb3e3afa | admin         |
| b5e5224549574edf9ff2caebbda9431d | ResellerAdmin |
+----------------------------------+---------------+
</code>
</pre>

<b>Sử dụng cURL</b>
<br>
<pre>
<code>
$ curl -s -H "X-Auth-Token: $OS_TOKEN" \
http://localhost:5000/v3/roles | python -mjson.tool
{
"links": {
"next": null,
"previous": null,
"self": "http://localhost:5000/v3/roles"
},
"roles": [
{
"id": "20cd9e77e2d44d3490d8c044f508c8f3",
"links": {
"self": "http://localhost:5000/v3/roles/20cd9e77e...044f508c8f3"
},
"name": "service"
},
{
"id": "2d357899bd5c430988772eb861fb7a68",
"links": {
"self": "http://localhost:5000/v3/roles/2d357899b...eb861fb7a68"
},
"name": "admin"
},
{
"id": "40df936c87824fd98b7e39da44f2dbde",
"links": {
"self": "http://localhost:5000/v3/roles/40df936c8...9da44f2dbde"
},
"name": "Member"
},
{
"id": "d1e7fed5471941b9aeebf15a341edef9",
"links": {
"self": "http://localhost:5000/v3/roles/d1e7fed54...15a341edef9"
},
"name": "ResellerAdmin"
},
{
"id": "face2e488b1c4562bc9f43f8a5e143db",
"links": {
"self": "http://localhost:5000/v3/roles/face2e488...3f8a5e143db"
},
"name": "anotherrole"
}
]
}
</code>
</pre>
</li>

<li><h3><a name="6">2.2.6. Liệt kê các domain</a></h3><br>
<b>Sử dụng OpenStackClient</b>
<br>
<pre>
<code>
$ openstack domain list
+---------+---------+---------+----------------------------------------------+
| ID      | Name    | Enabled | Description                                  |
+---------+---------+---------+----------------------------------------------+
| default | Default | True    | Owns users and projects for Identity API v2. |
+---------+---------+---------+----------------------------------------------+
</code>
</pre>

<b>Sử dụng cURL</b>
<br>
<pre>
<code>
$ curl -s -H "X-Auth-Token: $OS_TOKEN" \
http://localhost:5000/v3/domains | python -mjson.tool
{
"domains": [
{
"description": "Owns users and projects for Identity API v2.",
"enabled": true,
"id": "default",
"links": {
"self": "http://localhost:5000/v3/domains/default"
},
"name": "Default"
}
],
"links": {
"next": null,
"previous": null,
"self": "http://localhost:5000/v3/domains"
}
}
</code>
</pre>
</li>

<li><h3><a name="7">2.2.7. Tạo domain mới</a></h3><br>
<b>Sử dụng OpenStackClient</b>
<br>
<pre>
<code>
$ openstack domain create acme
+---------+----------------------------------+
| Field   | Value                            |
+---------+----------------------------------+
| enabled | True                             |
| id      | adf547d21ae148aa81c77b36b611d1c3 |
| name    | acme                             |
+---------+----------------------------------+
</code>
</pre>

<b>Sử dụng cURL</b>
<br>
<pre>
<code>
$ curl -s -H "X-Auth-Token: $OS_TOKEN" \
-H "Content-Type: application/json" -d '{ "domain": { "name": "acme"}}'
http://localhost:5000/v3/domains | python -mjson.tool
{
"domain": {
"enabled": true,
"id": "05a0fcbf796142bfbeb30d0fd3dfa67a",
"links": {
"self": "http://localhost:5000/v3/domains/05a0fcbf796142b...d3dfa67a"
},
"name": "acme"
}
}
</code>
</pre>

</li>

<li><h3><a name="8">2.2.8. Tạo project trong domain</a></h3><br>
<b>Sử dụng OpenStackClient</b>
<br>
<pre>
<code>
$ openstack project create tims_project \
--domain acme \
--description "tims dev project"
+-------------+----------------------------------+
| Field       | Value                            |
+-------------+----------------------------------+
| description | tims dev project                 |
| domain_id   | adf547d21ae148aa81c77b36b611d1c3 |
| enabled     | True                             |
| id          | 77941c6a73ed452eb65d36d7c962201c |
| is_domain   | False                            |
| name        | tims_project                     |
| parent_id   | None                             |
+-------------+----------------------------------+
</code>
</pre>

<b>Sử dụng cURL</b>
<br>
<pre>
<code>
$ curl -s -H "X-Auth-Token: $OS_TOKEN" \
-H "Content-Type: application/json" \
-d '{ "project": { "name": "tims_project", \
"domain_id": "05a0fcbf796142bfbeb30d0fd3dfa67a", \
"description": "tims dev project"}}' \
http://localhost:5000/v3/projects | python -mjson.tool
{
"project": {
"description": "tims dev project",
"domain_id": "05a0fcbf796142bfbeb30d0fd3dfa67a",
"enabled": true,
"id": "26436cea94ac4a40b890f05434f15aa4",
"is_domain": false,
"links": {
"self": "http://localhost:5000/v3/projects/26436cea94ac4...434f15aa4"
},
"name": "tims_project",
"parent_id": null
}
}
</code>
</pre>

</li>

<li><h3><a name="9">2.2.9. Tạo người dùng trong domain</a></h3><br>
<b>Sử dụng OpenStackClient</b>
<br>
<pre>
<code>
$ openstack user create tim --email tim@tim.ca \
--domain acme --description "tims openstack user account" \
--password s3cr3t
+-------------+----------------------------------+
| Field       | Value                            |
+-------------+----------------------------------+
| description | tims openstack user account      |
| domain_id   | adf547d21ae148aa81c77b36b611d1c3 |
| email       | tim@tim.ca                       |
| enabled     | True                             |
| id          | a5db8e8e6a994e05afe94aa21c8c4ec8 |
| name        | tim                              |
+-------------+----------------------------------+
</code>
</pre>
<b>Sử dụng cURL</b>
<br>
<pre>
<code>
$ curl -s -H "X-Auth-Token: $OS_TOKEN" \
-H "Content-Type: application/json" \
-d '{ "user": { "name": "tim", "password": "s3cr3t", \
"email": "tim@tim.ca", "domain_id": \
"05a0fcbf796142bfbeb30d0fd3dfa67a", "description": \
"tims openstack user account"}}' http://localhost:5000/v3/users \
| python -mjson.tool
{
"user": {
"description": "tims openstack user account",
"domain_id": "05a0fcbf796142bfbeb30d0fd3dfa67a",
"email": "tim@tim.ca",
"enabled": true,
"id": "6eced805da4649198dd1dd3bdddadd68",
"links": {
"self": "http://localhost:5000/v3/users/6eced805da4649198dd...dadd68"
},
"name": "tim"
}
}
</code>
</pre>

</li>

<li><h3><a name="10">2.2.10. Gán role cho người dùng trong một project</a></h3><br>
<b>Sử dụng OpenStackClient</b>
<br>
<pre>
<code>
$ openstack role add member --project tims_project --project-domain acme \
--user tim --user-domain acme
</code>
</pre>

<b>Sử dụng cURL</b>
<br>
<pre><code>
$ curl -s -X PUT -H "X-Auth-Token: $OS_TOKEN" \
http://localhost:5000/v3/projects/26436cea94ac4a40b890f05434f15aa4/users/6ece
d805da4649198dd1dd3bdddadd68/roles/40df936c87824fd98b7e39da44f2dbde
</code>
</pre>

</li>

<li><h3><a name="11">2.2.11. Xác thực với tài khoản người dùng mới</a></h3><br>
<b>Sử dụng OpenStackClient</b>
<br>
Thiết lập các biến môi trường, như user name, passwd, project, domain như sau:
<br>
<pre>
<code>
export OS_PASSWORD=s3cr3t
export OS_IDENTITY_API_VERSION=3
export OS_AUTH_URL=http://10.0.2.15:5000/v3
export OS_USERNAME=tim
export OS_PROJECT_NAME=tims_project
export OS_USER_DOMAIN_NAME=acme
export OS_PROJECT_DOMAIN_NAME=acme
</code>
</pre>

Thu thập token để đảm bảo người dùng có khả năng xác thực.
<br>
<pre>
<code>
$ openstack token issue
+------------+----------------------------------+
| Field      | Value                            |
+------------+----------------------------------+
| expires    | 2015-08-22T05:26:02.385430Z      |
| id         | 59c60758f9f947a58289900c1f87b700 |
| project_id | 77941c6a73ed452eb65d36d7c962201c |
| user_id    | 26898b5d27114f90a1f57c5333e3e9b4 |
+------------+----------------------------------+
</code>
</pre>

<b>Sử dụng cURL</b>
<br>
Tương tự như mục 2.2.1, cấu trúc payload tương tự như vậy nhưng cập nhật lại các giá trị. Để đơn giản, chúng ta sẽ gỡ bỏ thông tin các endpoints trong service catalog
<br>
<pre>
<code>
$ curl -i -H "Content-Type: application/json" -d ' "identity": {
"methods": ["password"],
"password": {
"user": {
"name": "tim",
"domain": { "name": "acme" },
"password": "s3cr3t"
}
}
},
"scope": {
"project": {
    "name": "tims_project",
"domain": { "name": "acme" }
}
}
}
}' http://localhost:5000/v3/auth/tokens
HTTP/1.1 201 Created
Date: Thu, 27 Aug 2015 22:47:01 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Subject-Token: 1bce8850bc6c4b9e8e90b6822885d93c
Vary: X-Auth-Token
x-openstack-request-id: req-a71ec134-60d8-4f86-8546-00877a48151f
Content-Length: 5326
Content-Type: application/json
{"token": {"methods": ["password"], "roles": [{"id": "4
0df936c87824fd98b7e39da44f2dbde", "name": "Member"}], "expires_at": "2015-08-27T2
3:47:01.322257Z", "project": {"domain": {"id": "05a0fcbf796142bfbeb30d0fd3dfa67a"
, "name": "acme"}, "id": "26436cea94ac4a40b890f05434f15aa4", "name": "tims_projec
t"}, "catalog": [{"endpoints": [{"region_id": "RegionOne", "url": "http://10.0.2.
15:35357/v2.0", "region": "RegionOne", "interface": "admin", "id": "19dfab5f51b24
dbe8cfc0e7d5f4677a7"}, {"region_id": "RegionOne", "url": "http://10.0.2.15:5000/v
2.0", "region": "RegionOne", "interface": "internal", "id": "763fef84e9bd43b58733
813d5b1f29bb"}, {"region_id": "RegionOne", "url": "http://10.0.2.15:5000/v2.0", "
region": "RegionOne", "interface": "public", "id": "d210b05177b24733b40146f7dcafd
b90"}], "type": "identity", "id": "8ae94fc3bb534ef2ae5bc16979e28eaf", "name": "ke
ystone"}], "extras": {}, "user": {"domain": {"id": "05a0fcbf796142bfbeb30d0fd3dfa
67a", "name": "acme"}, "id": "6eced805da4649198dd1dd3bdddadd68", "name": "tim"},
"audit_ids": ["rWvgwqBWSjq3sZgGWFNmVg"], "issued_at": "2015-08-27T22:47:01.322285
Z"}}
</code>
</pre>
Còn nhiều command khác mà người dùng hoặc quản trị viên có thể thực hiện, chi tiết hơn có thể sử dụng lệnh: <code>openstack --help</code> để tìm hiểu các command khác hoặc đọc tài liệu OpenStackClient. 
</li>

</ul>

</li>

<li><h3><a name="horizon">2.3. Sử dụng OpenStack client trên Horizon vận hành Keystone</a></h3>
<ul>
<li><h3><a name="231">2.3.1. Các thao tác vận hành Keystone sẵn sàng thông qua horizon</a></h3>
<ul>
<li>Nhiều thao tác vận hành Keystone có thể thực hiện qua Horizon, phụ thuộc vào file cấu hình Horizon.</li>
<li>Nếu enable v2 của Identity API, chỉ các thao tác CRUD với User và Project là được hỗ trợ (CRUD - Create, Read, Update, Delete).</li>
<li>Nếu enable v3 của Identity API, các thao tác CRUD với User, Group, Project, Domain, và Role đều được hỗ trợ, người dùng có thể xác thực trên nhiều domains.</li>
</ul>
</li>
    
<li><h3><a name="232">2.3.2. Truy cập các thao tác vận hành Identity</a></h3>
<br>
<img src="http://i.imgur.com/hMz0QaM.png"/>
</li>

<li><h3><a name="233">2.3.3. List, Set, Delete, Create, View as Project</a></h3>
<br>
<img src="http://i.imgur.com/GnplzJe.png"/>
</li>

<li><h3><a name="234">2.3.4. List, Set, Delete, Create, View as User</a></h3>
<br>
<img src="http://i.imgur.com/Dv38eLj.png"/>
</li>
</ul>

<li><h3><a name="tip">2.4. Tips, Trouleshooting</a></h3></li>
</ul>

