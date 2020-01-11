import unittest
from Test1 import print_depth, find_depth

class TestTest1(unittest.TestCase):
    
    def test_find_depth(self):
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        result = ['key1 1','key2 1','key3 2','key4 2','key5 3']

        self.assertEqual(find_depth(a, 1, []), result)

if __name__ == '__main__':
    unittest.main()