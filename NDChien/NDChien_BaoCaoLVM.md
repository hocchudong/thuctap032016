#Các tính năng nâng cao của LVM

Chuẩn bị:
Máy ảo chạy hệ điều hành Ubuntu 14.04 có chế độ LVM cho ổ đĩa.
Đã ad thêm các ổ cứng sau khi cài đặt


###Mục lục:
[1 Tính năng Snapshot ]#1)

- [1.1 Tạo Snapshot](#1.1)

- [1.2 Restoring Snapshot or Merging](#1.2)

[2 Tính năng Thin Provisioning Volumes](#2)

- [2.1 Setup Thin Pool and Volumes](#2.1)

- [2.2 Over Provisioning](#2.2)

[3 Tính năng Manage Multiple Logical Volume Management Disks using Striping I/O](#3)

- [3.1 Chuẩn bị](#3.1)

- [3.2 Logical Volume management using Striping I/O](#3.2)

[4 Tính năng LVM Migration](#4)

- [4.1 Chuẩn bị](#4.1)

- [4.2 LVM Mirroring Method](#4.2)

- [4.3 LVM pvmove Mirroring Method](#4.3)

====================== 

<a name="1"></a>
###1 Tính năng Snapshot

LVM Snapshots are space efficient pointing time copies of lvm volumes. It works only with lvm and consume the space only when changes are made to the source logical volume to snapshot volume. If source volume has a huge changes made to sum of 1GB the same changes will be made to the snapshot volume.
Snapshots can’t be use for backup option. Backups are Primary Copy of some data’s, so we cant use snapshot as a backup option.

<img src=http://i.imgur.com/w0JRnB5.jpg>

**Chuẩn bị**

<img src=http://i.imgur.com/2gYdklq.png>

Trên hình ta đã có một logical Volume lv-demo1 được mount tới thư mục rỗng /mnt/demo1 và Volume Group vg-demo1.

<a name="1.1"></a>
**1.1 Tạo Snapshot**

lv-demo1 thuộc vg-demo1 nên check xem vg-demo1 có còn dung lượng để tạo Snapshot.

**Tạo ổ Snapshot**
```sh
# lvcreate -L 1GB -s -n lv-demo1-snap /dev/vg-demo1/lv-demo1        
      
OR

# lvcreate --size 1G --snapshot --name  lv-demo1-snap /dev/vg-demo1/lv-demo1
```

-s: Creates Snapshot

-n: Name for snapshot

<img src=http://i.imgur.com/9X5dcsP.png>

Các thành phần câu lệnh:
```sh
-L 1GB: Đặt dung lượng cho ổ snapshot
-s: Tạo snapshot
-n: Tạo tên cho snapshot
lv-demo1-snap: Tên snapshot
/dev/vg-demo1/lv-demo1: Volume cần snapshot
```

Kiểm tra bằng lệnh lvs ta có thêm 1 LV lv-demo1-snap với cột data có % = 0.00

<img src=http://i.imgur.com/lbUNuOh.png>

**Nếu muốn xóa snapshot đã tạo**

`lvremove /dev/vg-demo1/lv-demo1-snap`

Ta copy một số file vào thư mục /mnt/demo1 

<img src=http://i.imgur.com/Fv7TMdd.png>

Ta có thể thấy 22% dung lượng của snapshot volume đã được dùng. Nếu bạn dùng quá dung lượng thì sẽ có thông báo **Input/output error** khi kiểm tra lvs

Để có nhiều thông tin hơn ta dùng lệnh lvdisplay vg-demo1/lv-demo1-snap

**Mở rộng Snapshot Volume**

`lvextend -L +1G /dev/vg-demo1/lv-demo1-snap`

**Mở rộng tự động**

Vào file /etc/lvm/lvm.conf và chỉnh sửa

<img src=http://i.imgur.com/Zr1E5yT.png>

Dòng 1: Khi dung lượng đạt tới 100%
Dòng 2: Kích thước volume sẽ tăng 20%

<a name="1.2"></a>
**1.2 Restoring Snapshot or Merging**

Để restore Snapshot chúng ta phải un-mount file system

`umount /mnt/demo1`

Check bằng lệnh df -h để kiểm tra đã un-mount thành công hay chưa.

**Restore snapshot**

`lvconvert --merge /dev/vg-demo1/lv-demo1-snap`

Sau khi quá trình kết thúc thì Snapshot Volume sẽ được xóa.

mount lại Volume và vào thư mục /mnt/demo1. Nếu các file copy đã bị xóa thì quá trình đã hoàn thành.

<a name="2"></a>
###2 Tính năng Thin Provisioning Volumes

Tính năng này cho phép chúng ta tạo ra số Volume có tổng dung lượng lớn hơn số lượng cho phép.

<img src=http://i.imgur.com/l60cF0T.jpg>

<a name="2.1"></a>
**2.1 Setup Thin Pool and Volumes**

Ta có 1 Physical Volume sdd1 dùng lệnh `vgcreate vg-thin /dev/sdd1` để tạo ra 1 Volume group cho Thin-Pool

<img src=http://i.imgur.com/lS0HDr8.jpg>

**Tạo 1 Thin-Pool**

`lvcreate -L 9GB --thinpool thin-demo vg-thin`

--thinpool: Để tạo thinpool

thin-demo: Tên của Thin Pool

vg-thin: Tên Volume Group

**Tạo Thin Volume từ Thin-Pool**

`lvcreate -V 2G --thin -n thin-demo-client1 vg-thin/thin-demo` tạo 1 Thin virtual volume với tên **thin-demo-client1** trong **thin-demo**

<img src=http://i.imgur.com/dv9lAEZ.jpg>

Ta sẽ tạo 4 Thin-demo-client 1,2,3,4 

Tạo 4 thư mục cient 1,2,3,4 trong /mnt. Tạo File System bằng mkfs và mount các Thin-demo-client vào các thư mục
```sh
mkdir /mnt/client1

mkfs.ext4 /dev/vg-thin/thin-demo-client1 

mount /dev/vg-thin/thin-demo-client1 /mnt/client1
```

**Copy file vào các thư mục client để dung lượng ổ tăng lên**

<img src=http://i.imgur.com/JrRbRds.jpg>

<a name="2.2"></a>
**2.2 Over Provisioning**

Bây giờ client5 đến và yêu cầu 2GB nhưng ta đã gán hết 8GB cho 4 client trước. Vậy là trên lý thuyết ta ko thể cho client 2GB nữa. 
Cách giải quyết là dùng chức năng Over Provisioning. (which means giving the space more than what I have).

**Tạo Thin-demo-client5. Tạo thư mục /mnt/client5. Tạo File System và mount thin-demo-client5.**

<img src=http://i.imgur.com/VkJwUbj.jpg>

**Copy file vào /mnt/client5**

<img src=http://i.imgur.com/e626ULh.jpg>

Phần dung lượng của Client đã tăng lên.

Tổng kết lại thì với 1 Thin-Pool 8GB, ta có thể chia ra số Thin Volume Client có tổng dung lượng lớn hơn 8GB nhưng tổng mức dùng của các Thin Volume Client ko lớn hơn 8GB.

<a name="3"></a>
###3 Tính năng Manage Multiple Logical Volume Management Disks using Striping I/O

LVM Striping là tính năng cho phép ghi dữ liệu lên nhiều ổ thay vì chỉ một ổ Physical volume.

Tính năng của Striping:

<ul>
<li>It will increase the performance of disk.</li>
<li>Saves from hard write over and over to a single disk.</li>
<li>Disk fill-up can be reduced using striping over multiple disk.</li>
</ul>

<a name="3.1"></a>
**3.1 Chuẩn bị**

Ta tạo 3 Physical volume, mỗi Volume là 1GB

<img src=http://i.imgur.com/31w4EIj.png>

Tạo Volume Group với tên vg-strip từ 3 Physical volume trên

`vgcreate vg-strip /dev/sd[b-d]1`

<img src=http://i.imgur.com/lNwSyos.png>

<a name="3.2"></a>
**3.2 Logical Volume management using Striping I/O**

Ta tạo Logical volume, Cần xác định giá trị strip, bao nhiêu dữ liệu sẽ được ghi.

`lvcreate -L 500M -n lv-strip -i3 vg-strip`

Ở đây ta tạo Logical volume tên là lv-strip có dung lượng 500M từ Volume Group vg-strip và xác định 3 tripe.
stripesize có kích thước là 64KB, Nếu muốn giá trị khác ta dùng thêm thành phần -I 

<img src=http://i.imgur.com/62sNtw4.png>

Gõ  `lvdisplay vg-strip/lv-strip -m`

ta sẽ thấy được lv-strip sẽ được ghi lên 3 stripe

<img src=http://i.imgur.com/E6NUkJn.png>

Phần dung lượng còn lại của sdb1,sbc1,sbd1 sau khi chia cho Thin-Pool

<img src=http://i.imgur.com/xZlRkgq.png>

<a name="4"></a>
###4 Tính năng LVM Migration

Tính năng này cho phép di chuyển dữ liệu từ logical volumes sang một ổ mới mà không làm mất dữ liệu hoặc downtime. Có thể áp dụng với disk SATA,SSD,SAN storage iSCSI or FC

<a name="4.1"></a>
**4.1 Chuẩn bị**

Ta có 1 Logical Volume được tạo ra từ Physical Volume /dev/sdb1. Và các Drive /dev/sdc, /dev/sdd mới gắn thêm.

<img src=http://i.imgur.com/tKSZWu6.png>

Mount lv-migration tới thư mục /mnt/demo và copy file 123.txt có nội dung bất kì vào thư mục.

Tạo Physical Volume /sdc1 và extend vào vg-migration.

<img src=http://i.imgur.com/myOFW7e.png>

<a name="4.2"></a>
**4.2 LVM Mirroring Method**

Ta dùng 'lvconvert' command  để migration dữ liệu sang ổ mới

`lvconvert -m 1 /dev/vg-migration/lv-migration /dev/sdc1`

-m: mirror (Tạo ổ migration)
1: 1 mirror

Quá trình hoàn tất. Dùng lvs -o+devices để kiểm tra thông tin.

<img src=http://i.imgur.com/nRBD535.png>

Khi đã tạo 1 mirror mới thì bạn có thể bỏ /dev/sdb1

`lvconvert -m 0 /dev/vg-migration/lv-migration /dev/sdb1`

Check lại với `lvs -o+devices` ta sẽ thấy lv-migration chỉ còn nối với /dev/sdc1

<img src=http://i.imgur.com/LWRZuJ5.png>

Check lại nội dung file 123.txt đã tạo bên trên để đảm bảo dữ liệu ko bị mất.

<a name="4.3"></a>
**4.3 LVM pvmove Mirroring Method**

Phần này sẽ hướng dẫn dùng 'pvmove' thay vì 'lvconvert'

Các bước chuẩn bị cũng như phần 4.1 tiếp theo ta sẽ dùng command 

`pvremove -n /dev/vg-migration/lv-migration /dev/sdb1 /dev/sdc1`

Đây là cách đơn giản nhưng trong thực tế thì thường sử dụng Mirroring hơn pvmove


Tham khảo:

http://www.tecmint.com/create-lvm-storage-in-linux/
 

