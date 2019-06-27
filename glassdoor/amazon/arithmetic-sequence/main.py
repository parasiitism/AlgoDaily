class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int

        1st appraoch
        - math, use n*(n+1)/2 to calculate the combination count instead of doing brute force

        Time    O(n)
        Space   O(1)
        20ms beats 100%
        31jan2019
        """
        if len(A) < 3:
            return 0
        diff = A[1]-A[0]
        start = 0
        res = 0
        for i in range(2, len(A)):
            temp = A[i]-A[i-1]
            if temp == diff:
                if i+1 == len(A):
                    res += self.cal(A, start, i)
                continue
            else:
                res += self.cal(A, start, i-1)
                # be careful: set the next start point from the previous item
                # take this case into consideration [1, 2, 3, 8, 13]
                start = i-1
                diff = temp
        return res

    def cal(self, nums, start, end):
        n = end - start - 1
        if n > 0:
            return n*(n+1)/2
        return 0


print(Solution().numberOfArithmeticSlices([1, 2, 3, 8, 13]))
print(Solution().numberOfArithmeticSlices([1, 2, 3, 8, 9, 10]))
print(Solution().numberOfArithmeticSlices([1, 2, 3, 4, 5]))
print(Solution().numberOfArithmeticSlices([1, 1, 2, 5, 7]))
print(Solution().numberOfArithmeticSlices([1, 3, 5, 7, 9]))
print(Solution().numberOfArithmeticSlices([3, -1, -5, -9]))
