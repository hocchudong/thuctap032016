Glance API


cURl API

CURL dùng để gửi request đến một đường dẫn trên Internet nào đó.

Check ID 
```sh
openstack user list
openstack project list
openstack domain list
```

```sh
root@controller:~# openstack user list
+----------------------------------+---------+
| ID                               | Name    |
+----------------------------------+---------+
| 05ecda2354d543469bb406398d6a85d2 | glance  |
| 109e83c7df52490e828fe0e37d700a27 | admin   |
| 19190768472040d198ef1ddc66d4808d | demo    |
| 22caed81974049bbb83558650d4c465c | neutron |
| f918c0382392424aac4b31fb6833c23c | nova    |
+----------------------------------+---------+
```

1 Get token
ARC
<img src= 
cURL

```sh 
root@controller:~# curl -i \
   -H "Content-Type: application/json" \
   -d '
 { "auth": {
     "identity": {
       "methods": ["password"],
       "password": {
         "user": {
           "id": "109e83c7df52490e828fe0e37d700a27",
           "password": "Welcome123"
         }
       }
     }
   }
 }' \
   http://10.10.10.40:5000/v3/auth/tokens ; echo
```
Kết quả trả về ta có token thuộc trường X-Subject-Token:
```sh
HTTP/1.1 201 Created
Date: Mon, 13 Jun 2016 15:37:12 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Subject-Token: gAAAAABXXtMoGTOvOfBdYIRMkwHvHIZLAGm6682RCb90QnZIkjm-jQd0WsjnTzeen-MLYkHdE2JL7Q6sA2ClxpJ24R-J8mdMHE_NDNF_t-MM49YBdWgAc4B48sgtlneRE6Nngyz1ltiRp3Zbyey74EtMGCSM49oz5Q
Vary: X-Auth-Token
X-Distribution: Ubuntu
x-openstack-request-id: req-03b6d033-f6f9-4d26-a4ac-c7585dc4bcd7
Content-Length: 308
Content-Type: application/json

{"token": {"issued_at": "2016-06-13T15:37:12.000000Z", "audit_ids": ["IouiUnFzRQiUCdPpgDd2Lg"], "methods": ["password"], "expires_at": "2016-06-13T16:37:12.438968Z", "user": {"domain": {"id": "fb3daecd2b494325b551de7bd1a11c75", "name": "default"}, "id": "109e83c7df52490e828fe0e37d700a27", "name": "admin"}}}
```

2 List image
```sh
curl -i \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXtMoGTOvOfBdYIRMkwHvHIZLAGm6682RCb90QnZIkjm-jQd0WsjnTzeen-MLYkHdE2JL7Q6sA2ClxpJ24R-J8mdMHE_NDNF_t-MM49YBdWgAc4B48sgtlneRE6Nngyz1ltiRp3Zbyey74EtMGCSM49oz5Q" \
  http://10.10.10.40:9292/v2/images ; echo
```
Kết quả trả về:
```sh
HTTP/1.1 200 OK
Content-Length: 651
Content-Type: application/json; charset=UTF-8
X-Openstack-Request-Id: req-71d86b9d-4a41-4bc9-a107-b4f9ad3e4fbf
Date: Mon, 13 Jun 2016 15:39:40 GMT

{"images": [{"status": "active", "name": "test", "tags": [], "container_format": "bare", "created_at": "2016-06-13T14:40:29Z", "size": 13287936, "disk_format": "qcow2", "updated_at": "2016-06-13T14:40:30Z", "visibility": "public", "self": "/v2/images/13ff79d9-a881-45f4-832c-5dc75691346f", "min_disk": 0, "protected": false, "id": "13ff79d9-a881-45f4-832c-5dc75691346f", "file": "/v2/images/13ff79d9-a881-45f4-832c-5dc75691346f/file", "checksum": "ee1eca47dc88f4879d8a229cc70a07c6", "owner": "ec6a0ee076c5431e86ec46c758dce0af", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}], "schema": "/v2/schemas/images", "first": "/v2/images"}
```

3 Create image (no data)
```sh
curl -i \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXtMoGTOvOfBdYIRMkwHvHIZLAGm6682RCb90QnZIkjm-jQd0WsjnTzeen-MLYkHdE2JL7Q6sA2ClxpJ24R-J8mdMHE_NDNF_t-MM49YBdWgAc4B48sgtlneRE6Nngyz1ltiRp3Zbyey74EtMGCSM49oz5Q" \
  -d '
{
    "container_format": "bare",
    "disk_format": "qcow2",
    "name": "demo",
    "id": "13ff79d9-a881-45f4-832c-5dc75691346f"
}' \
  http://10.10.10.40:9292/v2/images ; echo
```

Kết quả trả về:
```sh
HTTP/1.1 200 OK
Content-Length: 551
Content-Type: application/json; charset=UTF-8
X-Openstack-Request-Id: req-71d86b9d-4a41-4bc9-a107-b4f9ad3e4fbf
Date: Mon, 13 Jun 2016 15:41:00 GMT

{"status": "queued", "name": "demo", "tags": [], "container_format": "bare", "created_at": "2016-06-13T15:41:00Z", "size": null, "disk_format": "qcow2", "updated_at": "2016-06-13T15:41:00Z", "visibility": "private", "self": "/v2/images/13ff79d9-a881-45f4-832c-5dc75691346f", "min_disk": 0, "protected": false, "id": "13ff79d9-a881-45f4-832c-5dc75691346f", "file": "/v2/images/13ff79d9-a881-45f4-832c-5dc75691346f/file", "checksum": null, "owner": "5cfaded20e0c4959a807541ecad77a49", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}
```

4 Delete image

```sh
curl -i -X DELETE \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXtMoGTOvOfBdYIRMkwHvHIZLAGm6682RCb90QnZIkjm-jQd0WsjnTzeen-MLYkHdE2JL7Q6sA2ClxpJ24R-J8mdMHE_NDNF_t-MM49YBdWgAc4B48sgtlneRE6Nngyz1ltiRp3Zbyey74EtMGCSM49oz5Q" \
  http://10.10.10.40:9292/v2/images/ID image ; echo 
```


  
5 Deactivate image
```sh
curl -i -X POST \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXtMoGTOvOfBdYIRMkwHvHIZLAGm6682RCb90QnZIkjm-jQd0WsjnTzeen-MLYkHdE2JL7Q6sA2ClxpJ24R-J8mdMHE_NDNF_t-MM49YBdWgAc4B48sgtlneRE6Nngyz1ltiRp3Zbyey74EtMGCSM49oz5Q" \
   http://10.10.10.40:9292/v2/images/ID image/actions/deactivate ; echo
```

6 Reactivate image

```sh
curl -i -X POST \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXtMoGTOvOfBdYIRMkwHvHIZLAGm6682RCb90QnZIkjm-jQd0WsjnTzeen-MLYkHdE2JL7Q6sA2ClxpJ24R-J8mdMHE_NDNF_t-MM49YBdWgAc4B48sgtlneRE6Nngyz1ltiRp3Zbyey74EtMGCSM49oz5Q" \
   http://10.10.10.40:9292/v2/images/ID image/actions/reactivate ; echo
```

7 Upload binary image data

```sh
curl -i -X PUT \
 -H "X-Auth-Token: gAAAAABXXtMoGTOvOfBdYIRMkwHvHIZLAGm6682RCb90QnZIkjm-jQd0WsjnTzeen-MLYkHdE2JL7Q6sA2ClxpJ24R-J8mdMHE_NDNF_t-MM49YBdWgAc4B48sgtlneRE6Nngyz1ltiRp3Zbyey74EtMGCSM49oz5Q" 
 -H "Content-Type: application/octet-stream" \
   -d @/...../cirros-0.3.4-x86_64-disk.img http://10.10.10.40:9292/v2/images/ID image/file
```
Sau khi thực hiện xong câu lệnh, image sẽ chuyển từ trạng thái queued sang trạng thái active

8 Show image details

```sh
curl -i \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXtMoGTOvOfBdYIRMkwHvHIZLAGm6682RCb90QnZIkjm-jQd0WsjnTzeen-MLYkHdE2JL7Q6sA2ClxpJ24R-J8mdMHE_NDNF_t-MM49YBdWgAc4B48sgtlneRE6Nngyz1ltiRp3Zbyey74EtMGCSM49oz5Q" \
   http://10.10.10.40:9292/v2/images/ID image ; echo
```
