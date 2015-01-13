import unittest
from mapreducelib import mapexample1

class TestMap(unittest.TestCase):
     def setUp(self):
          pass

     def test_map_1(self):
          l1 = [1,2,3,4,5,6,]
          l2 = ['a','b','c','d','e','f',]
          self.assertEqual(mapexample1.map_list(l1, l2),[(1,'a'), (2,'b'), (3,'c'), (4, 'd'), (5, 'e'), (6,'f')])

     def test_map_2(self):
          l1 = ['apples', 'oranges', 'melon']
          l2 = []
          self.assertEqual(mapexample1.map_list(l1,l2), [('apples',None),('oranges',None),('melon',None)])

if __name__ == '__main__':
     unittest.main()
