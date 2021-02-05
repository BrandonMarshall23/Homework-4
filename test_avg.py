import unittest 
from avg_list import avg_list

list_1 = [5,10,15]
list_2 = [-5,-10,-15]
list_3 = []

class TestAvg(unittest.TestCase):
    def test_avg(self):
        self.assertAlmostEqual(avg_list(list_1),10)
        self.assertAlmostEqual(avg_list(list_2),-10)
        self.assertRaises(ValueError,avg_list,list_3)
        
if __name__ == "__main__":
    unittest.main()
