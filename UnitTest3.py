import unittest
from Test3 import Node, lca

class TestTest2(unittest.TestCase):
    
    def test_common_ancestor(self):
        one = Node(1, None)
        two = Node(2, one)
        three = Node(3, one)
        four = Node(4, two)
        five = Node(5, two)
        six = Node(6, three)
        seven = Node(7, three)
        eight = Node(8, four)
        nine = Node(9, four)

        self.assertEqual(lca(nine, seven), 1)
        self.assertEqual(lca(six, seven), 3)
        self.assertEqual(lca(three, seven), 3)
        self.assertEqual(lca(eight, nine), 4)
        self.assertEqual(lca(nine, five), 2)

if __name__ == '__main__':
    unittest.main()