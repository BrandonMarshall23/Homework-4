import unittest
from full_name import full_name

name_1 = full_name("pete", "seeger")
name_2 = full_name("brandon", "marshall")
name_3 = full_name("hello","world")

class TestName(unittest.TestCase):
    def test_name(self):
        self.assertEqual(name_1, "Pete Seeger")
        self.assertEqual(name_2, "Brandon Marshall")
        self.assertEqual(name_3, "Hello World")
        
        
if __name__ == "__main__":
  unittest.main()
