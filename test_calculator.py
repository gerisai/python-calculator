import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(5,2),10)

if __name__ == '__main__':
    unittest.main()