from datetime import datetime
from typing import Dict, List

LibraryDict = Dict[str, List[str]]

def nhap_kho_sach() -> LibraryDict:
    tudien: LibraryDict = {}
    nam_hien_tai = datetime.now().year
    while True:
        try:
            n = int(input("Nhập số lượng sách cần thêm (n > 0): "))
            if n > 0:
                break
            print("Số lượng sách phải lớn hơn 0!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    for i in range(n):
        print(f"\n--- Nhập thông tin cuốn sách thứ {i+1} ---")
        ma_so = input("Mã số sách: ").strip()
        ten_sach = input("Tên sách: ").strip()
        tac_gia = input("Tên tác giả: ").strip()
        nha_xb = input("Nhà xuất bản: ").strip()
        while True:
            try:
                nam_xb = int(input("Năm xuất bản: "))
                if nam_xb <= nam_hien_tai:
                    break
                print(f"Năm xuất bản không hợp lệ (phải <= {nam_hien_tai})!")
            except ValueError:
                print("Vui lòng nhập năm bằng số nguyên!")
        tudien[ma_so] = [ten_sach, tac_gia, nha_xb, str(nam_xb)]
    return tudien

def xoa_sach(tudien: LibraryDict, ma_so: str) -> None:
    if ma_so in tudien:
        del tudien[ma_so]
        print(f"Cuốn sách có mã số '{ma_so}' đã được xóa thành công.")
    else:
        print("Không tìm thấy cuốn sách cần xóa.")

def main() -> None:
    kho_sach = nhap_kho_sach()
    print(f"\nToàn bộ kho sách hiện tại:\n{kho_sach}")
   
    ma_can_xoa = input("\nNhập mã số sách cần xóa: ").strip()
    xoa_sach(kho_sach, ma_can_xoa)
    print(f"Kho sách sau khi cập nhật:\n{kho_sach}")

if __name__ == "__main__":
    main()
