\# Lời Giải Đề Thi Python Căn Bản



Kho lưu trữ mã nguồn lời giải các bài tập lập trình Python cơ bản (Mã đề thi: 11301). Mã nguồn đã được tái cấu trúc theo chuẩn viết code sạch (Clean Code), bổ sung Type Hints và Docstrings.



\## 📌 Danh sách các bài giải

\* \*\*Câu 1 (`question\_1.py`)\*\*: Kiểm tra miền giá trị, đếm chữ số lẻ, tính chuỗi phân số $S$.

\* \*\*Câu 2 (`question\_2.py`)\*\*: Phân tích chuỗi (đếm chữ hoa, kiểm tra đối xứng Palindrome, tổng chữ số).

\* \*\*Câu 3 (`question\_3.py`)\*\*: Thao tác dynamic mảng (List), lọc và tính tổng số dương chẵn, tìm tần suất phần tử.

\* \*\*Câu 4 (`question\_4.py`)\*\*: Quản lý thông tin sách bằng cấu trúc Dictionary.

\* \*\*Câu 5 (`question\_5.py`)\*\*: Lập trình hướng đối tượng (OOP) thiết kế Class `DienThoai`.



\## 🚀 Hướng dẫn chạy thử dự án

Chạy trực tiếp file script bằng lệnh:

&#x20; bash python src/question\_5.py 

\---



\### BƯỚC 3: Tạo Repository trên Website GitHub



1\. Truy cập vào trang web \[github.com](https://github.com) và đăng nhập tài khoản của bạn.

2\. Ở góc trên bên phải, bấm vào biểu tượng dấu \*\*`+`\*\* \\(\\rightarrow\\) Chọn \*\*New repository\*\*.

3\. Điền các thông tin sau:

\* \*\*Repository name\*\*: `python-fundamentals-exam`

\* \*\*Public/Private\*\*: Chọn \*\*Public\*\* để nhà tuyển dụng hoặc bạn bè có thể xem được.

\* \*\*LƯU Ý QUAN TRỌNG\*\*: \*\*KHÔNG\*\* tích chọn vào các ô \*Add a README file\*, \*Add .gitignore\*, hoặc \*Choose a license\* (vì chúng ta đã tạo thủ công dưới máy rồi).

4\. Bấm nút \*\*Create repository\*\* ở dưới cùng.

5\. Trang web sẽ chuyển hướng và hiển thị một đường link có đuôi `.git` (Ví dụ: `https://github.comten-cua-ban/python-fundamentals-exam.git`). \*\*Hãy copy lại đường link này\*\*.



\---



\### BƯỚC 4: Chạy các lệnh Git để tải dự án lên mạng



Quay lại cửa sổ \*\*PowerShell\*\* trên máy tính của bạn (đảm bảo bạn vẫn đang đứng ở thư mục `D:\\python-fundamentals-exam`), gõ tuần tự các lệnh sau:



```powershell

\# 1. Khởi tạo Git cho thư mục dự án

git init



\# 2. Thêm tất cả các file đã chuẩn bị vào hàng đợi

git add .



\# 3. Đóng gói mã nguồn kèm thông điệp ghi nhận lịch sử

git commit -m "feat: initial release with clean core solutions"



\# 4. Đổi tên nhánh mặc định thành 'main'

git branch -M main



\# 5. Liên kết thư mục dưới máy với kho lưu trữ trên GitHub (Thay link bạn vừa copy vào đây)

git remote add origin https://github.comten-cua-ban/python-fundamentals-exam.git



\# 6. Đẩy toàn bộ mã nguồn lên GitHub

git push -u origin main

