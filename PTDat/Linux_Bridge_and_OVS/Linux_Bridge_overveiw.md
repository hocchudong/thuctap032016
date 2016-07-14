#Linux Bridge

##1. Giới thiệu Linux bridge.

###a. Architect.

- Linux bridge là một soft-switch, một trong ba công nghệ cung cấp switch ảo trong hệ thống Linux (bên cạnh macvlan và OpenvSwitch), giải quyết vấn đề ảo hóa network bên trong các máy vật lý. 
- Bản chất, linux bridge sẽ tạo ra các switch layer 2 kết nối các máy ảo (VM) để các VM đó giao tiếp được với nhau và có thể kết nối được ra mạng ngoài. Linux bridge thường sử dụng kết hợp với hệ thống ảo hóa KVM-QEMU.

###b. Components.

![1]()

- Kiến trúc linux bridge minh họa như hình vẽ trên. Một số khái niệm liên quan tới linux bridge:
 <ul>
 <li>Port: tương đương với port của switch thật</li>
 <li>Bridge: tương đương với switch layer 2</li>
 <li>Tap: hay tap interface có thể hiểu là giao diện mạng để các VM kết nối với bridge cho linux bridge tạo ra</li>
 <li>FDB: chuyển tiếp các gói tin theo database để nâng cao hiệu năng switch</li>
 </ul>