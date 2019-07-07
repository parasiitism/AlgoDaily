"""
    1st approach: dynamic programming, learned from others
    - the basic idea is that when we pick a color, we should consider add up the cost from previous remaining colors
    e.g. pick red, consider previous cost from green and blue
    
    red = costs[i][0] + min(blue, green)

	- https://www.youtube.com/watch?v=fZIsEPhSBgM&t=1s

	Time	O(n)
	Space	O(1)
	44 ms, faster than 74.44% 
"""


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        red, blue, green = 0, 0, 0
        for i in range(len(costs)):
            tempRed = costs[i][0] + min(blue, green)
            tempBlue = costs[i][1] + min(red, green)
            tempGreen = costs[i][2] + min(red, blue)
            red, blue, green = tempRed, tempBlue, tempGreen
        return min(red, green, blue)


a = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(Solution().minCost(a))
