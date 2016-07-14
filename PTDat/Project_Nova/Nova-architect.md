#NOVA system architect.

![scr1.jpg](http://www.upsieutoc.com/images/2016/07/07/scr1.jpg)

- Nova bao hàm nhiều tiến trình của hệ thống, mỗi performing thực hiện các chức năng khác nhau. Giao diện người dùng là một REST API, trong khi đó các thành phần bên trong của Nova giao tiếp với nhau thông qua một cơ chế là RPC. 
- Các máy chủ API yêu cầu tiến trình REST. Đó là những gì thường liên quan đến database reads/writes, lựa chọn gửi RPC massage từ các Nova service khác , và tự tạo ra phản hồi từ REST. RPC massage được thực hiện thông qua `oslo.messaging` library, một abstrction trên đầu của massage queues. Hầu hết các thành phần chính của Nova có thể chạy trên nhiều máy chủ , và có một thành phần quản lý để lắng nghe từ RPC massages. Có một thành phần chính dó là nova-compute, ở đó là nơi duy nhất chạy trên hypervisor. Manager cũng các tùy chọn, có các nhiệm vụ định kỳ. 

#Component.

- Mô hình bên dưới cho chúng ta thấy được những thành phần chính khi triển khai một Nova điển hình.

![scr1.jpg](http://www.upsieutoc.com/images/2016/07/07/scr1.jpg)

- DB: sql database để lưu trữ dữ liệu.
- API: Thành phần để nhận HTTP request , chuyển đổi các lệnh và các giao tiếp thành các thành phần khác thông qua oslo.messaging queuses hoặc HTTP.
- Scheduler: Quyết định ,máy chủ được chọn trong mỗi trường hợp.
- Network: quản lý ip forwording, bridges, và vlan.
- Compute: Quản lý giao tiếp 
- với hypervisor và vitual machines.
- Conductor: Xử lý các yêu cầu mà cần sự phối hợ (build/resize), hoạt đọng như một proxy cơ sở dữ liệu, hoặc đối tượng chuyển đổi.