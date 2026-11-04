"""Unit Test cho các bài tập trong thư mục src."""

import unittest
from datetime import datetime
from unittest.mock import patch

from src.question_1 import dem_le, kiem_tra_mien_gia_tri, tinh_tong
from src.question_2 import dem_chu_hoa, kiem_tra_doi_xung, tinh_tong_chu_so
from src.question_3 import dem_phan_tu_k, nhap_danh_sach, tinh_tong_duong_chan
from src.question_4 import KhoSach, them_sach, tim_sach, xoa_sach
from src.question_5 import DienThoai


class TestQuestion1(unittest.TestCase):
    def test_kiem_tra_mien_gia_tri(self) -> None:
        self.assertTrue(kiem_tra_mien_gia_tri(1))
        self.assertTrue(kiem_tra_mien_gia_tri(1500))
        self.assertFalse(kiem_tra_mien_gia_tri(0))
        self.assertFalse(kiem_tra_mien_gia_tri(1501))

    def test_dem_chu_so_le(self) -> None:
        self.assertEqual(dem_le(123456), 3)
        self.assertEqual(dem_le(0), 0)
        self.assertEqual(dem_le(-135), 3)

    def test_tinh_tong(self) -> None:
        self.assertEqual(tinh_tong(0), 0)
        self.assertAlmostEqual(tinh_tong(3), 0.9166666667)

    def test_tinh_tong_n_am(self) -> None:
        with self.assertRaises(ValueError):
            tinh_tong(-1)


class TestQuestion2(unittest.TestCase):
    def test_dem_chu_hoa(self) -> None:
        self.assertEqual(dem_chu_hoa("PyThOn"), 3)
        self.assertEqual(dem_chu_hoa("python"), 0)

    def test_kiem_tra_doi_xung(self) -> None:
        self.assertTrue(kiem_tra_doi_xung("Madam"))
        self.assertTrue(kiem_tra_doi_xung("A man, a plan, a canal: Panama"))
        self.assertFalse(kiem_tra_doi_xung("Python"))

    def test_tinh_tong_chu_so(self) -> None:
        self.assertEqual(tinh_tong_chu_so("a1b2c3"), 6)
        self.assertEqual(tinh_tong_chu_so("khong co so"), 0)


class TestQuestion3(unittest.TestCase):
    def test_nhap_danh_sach_khong_luu_so_0(self) -> None:
        with patch("builtins.input", side_effect=["2", "0"]):
            self.assertEqual(nhap_danh_sach(), [2])

    def test_tinh_tong_duong_chan(self) -> None:
        self.assertEqual(tinh_tong_duong_chan([-4, -2, 1, 2, 4, 5]), 6)
        self.assertEqual(tinh_tong_duong_chan([]), 0)

    def test_dem_phan_tu_k(self) -> None:
        self.assertEqual(dem_phan_tu_k([1, 2, 2, 3], 2), 2)
        self.assertEqual(dem_phan_tu_k([1, 2, 3], 9), 0)


class TestQuestion4(unittest.TestCase):
    def setUp(self) -> None:
        self.kho_sach: KhoSach = {}

    def them_sach_mau(self) -> None:
        them_sach(
            self.kho_sach,
            "S001",
            "Python Co Ban",
            "Nguyen Van A",
            "NXB Tre",
            2024,
        )

    def test_them_va_tim_sach(self) -> None:
        self.them_sach_mau()
        ket_qua = tim_sach(self.kho_sach, "python")
        self.assertIn("S001", ket_qua)
        self.assertEqual(ket_qua["S001"]["nam_xuat_ban"], 2024)

    def test_tu_khoa_rong_khong_tra_ve_toan_bo(self) -> None:
        self.them_sach_mau()
        self.assertEqual(tim_sach(self.kho_sach, ""), {})

    def test_khong_cho_phep_ma_trung(self) -> None:
        self.them_sach_mau()
        with self.assertRaises(ValueError):
            self.them_sach_mau()

    def test_khong_cho_phep_thong_tin_rong(self) -> None:
        with self.assertRaises(ValueError):
            them_sach(self.kho_sach, "S002", "", "Tac gia", "NXB", 2024)

    def test_nam_xuat_ban_tuong_lai(self) -> None:
        with self.assertRaises(ValueError):
            them_sach(
                self.kho_sach,
                "S003",
                "Sach",
                "Tac gia",
                "NXB",
                datetime.now().year + 1,
            )

    def test_xoa_sach(self) -> None:
        self.them_sach_mau()
        self.assertTrue(xoa_sach(self.kho_sach, "S001"))
        self.assertFalse(xoa_sach(self.kho_sach, "S001"))


class TestQuestion5(unittest.TestCase):
    def tao_dien_thoai(self) -> DienThoai:
        return DienThoai("DT01", "Phone A", "Brand A", 5000, 10_000_000)

    def test_khoi_tao_va_hien_thi(self) -> None:
        dien_thoai = self.tao_dien_thoai()
        self.assertIn("Phone A", dien_thoai.thong_tin_dien_thoai())
        self.assertIn("10,000,000", str(dien_thoai))

    def test_cap_nhat_gia(self) -> None:
        dien_thoai = self.tao_dien_thoai()
        dien_thoai.cap_nhat_gia(12_000_000)
        self.assertEqual(dien_thoai.gia_ban, 12_000_000)

    def test_tu_choi_gia_khong_hop_le(self) -> None:
        with self.assertRaises(ValueError):
            self.tao_dien_thoai().cap_nhat_gia(0)

    def test_tu_choi_pin_khong_hop_le(self) -> None:
        with self.assertRaises(ValueError):
            DienThoai("DT02", "Phone B", "Brand B", 0, 1000)


if __name__ == "__main__":
    unittest.main()
