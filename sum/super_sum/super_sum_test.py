import unittest
from super_sum import super_sum

class MySuperSumTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(super_sum(), "empty tuple")
        
    def test_sum_of_numbers(self):
        self.assertEqual(super_sum(10, -20), -10)
        self.assertEqual(super_sum(10, 15), 25)
        self.assertEqual(super_sum(-10, -15), -25)
        self.assertEqual(super_sum(0, 0), 0)
        self.assertEqual(super_sum(-5, 15), 10)
        
        
    def test_nested_list(self):
        self.assertEqual(super_sum(11,2,[2,3]), 18)
        self.assertEqual(super_sum(10, [5,5,5],10), 35)
        self.assertEqual(super_sum(-10, [10,-25]), -25)
    def test_str_bool_available(self):    
        with self.assertRaises(ValueError):
            super_sum(2,2,[2,'myString',6])
        with self.assertRaises(ValueError):
            super_sum(2,"a")
        with self.assertRaises(ValueError):
            super_sum('another_num')
        

if __name__ == '__main__':
    unittest.main()
    