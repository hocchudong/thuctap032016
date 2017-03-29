# Hướng dẫn cài đặt OMD-Grafana trên môi trường docker - Ubuntu 14.04.

# 1. Các thông tin cần nắm được
- Docker là công cụ tạo môi trường đóng gói các ứng dụng trong các container. 
- Ví dụ: bạn phải dựng một con web server apache để chạy các service là php, mysql. Thay vì phải tạo 1 con máy ảo riêng biệt thì bạn có thể đóng gói các ứng dụng trên (apache, php, mysql) vào 1 container, và chạy ngay trên chính máy chủ.
- Các container này sẽ chạy độc lập, **không** tác động đến máy chủ (máy chủ cài đặt docker), đến các container khác. 
- Các container dùng chung kernel với máy host. => Có tốc độ nhanh, nhẹ, tiết kiếm tài nguyên so với máy ảo.
- Mỗi container được xây dựng dựa trên file ảnh (image). File image này chỉ có thể đọc. Khi container được tạo ra, docker sẽ cung cấp thêm 1 lớp có thể ghi được (`writabe-layer`) cho container đó. Các thay đổi trong container sẽ được ghi ở lớp này.
- Khái niệm image: image được sử dụng để đóng gói ứng dụng và các thành phần phụ thuộc của ứng dụng.
- Để tìm hiểu thêm thông tin về docker, các bạn có thể ghé thăm 2 địa chỉ dưới dây:
  - https://github.com/hocchudong/ghichep-docker
  - https://docs.docker.com/

# 2. Cài đặt docker.
- Gần đây thì docker vừa tung ra phiển bản thương mại Docker Enterprise Edition (Docker EE) cho môi trường doanh nghiệp.
- Song song với phiên bản Docker EE, thì Docker vẫn cung cấp phiên bản Docker Community Edition (CE), miễn phí cho cộng động.
- Trong bài này, tôi sẽ sử dụng phiên bản docker ce.

## 2.1 Cài đặt bằng script.
- Docker đã viết sẵn cho chúng ta đoạn script để cài đặt docker trên môi trường Linux. 
- Chỉ với một câu lệnh, **bùm**, có ngay docker trên máy của chúng ta :v.
```sh
curl -sSL https://get.docker.io | bash
```

## 2.2 Cài đặt bằng tay.
- Cài đặt các gói bổ sung cho phiên bản Trusty 14.04
```sh
$ sudo apt-get update

$ sudo apt-get install \
    linux-image-extra-$(uname -r) \
    linux-image-extra-virtual
```

- Cài đặt các gói cần thiết
```sh
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

- Thêm Docker’s official GPG key
```sh
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

- Install docker
```sh
$ sudo apt-get update
$ sudo apt-get install docker-ce
```

- Như vậy, bạn đã cài đặt xong docker. Kiểm tra version docker cài đặt:
```sh
$ docker --version
Docker version 17.03.0-ce, build 60ccb22
```

# 3. Tạo container OMD-Grafana
- Build image: Trong image này đã chứa sẵn các ứng dụng đã được cấu hình: `OMD with Grafana, InfluxDB, Nagflux and Histou`

```sh
$ git clone https://github.com/Griesbacher/omd-grafana-container.git
$ cd omd-grafana-container
$ docker build -t griesbacher/omd-grafana .
```

- Kiểm tra
```sh
root@docker4:~# docker images
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
griesbacher/omd-grafana   latest              64abe77153bd        15 hours ago        1.13 GB
```

- Tạo container dựa trên image vừa build
```sh
$ docker run -it -p 80:80 -p 443:443 -h omd --name=omd griesbacher/omd-grafana
```

Giải thích:
  - `-p 80:80 -p 443:443`: Tùy chọn này sẽ `expose` port trong container với port của máy host. Vì sao phải expose? Bởi vì khi bạn chạy container, các ứng dụng này chạy bên trong container, các port LISTEN cũng nằm trong container. Vì vậy, khi bạn muốn truy cập từ bên ngoài vào ứng dụng, thì không thể được. Do đó, bạn phải `expose` port trong container ra máy host, mới có thể truy cập từ bên ngoài.
   - `-h omd`: Tùy chọn đặt hostname cho container.
   - `--name=omd`: Đặt tên container.
   - `griesbacher/omd-grafana`: Chỉ ra container sẽ được run dựa trên image này.

- Để truy cập vào container, dùng lệnh sau:
```sh
$ docker exec -it omd /bin/bash
```

- Kết quả:
Truy cập vào địa chỉ: `https://ip/default` trong đó `ip` là địa chỉ ip của máy host, với thông tin đăng nhập là:
```sh
user: omdadmin
pass: omd
```

![]()

![]()


# 4. Reference
- https://docs.docker.com/engine/installation/linux/ubuntu/
- https://github.com/Griesbacher/omd-grafana-container
- https://github.com/hocchudong/ghichep-docker