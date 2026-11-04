# 🐍 Python Fundamentals

**Kho lưu trữ bài tập, kiến thức và thực hành Python từ cơ bản đến nâng cao.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-unittest-2ea44f)](https://docs.python.org/3/library/unittest.html)

---

## 📌 Giới thiệu

Repository này lưu trữ quá trình học tập và thực hành Python. Nội dung bắt đầu từ các bài tập nền tảng, sau đó mở rộng sang tư duy giải quyết vấn đề, lập trình hướng đối tượng, kiểm thử và các dự án nhỏ.

**Mục tiêu:**
- Luyện tư duy thuật toán và kỹ năng phân tích bài toán.
- Viết Python rõ ràng, dễ đọc và dễ bảo trì.
- Thực hành chia chương trình thành hàm và module.
- Làm quen với Type Hints, Docstrings và Unit Test.
- Xây dựng nền tảng để học Backend, Data và AI/ML.

## 🗂️ Cấu trúc dự án

```text
python/
├── .github/
│   └── workflows/
│       └── tests.yml
├── docs/
│   └── learning-roadmap.md
├── src/
│   ├── __init__.py
│   ├── question_1.py
│   ├── question_2.py
│   ├── question_3.py
│   ├── question_4.py
│   └── question_5.py
├── tests/
│   ├── __init__.py
│   └── test_questions.py
├── .gitignore
└── README.md
```

## 📚 Danh sách bài tập

| File | Nội dung | Kiến thức |
|---|---|---|
| `question_1.py` | Kiểm tra miền giá trị, đếm chữ số lẻ, tính tổng phân số | Vòng lặp, điều kiện, hàm |
| `question_2.py` | Đếm chữ hoa, kiểm tra chuỗi đối xứng, tính tổng chữ số | String, slicing, comprehension |
| `question_3.py` | Nhập và xử lý danh sách số nguyên | List, vòng lặp, xử lý dữ liệu |
| `question_4.py` | Quản lý kho sách | Dictionary, kiểm tra dữ liệu |
| `question_5.py` | Xây dựng lớp điện thoại | Class, Object, Constructor, phương thức |

## ⚙️ Yêu cầu

- Python 3.10 trở lên.
- Git (nếu muốn clone repository).
- Không cần cài thư viện bên ngoài cho các bài tập và bộ kiểm thử hiện tại.

## 🚀 Cài đặt và chạy

### 1. Clone repository

```bash
git clone https://github.com/nguyennhuduc-dev/python.git
cd python
```

### 2. Chạy một bài tập

Windows PowerShell:

```powershell
python src/question_1.py
```

Thay `question_1.py` bằng file muốn chạy.

### 3. Chạy toàn bộ Unit Test

Đứng tại thư mục gốc repository:

```bash
python -m unittest discover -s tests -v
```

Bộ kiểm thử dùng `unittest` có sẵn trong Python nên không cần cài package. Cách chạy theo cơ chế test discovery được mô tả trong [tài liệu Python](https://docs.python.org/3/library/unittest.html#test-discovery).

## 🧪 Kiểm thử tự động

Mỗi lần có thay đổi được đẩy lên GitHub, GitHub Actions sẽ chạy Unit Test trên Python 3.10, 3.11 và 3.12.

Các bài kiểm thử tập trung vào:
- Kết quả đúng với dữ liệu thông thường.
- Dữ liệu biên và danh sách rỗng.
- Dữ liệu không hợp lệ.
- Mã sách trùng và thao tác xóa mã không tồn tại.
- Giá trị hợp lệ khi khởi tạo đối tượng OOP.

## 🧭 Lộ trình học tập

Xem [Learning Roadmap](docs/learning-roadmap.md) để theo dõi các chủ đề dự kiến: Python Fundamentals, Data Structures, OOP, Advanced Python, Testing và Mini Projects.

## 🧹 Quy ước viết code

- Tên hàm và biến dùng `snake_case`.
- Tên lớp dùng `PascalCase`.
- Hàm quan trọng có Docstring.
- Khai báo Type Hints khi giúp mã nguồn dễ hiểu hơn.
- Tách phần xử lý nghiệp vụ khỏi phần nhập/xuất khi phù hợp.
- Viết Unit Test cho các hàm có logic cần kiểm chứng.

Tham khảo [PEP 8](https://peps.python.org/pep-0008/) và [Python unittest](https://docs.python.org/3/library/unittest.html).

## 🛠️ Công nghệ

- **Language:** Python
- **Testing:** unittest
- **Automation:** GitHub Actions
- **Version Control:** Git & GitHub

## 📈 Định hướng phát triển

- [x] Chuẩn hóa 5 bài tập hiện tại.
- [x] Bổ sung kiểm tra dữ liệu và tài liệu hàm.
- [x] Tạo bộ Unit Test.
- [x] Thiết lập kiểm thử tự động.
- [x] Viết lộ trình học tập.
- [ ] Bổ sung bài tập về thuật toán và cấu trúc dữ liệu.
- [ ] Phát triển mini project có dữ liệu thực tế.
- [ ] Mở rộng nội dung OOP và Python nâng cao.

## 👨‍💻 Tác giả

**Nguyễn Như Đức**  
GitHub: [@nguyennhuduc-dev](https://github.com/nguyennhuduc-dev)

---

<div align="center">

*Learn consistently. Practice deliberately. Build something useful.*

</div>
