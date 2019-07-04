"""
    1st approach: custom sort

    Time    O(nlogn)
    Space   O(n)
    108 ms, faster than 64.33% 
"""


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        for i in range(1, n+1):
            arr.append(i)
        arr = sorted(arr, key=lambda x: str(x))
        return arr


s = Solution()

a = 13
print(s.lexicalOrder(a))

a = 1000
print(s.lexicalOrder(a))
