def dem_chu_hoa(s: str) -> int:
    return sum(1 for char in s if char.isupper())

def kiem_tra_doi_xung(s: str) -> bool:
    return s == s[::-1]


def tinh_tong_chu_so(s: str) -> int:
    return sum(int(char) for char in s if char.isdigit())

def main() -> None:
    s = input("Nhập chuỗi s từ bàn phím: ")
    so_chu_hoa = dem_chu_hoa(s)
    if so_chu_hoa == 0:
        print("Chuỗi không có ký tự chữ hoa.")
    else:
        print(f"Số ký tự chữ hoa: {so_chu_hoa}")
    
    if kiem_tra_doi_xung(s):
        print("Chuỗi đối xứng.")
    else:
        print("Chuỗi không đối xứng.")

    print(f"Tổng các chữ số trong chuỗi: {tinh_tong_chu_so(s)}")

if __name__ == "__main__":
    main()
