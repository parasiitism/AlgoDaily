import unittest
from main import f

class TestMySolution(unittest.TestCase):

    def test_1(self):
        res = f([4,0,2,2])
        self.assertEqual(res, [4,0,4,0], "should be [4,0,4,0]")

    def test_2(self):
        res = f([4,2,2,3])
        self.assertEqual(res, [8,0,0,3], "should be [8,0,0,3]")
    
    def test_3(self):
        res = f([8,4,2,2,3])
        self.assertEqual(res, [16,0,0,0,3], "should be [16,0,0,0,3]")
    
    def test_4(self):
        res = f([0,0,10,-5,-5,0,3])
        self.assertEqual(res, [0,0,10,-10,0,0,3], "should be [0,0,10,-10,0,0,3]")

if __name__ == '__main__':
    unittest.main()