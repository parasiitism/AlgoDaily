class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return [0]
        res = [0, 1]
        cnt = 1
        while cnt < n:
            mirror = []
            for i in range(len(res) - 1, -1, -1):
                temp = res[i] + (1 << cnt)
                mirror.append(temp)
            res = res + mirror
            cnt += 1
        return res


a = 1
b = a + (1 << 1)
print(a, b)

print(Solution().grayCode(-1))
print(Solution().grayCode(0))
print(Solution().grayCode(1))
print(Solution().grayCode(2))
print(Solution().grayCode(3))
print(Solution().grayCode(4))
