#LAB Bonding kết hợp GNS3
#Mục lục

**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [1. Cài đặt GNS3 tích hợp với IOU](#gns3iou)
- [2. LAB cấu hình Bonding 2 Switch](#lab)
- [Tài liệu tham khảo](#thamkhao)

<a name="gns3iou"></a>
#1. Cài đặt GNS3 tích hợp với IOU
- Cisco IOS trên nền Unix được biết đến như là Cisco IOU (internal Cisco use only).
- IOU cho phép chạy IOS Cisco trên nền x86 trong khi GNS3 phải giả lập phần cứng.
- Khác biệt lớn nhất là IOU có thể chạy nhiều IOS instance hơn GNS3, nhưng GNS3 có thể chạy IOS thật.

##1.1 Công cụ
- GNS3:
https://www.gns3.com/software

- Download VM GNS3 tại đây: Ở đây sẽ update những bản GNS3 mới nhất.

https://github.com/GNS3/gns3-gui/releases

- Download IOS cho IOU.

https://www.dropbox.com/s/es46wrxfajvrnbk/55EAD4B54E75A459176E0605F8BE32C9706E2CBA.torrent?dl=0

##1.2 Cài đặt vmware.
##1.3 Cài đặt GNS3.
##1.4 Import VM GNS3 vào vmware.
![](https://lh5.googleusercontent.com/1V6Jh306YdPUsrVTvZqgtgU-CUE1oluZd4b7GlB3Aug34G3YCWfEojxZ7ziEvCc6kK5mkOaXiaNwFBmjC9a5ToIs1TPLKUHEVQXSrmtzuYwAZ-iYpc_Consa9nLHCcdzQx9VwjvgjBcNtIjCiA)

Khởi động máy VM GNS3, ta được hính sau:
![](http://image.prntscr.com/image/22d007a96a4c46739f2f9370f53946f8.png)

##1.5 Upload IOU
Để upload IOU, truy cập vào địa chỉ `http://<ip_server>:3080/upload`



![](http://image.prntscr.com/image/fa147885527240f6b0f8e28fc512d32f.png)

- Chọn các file IOU mà bạn đã tải ở trên và tiến hành upload IOU.

##1.6 Tích hợp GNS3 với IOU
- Cấu hình địa chỉ host binding: Là địa chỉ ip của máy thật cài GNS3.
![](http://image.prntscr.com/image/a0391ca0368141c0b59e8871e8ebdce0.png)

- Enable GNS3 VM Server
![](http://image.prntscr.com/image/c76e39b553fd44cb86f646e1482e55dc.png)

- ADD Remote server: Là địa chỉ ip của máy vm-gns3.
![](http://image.prntscr.com/image/b33796df66344b3283fab067365a6d88.png)

- ADD license IOU

Nội dung file `iourc.txt`:
```sh
[license]
gns3vm = dcf51841aaabfb0d;
```

![](http://image.prntscr.com/image/650fb92eb07241cab124ba09b4daa6cb.png)

- ADD device
![](http://image.prntscr.com/image/a473e4a3ae8e426b97b9d4a1104cb38b.png)

![](http://image.prntscr.com/image/e9182c38bbe541d08a288d0bc46a5726.png)


<a name="lab"></a>
#2. LAB cấu hình Bonding 2 Switch
##2.1 Mô hình
![](http://image.prntscr.com/image/f46aec00a1714a5e99bda0429308d71b.png)

##2.2 Cấu hình
- Trên SW2
```sh
configure t
int range e0/0 -1
channel-group 20 mode passive
```

- Trên SW1
```sh
configure t
int range e0/0 -1
channel-group 10 mode active
```

- Kết quả: Chạy lệnh `show etherchannel summary` trên SW1
```sh
SW1#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
10     Po10(SU)        LACP      Et0/0(P)    Et0/1(P)
```

Ở cột Protocol giá trị là LACP, và cột Port thấy kí hiệu P (ý nghĩa là hai đường kết nối đã được "bó" lại trên 1 kênh logic) thì cấu hình đã chính xác.


<a name="thamkhao"></a>
#Tài liệu tham khảo

http://svuit.vn/threads/cai-dat-gns3-tich-hop-iou-1183/

http://svuit.vn/threads/invalid-iou-license-key-1184/

https://github.com/hocchudong/Thuc-tap-thang-03-2016/blob/master/ThaiPH/CiscoNetworkLab/ThaiPH_gns3_network_bonding.md

http://letusexplain.blogspot.com/2015/07/cisco-iou-l2-l3-lab-with-gns3-switching.html
