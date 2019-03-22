"""
    this is a final follow-up of strobogrammatic number

    my approach is to reuse the algo from strobogrammatic ii
    - generate all numbers
    - for each number, compare with low and high, and then put it into the result if match

    Time    O(n) i need to generate all numbers, (n+1)*n/2
    Space   O(n)
    516ms beats 27.21%
"""


class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        digitCount = len(high)
        nums = self.findStrobogrammatic(digitCount)
        res = 0
        for num in nums:
            if int(low) <= int(num) and int(num) <= int(high):
                res += 1
        return res

    def findStrobogrammatic(self, n):
        singles = ["0", "1", "8"]
        pairs = ["00", "11", "69", "88", "96"]

        if n == 0:
            return []
        elif n == 1:
            return singles

        res = ["0", "1", "8"]

        def helper(cnt, s, shouldEnd=False):
            res.append(s)

            if shouldEnd:
                return
            if cnt >= n:
                return
            else:
                pos = cnt/2
                if cnt+1 <= n:
                    for i in range(len(singles)):
                        helper(cnt+1, s[:pos]+singles[i]+s[pos:], True)
                if cnt+2 <= n:
                    for i in range(len(pairs)):
                        helper(cnt+2, s[:pos]+pairs[i]+s[pos:])

        for i in range(1, len(pairs)):
            helper(2, pairs[i])

        return res


print(Solution().strobogrammaticInRange("50", "100"))
print(Solution().strobogrammaticInRange("0", "1680"))
