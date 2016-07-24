# Cisco IOU L2 L3 lab với GNS3
# Mục lục
<h3><a href="#concept">1. Các phần mềm yêu cầu cho bài lab</a></h3>
<h3><a href="#iouvm_vir">2. Cài đặt GNS3 IOU VM trên Virtual Box</a></h3>
<h3><a href="#cfg_iou_server">3. Cấu hình IOU Server trên GNS3</a></h3>
<h3><a href="#integ">4. Tích hợp GNS3 với Cisco IOU</a></h3>
<h3><a href="#setup">5. Cấu hình network bonding với GNS3 và IOU switch</a></h3>
<ul>
    <li><a href="#topology">5.1. Mô hình lab</a></li>
    <li><a href="#cfg_sw">5.2. Cấu hình các switch</a></li>
</ul>
<h3><a href="#ref">6. Tham khảo</a></h3>
---

<h2><a name="concept">1. Các phần mềm yêu cầu cho bài lab</a></h2>
<div>
<ul>
    <li>Cài đặt GNS3 (bài lab sử dụng bản 1.3.3). <a href="https://github.com/GNS3/gns3-gui/releases/tag/v1.3.3">Tải GNS3 1.3.3.</a></li>
    <li>Virtual Box, tải <a href="https://www.virtualbox.org/">tại đây.</a></li>
    <li>IOU Images: sử dụng để tạo switch trên GNS3. Tải IOU Images sử dụng <a href="http://www.bittorrent.com/bittorrent-free">bittorent</a>. File torrent một số IOU Images mẫu có thể tải <a href="https://www.dropbox.com/s/es46wrxfajvrnbk/55EAD4B54E75A459176E0605F8BE32C9706E2CBA.torrent?dl=0">tại đây</a>.</li>
    <li>GNS3 IOU VM: đây là server để chạy các Switch VM. Tải image GNS3 IOU VM: <a href="http://sourceforge.net/projects/gns-3/files/IOU%20VMs/">http://sourceforge.net/projects/gns-3/files/IOU%20VMs/</a>. Chú ý chọn file *.ova phiên bản phù hợp với phiên bản GNS3, ở đây chọn file <a href="https://sourceforge.net/projects/gns-3/files/IOU%20VMs/GNS3%20IOU%20VM_1.3.3.ova/download">GNS3 IOU VM_1.3.3.ova</a></li>
    <li>IOURC: là file Cisco license cho các IOU Images. <a href="https://www.dropbox.com/s/8r64q7ttnigymrj/iourc.txt?dl=0">Tải IOURC.</a></li>
</ul>
</div>

<h2><a name="iouvm_vir">2. Cài đặt GNS3 IOU VM trên Virtual Box</a></h2>
<div>
    <ul>
        <li>Mở VirtualBox, import file *.ova đã tải về để tạo server.
        <br><br>
        <img src="http://i.imgur.com/l3Xm6pi.png">
        <br><br>
        </li>
        <li>Duyệt tới file *.ova, sau đó click Next
        <br><br>
        <img src="http://i.imgur.com/DiMQLkK.png">
        <br><br>
        </li>
        <li>Ở cửa sổ tiếp theo, click Import
        <br><br>
        <img src="http://i.imgur.com/ympa8bb.png">
        <br><br>
        </li>
        <li>Sau khi import xong ta có một máy ảo làm server. Tiến hành chỉnh sửa lại chế độ card mạng chọn lại card mạng cho server này hoạt động ở chế độ <b>Host Only</b>
        <br><br>
        <img src="http://i.imgur.com/Wph5zZb.png">
        <br><br>        
        </li>
        <li>Mở server lên, kiểm tra địa chỉ IP của server.(User: root, mật khẩu: cisco). Ví dụ địa chỉ server ở đây là: 10.10.100.128
        <br><br>
        <img src="http://i.imgur.com/IdYU537.png">
        <br><br>  
        </li>
        <li>Truy cập vào server trên trình duyệt để upload image của các switch lên server. Truy cập địa chỉ: <code>http://&lt;ip_server&gt;:8000/upload</code>. Ví dụ: http://10.10.100.128:8000/upload.</li>
        <br><br>
        <img src="http://i.imgur.com/oXi3a4n.png">
        <br><br>         
        <li>Sau khi tải file nén các image mẫu của các IOU switch về (sử dụng bittorent), giải nén ra ta sẽ có một số image mẫu như hình:
        <br><br>
        <img src="http://i.imgur.com/1V9YMJv.png">
        <br><br>
        </li>
        <li>Tiến hành upload một số image mẫu lên như hình.
        <br><br>
        <img src="http://i.imgur.com/Txws3qQ.png">
        <br><br>
        Sau khi upload thành công, chú ý note lại đường dẫn lưu image trên server của image tải lên.(đường dẫn này dùng trong cấu hình switch bên dưới)
        </li>
    </ul>
</div>
<h2><a name="cfg_iou_server">3. Cấu hình IOU Server trên GNS3</a></h2>
<div>Mở GNS3 lên và chuyển sang tab: <code>Edit->Preferences</code> hoặc sử dụng phím tắt <code>Ctrl+Shift+P</code> để mở cửa sổ cấu hình. Trên cửa sổ cấu hình chuyển sang tab <code>Server->Remote servers</code>. Sau đó cấu hình như hình minh họa bên dưới.
        <br><br>
        <img src="http://i.imgur.com/jxrjmDX.png">
        <br><br>
</div>
<h2><a name="integ">4. Tích hợp GNS3 với Cisco IOU</a></h2>
<div>
    Trước hết ta cần import cisco license để sử dụng các IOU images. Vẫn trong cửa sổ cấu hình như mục 3, chuyển sang tab <code>IOS on UNIX->General</code>. Nhấn "Browse" duyệt tới file license đã tải rồi lick Apply->OK để áp dụng cấu hình.
        <br><br>
        <img src="http://i.imgur.com/Zi2xtxp.png">
        <br><br>   
    Bây giờ ta sẽ tiến hành tạo switch layer 2 sử dụng file image đã tải lên server. Vẫn trong cửa sổ cấu hình của GNS3, chuyển sang tab <code>IOS on UNIX->IOU devices</code>. Click New tạo switch mới. 
        <br><br>
        <img src="http://i.imgur.com/2NwOWgQ.png">
        <br><br>   
    Click Next, nếu có thông báo hiện ra thì click OK. Sau đó đặt trên cho switch và paste đường dẫn của image trên server đã note lại ở bước 2, rồi click Finish tạo switch.
        <br><br>
        <img src="http://i.imgur.com/tU2GHQh.png">
        <br><br>      
        <img src="http://i.imgur.com/Bxf5lYN.png">
        <br><br>  
    Cuối cùng Click Apply->OK để xác nhận tạo switch mới.
        <br><br>      
        <img src="http://i.imgur.com/8kMC7qi.png">
        <br><br>      
</div>
<h2><a name="setup">5. Cấu hình network bonding với GNS3 và IOU switch</a></h2>
<ul>
    <li><h3><a name="topology">5.1. Mô hình lab</a></h3>
Mô hình lab sử dụng 2 switch đã tạo ở bước trên, tạo 2 đường kết nối giữa 2 switch và tiến hành cấu hình bonding trên 2 switch này.
        <br><br>      
        <img src="http://i.imgur.com/0iuWafd.png">
        <br><br>  
    </li>
    <li><h3><a name="cfg_sw">5.2. Cấu hình các switch</a></h3>
Chú ý sử dụng switch đã tạo, ví dụ như hình bên dưới.
        <br><br>      
        <img src="http://i.imgur.com/SFBUmNN.png">
        <br><br> 
    </li>
Bật các switch lên, sau đó click chuột phải vào mỗi switch, chọn <code>Console</code> để mở cửa sổ cấu hình.
<br>
Cấu hình trên switch 2 trước, lần lượt thực hiện các lệnh sau:
<pre>
    <code>
        conf t
        int range e0/0 -1
        sw t en d
        sw m t
        sw non
        channel-group 20 mode ?
        channel-group 20 mode passive
        end
    </code>
</pre>
Cấu hình trên switch 1, gõ từng lệnh cấu hình sau:
<pre>
    <code>
        conf t
        int range e0/0 -1
        sw t en d
        sw m t
        sw non
        channel-group 10 mode ?
        channel-group 10 mode active
        end
        wr
    </code>
</pre>
Trên switch 1, sau khi cấu hình xong, gõ lệnh kiểm tra <code>show etherchannel summary</code>. Kết quả thành công sẽ tương tự như sau:
<pre>
    <code>
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
    </code>
</pre>
Chú ý bảng cuối cùng thấy ở cột <b>Protocol</b> giá trị là <b>LACP</b>, và cột <b>Port</b> thấy kí hiệu P (ý nghĩa là hai đường kết nối đã được "bó" lại trên 1 kênh logic) thì cấu hình đã chính xác.
</ul>
<h2><a name="ref">6. Tham khảo</a></h2>
<div>
    [1] - <a href="http://letusexplain.blogspot.com/2015/07/cisco-iou-l2-l3-lab-with-gns3-switching.html">http://letusexplain.blogspot.com/2015/07/cisco-iou-l2-l3-lab-with-gns3-switching.html</a>
    <br>
    [2] - <a href="https://www.youtube.com/watch?v=vAitTGfsuJE">https://www.youtube.com/watch?v=vAitTGfsuJE</a>
    <br>
    [3] - <a href="https://www.youtube.com/watch?v=akGp2NX_0zI">https://www.youtube.com/watch?v=akGp2NX_0zI</a>
</div>
