class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]

        classic approach
        - gray's reflect and prefix method ./gray_code.png
        - the idea is mirror the reversed numbers of the previous array and add '1' at the beginning of each number
        e.g.
            n=1 [0,1]
            n=2 [00, 01, 11, 10] <= added 11 and 10
            n=3 [00, 01, 11, 10, 110, 111, 101, 100] <= added 110, 111, 101, 100

        24ms beats 97.54%
        Time 	O(2^n) when n=3, there are 8 items in the result
        Space	O(2^n)
        10feb2019
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
