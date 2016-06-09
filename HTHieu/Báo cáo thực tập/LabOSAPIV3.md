#Hướng dẫn dùng Advanced RESTClient để test Openstack API v3

##Mục lục

##Xác thực

- Các yếu tố để lab bài trên:
<ul>
<li>Controller ip:10.10.10.40</li>
<li>Password:Welcom123</li>
<li>Port keystone:35357</li>
<li>User:admin</li>
<li>Project:admin</li>

- Truy cập trang `http://developer.openstack.org/api-ref-identity-v3.html` để tham khảo

- Quá trình xác thực: Mỗi một yêu cầu mà gửi đến API đều yêu cầu có X-Auth-Token header. Các máy client sẽ chứa tokens này, sử dụng để gửi đến các dịch vụ khác. Qúa trình xác thực được thể hiện ở đây:
<img src=http://imgur.com/pldoUrB>

- Tiến hành:
<ul>
<li>Lấy tokens hệ thống:</li>
<img src=http://imgur.com/oY4zXsn>
<ul>
`{
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "id": "186477b517dd4801b89c64d160c9d1e9" #dùng lệnh:openstack user list để lấy id
                    "password": "Welcome123"
                }
            }
        },
        "scope": {
            "project": {
                "id": "980918b3c204419bab89c37ab05005e5"#dùng lệnh:openstack project list để lấy id project
            }
        }
    }
}`
</ul>
<li>URL gồm có địa chỉ của password, port keystone service và API v3</li>
<li>Yêu cầu sử dụng giao thức POST</li>
<li>Chèn data gồm có user id, password, project id</li>
<li>Phản hồi về 400 hoặc 401 HTTP có nghĩa là request sai URL hoặc data sai định dạng, phản hồi 201 HTTP là xác thực thành công và trả về file json chứa các thông tin các service của dịch vụ và token của user admin</li>
<li>Kết quả trả về</li>
<img src=http://imgur.com/Qcze1ko>
</ul>
- Lấy userlist:
<ul>
<li>Phần header trả về</li>
<img src=http://imgur.com/cpjxIS1>
<li>Điền các trường như trong hình</li>
<img src=http://imgur.com/vwk61pe>
<li>URL (ô số 1) gồm địa chỉ của controller, API v2.0/tenants<\li>
<li>List user sử dụng phương thức GET<\li>
<li>Thêm header cho yêu cầu với Key là X-Auth-Token giá trị tokens id lấy ở bước 1.<\li>

##Sử dụng python và REST client.
- Code:
`
import requests
import json


def gettoken():
    url = 'http://10.10.10.40:35357/v3/auth/tokens'
    data = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "id": "186477b517dd4801b89c64d160c9d1e9",
                        "password": "Welcome123"
                    }
                }
            },
            "scope": {
                "project": {
                    "id": "980918b3c204419bab89c37ab05005e5"
                }
            }
        }
    }
    a = requests.post(url, json.dumps(data), headers={'Content_Type': 'application/json'})
    if a.status_code != 201:
        raise Exception("login returned %d, body: %s" % (a.status_code, a.text))
    else:
        return a


# reponse=gettoken().headers
# print reponse.get('Vary')
# print reponse.get('X-Subject-Token')

def getlist():
    url = 'http://10.10.10.40:35357/v3/users'
    reponse = gettoken().headers
    vary = reponse.get('Vary')
    xstoken = reponse.get('X-Subject-Token')
    # print vary
    # print xstoken
    a = requests.get(url=url,headers={vary:xstoken})
    if a.status_code != 200:
        raise Exception("login returned %d, body: %s" % (a.status_code, a.text))
    else:return a.json()

b=getlist()
print b
`
