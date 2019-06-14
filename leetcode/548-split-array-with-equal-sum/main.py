"""
    1st approach: prefix sum + hashtable
    - calculate the prefix sum from 0 to n-1
    - sum between ranges are
        - 0 -> i-1:     prefixsums[i-1]
        - i+1 -> j-1:   prefixsums[j-1] - prefixsums[i]
        - j+1 -> k-1:   prefixsums[k-1] - prefixsums[j]
        - k+1 -> n-1:   prefixsums[-1] - prefixsums[k]
    - divide the array at each index,j, and see if there is i on the left and k on the right
    
    ref:
    - https://www.jianshu.com/p/b766486b3096

    Time    O(n^2)
    Space   O(n)
    2120 ms, faster than 47.41%
"""


class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prefixsum = 0
        prefixsums = []
        for num in nums:
            prefixsum += num
            prefixsums.append(prefixsum)

        for j in range(len(nums)):
            hs = set()
            for i in range(1, j-1):
                if prefixsums[i-1] == prefixsums[j-1] - prefixsums[i]:
                    hs.add(prefixsums[i-1])
            for k in range(j+2, len(nums)-1):
                if prefixsums[-1] - prefixsums[k] == prefixsums[k-1] - prefixsums[j]:
                    key = prefixsums[-1]-prefixsums[k]
                    if key in hs:
                        return True
        return False


s = Solution()

# true
a = [1, 2, 1, 2, 1, 2, 1]
print(s.splitArray(a))

# true
a = [1, 2, 1, 3, 0, 0, 2, 2, 1, 3, 3]
print(s.splitArray(a))

# false
a = [1, 4, 1, 3, 1, -14, 1, -13]
print(s.splitArray(a))

# true
a = [1, 2, -1, 1, 2, 5, 2, 5, 2]
print(s.splitArray(a))
