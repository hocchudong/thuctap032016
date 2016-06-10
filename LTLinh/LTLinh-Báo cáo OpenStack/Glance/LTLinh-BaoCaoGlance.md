#OpenStack Glance
OpenStack Glance là một dịch vụ image, cung cấp khám phá, đăng ký và lấy cho disk và server images. Glance là trung tâm kho chứa các images virtual. Glance có RESTful API cho phép truy vấn VM image metadata cũng như thu hồi các images. VM images có sẵn thông qua glance có thể được lưu trữ từ nhiều địa điểm từ hệ thống tập tin đơn giản đến Object Storage System (Switf).

Trong glance, images được lưu dưới dạng các template, được sử dụng để tạo một máy ảo mới. Glance được thiết kế là một dịch vụ độc lập cần thiết cho các disk images ảo, đặt thành các tổ chức. Glance cung cấp giải pháp end-to end cho quản lý image disk của cloud. Nó có thể take snapshots từ những máy ảo đang chạy để sao lưu.

#Mục lục: 
**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [1. Các thành phần trong Glance.](#thanh_phan)
- [2. Kiến trúc của Glance.](#kien_truc)
- [3. Glance Formats:](#format)
- [4. Glance Status Flow](#status_flow)
- [5. Glance Configuration Files](#config_file)
- [6. Image and Instance](#image_instance)
- [7. Các chú ý đối với glance](#chu_y)
- [8. Multiple store locations for Glance images](#multi_store)
- [9. Glance Image Cache](#image_cache)
- [10. Tài liệu tham khảo](#tailieuthamkhao)

<a name="thanh_phan"></a>
##1. Các thành phần trong Glance.

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing2.png)

- **Glance-API:** Nơi đồng ý các API calls để phát hiện, thu hồi và lưu trữ images.
- **Glance-Registry:** Nơi lưu trữ, xử lý và lấy các thông tin metadata cho images.
- **database:** Lưu trữ các metadata.
- **Storage repository:** Tích hợp với các thành phần bên ngoài khác như hệ thống file thường, Amazon S3 và HTTP cho images.

Glance đồng ý các API request images từ người dùng cuối hoặc các thành phần của NOVA và có thể lưu các file vào Object storage service (swift), hoặc các storage repository khác.

Dịch vụ image hỗ trợ các back end để lưu trữ:

- **File system:** Mặc định, các file images của virtual machine được lưu vào hệ thống file. Đây là giải pháp đơn giản.
- **Object Storage:** The OpenStack highly available service for storing objects.
- **Block storage:** The OpenStack highly available service for storing blocks.
- **Vmware:** ESX/ESXi or vCenter Server target system.
- **S3:** The Amazon S3 service.
- **HTTP**: Openstack image có thể đọc images của máy ảo trên internet thông qua giao thức http. Cách này chỉ có thể đọc.
- **RADOS Block Device (RBD):** Stores images inside of a Ceph storage cluster using Ceph’s RBD interface.
- **Sheepdog:** Hệ thống phân phối lưu trữ cho QEMU/KVM.
- **GridFS:** Lưu trũ images bằng cách sử dụng MongoDB.

<a name="kien_truc"></a>
##2. Kiến trúc của Glance.
Glance có kiến trúc client-server và cung cấp REST API để request đến server. Request từ client sẽ được đồng ý thông qua REST API và đợi Keystone xác nhận. Glance Domain controller quản lý tất cả hoạt động nội bộ, được chia thành các lớp, mỗi lớp thực hiện các nhiệm vụ riêng.

Glance store là nơi giao tiếp giữa các lớp glance và storage backend bên ngoài hoặc local file system và cung cấp interface thống nhất để truy cập. Glance sử dụng SQL để truy cập cho mỗi thành phần trong hệ thống. 

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing11.png)


Kiến trúc của Glance bao gồm nhiều thành phần:

- **Client:** Bất kỳ một ứng dụng được sử dụng Glance server.
- **REST API:** Các chức năng Glance được phơi bày thông qua REST.
- **Database Abstraction Layer (DAL):** Là một interface cho lập trình ứng dụng. Dùng để thống nhất các thông tin liên lạc giữa Glance và databases.
- **Glance Domain Controller:** Thực hiện các chức năng chính của Glance: authorization, notifications, policies, database connections.
- **Glance Store:** Tương tác giữa Glance và các data stores khác nhau.
- **Registry Layer:** Là lớp tùy chọn, tổ chức các thông tin liên lạc giữa domain và DAL bằng cách sử dụng một dịch vụ riêng biệt.

<a name="format"></a>
##3. Glance Formats:
Khi chúng ta uploading một file image đến glance, chúng ta cần xác định formats của Virtual machine images. Glance hỗ trợ nhiều định dạng như Disk format và Container Formats. Virtual disk tương tự như ổ đĩa máy thật, chỉ cô động trong một tập tin. Ảo hóa khác nhau hỗ trợ các disk formats khác nhau.

**Disk format:** Disk format của images máy ảo là định dạng của tập tin image cơ bản. Các nhà cung cấp thiết bị ảo có định dạng khác nhau để đưa ra những thông tin chứa trong một hình ảnh đĩa của máy ảo. Sau đây là các định dạng được hỗ trợ bởi Glance.

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing6.png)


**Container Formats:** Glance cũng hỗ trợ các khái niệm về container format, trong đó mô tả các định dạng tập tin và có chứa metadata để bổ sung vào máy ảo. Lưu ý rằng chuỗi định dạng container hiện không được sử dụng bởi Glance hoặc các thành phần OpenStack khác, vì vậy để an toàn chỉ cần xác định `bare` như là định dạng container nếu bạn không chắc chắc. Sau đây là các container format được hỗ trợ trong Glance.

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing8.png)


Chú ý, Container Formats hiện không được sử dụng bởi Glance hoặc các thành phần khác của OpenStack. Vì vậy, `bare` được cho là định dạng container. Khi chúng ta tải lên một image trong glane, bare có nghĩa là không contrainer.

<a name="status_flow"></a>
##4. Glance Status Flow
Glance status flow hiển thị status của image khi chúng ta uploading. Khi chúng ta tạo một image, bước đầu tiên là xếp hàng, image sẽ nằm trong hàng đợi trong một thời gian ngắn để định danh, dành cho image và sẵn sàng upload. Sau khi xếp hạng, image đi đến status `Saving` có nghĩa là không được tải lên hoàn toàn. Một khi image được tải lên hoàn toàn thì status `Active`. Khi uploading thất bại, nó sẽ đi vào trạng thái `killed` hoặc `delete`. Chúng ta có thể tắt và kích hoạt lại các image được tải lên bằng cách sử dụng dòng lệnh.
Ta có sơ đồ dưới: 
![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing1.jpg)


- **queued:** Việc nhận dạng hình ảnh được dành cho Glance registry. Không có dữ liệu image nào được tải lên Gance và kích thước image không được set 0 khi tạo.
- **saving:** Biểu thị dữ liệu raw của images khi bắt đầu được upload lên glance. Khi image được đăng ký với lệnh call to POST /images và header hiện tại là `x-image-meta-location`, image đó sẽ không bao giờ được trong tình trạng `saving` (như dữ liệu image đã có sẵn ở một vị trí khác). 

- **active:** Biểu thị image có sẵn trong Glance. Điều này xảy ra khi image data được tải lên, hoặc kích thước hình ảnh được thiết về 0 khi tạo.

- **deactivated:** Biểu thị truy cập đến image data không được phép với bất kỳ user nào không phải là admin. Nghiêm cấm các hoạt động như image export và image cloning có thể yêu cầu image data.

- **killed:** Biểu thị rằng một lỗi xảy ra trong quá trình tải image lên, và image này không đọc được.

- **delete:** Glance giữ lại các thông tin về image, nhưng nó không còn sẵn để sử dụng. Một image trong state sẽ được gỡ bỏ tự động vào một ngày sau đó.
- **Deactivating and Reactivating an image:** Chúng ta có thể deactive tạm thời 1 image. Sau đó có thể active lại hoặc loại bỏ nó. 
- **pending_delete:** Tương tự như trạng thái `deleted`. Image khi ở trạng thái này thì không thể khôi phục.

<a name="config_file"></a>
##5. Glance Configuration Files
Thư mục chưa file cấu hình glance `/etc/glance`

- **metadefs:** This directory contains predefined namespaces for Glance Metadata Definitions Catalog. Files from this directory can be loaded into the database using `db_load_metadefs` command for glance-manage. Similarly you can unload the definitions using `db_unload_metadefs` command.
- **Glance-api.conf:** File cấu hình api.
- **Glance-registry.conf:** File cấu hình registry, là nơi lưu trữ metadata của images.
- **Glance-scrubber.conf:** Utility used to clean up images that have been deleted. Nhiều glance-scrubber có thể chạy trên một deployment. Tuy nhiên, chỉ có một hành động clean-up scrubber trong glance-scrubber.conf. Clean-up scrubber phối hợp với các glance scrubbers khác bằng cách duy trì một hàng đợi những image cần được hủy bỏ. Nó cũng quy định cụ thể các mục cấu hình quan trọng như thời gian giữa các lần chạy, chiều dài thời gian của hình ảnh  có thể được cấp phát trước khi họ xóa cũng như các lựa chọn kết nối registry. Nó có thể chạy như một công việc định kỳ hoặc long-running daemon.
- **glance-api-paste.ini:** 
- **glance-registry-paste.ini:**
- **glance-cache.conf:**     
- **glance-manage.conf:**      
- **schema-image.json:**
- **policy.json:** Bổ sung kiểm soát truy cập cho image service. Chúng ta có thể xác định vai trò, chính sách, bảo mật trong glance.

<a name="image_instance"></a>
##6. Image and Instance
Như đã nói ở trên, Disk images được lưu trữ dưới dạng các tamplate. Dịch vụ Image điều khiển lưu trữ và quản lý các images. Instance là các máy ảo độc lập mà chạy trên compute node, compute node quản lý các instance. Người dùng có thể khởi động bất kỳ số lượng các instance từ các image giống nhau.Mỗi instance được lauched được thực hiện bằng cách sao chép base image, bất kỳ sửa đổi về instance không ảnh hưởng đến base image. Chúng ta có thể take snapshot instance đang chạy và có thể được sử dụng để khởi động các instance khác.

Khi chúng ta khởi động một instance, chúng ta cần phải xác định flavor, là đại diện cho tài nguyên ảo. Flavors xác định cpu, ram có sẵn, kích thước ổ đĩa. OpenStack dung cấp các flavor được xác định trước, và chúng ta có thể tạo và sửa các flavors theo ý mình.

Sơ đồ dưới đây cho biết tình trạng hệ thống trước khi launching một instance. Các image store, có số lượng image được xác định trước, compute nod chứa vcpu sẵn, bộ nhớ và tài nguyên đĩa địa phương và cinder-volume chứa số lượng contains number được xác định trước.

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/Untitled-drawing2.jpg)



Trước khi launching chọn một image, flavor và bất kỳ thuộc tính tùy chọn.flavor được lựa chọn cung cấp một root volume, dán nhãn là VDA và lưu trữ tạm thời bổ sung được dán nhãn là VDB và cinder-volume là ánh xạ tới ảo đĩa thứ ba và gọi nó là VDC.

![](http://www.sparkmycloud.com/blog/wp-content/uploads/2016/01/new.jpg)


Trong hình này, các image base được sao chép vào local disk từ các image store. VDA là đĩa đầu tiên mà các instances truy cập, các instance bắt đầu nhanh hơn nếu kích thước của image là nhỏ hơn như ít dữ liệu cần phải được sao chép trên mạng. VDB là một đĩa trống tạm thời được tạo ra dùng với instance, nó sẽ được xóa khi dụ chấm dứt.

VDC kết nối với cinder-volume sử dụng iSCSI. Sau khi compute node quy định các vCPU và tài nguyên bộ nhớ, các instance khởi động lên từ khối lượng gốc vda. Instance chạy và thay đổi dữ liệu trên các đĩa. Nếu volume store nằm trên một mạng riêng biệt, tùy chọn `my_block_storage_ip` quy định trong tập tin cấu hình storage node chỉ đạo lưu lượng dữ liệu image với các compute node.

Khi instance được xóa bỏ, the state is reclaimed with the exception of the persistent volume. Việc lưu trữ tạm thời bị purged; bộ nhớ và tài nguyên vCPU được giải phóng. Những image vẫn không thay đổi trong suốt quá trình này.

<a name="chu_y"></a>
##7. Các chú ý đối với glance.
###7.1 Thư mục lưu trữ images.
`/var/lib/glance/images`

- Đoạn file cấu hình thư mục lưu trữ image trong `glance-api.conf`
```sh
[glance_store]
default_store = file
stores = file,http
filesystem_store_datadir = /var/lib/glance/images/
```

###7.2 Thư mục chứa file cấu hình glance:
Mình đã nói ở mục 5 ở trên. :D

###7.3 Thư mục chứa log glance
`/var/log/glance/`

- **glance-api.log:** Image service API server
- **glance-registry.log:** Image service Registry server

<a name="multi_store"></a>
##8. Multiple store locations for Glance images
- First we need to create the directories where hard disks are going to be mounted
```sh
sudo mkdir /var/lib/glance/lvm-images
sudo mkdir /var/lib/glance/extended-images
```

- Next, we mount the devices at the directories created in the previous step
```sh
sudo mount /dev/sdc1 /var/lib/glance/lvm-images/
sudo mount /dev/sdd1 /var/lib/glance/extended-images/
```

- An important step is making the glance user the owner of that directories
```sh
chown glance:glance /var/lib/glance/lvm-images/
chown glance:glance /var/lib/glance/extended-images/
```

- Cấu hình config `/etc/glance/glance-api.conf`

Chúng ta tìm kiếm đoạn `Filesystem Store Options` và thay đổi nó:

Chúng ta để trống tùy chọn `filesystem_store_datadir=`. Nếu chúng ta *comment* tùy chọn này thì glance sẽ sử dụng **default store location** và sẽ báo lỗi khi tạo image.

Và chúng ta sẽ thêm tùy chọn `filesystem_store_datadirs`, một dòng cho một thư mục mà ta đã tạo ở bước trên.

Chúng ta sử dụng **priorities** trên glance. priority 200 được ưu tiên hơn priority 100. Nếu chúng ta không chỉ định mức độ ưu tiên nào, thì mặc định sẽ là 0.

```sh
# ============ Filesystem Store Options ========================
filesystem_store_datadir=
filesystem_store_datadirs=/var/lib/glance/images
filesystem_store_datadirs=/var/lib/glance/lvm-images:200
filesystem_store_datadirs=/var/lib/glance/extended-images:100
```

- Khởi động lại dịch vụ glance-api: `service glance-api restart`

- Up một file image: 
```sh
openstack image create "cirros" \
 --file cirros-0.3.4-x86_64-disk.img \
 --disk-format qcow2 --container-format bare \
 --public
```

- Vào thư mục kiểm tra image đã tồn tại. Thư mục `lvm-images`
```sh
root@controller:/var/lib/glance/lvm-images# ls -la
total 25984
drwxr-xr-x 3 glance glance     4096 Jun  8 15:22 .
drwxr-xr-x 6 glance glance     4096 Jun  8 14:17 ..
-rw-r----- 1 glance glance 13287936 Jun  8 15:22 10a43894-96c7-46b1-b5b9-1af7c7fdc258
-rw-r----- 1 glance glance 13287936 Jun  8 15:19 c370939a-58f1-4b4f-a52f-8fff010b0b16
drwx------ 2 root   root      16384 Jun  8 15:11 lost+found
root@controller:/var/lib/glance/lvm-images# 
```
- `glance image-list`
```sh
root@controller:/var/lib/glance/lvm-images# glance image-list
+--------------------------------------+--------+
| ID                                   | Name   |
+--------------------------------------+--------+
| 36bafa1e-082a-42d7-bfa7-4d6535f00754 | cirros |
| c370939a-58f1-4b4f-a52f-8fff010b0b16 | cirros |
| 10a43894-96c7-46b1-b5b9-1af7c7fdc258 | cirros |
+--------------------------------------+--------+
root@controller:/var/lib/glance/lvm-images# 
```

<a name="image_cache"></a>
##9. Glance image cache.

Glance API server có thể cấu hình tùy chọn local image cache. Local image cache là một bản sao của file image, cho phép nhiều API server để phục vụ cùng một file image giống nhau, dẫn đến sự gia tăng khả năng mở rộng do sự gia tăng số lượng thiết bị đầu cuối phục vụ một image file.

Người dùng cuối không hề biết là Glance API lấy file từ local cache hay từ backend storage system.


###9.1 Configuration options for the Image Cache
Cấu hình glance cache ở 2 file: Một cho cấu hình máy chủ và một cho các tiện ích. `glance-api.conf` cho server và `glance-cache.conf` cho tiện ích.

Những cấu hình dưới đây phải cấu hình giống nhau trên cả 2 file

- **image_cache_dir:** Thư mục lưu trữ dữ liệu cache.
- **image_cache_sqlite_db:**  Đường dẫn sqlite database được sử dụng để quản lý cache. Đây là đường dẫn tương đối từ `image_cache_dir` (Mặc định là cache.db).
- **image_cache_driver:** Driver sử dụng cho quản lý cache (Mặc định là sqlite).
- **image_cache_max_size: ** Kích thước tối đa của cache. `glance-cache-pruner` sẽ xóa bỏ những images cũ nhất cho đến dưới giá trị này. (Default:10 GB)
- **image_cache_stall_time:** Khoảng thời gian một file image chưa hoàn thiện nằm trong bộ nhớ cache. Sau đó, fileimage chưa hoàn thiện này sẽ bị xóa. (Default:1 day)

###9.2 Cấu hình file `glance-cache.conf`

- **admin_user:** The username for an admin account, this is so it can get the image data into the cache.
- **admin_password:** The password to the admin account.
- **admin_tenant_name:** The tenant of the admin account.
- **auth_url:** The URL used to authenticate to keystone. This will be taken from the environment varibles if it exists.
- **filesystem_store_datadir:** This is used if using the filesystem store, points to where the data is kept.
- **filesystem_store_datadirs:** This is used to point to multiple filesystem stores.
- **registry_host:** The URL to the Glance registry.

###9.3 Các câu lệnh mở rộng
- Controlling the Growth of the Image Cache: 
Sử dụng lệnh `glance-cache-pruner` để xóa các file image cache sao cho bộ nhớ cache không vượt quá giới hạn tối đa, trong tùy chọn `image_cache_max_size`.

- Cleaning the Image Cache: 
Theo thời gian, image cache có thể lưu trữ các file image bị stalled hoặc invaild. Stalled image là kết quả của việc image cache ghi thất bại. Invaild image là kết quả của việc file image không được viết đúng vào đĩa.

- Prefetching Images into the Image Cache: 
When spinning up a new API server, administrators may wish to prefetch these image files into the local image cache to ensure that reads of those popular image files come from a local cache.

To queue an image for prefetching, you can use one of the following methods:
```sh
$> glance-cache-manage --host=<HOST> queue-image <IMAGE_ID>
```

- Finding Which Images are in the Image Cache
```sh
$> glance-cache-manage --host=<HOST> list-cached
```

hoặc
```sh
ls -lhR $IMAGE_CACHE_DIR
```

- Manually Removing Images from the Image Cache
```sh
$> glance-cache-manage --host=<HOST> delete-cached-image <IMAGE_ID>
```


<a name="tailieuthamkhao"></a>
##10. Tài liệu tham khảo

[http://docs.openstack.org/developer/glance/cache.html](http://docs.openstack.org/developer/glance/cache.html)

[http://docs.openstack.org/mitaka/config-reference/image-service.html](http://docs.openstack.org/mitaka/config-reference/image-service.html)

[http://www.sparkmycloud.com/blog/openstack-glance/](http://www.sparkmycloud.com/blog/openstack-glance/)

[http://docs.openstack.org/developer/glance/formats.html](http://docs.openstack.org/developer/glance/formats.html)

[http://egonzalez.org/multiple-store-locations-for-glance-images/](http://egonzalez.org/multiple-store-locations-for-glance-images/)



