# Nội dung: Lập trình thử nghiệm công cụ phát hiên đường nét ảnh.
    - Input: Một ảnh chụp (ảnh màu RGB, ảnh đa mức xám,...)
    - Ouput: Một ảnh đường nét đã hiệu chỉnh.

# Cơ sở lý thuyết
* Lý thuyết đã tìm hiểu:
- Cấu trúc dữ liệu ảnh số: ma trận các pixels
    + Đối với ảnh màu: 3 giá trị r,g,b
    + Đối với ảnh xám: 1 giá trị duy nhất

- Convert ảnh màu sang ảnh xám: Red * 0.1140 + Green * 0.5870 + Blue * 0.2989

- Bộ lọc đạo hàm: 
    + Với ảnh số không thể tính đạo hàm, nên sử dụng phép tính chập (convolution) để tính gần đúng đạo hàm của ảnh
    + Tìm hiểu về phép tính tích chập với ảnh: là phép tính giữa 1 ma trận ảnh (I) với 1 kernel, kết hợp padding vs stride

- Thuật toán Canny tìm cạnh:
    + Giảm nhiễu bằng bộ lọc Gaussian
    + Tính gradient của ảnh (magnitude và direction), sử dụng bộ lọc Sobel:
              [[-1, 0, 1],
        Gx =   [-2, 0, 2]   * I
               [-1, 0, 1]]
        
              [[-1, -2, -1],
        Gy =   [0,  0,  0]   * I
               [1,  2,  1]]
        
    + Triệt tiêu phi tối đa:
        Bỏ đi những pixel không được coi là 1 phần của edge, hay là chỉ giữ lại cạnh.

    + Ngưỡng độ trễ (Hysteresis Thresholding):
        Quy định trước 2 giá trị ngưỡng (threshold) t1 và t2 (t1 < t2)
        Một cạnh bất kì có cường độ gradient lớn hơn t2 thì chắc chắn là các cạnh
        và những cạnh có cường độ gradient nhỏ hơn t1 sẽ không được coi là cạnh. 
        Nếu một cạnh mà có những điểm ảnh nằm trong ngưỡng này thì có thể được xem xét thuộc cùng một cạnh hoặc không thuộc dựa trên sự kết nối của các điểm với nhau.

- Tìm hiểu về kivy và .kv file để xây GUI

* Triển khai thực hiện:
- Đã triển khai thành công thuật toán Canny sử dụng thư viện OpenCV.

- Xây dựng tạm thời 1 giao diện đơn giản bằng Kivy, với các tính năng load và xử lí ảnh, đang hoàn thiện chức năng lưu ảnh.