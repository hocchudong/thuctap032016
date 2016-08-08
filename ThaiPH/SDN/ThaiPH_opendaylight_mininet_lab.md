# Lab SDN - OpenDaylight SDN controller với Mininet Emulator
# Mục lục
<h3><a href="#odl">1. OpenDaylight SDN Controller</a></h3>
<h3><a href="#mininet">2. Mininet Emulator</a></h3>
<h3><a href="#lab">3. Dựng lab SDN sử dụng OpenDaylight và Mininet</a></h3>
<ul>
    <li><a href="#topo">3.1. Topology</a></li>
    <li><a href="#cfg">3.2. Cài đặt và cấu hình</a></li>
</ul>
<h3><a href="#ref">4. Tham khảo</a></h3>

---

<h2><a name="odl">1. OpenDaylight SDN Controller</a></h2>
<div>
<ul>
    <li>
        OpenDaylight là phần mềm mã nguồn mở dành cho Software Defined Networking (SDN) sử dụng giao thức mở cung cấp khả năng kiểm soát tập trung, có khả năng lập trình được và theo dõi các thiết bị mạng. Giống như nhiều SDN Controllers khác, OpenDaylight hỗ trợ OpenFlow, cũng như cung cấp các giải pháp mạng khác sẵn sàng để cài đặt khi có yêu cầu.      
    </li>
    <li>
        OpenDaylight cung cấp giao diện cho phép kết nối các thiết bị mạng nhanh chóng và thông minh để tối ưu hiệu năng mạng
    </li>
    <li>
        OpenDaylight Controller cung cấp northbound APIs, được sử dụng bởi các ứng dụng. Các ứng dụng này sử dụng controller để thu thập thông tin về mạng, chạy các thuật toán để kiểm soát, phân tích, sau đó sử dụng OpenDaylight Controller tạo các rules mới cho mạng.
    </li>
    <li>
        OpenDaylight Controller viết bằng ngôn ngữ Java, có nghĩa là có thể sử dụng OpenDaylight Controller trên bất kì môi trường nào hỗ trợ Java. Tuy nhiên để đạt hiệu năng tốt nhất, OpenDaylight nên chạy trên môi trường Linux hỗ trợ JVM tối thiểu 1.7.
    </li>
</ul>
</div>

<h2><a name="mininet">2. Mininet Emulator</a></h2>
<div>
<ul>
    <li>
         Mininet là một công cụ giả lập mạng, bao gồm tập hợp các hosts đầu cuối, các switches, routers và các liên kết trên một Linux kernel. Mininet sử dụng công nghệ ảo hóa (ở mức đơn giản) để tạo nên hệ thống mạng hoàn chỉnh, chạy chung trên cùng một kernel, hệ thống và user code. 
    </li>
    <li>
        Các host ảo, switch, liên kết và các controller trên mininet là các thực thể thực sự, được giả lập dưới dạng phần mềm thay vì phần cứng. Một host mininet có thể thực hiện ssh vào đó, chạy bất kì phần mềm nào đã cài trên hệ thống linux (môi trường mà mininet đang chạy). Các phần mềm này có thể gửi gói tin thông các ethernet interface của mininet với tốc độ liên kết và trễ đặt trước. 
    </li>
    <li>
        Mininet cho phép tạo topo mạng nhanh chóng, tùy chỉnh được topo mạng, chạy được các phần mềm thực sự như web servers, TCP monitoring, Wireshark; tùy chỉnh được việc chuyển tiếp gói tin. Mininet cũng dễ dàng sử dụng và không yêu cầu cấu hình đặc biệt gì về phần cứng để chạy: mininet có thể cài trên laptop, server, VM, cloud (linux).
    </li>
</ul>
</div>

<h2><a name="lab">3. Dựng lab SDN sử dụng OpenDaylight và Mininet</a></h2>
<ul>
    <li><h3><a name="topo">3.1. Topology</a></h3>
<br><br>
<img src="http://i.imgur.com/Vde39t1.jpg">
<br><br>
Chuẩn bị 2 máy ảo (chạy trên VMWare Workstation) cài ubuntu server 14.04, mỗi máy có hai card mạng như sau:
            <ul>
                <li><b>Card NAT: </b>
                Thuộc dải <i>172.16.69.0/24</i> (dải NAT hay VMNet8 của VMWare)
                </li>
                <li><b>Card Host Only: </b>
                Thuộc dải <i>10.10.10.0/24</i> (ở đây là dải VMNet2 chế độ Host Only)
                </li>
            </ul>
    </li>

    <li><h3><a name="cfg">3.2. Cài đặt và cấu hình</a></h3>
        <h4>Mininet Host</h4>
        <div>
            <ul>
                <li>Đảm bảo cấu hình card mạng tương tự như sau:
        <pre>
            <code>
        mininet@mininet-vm:~$ landscape-sysinfo
          System load:  0.43              Processes:           79
          Usage of /:   26.0% of 6.76GB   Users logged in:     1
          Memory usage: 9%                IP address for eth0: 172.16.69.177
          Swap usage:   0%                IP address for eth1: 10.10.10.176     

          Graph this data and manage this system at:
            https://landscape.canonical.com/
            </code>
        </pre>
                </li>
                <li>
                    Cài đặt mininet, sử dụng một trong hai cách sau:
                    <ul>
                        <li>Tải Mininet VM image đã cài sẵn Mininet và các thành phần cần thiết rồi cấu hình lại card mạng như trên. Có thể tải Mininet VM <a href="https://github.com/mininet/mininet/wiki/Mininet-VM-Images">tại đây.</a></li>
                        <li>Cài đặt mininet manual, thực hiện các lệnh sau để cài đặt mininet:
        <pre>
            <code>
        sudo apt-get update
        sudo apt-get install git
        git clone git://github.com/mininet/mininet
        cd mininet
        git tag  # list available versions
        git checkout -b 2.2.1 2.2.1  # or whatever version you wish to install
        cd ..
        mininet/util/install.sh -a
            </code>
        </pre>
                        </li>
                    </ul> 
                </li>
            </ul>
        </div>

        <h4>OpenDaylight Host</h4>
        <div>
            <ul>
                <li>Đảm bảo cấu hình card mạng tương tự như sau:
        <pre>
            <code>
        ovs@opendaylight:~$ landscape-sysinfo
          System load:  0.2                Users logged in:       1
          Usage of /:   27.4% of 17.34GB   IP address for eth0:   172.16.69.162
          Memory usage: 5%                 IP address for eth1:   10.10.10.165
          Swap usage:   0%                 IP address for virbr0: 192.168.122.1
          Processes:    383     

          Graph this data and manage this system at:
            https://landscape.canonical.com/
            </code>
        </pre>
                </li>
                <li>Cài đặt java và cấu hình biến môi trường JAVA_HOME:
<pre>
    <code>
sudo apt-get install openjdk-7-jdk

# mo file /etc/environment
sudo vi /etc/environment

#them dong sau vao cuoi file
JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64

#ap dung cau hinh
source /etc/environment
    </code>
</pre>
                </li>

                <li>
                    Tải OpenDaylight Beryllium <a href="https://nexus.opendaylight.org/content/groups/public/org/opendaylight/integration/distribution-karaf/0.4.0-Beryllium/distribution-karaf-0.4.0-Beryllium.zip">tại đây.</a>
                </li>

                <li>Giải nén, chạy OpenDaylight và cài đặt các feature cần thiết:
<pre>
    <code>
unzip distribution-karaf-0.4.0-Beryllium.zip
cd distribution-karaf-0.4.0-Beryllium/
./bin/karaf

# doi cho OpenDaylight khoi dong len thi cai cac feature can thiet nhu sau
feature:install odl-restconf odl-l2switch-switch odl-mdsal-apidocs odl-dlux-all
    </code>
</pre>

Giao diện OpenDaylight trên terminal sẽ tương tự như sau:
<br><br>
<img src="http://i.imgur.com/06AwYFN.png">
<br><br>
                </li>
            </ul>
        </div>

        <h4>Tạo topo và kiểm tra thông tin flow trên OpenDaylight</h4>
        <div>
            <ul>
                <li>Trên <b>Mininet Host</b>, chạy lệnh sau tạo topo đơn giản gồm ba host và 3 OpenFlow switch:
<pre>
    <code>
# tao topo, vao giao dien <i>mininet></i>
sudo mn --topo linear,3 --mac --controller=remote,ip=172.16.69.162,port=6633 --switch ovs,protocols=OpenFlow13

# ping kiem tra ket noi
pingall
    </code>
</pre>
                </li>

                <li>Mở trình duyệt truy cập địa chỉ: http://ip_odl_host:8181/index.html (ví dụ ở đây là http://172.16.69.162:8181/index.html). Nhập username và password đều là: <i>admin</i>. Topo sẽ hiện lên tương tự như sau:
                <br><br>
                <img src="http://i.imgur.com/yYjQ5uy.png">
                <br><br>
                Xem thông tin trên các openflow switch:
                <br><br>
                <img src="http://i.imgur.com/hkD4c86.png">
                <br><br>
                </li>
            </ul>
        </div>

    </li>

</ul>
<h2><a name="ref">4. Tham khảo</a></h2>
<div>
    [1] - <a href="https://github.com/mininet/mininet/wiki/Introduction-to-Mininet">https://github.com/mininet/mininet/wiki/Introduction-to-Mininet</a>
    <br>
    [2] - <a href="http://www.brianlinkletter.com/using-the-opendaylight-sdn-controller-with-the-mininet-network-emulator/">http://www.brianlinkletter.com/using-the-opendaylight-sdn-controller-with-the-mininet-network-emulator/</a>
    <br>
    [3] - <a href="https://www.opendaylight.org/introduction-getting-started-guide">https://www.opendaylight.org/introduction-getting-started-guide</a>
</div>