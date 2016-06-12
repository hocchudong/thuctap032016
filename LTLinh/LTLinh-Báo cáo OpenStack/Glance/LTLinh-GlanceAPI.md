#Glance API
Trong bài nào, mình sẽ hướng dẫn mọi người sử dụng các API mà OpenStack đã cung cấp cho chúng ta.
Mình sẽ hướng dẫn trên 2 công cụ, đó là **cURL** và **Advanced REST client** - addons của Chrome.

#Mục Lục


#1. Advanced REST client(ARC)
- Hướng dẫn sử dụng Advanced REST client(ARC), các bạn có thể tham khảo tại đây: https://github.com/hocchudong/API-Openstack

#2. cURL
curl is a command line tool for transferring data with URL syntax, supporting DICT, FILE, FTP, FTPS, Gopher, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, Telnet and TFTP. curl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies, cookies, user+password authentication (Basic, Digest, NTLM, Negotiate, kerberos...), file transfer resume, proxy tunneling and a busload of other useful tricks.


#3. Các thao tác cơ bản
##3.1 Get token.
|:----:|:----:|
|URL | /v3/auth/tokens|
|method| POST|

####3.1.1 ARC
- Request Header
```sh
Content-Type: application/json
```

- **Request parameters**
```sh
{
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "id": "b257b3d429b8449b87cb9f2454ae9009",
                    "password": "Welcome123"
                }
            }
        }
    }
}
``` 

- **Response Header**
```sh

Date: Sun, 12 Jun 2016 16:14:06 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Subject-Token: gAAAAABXXYpOBlipqKH_tBqoTAmWTtCyP_IfpGy4QzEFQ1ign3XJ2xiNeS6V6c6XCjFcVG6A_DI2gr8f4R2_OUPmbXIjmd-6YcP_vpxc_Nz7ST2ICPCFFfAX7BFBgQIVjWeU3Ulb-oi1x70fjDNRgKLzehAVWK5PXg
Vary: X-Auth-Token
X-Distribution: Ubuntu
X-Openstack-Request-Id: req-48e1a2dd-91f0-49a3-8ec0-1b1a53f156a1
Content-Length: 308
Content-Type: application/json
```

**Ta chú ý trong trường `X-Subject-Token` ở đoạn Header trả về. Trường này chính là token ta cần lấy.**

- **Response parameters**
```sh
{
  "token": {
    "issued_at": "2016-06-12T16:14:06.000000Z",
    "audit_ids": [
      "JmJxovS_Q9i_6ss4po9XcA"
    ],
    "methods": [
      "password"
    ],
    "expires_at": "2016-06-12T17:14:06.736513Z",
    "user": {
      "domain": {
        "id": "03a12ef5af594cbd917dd5c55d8984f8",
        "name": "default"
      },
      "id": "b257b3d429b8449b87cb9f2454ae9009",
      "name": "admin"
    }
  }
}
```

- Demo
![](http://image.prntscr.com/image/b9f97a750fe343ca8a1aec00c445af42.png)

![](http://image.prntscr.com/image/a40fde237b2d487ab0ff2fb32e0c2d46.png)

###3.1.2 cURL
- Lệnh: 
```sh
curl -i \
  -H "Content-Type: application/json" \
  -d '
{ "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "id": "b257b3d429b8449b87cb9f2454ae9009",
          "password": "Welcome123"
        }
      }
    }
  }
}' \
  http://10.10.10.100:5000/v3/auth/tokens ; echo
```

- Kết quả
```sh
HTTP/1.1 201 Created
Date: Sun, 12 Jun 2016 16:36:50 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Subject-Token: gAAAAABXXY-vfn99ZR3nSp1oyagJROHWIAC1Mkiy4lA4PROaO3Ja6B34U0EyvT8tXM4KIpPtaO0RXRvnL1IRLWfA2zLFfMS6KggfR6anEaGd_mvG25o-C6ktro9tppRgkl8sjVxbQkxivTXNLRqWNvqvyaEk3d63jA
Vary: X-Auth-Token
X-Distribution: Ubuntu
x-openstack-request-id: req-164a6f89-8e9b-4a55-8e29-7f16b557259d
Content-Length: 308
Content-Type: application/json

{"token": {"issued_at": "2016-06-12T16:37:03.000000Z", "audit_ids": ["T5wR3uuoS5KwjUK0wDxNxg"], "methods": ["password"], "expires_at": "2016-06-12T17:37:02.962001Z", "user": {"domain": {"id": "03a12ef5af594cbd917dd5c55d8984f8", "name": "default"}, "id": "b257b3d429b8449b87cb9f2454ae9009", "name": "admin"}}}

```
**=> Cũng như trên, token ta cần get nằm ở trường `X-Subject-Token`**

**Và kể từ bây giờ, mỗi hành động gì, các bạn phải chèn thêm trường X-Auth-Token, có giá trị là token và header thì câu lệnh mới có thể sử dụng được.

##3.2. Get List images
|:----:|:----:|
|URL | /v2/images |
|method| GET |

###3.2.1 ARC
- Request Header
```sh
Content-Type: application/json
X-Auth-Token: Chính là token mà bạn vừa get ở trên.
```

- - **Response parameters**
```sh
{
  "images": [
    {
      "status": "active",
      "name": "cirros",
      "tags": [],
      "container_format": "bare",
      "created_at": "2016-06-12T14:23:32Z",
      "size": 13287936,
      "disk_format": "qcow2",
      "updated_at": "2016-06-12T14:23:34Z",
      "visibility": "public",
      "self": "/v2/images/ec910882-fe28-43b1-a9e3-8a9388b2a64f",
      "min_disk": 0,
      "protected": false,
      "id": "ec910882-fe28-43b1-a9e3-8a9388b2a64f",
      "file": "/v2/images/ec910882-fe28-43b1-a9e3-8a9388b2a64f/file",
      "checksum": "ee1eca47dc88f4879d8a229cc70a07c6",
      "owner": "5cfaded20e0c4959a807541ecad77a49",
      "virtual_size": null,
      "min_ram": 0,
      "schema": "/v2/schemas/image"
    },
    {
      "status": "active",
      "name": "testlinh",
      "tags": [],
      "container_format": "bare",
      "created_at": "2016-06-10T04:30:59Z",
      "size": 6909873,
      "disk_format": "qcow2",
      "updated_at": "2016-06-10T04:34:50Z",
      "visibility": "public",
      "self": "/v2/images/c3c85c0d-d104-430f-9793-87de88d1de53",
      "min_disk": 0,
      "protected": false,
      "id": "c3c85c0d-d104-430f-9793-87de88d1de53",
      "file": "/v2/images/c3c85c0d-d104-430f-9793-87de88d1de53/file",
      "checksum": "c0d3bf29d8b72866322e3514a6a8b4a0",
      "owner": "5cfaded20e0c4959a807541ecad77a49",
      "virtual_size": null,
      "min_ram": 0,
      "schema": "/v2/schemas/image"
    },
    {
      "status": "active",
      "name": "Ubuntu",
      "tags": [],
      "container_format": "bare",
      "created_at": "2016-06-08T11:00:05Z",
      "size": 59,
      "disk_format": "qcow2",
      "updated_at": "2016-06-10T03:03:01Z",
      "visibility": "public",
      "self": "/v2/images/ee8fa0ec-7a8f-49df-b1a6-f6ed1e13ff71",
      "min_disk": 0,
      "protected": false,
      "id": "ee8fa0ec-7a8f-49df-b1a6-f6ed1e13ff71",
      "file": "/v2/images/ee8fa0ec-7a8f-49df-b1a6-f6ed1e13ff71/file",
      "checksum": "7da60e957e9f31148e535028a0a9c2f8",
      "owner": "5cfaded20e0c4959a807541ecad77a49",
      "virtual_size": null,
      "min_ram": 0,
      "schema": "/v2/schemas/image"
    },
    {
      "status": "active",
      "name": "Ubuntu",
      "tags": [],
      "container_format": "bare",
      "created_at": "2016-06-08T10:50:52Z",
      "size": 0,
      "disk_format": "qcow2",
      "updated_at": "2016-06-10T02:17:15Z",
      "visibility": "public",
      "self": "/v2/images/7d639bc3-0562-435f-980a-7598c40da68a",
      "min_disk": 0,
      "protected": false,
      "id": "7d639bc3-0562-435f-980a-7598c40da68a",
      "file": "/v2/images/7d639bc3-0562-435f-980a-7598c40da68a/file",
      "checksum": "d41d8cd98f00b204e9800998ecf8427e",
      "owner": "5cfaded20e0c4959a807541ecad77a49",
      "virtual_size": null,
      "min_ram": 0,
      "schema": "/v2/schemas/image"
    },
    {
      "status": "active",
      "name": "cirros",
      "tags": [],
      "container_format": "bare",
      "created_at": "2016-06-08T08:22:04Z",
      "size": 13287936,
      "disk_format": "qcow2",
      "updated_at": "2016-06-08T08:22:05Z",
      "visibility": "public",
      "self": "/v2/images/10a43894-96c7-46b1-b5b9-1af7c7fdc258",
      "min_disk": 0,
      "protected": false,
      "id": "10a43894-96c7-46b1-b5b9-1af7c7fdc258",
      "file": "/v2/images/10a43894-96c7-46b1-b5b9-1af7c7fdc258/file",
      "checksum": "ee1eca47dc88f4879d8a229cc70a07c6",
      "owner": "5cfaded20e0c4959a807541ecad77a49",
      "virtual_size": null,
      "min_ram": 0,
      "schema": "/v2/schemas/image"
    },
    {
      "status": "active",
      "name": "cirros",
      "tags": [],
      "container_format": "bare",
      "created_at": "2016-06-08T08:19:20Z",
      "size": 13287936,
      "disk_format": "qcow2",
      "updated_at": "2016-06-08T08:19:21Z",
      "visibility": "public",
      "self": "/v2/images/c370939a-58f1-4b4f-a52f-8fff010b0b16",
      "min_disk": 0,
      "protected": false,
      "id": "c370939a-58f1-4b4f-a52f-8fff010b0b16",
      "file": "/v2/images/c370939a-58f1-4b4f-a52f-8fff010b0b16/file",
      "checksum": "ee1eca47dc88f4879d8a229cc70a07c6",
      "owner": "5cfaded20e0c4959a807541ecad77a49",
      "virtual_size": null,
      "min_ram": 0,
      "schema": "/v2/schemas/image"
    },
    {
      "status": "active",
      "name": "cirros",
      "tags": [],
      "container_format": "bare",
      "created_at": "2016-06-07T16:43:20Z",
      "size": 13287936,
      "disk_format": "qcow2",
      "updated_at": "2016-06-07T16:43:22Z",
      "visibility": "public",
      "self": "/v2/images/36bafa1e-082a-42d7-bfa7-4d6535f00754",
      "min_disk": 0,
      "protected": false,
      "id": "36bafa1e-082a-42d7-bfa7-4d6535f00754",
      "file": "/v2/images/36bafa1e-082a-42d7-bfa7-4d6535f00754/file",
      "checksum": "ee1eca47dc88f4879d8a229cc70a07c6",
      "owner": "5cfaded20e0c4959a807541ecad77a49",
      "virtual_size": null,
      "min_ram": 0,
      "schema": "/v2/schemas/image"
    }
  ],
  "schema": "/v2/schemas/images",
  "first": "/v2/images"
}
```
- demo
![](http://image.prntscr.com/image/d3e8e5087b55410698e4a93f47486ae4.png)

###3.2.2 cURL
- Lệnh
```sh
curl -i \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXY-vfn99ZR3nSp1oyagJROHWIAC1Mkiy4lA4PROaO3Ja6B34U0EyvT8tXM4KIpPtaO0RXRvnL1IRLWfA2zLFfMS6KggfR6anEaGd_mvG25o-C6ktro9tppRgkl8sjVxbQkxivTXNLRqWNvqvyaEk3d63jA" \
  http://10.10.10.100:9292/v2/images ; echo
```

- Kết quả
```sh
HTTP/1.1 200 OK
Content-Length: 4157
Content-Type: application/json; charset=UTF-8
X-Openstack-Request-Id: req-bfff7ec5-5e20-4235-9c68-dd5449281da7
Date: Sun, 12 Jun 2016 16:57:30 GMT

{"images": [{"status": "active", "name": "cirros", "tags": [], "container_format": "bare", "created_at": "2016-06-12T14:23:32Z", "size": 13287936, "disk_format": "qcow2", "updated_at": "2016-06-12T14:23:34Z", "visibility": "public", "self": "/v2/images/ec910882-fe28-43b1-a9e3-8a9388b2a64f", "min_disk": 0, "protected": false, "id": "ec910882-fe28-43b1-a9e3-8a9388b2a64f", "file": "/v2/images/ec910882-fe28-43b1-a9e3-8a9388b2a64f/file", "checksum": "ee1eca47dc88f4879d8a229cc70a07c6", "owner": "5cfaded20e0c4959a807541ecad77a49", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}, {"status": "active", "name": "testlinh", "tags": [], "container_format": "bare", "created_at": "2016-06-10T04:30:59Z", "size": 6909873, "disk_format": "qcow2", "updated_at": "2016-06-10T04:34:50Z", "visibility": "public", "self": "/v2/images/c3c85c0d-d104-430f-9793-87de88d1de53", "min_disk": 0, "protected": false, "id": "c3c85c0d-d104-430f-9793-87de88d1de53", "file": "/v2/images/c3c85c0d-d104-430f-9793-87de88d1de53/file", "checksum": "c0d3bf29d8b72866322e3514a6a8b4a0", "owner": "5cfaded20e0c4959a807541ecad77a49", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}, {"status": "active", "name": "Ubuntu", "tags": [], "container_format": "bare", "created_at": "2016-06-08T11:00:05Z", "size": 59, "disk_format": "qcow2", "updated_at": "2016-06-10T03:03:01Z", "visibility": "public", "self": "/v2/images/ee8fa0ec-7a8f-49df-b1a6-f6ed1e13ff71", "min_disk": 0, "protected": false, "id": "ee8fa0ec-7a8f-49df-b1a6-f6ed1e13ff71", "file": "/v2/images/ee8fa0ec-7a8f-49df-b1a6-f6ed1e13ff71/file", "checksum": "7da60e957e9f31148e535028a0a9c2f8", "owner": "5cfaded20e0c4959a807541ecad77a49", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}, {"status": "active", "name": "Ubuntu", "tags": [], "container_format": "bare", "created_at": "2016-06-08T10:50:52Z", "size": 0, "disk_format": "qcow2", "updated_at": "2016-06-10T02:17:15Z", "visibility": "public", "self": "/v2/images/7d639bc3-0562-435f-980a-7598c40da68a", "min_disk": 0, "protected": false, "id": "7d639bc3-0562-435f-980a-7598c40da68a", "file": "/v2/images/7d639bc3-0562-435f-980a-7598c40da68a/file", "checksum": "d41d8cd98f00b204e9800998ecf8427e", "owner": "5cfaded20e0c4959a807541ecad77a49", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}, {"status": "active", "name": "cirros", "tags": [], "container_format": "bare", "created_at": "2016-06-08T08:22:04Z", "size": 13287936, "disk_format": "qcow2", "updated_at": "2016-06-08T08:22:05Z", "visibility": "public", "self": "/v2/images/10a43894-96c7-46b1-b5b9-1af7c7fdc258", "min_disk": 0, "protected": false, "id": "10a43894-96c7-46b1-b5b9-1af7c7fdc258", "file": "/v2/images/10a43894-96c7-46b1-b5b9-1af7c7fdc258/file", "checksum": "ee1eca47dc88f4879d8a229cc70a07c6", "owner": "5cfaded20e0c4959a807541ecad77a49", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}, {"status": "active", "name": "cirros", "tags": [], "container_format": "bare", "created_at": "2016-06-08T08:19:20Z", "size": 13287936, "disk_format": "qcow2", "updated_at": "2016-06-08T08:19:21Z", "visibility": "public", "self": "/v2/images/c370939a-58f1-4b4f-a52f-8fff010b0b16", "min_disk": 0, "protected": false, "id": "c370939a-58f1-4b4f-a52f-8fff010b0b16", "file": "/v2/images/c370939a-58f1-4b4f-a52f-8fff010b0b16/file", "checksum": "ee1eca47dc88f4879d8a229cc70a07c6", "owner": "5cfaded20e0c4959a807541ecad77a49", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}, {"status": "active", "name": "cirros", "tags": [], "container_format": "bare", "created_at": "2016-06-07T16:43:20Z", "size": 13287936, "disk_format": "qcow2", "updated_at": "2016-06-07T16:43:22Z", "visibility": "public", "self": "/v2/images/36bafa1e-082a-42d7-bfa7-4d6535f00754", "min_disk": 0, "protected": false, "id": "36bafa1e-082a-42d7-bfa7-4d6535f00754", "file": "/v2/images/36bafa1e-082a-42d7-bfa7-4d6535f00754/file", "checksum": "ee1eca47dc88f4879d8a229cc70a07c6", "owner": "5cfaded20e0c4959a807541ecad77a49", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}], "schema": "/v2/schemas/images", "first": "/v2/images"}

```

##3.3 Create image
|:----:|:----:|
|URL | /v2/images |
|method| POST |

###3.3.1 ARC
- Request Header
```sh
Content-Type: application/json
X-Auth-Token: Chính là token mà bạn vừa get ở trên.
```
- Request parameters
```sh
{
    "container_format": "bare",
    "disk_format": "qcow2",
    "name": "TESTLT",
    "id": "f7b66836-50ec-4c54-8b24-1d12888a8b80"
}
```
- Response Header
Trong Response Header có một trường trả về là
```sh
Location: http://10.10.10.100:9292/v2/images/f7b66836-50ec-4c54-8b24-1d12888a8b80
```

chỉ ra đường dẫn của file image vừa được tạo ra 
- Response parameters
```sh
{
  "status": "queued",
  "name": "TESTLT",
  "tags": [],
  "container_format": "bare",
  "created_at": "2016-06-12T17:08:02Z",
  "size": null,
  "disk_format": "qcow2",
  "updated_at": "2016-06-12T17:08:02Z",
  "visibility": "private",
  "self": "/v2/images/f7b66836-50ec-4c54-8b24-1d12888a8b80",
  "min_disk": 0,
  "protected": false,
  "id": "f7b66836-50ec-4c54-8b24-1d12888a8b80",
  "file": "/v2/images/f7b66836-50ec-4c54-8b24-1d12888a8b80/file",
  "checksum": null,
  "owner": "5cfaded20e0c4959a807541ecad77a49",
  "virtual_size": null,
  "min_ram": 0,
  "schema": "/v2/schemas/image"
}
```

![](http://image.prntscr.com/image/d8eada47059c46e090a026d518c1e398.png)


###3.3.2 cURL
- Lệnh
```sh
curl -i \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXZhNQDk4L9xXyLPBxHms3L_2u5Q96CY7rDHMWVj1kQqxdmx_v4ARcALf9t7nDcbJ5y8dR7pqi60VmGZEG5wgLzP1VbSUH9FWAzXqaHeio5H4stKjrxZGw6Hyd9eKYG7YGFo06aT-jmugYB35BV_wfc-LTbHDGlFhxdoyJqJg-y1Ow6A" \
  -d '
{
    "container_format": "bare",
    "disk_format": "qcow2",
    "name": "TESTLT",
    "id": "0c1ffd08-68b4-4206-9f66-26a370228bc2"
}' \
  http://10.10.10.100:9292/v2/images ; echo
```
- Kết Quả
```sh
HTTP/1.1 201 Created
Content-Length: 551
Content-Type: application/json; charset=UTF-8
Location: http://10.10.10.100:9292/v2/images/0c1ffd08-68b4-4206-9f66-26a370228bc2
X-Openstack-Request-Id: req-996afff9-822a-492f-8c04-1d68e768e370
Date: Sun, 12 Jun 2016 17:14:17 GMT

{"status": "queued", "name": "TESTLT", "tags": [], "container_format": "bare", "created_at": "2016-06-12T17:14:17Z", "size": null, "disk_format": "qcow2", "updated_at": "2016-06-12T17:14:17Z", "visibility": "private", "self": "/v2/images/0c1ffd08-68b4-4206-9f66-26a370228bc2", "min_disk": 0, "protected": false, "id": "0c1ffd08-68b4-4206-9f66-26a370228bc2", "file": "/v2/images/0c1ffd08-68b4-4206-9f66-26a370228bc2/file", "checksum": null, "owner": "5cfaded20e0c4959a807541ecad77a49", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}
```

##3.4 Show image details
|:----:|:----:|
|URL | /v2/images/​{image_id}​ |
|method| GET |

###3.4.1 ARC
- Request header: 
```sh
Content-Type: application/json
X-Auth-Token: Chính là token mà bạn vừa get ở trên.
```

- Request parameters: image_id
- Response parameters
```sh
{
  "status": "queued",
  "name": "TESTLT",
  "tags": [],
  "container_format": "bare",
  "created_at": "2016-06-12T17:08:02Z",
  "size": null,
  "disk_format": "qcow2",
  "updated_at": "2016-06-12T17:08:02Z",
  "visibility": "private",
  "self": "/v2/images/f7b66836-50ec-4c54-8b24-1d12888a8b80",
  "min_disk": 0,
  "protected": false,
  "id": "f7b66836-50ec-4c54-8b24-1d12888a8b80",
  "file": "/v2/images/f7b66836-50ec-4c54-8b24-1d12888a8b80/file",
  "checksum": null,
  "owner": "5cfaded20e0c4959a807541ecad77a49",
  "virtual_size": null,
  "min_ram": 0,
  "schema": "/v2/schemas/image"
}
```

- demo
![](http://image.prntscr.com/image/86b476f8f2464fd1a0174abfa6ff5cd7.png)

###3.4.2 cURL
- Lệnh
```sh
curl -i \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXZhNQDk4L9xXyLPBxHms3L_2u5Q96CY7rDHMWVj1kQqxdmx_v4ARcALf9t7nDcbJ5y8dR7pqi60VmGZEG5wgLzP1VbSUH9FWAzXqaHeio5H4stKjrxZGw6Hyd9eKYG7YGFo06aT-jmugYB35BV_wfc-LTbHDGlFhxdoyJqJg-y1Ow6A" \
  http://10.10.10.100:9292/v2/images/0c1ffd08-68b4-4206-9f66-26a370228bc2 ; echo
```

- Kết quả
```sh
HTTP/1.1 200 OK
Content-Length: 584
Content-Type: application/json; charset=UTF-8
X-Openstack-Request-Id: req-5f501855-3c18-41b5-8d0b-28786b605d1f
Date: Sun, 12 Jun 2016 18:02:08 GMT

{"status": "active", "name": "TESTLT", "tags": [], "container_format": "bare", "created_at": "2016-06-12T17:14:17Z", "size": 6909873, "disk_format": "qcow2", "updated_at": "2016-06-12T17:56:58Z", "visibility": "private", "self": "/v2/images/0c1ffd08-68b4-4206-9f66-26a370228bc2", "min_disk": 0, "protected": false, "id": "0c1ffd08-68b4-4206-9f66-26a370228bc2", "file": "/v2/images/0c1ffd08-68b4-4206-9f66-26a370228bc2/file", "checksum": "c0d3bf29d8b72866322e3514a6a8b4a0", "owner": "5cfaded20e0c4959a807541ecad77a49", "virtual_size": null, "min_ram": 0, "schema": "/v2/schemas/image"}
```
##3.5 Delete image
|:----:|:----:|
|URL | /v2/images/{image_id}​ |
|method| DELETE |

###3.5.1 ARC
- Request header: 
```sh
Content-Type: application/json
X-Auth-Token: Chính là token mà bạn vừa get ở trên.
```

- Request parameters: image_id

- demo
![](http://image.prntscr.com/image/c4b9bf5cbf93470ead8361ec8e05b683.png)

###3.5.2 cURL
- Lệnh
```sh
curl -i -X DELETE \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXZhNQDk4L9xXyLPBxHms3L_2u5Q96CY7rDHMWVj1kQqxdmx_v4ARcALf9t7nDcbJ5y8dR7pqi60VmGZEG5wgLzP1VbSUH9FWAzXqaHeio5H4stKjrxZGw6Hyd9eKYG7YGFo06aT-jmugYB35BV_wfc-LTbHDGlFhxdoyJqJg-y1Ow6A" \
  http://10.10.10.100:9292/v2/images/f7b66836-50ec-4c54-8b24-1d12888a8b80 ; echo
```
- Kết quả
```sh
HTTP/1.1 204 No Content
Content-Type: text/html; charset=UTF-8
Content-Length: 0
X-Openstack-Request-Id: req-89a16eb7-dcba-48ec-96a2-6ce561b68931
Date: Sun, 12 Jun 2016 18:05:14 GMT
```
##3.6 Deactivate image
|:----:|:----:|
|URL | /v2/images/{image_id}​/actions/deactivate |
|method| POST |

###3.6.1 ARC
- Request header: 
```sh
Content-Type: application/json
X-Auth-Token: Chính là token mà bạn vừa get ở trên.
```

- Request parameters: image_id

- demo
![](http://image.prntscr.com/image/0dc456f7a08c4e08a18145f18f28ab38.png)

###3.6.2 
- Lệnh
```sh
curl -i -X POST \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXZhNQDk4L9xXyLPBxHms3L_2u5Q96CY7rDHMWVj1kQqxdmx_v4ARcALf9t7nDcbJ5y8dR7pqi60VmGZEG5wgLzP1VbSUH9FWAzXqaHeio5H4stKjrxZGw6Hyd9eKYG7YGFo06aT-jmugYB35BV_wfc-LTbHDGlFhxdoyJqJg-y1Ow6A" \
  http://10.10.10.100:9292/v2/images/0c1ffd08-68b4-4206-9f66-26a370228bc2/actions/deactivate ; echo
```

- Kết quả
```sh
HTTP/1.1 204 No Content
Content-Type: text/html; charset=UTF-8
Content-Length: 0
X-Openstack-Request-Id: req-a74b9e29-8c5d-4cdd-a611-5e30749ef3e1
Date: Sun, 12 Jun 2016 18:09:01 GMT
```

![](http://image.prntscr.com/image/5592933b253f4f9881dddf636ea9d44f.png)

##3.7 Reactivate image
|:----:|:----:|
|URL | /v2/images/{image_id}​​/actions/reactivate |
|method| POST |

###3.7.1 ARC
```sh
Content-Type: application/json
X-Auth-Token: Chính là token mà bạn vừa get ở trên.
```

- Request parameters: image_id

- demo
![](http://image.prntscr.com/image/4d9df57339414ba6b3bc6aa89106b807.png)

###3.7.2 cURL
- Lệnh
```sh
curl -i -X POST \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXZhNQDk4L9xXyLPBxHms3L_2u5Q96CY7rDHMWVj1kQqxdmx_v4ARcALf9t7nDcbJ5y8dR7pqi60VmGZEG5wgLzP1VbSUH9FWAzXqaHeio5H4stKjrxZGw6Hyd9eKYG7YGFo06aT-jmugYB35BV_wfc-LTbHDGlFhxdoyJqJg-y1Ow6A" \
  http://10.10.10.100:9292/v2/images/0c1ffd08-68b4-4206-9f66-26a370228bc2/actions/reactivate; echo

```

- Kết quả
```sh
HTTP/1.1 204 No Content
Content-Type: text/html; charset=UTF-8
Content-Length: 0
X-Openstack-Request-Id: req-74f37641-9846-430b-a120-ec5130c293fe
Date: Sun, 12 Jun 2016 18:10:03 GMT
```

![](http://image.prntscr.com/image/418da789c1434645ba592bef4aa2ab7c.png)


##3.8 Upload binary image data
|:----:|:----:|
|URL | /v2/images/{image_id}​​​/file |
|method| PUT |
|Header|Content-Type: application/octet-stream|

#3.8.1 cURL
- Lệnh
```sh
curl -i -X PUT -H "X-Auth-Token: gAAAAABXXZhNQDk4L9xXyLPBxHms3L_2u5Q96CY7rDHMWVj1kQqxdmx_v4ARcALf9t7nDcbJ5y8dR7pqi60VmGZEG5wgLzP1VbSUH9FWAzXqaHeio5H4stKjrxZGw6Hyd9eKYG7YGFo06aT-jmugYB35BV_wfc-LTbHDGlFhxdoyJqJg-y1Ow6A" -H "Content-Type: application/octet-stream" \
   -d @/root/cirros-0.3.4-x86_64-disk.img http://10.10.10.100:9292/v2/images/0c1ffd08-68b4-4206-9f66-26a370228bc2/file
```
Trong đó: 
-d @/root/cirros-0.3.4-x86_64-disk.img: là nơi lưu file image gốc.
- Kết quả
```sh
HTTP/1.1 100 Continue

HTTP/1.1 204 No Content
Content-Type: text/html; charset=UTF-8
Content-Length: 0
X-Openstack-Request-Id: req-aaa16460-e75f-478b-bcc9-2df9a3588994
Date: Sun, 12 Jun 2016 17:56:58 GMT
```
**=> Sau khi thực hiện xong câu lệnh, image sẽ chuyển từ trạng thái `queued` sang trạng thái `active`**

##3.9 Download binary image data
|:----:|:----:|
|URL | /v2/images/{image_id}​​​/file |
|method| GET |

###3.9.1 ARC
- Request header: 
```sh
Content-Type: application/json
X-Auth-Token: Chính là token mà bạn vừa get ở trên.
```

- Request parameters: image_id

- demo
![](http://image.prntscr.com/image/96fa4aafbe054e4098e3a0ad1353e53b.png)


###3.9.2 cURL
- Lệnh
```sh
curl -i \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: gAAAAABXXZhNQDk4L9xXyLPBxHms3L_2u5Q96CY7rDHMWVj1kQqxdmx_v4ARcALf9t7nDcbJ5y8dR7pqi60VmGZEG5wgLzP1VbSUH9FWAzXqaHeio5H4stKjrxZGw6Hyd9eKYG7YGFo06aT-jmugYB35BV_wfc-LTbHDGlFhxdoyJqJg-y1Ow6A" \
  http://10.10.10.100:9292/v2/images/36bafa1e-082a-42d7-bfa7-4d6535f00754/file ; echo
```
- Kết quả




