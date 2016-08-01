#LAB OpenVSwitch sử dụng chức năng QoS, dùng công cụ iperf để đo kết quả.

#Mục lục
**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [1. Giới thiệu](#gioithieu)
- [2. Mô hình](#mohinh)
- [3. Cấu hình](#cauhinh)
- [4. Sử dụng Iperf để đo kết quả.](#iperf)
	- [4.1 Kết quả rước khi sử dụng chức năng QoS](#truoc)
	- [4.2 Kết quảSau khi sử dụng chức năng QoS](#sau)
- [Tài liệu tham khảo](#thamkhao)

<a name="gioithieu"></a>
#1. Giới thiệu
QoS (Quality of Service) trong OpenVSwitch là tính năng cho phép điều khiển lưu lượng, băng thông truyền qua các interface khi kết nối với switch được tạo ra bởi OpenVSwitch.

<a name="mohinh"></a>
#2. Mô hình

![](http://i.imgur.com/ngSm8Gm.png)

<a name="cauhinh"></a>
#3. Cấu hình
##3.1 Trên VM1
- Chạy lệnh:
```sh
ovs-vsctl set interface vnet0 ingress_policing_rate=10
ovs-vsctl set interface vnet0 ingress_policing_burst=10
```

- Kết quả: Chạy lệnh `ovs-vsctl list interface vnet0`
```sh
root@adk:~# ovs-vsctl list interface vnet0
_uuid               : 08a42f2b-29cb-4ae1-9587-4bd722b593b7
admin_state         : up
bfd                 : {}
bfd_status          : {}
cfm_fault           : []
cfm_fault_status    : []
cfm_health          : []
cfm_mpid            : []
cfm_remote_mpids    : []
cfm_remote_opstate  : []
duplex              : full
external_ids        : {attached-mac="52:54:00:42:b7:bb", iface-id="30c356e4-3f99-4d45-a4c4-8b87b9b9ce35", iface-status=active, vm-id="1871cd13-209b-705e-28d6-eee28e980a93"}
ifindex             : 10
ingress_policing_burst: 10
ingress_policing_rate: 10
lacp_current        : []
link_resets         : 1
link_speed          : 10000000
link_state          : up
mac                 : []
mac_in_use          : "fe:54:00:42:b7:bb"
mtu                 : 1500
name                : "vnet0"
ofport              : 1
ofport_request      : []
options             : {}
other_config        : {}
statistics          : {collisions=0, rx_bytes=300215690, rx_crc_err=0, rx_dropped=0, rx_errors=0, rx_frame_err=0, rx_over_err=0, rx_packets=198907, tx_bytes=112757, tx_dropped=0, tx_errors=0, tx_packets=602}
status              : {driver_name=tun, driver_version="1.6", firmware_version=""}
type                : ""
```

##3.2 Trên VM2
- Chạy lệnh
```sh
ovs-vsctl set interface vnet1 ingress_policing_rate=10
ovs-vsctl set interface vnet1 ingress_policing_burst=10
```

- Kết quả
```sh
root@adk:~# ovs-vsctl list interface vnet1
_uuid               : b9af62ee-cc24-4e1d-8f83-0023a63de2b1
admin_state         : up
bfd                 : {}
bfd_status          : {}
cfm_fault           : []
cfm_fault_status    : []
cfm_health          : []
cfm_mpid            : []
cfm_remote_mpids    : []
cfm_remote_opstate  : []
duplex              : full
external_ids        : {attached-mac="52:54:00:5b:24:ec", iface-id="43933662-fb50-41f9-a7a7-2b687615e76b", iface-status=active, vm-id="e11e2906-5818-40f9-a6f2-82590cf24fcd"}
ifindex             : 11
ingress_policing_burst: 10
ingress_policing_rate: 10
lacp_current        : []
link_resets         : 1
link_speed          : 10000000
link_state          : up
mac                 : []
mac_in_use          : "fe:54:00:5b:24:ec"
mtu                 : 1500
name                : "vnet1"
ofport              : 3
ofport_request      : []
options             : {}
other_config        : {}
statistics          : {collisions=0, rx_bytes=32994, rx_crc_err=0, rx_dropped=0, rx_errors=0, rx_frame_err=0, rx_over_err=0, rx_packets=256, tx_bytes=300279208, tx_dropped=0, tx_errors=0, tx_packets=199101}
status              : {driver_name=tun, driver_version="1.6", firmware_version=""}
type                : ""
```

<a name="iperf"></a>
#4. Sử dụng Iperf để đo kết quả.
- Iperf là công cụ để đo băng thông qua mạng.
- Để hiểu rõ hơn công cụ iperf, hãy tham khảo `https://github.com/ducnc/iperf`
- Để thực hiện test, ta thực hiện:
  - Trên VM2, chạy lệnh `iperf -s -u -p 8080`
  - Trên VM1, chạy lệnh `iperf -c 172.16.69.131 -u -p 8080 -b 100m`

<a name="truoc"></a>
##4.1 Kết quả rước khi sử dụng chức năng QoS

![](http://image.prntscr.com/image/621187ca3c0d408baa98b7ba1c5ecc5f.png)

<a name="sau"></a>
##4.2 Kết quảSau khi sử dụng chức năng QoS

![](http://image.prntscr.com/image/e79fc373203c4ad68cbce624badade99.png)


![](http://image.prntscr.com/image/5390e065dfee4453bd7c95e25a777afd.png)

<a name="thamkhao"></a>
#Tài liệu tham khảo

http://openvswitch.org/support/config-cookbooks/qos-rate-limiting/

https://software.intel.com/en-us/articles/qos-configuration-and-usage-for-open-vswitch-with-dpdk
