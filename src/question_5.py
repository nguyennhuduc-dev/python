class DienThoai:
    
    def __init__(self, ma_may: str, ten_may: str, hang_sx: str, dung_luong_pin: int, gia_ban: int) -> None:
        self.MaMay = ma_may
        self.TenMay = ten_may
        self.HangSanXuat = hang_sx
        self.DungLuongPin = dung_luong_pin
        self.GiaBan = gia_ban

    def thongtindienthoai(self) -> None:
        print(f"   Mã máy       : {self.MaMay}")
        print(f"   Tên máy      : {self.TenMay}")
        print(f"   Hãng sản xuất: {self.HangSanXuat}")
        print(f"   Dung lượng pin: {self.DungLuongPin} mAh")
        print(f"   Giá bán      : {self.GiaBan:,} VND")
        print("-" * 40)


def main() -> None:
    dt01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    dt02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)
    print("--- THÔNG TIN CHI TIẾT THIẾT BỊ ---")
    dt01.thongtindienthoai()
    dt02.thongtindienthoai()

if __name__ == "__main__":
    main()
