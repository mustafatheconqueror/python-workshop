import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_add_with_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_add_with_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)
    
    def test_add_with_positive_and_negative_numbers(self):
        self.assertEqual(add(1, -2), -1)
    
    def test_add_with_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_with_float(self):
        self.assertEqual(add(1.5, 2.5), 4.0)

if __name__ == "__main__":
    unittest.main()