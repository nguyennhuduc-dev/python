"""Bài 2: Các thao tác xử lý chuỗi."""


def dem_chu_hoa(s: str) -> int:
    """Đếm số ký tự chữ hoa trong chuỗi."""
    return sum(1 for ky_tu in s if ky_tu.isupper())


def kiem_tra_doi_xung(s: str) -> bool:
    """Kiểm tra chuỗi đối xứng, không phân biệt hoa/thường và dấu cách.

    Các ký tự không phải chữ hoặc số được bỏ qua.
    """
    chuoi_chuan_hoa = "".join(
        ky_tu.casefold() for ky_tu in s if ky_tu.isalnum()
    )
    return chuoi_chuan_hoa == chuoi_chuan_hoa[::-1]


def tinh_tong_chu_so(s: str) -> int:
    """Tính tổng các chữ số thập phân xuất hiện trong chuỗi."""
    return sum(int(ky_tu) for ky_tu in s if ky_tu.isdecimal())


def main() -> None:
    """Nhập chuỗi và hiển thị kết quả xử lý."""
    s = input("Nhập chuỗi s: ")

    so_chu_hoa = dem_chu_hoa(s)
    print(f"Số ký tự chữ hoa: {so_chu_hoa}")

    ket_qua = "đối xứng" if kiem_tra_doi_xung(s) else "không đối xứng"
    print(f"Chuỗi {ket_qua}.")
    print(f"Tổng các chữ số trong chuỗi: {tinh_tong_chu_so(s)}")


if __name__ == "__main__":
    main()
