"""
    questions to ask:
    - the value must be within the range 0 to len(nums)-1 ? yes
    - all numbers are distinct? yes
"""

"""
    1st approach: brute force
    - for every node, find out the max length of the chain

    Time    O(n^2)
    Space   O(n)
    TLE
"""


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            s = set()
              cur = num
               while cur not in s:
                    s.add(cur)
                    cur = nums[cur]
                res = max(res, len(s))
        return res


"""
    2nd approach: learned from others
    - optimize 1st approach
    - for every node, find out the max length of the chain
    - since numbers must be from 0 to n-1 and all DISTINCT, there must be loops
    therefore if we cache the visited loops, we can avoid redundant calculation

    e.g. [5,4,0,3,1,6,2]
    loops are
    [5,6,2,0] -> then go back to 5
    [4,1] -> then go back to 4
    [3] -> then go back to 3

    lets say at index 2, where value is 0. since we know that 0 is in a loop, the max length we can get is 4

    Time    O(n)
    Space   O(n)
    100 ms, faster than 47.05%
"""


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        res = 0
        for num in nums:
            if num not in visited:
                cur = num
                count = 0
                # find the whole loop
                # put every node into visited to avoid redundant calculation
                while True:
                    count += 1
                    visited.add(cur)
                    cur = nums[cur]
                    if cur == num:
                        break
                res = max(res, count)
        return res

print(Solution().arrayNesting([5,4,0,3,1,6,2]))
