"""Bài 4: Quản lý kho sách bằng Dictionary."""

from datetime import datetime
from typing import TypeAlias

ThongTinSach: TypeAlias = dict[str, str | int]
KhoSach: TypeAlias = dict[str, ThongTinSach]


def them_sach(
    kho_sach: KhoSach,
    ma_so: str,
    ten_sach: str,
    tac_gia: str,
    nha_xuat_ban: str,
    nam_xuat_ban: int,
) -> None:
    """Thêm sách sau khi kiểm tra dữ liệu.

    Raises:
        ValueError: Nếu mã trùng, trường văn bản rỗng hoặc năm không hợp lệ.
    """
    ma_so = ma_so.strip()
    ten_sach = ten_sach.strip()
    tac_gia = tac_gia.strip()
    nha_xuat_ban = nha_xuat_ban.strip()

    if not all((ma_so, ten_sach, tac_gia, nha_xuat_ban)):
        raise ValueError("Mã sách và các thông tin không được để trống.")
    if ma_so in kho_sach:
        raise ValueError(f"Mã sách '{ma_so}' đã tồn tại.")
    if not 1 <= nam_xuat_ban <= datetime.now().year:
        raise ValueError("Năm xuất bản không hợp lệ.")

    kho_sach[ma_so] = {
        "ten_sach": ten_sach,
        "tac_gia": tac_gia,
        "nha_xuat_ban": nha_xuat_ban,
        "nam_xuat_ban": nam_xuat_ban,
    }


def xoa_sach(kho_sach: KhoSach, ma_so: str) -> bool:
    """Xóa sách theo mã; trả về False nếu không tìm thấy."""
    return kho_sach.pop(ma_so.strip(), None) is not None


def tim_sach(kho_sach: KhoSach, tu_khoa: str) -> KhoSach:
    """Tìm sách theo mã hoặc tên sách, không phân biệt hoa/thường.

    Từ khóa rỗng trả về dictionary rỗng để tránh khớp toàn bộ kho sách.
    """
    tu_khoa = tu_khoa.strip().casefold()
    if not tu_khoa:
        return {}

    return {
        ma_so: thong_tin.copy()
        for ma_so, thong_tin in kho_sach.items()
        if tu_khoa in ma_so.casefold()
        or tu_khoa in str(thong_tin["ten_sach"]).casefold()
    }


def nhap_kho_sach() -> KhoSach:
    """Nhập danh sách sách từ bàn phím."""
    kho_sach: KhoSach = {}

    while True:
        try:
            so_luong = int(input("Nhập số lượng sách cần thêm: "))
            if so_luong > 0:
                break
            print("Số lượng phải lớn hơn 0.")
        except ValueError:
            print("Vui lòng nhập số nguyên.")

    for vi_tri in range(1, so_luong + 1):
        print(f"\n--- Cuốn sách thứ {vi_tri} ---")
        while True:
            try:
                ma_so = input("Mã sách: ")
                ten_sach = input("Tên sách: ")
                tac_gia = input("Tác giả: ")
                nha_xuat_ban = input("Nhà xuất bản: ")
                nam_xuat_ban = int(input("Năm xuất bản: "))
                them_sach(
                    kho_sach,
                    ma_so,
                    ten_sach,
                    tac_gia,
                    nha_xuat_ban,
                    nam_xuat_ban,
                )
                break
            except ValueError as loi:
                print(f"Dữ liệu chưa hợp lệ: {loi}")
                print("Vui lòng nhập lại cuốn sách này.")

    return kho_sach


def main() -> None:
    """Chạy chương trình quản lý kho sách mẫu."""
    kho_sach = nhap_kho_sach()
    print("\n--- KHO SÁCH ---")
    for ma_so, thong_tin in kho_sach.items():
        print(f"{ma_so}: {thong_tin}")

    ma_can_xoa = input("\nNhập mã sách cần xóa: ").strip()
    if xoa_sach(kho_sach, ma_can_xoa):
        print("Đã xóa sách.")
    else:
        print("Không tìm thấy mã sách.")

    print(f"Kho sách sau cập nhật: {kho_sach}")


if __name__ == "__main__":
    main()
