"""
    1st approach:
    - 2 pointers, expand from center
    
    Time    O(n)
    Space   O(n)
    32 ms, faster than 49.54%
"""


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        # find out the min/max of the equation
        if a == 0 and b > 0:
            return [self.computeY(num, a, b, c) for num in nums]
        elif a == 0 and b < 0:
            return [self.computeY(num, a, b, c) for num in nums[::-1]]
        elif a == 0 and b == 0:
            return [self.computeY(num, a, b, c) for num in nums]
        minmaxX = -b/float(2*a)
        minmaxY = self.computeY(minmaxX, a, b, c)
        # find the closest index
        closest = 0
        res = []
        for i in range(len(nums)):
            if abs(nums[i] - minmaxX) < abs(nums[closest] - minmaxX):
                closest = i
        # expand from center
        i, j = closest, closest+1
        while i >= 0 or j < len(nums):
            # check left hand side
            left = float('-inf')
            if i >= 0:
                left = self.computeY(nums[i], a, b, c)
            # check right hand side
            right = float('inf')
            if j < len(nums):
                right = self.computeY(nums[j], a, b, c)
            # find the closest one
            if abs(left - minmaxY) < abs(right - minmaxY):
                res.append(self.computeY(nums[i], a, b, c))
                i -= 1
            else:
                res.append(self.computeY(nums[j], a, b, c))
                j += 1
        if a < 0:
            return res[::-1]
        return res

    def computeY(self, x, a, b, c):
        return a*x*x + b*x + c


print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], 1, 3, 5))
print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], -1, 3, 5))
print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], 1, -3, 5))
print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], -1, -3, 5))

print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], 2, 6, 2))
print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], -2, 6, 2))
print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], 2, -6, 2))
print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], -2, -6, 2))

print(Solution().sortTransformedArray([-10, -9, -8, -7, -6], 1, 4, 2))
print(Solution().sortTransformedArray([6, 7, 8, 9, 10], 1, 4, 2))

# # corner case
print(Solution().sortTransformedArray([], 2, 6, 2))
print(Solution().sortTransformedArray([0], 2, 6, 2))
print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], 0, 6, 2))
print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], 0, -6, 2))
print(Solution().sortTransformedArray([-6, -4, -2, 2, 4, 6], 0, 0, 2))
