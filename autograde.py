"""Autograder đơn giản cho repository Python Fundamentals.

Chạy từ thư mục gốc:
    python autograde.py

Có thể chỉ định thư mục và mẫu tên file test:
    python autograde.py --start-dir tests --pattern "test*.py"
"""

from __future__ import annotations

import argparse
import sys
import unittest
from pathlib import Path


class GradeResult(unittest.TextTestResult):
    """Lưu kết quả kiểm thử và hiển thị điểm tổng kết."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_tests = 0

    def startTest(self, test):
        self.total_tests += 1
        super().startTest(test)

    def print_summary(self) -> None:
        passed = self.total_tests - len(self.failures) - len(self.errors) - len(self.skipped)
        failed = len(self.failures)
        errors = len(self.errors)
        skipped = len(self.skipped)
        score = (passed / self.total_tests * 100) if self.total_tests else 0.0

        print("\n" + "=" * 58)
        print("                 KET QUA AUTOGRADER")
        print("=" * 58)
        print(f"Tổng số bài kiểm tra : {self.total_tests}")
        print(f"Đạt                  : {passed}")
        print(f"Thất bại             : {failed}")
        print(f"Lỗi                  : {errors}")
        print(f"Bỏ qua               : {skipped}")
        print(f"Điểm                 : {score:.2f}/100")
        print("=" * 58)

        if failed == 0 and errors == 0:
            print("KẾT LUẬN: TẤT CẢ TEST ĐỀU ĐẠT!")
        else:
            print("KẾT LUẬN: CẦN KIỂM TRA LẠI CÁC TEST THẤT BẠI.")


class GradeRunner(unittest.TextTestRunner):
    """Test runner sử dụng GradeResult."""

    resultclass = GradeResult

    def run(self, test):
        result = super().run(test)
        result.print_summary()
        return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Chạy Unit Test và chấm điểm repository Python."
    )
    parser.add_argument(
        "--start-dir",
        default="tests",
        help="Thư mục chứa các file kiểm thử (mặc định: tests).",
    )
    parser.add_argument(
        "--pattern",
        default="test*.py",
        help="Mẫu tên file kiểm thử (mặc định: test*.py).",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Ẩn chi tiết từng test, chỉ hiển thị tổng kết.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent
    start_dir = (root / args.start_dir).resolve()

    if not start_dir.is_dir():
        print(f"Không tìm thấy thư mục kiểm thử: {start_dir}", file=sys.stderr)
        return 2

    print("PYTHON FUNDAMENTALS - AUTOGRADER")
    print(f"Thư mục kiểm thử: {start_dir}")
    print(f"Mẫu file: {args.pattern}")
    print("-" * 58)

    loader = unittest.TestLoader()
    suite = loader.discover(
        start_dir=str(start_dir),
        pattern=args.pattern,
        top_level_dir=str(root),
    )

    if loader.errors:
        print("Không thể tải một hoặc nhiều file kiểm thử:")
        for error in loader.errors:
            print(error)
        return 2

    verbosity = 0 if args.quiet else 2
    runner = GradeRunner(stream=sys.stdout, verbosity=verbosity)
    result = runner.run(suite)

    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
