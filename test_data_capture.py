import unittest
from random import randint

from data_capture import DataCapture


class TestDataCapture(unittest.TestCase):
    def setUp(self) -> None:
        self.capture = DataCapture()
        self.capture.add(3)
        self.capture.add(9)
        self.capture.add(3)
        self.capture.add(4)
        self.capture.add(6)
        return super().setUp()

    def test_add(self):
        capture = DataCapture()
        capture.add(3)
        self.assertIn(3, capture.items)

    def test_add_raise_value_error_non_ints(self):
        capture = DataCapture()
        with self.assertRaises(ValueError):
            capture.add("a")

    def test_add_raise_error_for_negatives(self):
        capture = DataCapture()
        with self.assertRaises(ValueError):
            capture.add(-4)

    def test_add_multiple_items(self):
        capture = DataCapture()
        for _ in range(20):
            capture.add(randint(0, 1000))
        self.assertEqual(20, len(capture.items))

    def test_stats_less(self):
        stats = self.capture.build_stats()
        self.assertEqual(2, stats.less(4))

    def test_stats_between(self):
        stats = self.capture.build_stats()
        self.assertEqual(4, stats.between(3, 6))

    def test_stats_greater(self):
        stats = self.capture.build_stats()
        self.assertEqual(2, stats.greater(4))


if __name__ == "__main_":
    unittest.main()
