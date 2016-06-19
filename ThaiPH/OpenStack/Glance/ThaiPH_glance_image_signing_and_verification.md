# Glance Image Signing and Verification
# Mục lục
<h3><a href="#problem">1. Đặt vấn đề</a></h3>
<h3><a href="#proposed">2. Đề xuất thay đổi</a></h3>
<ul>
<li><a href="#workflow">2.1. Tiến trình xác thực chữ ký của Glance</a></li>
<li><a href="#explain">2.2. Các tùy chọn thay thế</a></li>
</ul>
<h3><a href="#ref">3. Tham khảo</a></h3>
---

<h2><a name="problem">1. Đặt vấn đề</a></h2>
<div>
Trước bản phát hành Liberty, không hề có phương thức nào cho các user để xác nhận rằng image họ tải lên có bị thay đổi hay không. Một image bị thay đổi có thể xảy ra trong quá trình upload từ user lên Glance hoặc Glance chuyển image tới Nova, hoặc cũng có thể do chính Glance tự mình thay đổi mà không có tác động từ phía người dùng. Một image bị thay đổi có thể chứa mã độc. Bởi vậy việc cung cấp cơ chế chữ ký số cho image và xác nhận chữ ký cho phép user xác nhận xem image có bị thay đổi không trước khi boot image tạo máy ảo. 
<br>
Tính năng này hỗ trợ một số use cases như sau:
<ul>
<li>Người dùng cuối tải image lên Glance</li>
<li>Image được tạo bởi Nova và Nova sẽ ký lên image theo yêu cầu của người dùng cuối. Image này sẽ được tải từ Nova lên Glance.</li>
<li>Nova yêu cầu một image dã được ký tạo máy ảo và tải image về từ Glance, tiến hành chứng thực trước khi boot image.</li>
</ul>
</div>
<h2><a name="proposed">2. Đề xuất thay đổi</a></h2>
<ul>
<li><h3><a name="workflow">2.1. Tiến trình xác thực chữ ký của Glance</a></h3>
<img src="http://i.imgur.com/QAgKP0h.png"/>
<br><br>
Trên đây là workflow của tiến trình xác thực chữ ký của image áp dụng cho các usecases đã đề cập ở mục 1(từ bước 1 tới bước 10 là liên quan tới trường hợp người dùng upload image lên Glance, từ bước 11 trở đi là liên quan tới trường hợp Nova yêu cầu image từ Glance dể boot máy ảo):
<ul>
<li><b>Bước 1: </b>Tạo image</li>
<li><b>Bước 2: </b>Tạo cặp key theo thuật toán mã hóa khóa bất đối xứng</li>
<li><b>Bước 3: </b>Tạo certificate</li>
<li><b>Bước 4: </b>Ký lên image sử dụng Private Key. Chú ý bước này có sự khác biệt giữa Liberty và Mitaka:
<ul>
<li><b>Liberty: </b>Trước khi ký lên image, dữ liệu của image sẽ được băm sử dụng thuật toán MD5. Dữ liệu của image sẽ được chia thành từng phần nhỏ rồi băm. Cuối cùng ta sẽ thu lại được một mã băm <b>checksum_hash</b> của dữ liệu image. Tiếp đó mã này sẽ được sử dụng vào thuật toán băm thứ hai là SHA-256.</li>
<li><b>Mitaka: </b>Không sử dụng thuật toán MD5 để băm dữ liệu của image. Tuy nhiên dữ liệu của image sẽ bị băm một lần sử dụng thuật toán SHA-256.</li>
</ul>
Tiếp đó sử dụng Private Key đã tạo ở bước 2 để ký lên image đã bị băm.
</li>
<li><b>Bước 5: </b>Lưu trữ Public Key certificate lên Key Manager sử dụng giao diện Castellan, đồng thời thu lại giá trị <b>signature_certificate_uuid</b> sử dụng cho quá trình upload image và thu thập Public Key certificate.</li>
<li><b>Bước 6: </b>Upload Image lên Glance kèm theo các thuộc tính liên quan tới chữ ký số.(các Signature metadata). Các thuộc tính này bao gồm:
<ul>
<li><b>signature: </b>chính là chữ ký số ta thu được. Tùy thuộc phiên bản Liberty hay Mitaka mà chữ ký số này sẽ được tạo ra khác nhau(theo giải thích ở bước 4). Với Liberty: <b>signature = RSA-PSS(SHA-256(MD5(IMAGE-CONTENT)))</b>. Với Mitaka: <b>signature = RSA-PSS(SHA-256(IMAGE-CONTENT))</b></li>
<li><b>signature_key_type: </b>là loại key được sử dụng để tạo chữ ký số. Ví dụ: RSA-PSS</li>
<li><b>signature_hash_method: </b>là phương thức băm được sử dụng để tạo chữ kỹ. Ví dụ: SHA-256</li>
<li><b>signature_certificate_uuid: </b>chính là cert_uuid thu được ở bước 5 khi tiến hành lưu trữ certificate.</li>
<li><b>mask_gen_algorithm: </b>giá trị này chỉ ra thuật toán tạo mặt nạ được sử dụng trong quá trình tạo ra chữ ký số. Ví dụ: <b>MGF1</b>. Giá trị này chỉ sử dụng cho mô hình RSA-PSS.</li>
<li><b>pss_salt_length: </b>định nghĩa <b>sal length</b> sử dụng trong quá trình tạo chữ ký và chỉ áp dụng cho mô hình RSA-PSS. Giá trị mặc định là <b>PSS.MAX_LENGTH</b>.</li>
</ul>
</li>
<li><b>Bước 7: </b>Glance sẽ yêu cầu Public Key Certificate từ Key Manager. Để làm điều này Glance phải sử dụng <b>signature_certificate_uuid</b> thu được trong quá trình tải image lên của người dùng.</li>
<li><b>Bước 8: </b>Key Manager trả lại Public key Certificate</li>
<li><b>Bước 9: </b>Xác thực Signature của image sử dụng public key thu được cùng với các signature metadata khi image được upload lên. Việc xác thực này được thực hiện bởi module <b>signature_utils</b>.</li>
<li><b>Bước 10: </b>Lưu lại image nếu chứng thực thành công. Nếu chứng thực thất bại, Glance sẽ đưa image đó vào trạng thái <b>killed</b> và gửi thông báo lại cho người dùng kèm theo lý do tại sao image upload bị lỗi.</li>
<li><b>Bước 11 : </b>Nova gửi yêu cầu tới Glance lấy Image và metadata để boot máy ảo.</li>
<li><b>Bước 12 : </b>Glance gửi lại Nova image kèm theo metadata để chứng thực.</li>
<li><b>Bước 13: </b>Nova yêu cầu Public Key Certificate từ Key Manager bằng việc sử dụng cert_uuid tương tác với giao diện Castellan</li>
<li><b>Bước 14: </b>Key Manager trả về Public Key Certificate lại cho Nova</li>
<li><b>Bước 15: </b>Nova xác nhận chứng chỉ. Chức năng này được thực hiện nếu chỉnh sửa module signature_utils của nova để kết hợp việc xác nhận chứng chỉ (certificate validation) vào  workflow của tiến trình xác thực chữ ký(signature verification).</li>
<li><b>Bước 16: </b>Xác thực chữ ký của image. Để làm điều này, ta phải cấu hình trong file <b>nova.conf</b> của nova, thiết lập giá trị <b>verify_glance_signatures = true</b>. Như vậy, Nova sẽ sử dngj các thuộc tính của image, bao gồm các thuộc tính cần thiết cho quá trình xác thực chữ ký image(signature metadata). Nova sẽ đưa dữ liệu của image và các thuộc tính của nó tới module <b>signature_utils</b> để xác thực chữ ký.</li>
<li><b>Bước 11: </b>Nếu việc xác thực chữ ký thành công, nova sẽ tiến hành boot máy ảo sử dụng image đó và ghi vào log chỉ ra rằng việc xác thực chữ ký thành côn kèm theo các thông tin về signing certificate. Ngược lại nếu xác nhận thất bại, Nova sẽ không boot image đó và lưu lại lỗi vào log.</li>
</ul>

</li>
<li><h3><a name="explain">2.2. Các tùy chọn thay thế</a></h3></li>
</ul>
<h2><a name="ref">3. Tham khảo</a></h2>
<div>
[1] - <a href="https://specs.openstack.org/openstack/glance-specs/specs/mitaka/approved/image-signing-and-verification-support.html">https://specs.openstack.org/openstack/glance-specs/specs/mitaka/approved/image-signing-and-verification-support.html</a>
<br>
[2] - <a href="https://specs.openstack.org/openstack/nova-specs/specs/mitaka/implemented/image-verification.html">https://specs.openstack.org/openstack/nova-specs/specs/mitaka/implemented/image-verification.html</a>
</div>