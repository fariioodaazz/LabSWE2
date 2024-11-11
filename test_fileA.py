import unittest
from fileA import MathOperations

class TestSqrRootFunction(unittest.TestCase):
    def setUp(self):
        self.math_ops = MathOperations()

    def test_positive_number(self):
        self.assertEqual(self.math_ops.sqr_root(4), 2.0)

    def test_zero(self):
        self.assertEqual(self.math_ops.sqr_root(0), 0.0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            self.math_ops.sqr_root(-1)

if __name__ == '__main__':
    unittest.main()
