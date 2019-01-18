class Solution(object):
    """
    40ms beats 53.53%
    """

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        n -= 1
        while n > 0:
            result = self.buildNext(result)
            n -= 1
        return result

    def buildNext(self, s):
        result = ""
        cur = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if cur == s[i]:
                cnt += 1
            else:
                result += str(cnt)+cur
                cur = s[i]
                cnt = 1
        if cnt > 0:
            result += str(cnt)+cur
        return result


print(Solution().countAndSay(1))
print(Solution().countAndSay(2))
print(Solution().countAndSay(3))
print(Solution().countAndSay(4))
print(Solution().countAndSay(5))
