#Storage
*Mục lục:*

[1 Block storage](#1)

[2 Disk partition](#2)

[3 Formatting and Filesystems](#3)

[4 Quản lý Storage Devices](#4)

[5 Partition and Format Storage Devices in Linux](#5)

==========================

<a name="1"></a>
###1 Block storage

Block storage là tên khác của block device. Một block device là một phần cứng dùng để chứa data (HDD,SSD,flash memory ...).

<a name="2"></a>
###2 Disk partition

Partitioning cho phép phân chia thành các phân vùng khác nhau cho các mục đích sử dụng. Disk có thể format và sử dụng mà không phải phân chia (partitioning).
Có 2 kiểu format là MBR hoặc GPT.

<ul>
<li>MBR: Là một phân vùng hệ thống có nhiều giới hạn. Ko thể dùng disk lớn hơn 2TB, và chỉ có tối đa 4 primary partition.</li>
<li>GPT: Đưa ra để giải quyết các hạn chế của MBR. </li>
</ul>

<a name="3"></a>
###3 Formatting and Filesystems

Để sử dụng disk cần phải format. Formatting là tiến trình của việc viết filesystem lên disk và chuẩn bị nó cho các file hệ thống. Một filesystem là một hệ thống, nó cấu trúc dữ liệu và điều khiển cách viết và thu hồi.
Nếu ko có filesystem thì ko thể sử dụng storage device.

Các filesystems phổ biến:

<ul>
<li>EXT4: Là phiên bản thứ 4 của hệ thống extended filesystem. Thích hợp với ổ SSD. Có cơ chế Journaling để đảm bảo việc ghi dữ liệu lên ổ cứng.</li> 
<li>XFS: Chuyên dùng cho vấn đề về hiệu suất và dữ liệu lớn. Có tính năng snapshoot. Có thể mất dữ liệu khi mất điện đột ngột.</li> 
<li>BTRFS: Cho phép quản lý các volume với tính năng snapshoot, cloning... </li> 
<li>ZFS: Vẫn đang được phát triển bởi Oracle.</li> 
<li>JFS: Tốn ít tài nguyên. Đạt hiệu suất tốt với nhiều file dung lượng lớn, nhỏ khác nhau.</li> 
</ul>

<a name="4"></a>
###4 Quản lý Storage Devices

Trong linux mọi thứ đều được định nghĩa bằng 1 file. Storage drives được xác định như 1 file trong thư mục /dev ví dụ /dev/sda.
Các thư mục con được xác định bằng các dạng

<ul><
<li>By-LABEL, UUID</li>
<li>Partlabel, Partuuid (Được dùng với GPT)</li>
<li>ID, Path</li>
</ul>

Dùng lệnh df với các options để biết các thông tin về về storage device

- df -h 
- df -h -x tmpfs 
- ... 

Dùng lệnh lsblk với các options để có thông tin về các Block-devices
<ul>
<li>lsblk</li>
<li>lsblk --t</li>
<li>lsblk --fs </li>
<li>lsblk -o NAME,FSTYPE,LABEL,UUID,MOUNTPOINT</li>
<li>...</li>
</ul>
Mount command:

<ul>
<li>mount -t ext4 /dev/sda1 /mnt </li>
<li>mount -t ext4 -o defaults,ro /dev/sda1 /mnt </li>
<li>mount -a ( mount tất các các filesystems được nêu trong /etc/fstab) </li>
</ul>

Listing Filesystem Mount Options:

`findmnt /mnt`

```sh
TARGET SOURCE    FSTYPE OPTIONS
/mnt   /dev/sda1 ext4   ro,relatime,data=ordered
```

<a name="5"></a>
###5 Partition and Format Storage Devices in Linux

Tool: parted

Định dạng ổ:

```sh
parted /dev/sda mklabel gpt
parted /dev/sda mklabel msdos
```

Tạo partition

`parted -a opt /dev/sdc mkpart primary ext4 0% 100%`

Tạo filesystem 

`mkfs.ext4 /dev/sdc1`



Tham khảo:
[1]- http://www.quantrimang.com.vn/print/84900.aspx
[2]- https://www.digitalocean.com/community/tutorials/how-to-perform-basic-administration-tasks-for-storage-devices-in-linux
[3]- https://www.digitalocean.com/community/tutorials/an-introduction-to-storage-terminology-and-concepts-in-linux
[4]- https://www.digitalocean.com/community/tutorials/how-to-partition-and-format-storage-devices-in-linux









