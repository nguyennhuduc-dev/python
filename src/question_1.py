"""Bài 1: Kiểm tra miền giá trị, đếm chữ số lẻ và tính tổng phân số."""


def kiem_tra_mien_gia_tri(n: int) -> bool:
    """Trả về True nếu n thuộc đoạn [1, 1500]."""
    return 1 <= n <= 1500


def dem_le(n: int) -> int:
    """Đếm số chữ số lẻ trong trị tuyệt đối của n."""
    n = abs(n)
    dem = 0

    while n > 0:
        chu_so = n % 10
        if chu_so % 2 != 0:
            dem += 1
        n //= 10

    return dem


def tinh_tong(n: int) -> float:
    """Tính S = 1/2 + 1/4 + ... + 1/(2n).

    Raises:
        ValueError: Nếu n âm.
    """
    if n < 0:
        raise ValueError("n phải lớn hơn hoặc bằng 0.")

    return sum(1 / (2 * i) for i in range(1, n + 1))


def main() -> None:
    """Chạy chương trình nhập liệu và hiển thị kết quả."""
    while True:
        try:
            n = int(input("Nhập n (1 <= n <= 1500): "))
            if kiem_tra_mien_gia_tri(n):
                break
            print("Giá trị n phải nằm trong đoạn [1, 1500].")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    print(f"Số chữ số lẻ của {n}: {dem_le(n)}")
    print(f"Giá trị S({n}): {tinh_tong(n):.4f}")


if __name__ == "__main__":
    main()
