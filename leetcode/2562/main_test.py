import unittest
from main import Solution

class TestMySolution(unittest.TestCase):

    # Method 1: use the class method
    # @classmethod
    # def setUpClass(self):
    #     self.sol = Solution()
    
    # Method 2: override the init
    def __init__(self, *args, **kwargs):
        super(TestMySolution, self).__init__(*args, **kwargs)
        self.sol = Solution()

    def test_1(self):
        res = self.sol.findTheArrayConcVal([7,52,2,4])
        self.assertEqual(res, 596, "should be 596")
    
    def test_2(self):
        res = self.sol.findTheArrayConcVal([5,14,13,8,12])
        self.assertEqual(res, 673, "should be 596")

if __name__ == '__main__':
    unittest.main()