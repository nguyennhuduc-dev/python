"""Bài 3: Nhập và xử lý danh sách số nguyên."""


def nhap_danh_sach() -> list[int]:
    """Nhập số nguyên đến khi người dùng nhập 0.

    Giá trị 0 là ký hiệu kết thúc và không được thêm vào danh sách.
    """
    danh_sach: list[int] = []

    while True:
        try:
            gia_tri = int(input("Nhập số nguyên (0 để kết thúc): "))
            if gia_tri == 0:
                break
            danh_sach.append(gia_tri)
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    return danh_sach


def tinh_tong_duong_chan(ds: list[int]) -> int:
    """Tính tổng các phần tử dương và chẵn."""
    return sum(so for so in ds if so > 0 and so % 2 == 0)


def dem_phan_tu_k(ds: list[int], k: int) -> int:
    """Đếm số lần k xuất hiện trong danh sách."""
    return ds.count(k)


def main() -> None:
    """Chạy chương trình nhập và xử lý danh sách."""
    danh_sach = nhap_danh_sach()
    print(f"Danh sách vừa nhập: {danh_sach}")

    tong = tinh_tong_duong_chan(danh_sach)
    print(f"Tổng các số dương chẵn: {tong}")

    try:
        k = int(input("Nhập phần tử k cần đếm: "))
        so_lan = dem_phan_tu_k(danh_sach, k)
        print(f"Số lần xuất hiện của {k}: {so_lan}")
    except ValueError:
        print("k phải là một số nguyên hợp lệ.")


if __name__ == "__main__":
    main()
