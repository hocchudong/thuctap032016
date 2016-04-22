#Báo cáo dựng lab DHCP

#1.Mô hình
<img src=http://imgur.com/uli6VaL.png>

#2.Các bước thực hiện

-B1:cài gói isc-dhcp-server qua lênh `sudo apt-get install isc-dhcp-server`

-B2:dùng lênh `vi` sửa file /etc/default/isc-dhcp-server 

`sudo vi /etc/default/isc-dhcp-server`

trong file chọn eth0 :

`INTERFACES="eth0"`

<img src=http://imgur.com/wu3xSaF.png>

-B3:Dùng `vi` cấu hình card mạng như hình

`sudo vi /etc/network/interfaces`

<img src=http://imgur.com/2iK1qnu.png>

-B4:Cấu hình file dhcpd.conf dùng lệnh

`sudo vi /etc/dhcp/dhcpd.conf` để ghi file có nội dung như hình
 
 <img src=sudo vi /etc/dhcp/dhcpd.conf.png>
 
 -B5: chạy lệnh `ifdown -a && ifup -a` để cấu hính lại mạng và lệnh `sudo service isc-dhcp-server start` để chạy server

-B6:Trên client setup dhcp cho địa chỉ IP rồi chạy lênh `sudo ifconfig`

<img src=http://imgur.com/pffNW17.png> 