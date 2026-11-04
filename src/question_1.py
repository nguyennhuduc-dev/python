# B.

def dem_le(n: int) -> int:
    dem = 0
    while n > 0:
        tam = n % 10
        if tam % 2 != 0:
            dem += 1
        n //= 10
    return dem

# C.

def tinh_tong(n: int) -> float:
    return sum(1 / (2 * i) for i in range(1, n + 1))

def main() -> None:
    while True:
        try:
            n = int(input("Nhập giá trị n (1 <= n <= 1500): "))
            if 1 <= n <= 1500:
                break 
            print("Giá trị ngoài đoạn [1; 1500]. Vui lòng nhập lại!")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
    print(f"Số lượng chữ số lẻ của {n} là: {dem_le(n)}")
    print(f"Giá trị của chuỗi S({n}) là: {tinh_tong(n):.4f}")

if __name__ == "__main__":
    main()