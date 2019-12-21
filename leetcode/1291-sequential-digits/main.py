"""
    1st: kinda brute-force

    Time    O(logN) -> O(N) hard to determine
    Space   O(logN) -> O(N)
    24 ms, faster than 5.78%
"""


class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        heads = [
            '12',
            '123',
            '1234',
            '12345',
            '123456',
            '1234567',
            '12345678',
            '123456789'
        ]
        nums = []
        for head in heads:
            temp = head
            while temp[-1] != '0':
                nums.append(int(temp))
                temp = temp[1:]
                temp += str(int(temp[-1]) + 1)
        res = []
        for num in nums:
            if low <= num <= high:
                res.append(num)
        return res
