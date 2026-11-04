"""Bài 5: Xây dựng lớp DienThoai theo hướng đối tượng."""


class DienThoai:
    """Đại diện cho một chiếc điện thoại."""

    def __init__(
        self,
        ma_may: str,
        ten_may: str,
        hang_sx: str,
        dung_luong_pin: int,
        gia_ban: int,
    ) -> None:
        if not all(
            isinstance(gia_tri, str) and gia_tri.strip()
            for gia_tri in (ma_may, ten_may, hang_sx)
        ):
            raise ValueError("Mã máy, tên máy và hãng sản xuất không được trống.")
        if dung_luong_pin <= 0:
            raise ValueError("Dung lượng pin phải lớn hơn 0.")
        if gia_ban <= 0:
            raise ValueError("Giá bán phải lớn hơn 0.")

        self.ma_may = ma_may.strip()
        self.ten_may = ten_may.strip()
        self.hang_san_xuat = hang_sx.strip()
        self.dung_luong_pin = dung_luong_pin
        self.gia_ban = gia_ban

    def cap_nhat_gia(self, gia_moi: int) -> None:
        """Cập nhật giá bán nếu giá mới hợp lệ."""
        if gia_moi <= 0:
            raise ValueError("Giá bán phải lớn hơn 0.")
        self.gia_ban = gia_moi

    def thong_tin_dien_thoai(self) -> str:
        """Trả về thông tin điện thoại dưới dạng chuỗi."""
        return (
            f"Mã máy: {self.ma_may}\n"
            f"Tên máy: {self.ten_may}\n"
            f"Hãng sản xuất: {self.hang_san_xuat}\n"
            f"Dung lượng pin: {self.dung_luong_pin:,} mAh\n"
            f"Giá bán: {self.gia_ban:,} VND"
        )

    def __str__(self) -> str:
        return self.thong_tin_dien_thoai()


def main() -> None:
    """Tạo và hiển thị hai đối tượng điện thoại mẫu."""
    dien_thoai_1 = DienThoai(
        "DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000
    )
    dien_thoai_2 = DienThoai(
        "DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29_990_000
    )

    print("--- THÔNG TIN ĐIỆN THOẠI ---")
    print(dien_thoai_1)
    print("-" * 40)
    print(dien_thoai_2)


if __name__ == "__main__":
    main()
