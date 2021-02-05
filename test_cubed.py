import unittest
from cubed_number import cubed_number

class TestCubed(unittest.TestCase):
    def test_cubed(self):
        self.assertAlmostEqual(cubed_number(-2),-8)
        self.assertAlmostEqual(cubed_number(1),1)
        self.assertAlmostEqual(cubed_number(0),0)
        self.assertAlmostEqual(cubed_number(5.5),166.375)



if __name__ == "__main__":
  unittest.main()
