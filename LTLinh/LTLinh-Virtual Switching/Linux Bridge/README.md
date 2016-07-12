#Linux Bridge
#Mục lục
#1. Khái niệm - Chức năng.
- Bridge là một cách để kết nối hai đoạn Ethernet với nhau một cách độc lập các giao thức. Các gói tin được chuyển tiếp dựa trên địa chỉ Ethernet (MAC Address), chứ không phải là địa chỉ IP.Khi bạn nối hai mạng Ethernet, hai mạng trở thành một mạng Ethernetđơn (lớn hơn).
- Linux bridge là một phần mềm đươc tích hợp vào trong nhân Linux để giải quyết vấn đề ảo hóa phần network trong các máy vật lý.
- Linux bridge sẽ tạo ra các switch layer 2 kết nối các máy ảo (VM) để các VM đó giao tiếp được với nhau và có thể kết nối được ra mạng ngoài.
- `bridge-utils`: Gói bridge-utils chứa một tiện ích cần thiết để tạo và quản lý các thiết bị bridge. Điều này rất hữu ích trong việc thiết lập hệ thống mạng cho một máy ảo được lưu trữ.
- Linux bridge thường sử dụng kết hợp với hệ thống ảo hóa KVM-QEMU.
#2. Kiến trúc.
![](http://image.prntscr.com/image/f2e8a840f7e547e298649f3d9c22377b.png)

##2.1 Linux Bridge với KVM
![](http://i.imgur.com/t15QQny.png)

- `Bridge`: tương đương với switch layer 2
- `Port`: tương đương với port của switch thật
- `Tap (tap interface)`: có thể hiểu là giao diện mạng để các VM kết nối với bridge cho linux bridge tạo ra
- `fd (forward data)`: chuyển tiếp dữ liệu từ máy ảo tới bridge

#3. Các tính năng
- STP: Spanning Tree Protocol - giao thức chống lặp gói tin trong mạng
- VLAN: chia switch (do linux bridge tạo ra) thành các mạng LAN ảo, cô lập traffic giữa các VM trên các VLAN khác nhau của cùng một switch.
- FDB (forwarding database): chuyển tiếp các gói tin theo database để nâng cao hiệu năng switch. Database lưu các địa chỉ MAC mà nó học được. Khi gói tin Ethernet đến, bridge sẽ tìm kiếm trong database có chứa MAC address không. Nếu không, nó sẽ gửi gói tin đến tất cả các cổng.

#4. So sánh với các giải pháp khác.
#5. LAB.
- note: Đường dẫn cấu hình card mạng trong kvm. `/var/lib/libvirt/network`


#Tài liệu tham khảo.
https://wiki.debian.org/BridgeNetworkConnections
