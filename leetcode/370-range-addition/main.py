"""
    brute force: LTE
"""


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        nums = length * [0]
        for a, b, c in updates:
            for i in range(a, b+1):
                nums[i] += c
        return nums


"""
    1st approach: prefix sum

    e.g.

    [0, 0, 0, 0, 0]

    operate [1,3,2]
    it beomes [0,2,2,2,0] but actually we can simply as [0,2,0,0,-2,0]

    operate [2,4,3]
    it becomes [0,2,5,5,3] but actually we can simply as [0,2,3,0,-2,-3]

    operate [0,2,-2]
    it becomes [-2,0,3,5,3] but actually we can simply as [-2,2,3,2,-2,-3]

    now we do prefix sum on the simplied array
    [-2,2,3,2,-2,-3]
      | | | | |
     -2 | | | |
        0 | | |
          3 | |
            5 |
              3
    [-2,0,3,5,3] <- finally we get the result


    Time    O(N+K)
    Space   O(N)
    148 ms, faster than 78.85%
"""


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        nums = (length + 1) * [0]
        for a, b, c in updates:
            nums[a] += c
            nums[b+1] -= c
        res = []
        acc = 0
        for i in range(length):
            acc += nums[i]
            res.append(acc)
        return res
