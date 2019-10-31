"""
    1st: binary search
    - put indeces of one, two, three in their corresponding arrays
        e.g. colors = [1,1,2,1,3,2,2,3,3]
        ones = [0,1,3]
        twos = [2,5,6]
        thress = [4,7,8]
    - iterate the input queries, find the nearest index of target in corresponding arr
        e.g. query = [6,1]
        find the nearest 3 from index 5 is at index 4
        thress = [4,7,8]
                  ^


    Time    O(QlogC)
    Space   O(C)
    2028 ms, faster than 23.36%
"""


class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        matrix = [[], [], []]
        for i in range(len(colors)):
            if colors[i] == 1:
                matrix[0].append(i)
            elif colors[i] == 2:
                matrix[1].append(i)
            elif colors[i] == 3:
                matrix[2].append(i)
        res = []
        for i, c in queries:
            if len(matrix[c-1]) == 0:
                res.append(-1)
            else:
                r = self.bsearch_nearest(matrix[c-1], i)
                idx = matrix[c-1][r]
                steps = abs(idx - i)
                res.append(steps)
        return res

    def bsearch_nearest(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        # checking
        if right < 0:
            return 0
        if left > len(nums)-1:
            return len(nums)-1
        # compare
        if abs(target - nums[right]) < abs(target - nums[left]):
            return right
        return left
