from typing import List

def nhap_danh_sach() -> List[int]:
    danh_sach = []
    while True:
        try:
            x = int(input("Nhập phần tử số nguyên (Nhập 0 để ngưng): "))
            danh_sach.append(x)
            if x == 0:
                break
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")
    return danh_sach

def tinh_tong_duong_chan(ds: List[int]) -> int:
    return sum(i for i in ds if i > 0 and i % 2 == 0)

def dem_phan_tu_k(ds: List[int], k: int) -> int:
    return ds.count(k)


def main() -> None:
    danh_sach = nhap_danh_sach()
    print(f"Danh sách vừa nhập: {danh_sach}")
   
    tong = tinh_tong_duong_chan(danh_sach)
    if tong > 0:
        print(f"Tổng các số dương chẵn trong danh sách: {tong}")
    else:
        print("Không có số dương chẵn trong danh sách.")
    try:
        k = int(input("Nhập phần tử k cần đếm: "))
        solan = dem_phan_tu_k(danh_sach, k)
        if solan == 0:
            print(f"Không có phần tử {k} trong danh sách.")
        else:
            print(f"Số lần xuất hiện của {k} là: {solan} lần")
    except ValueError:
        print("Giá trị k phải là số nguyên!")

if __name__ == "__main__":
    main()
