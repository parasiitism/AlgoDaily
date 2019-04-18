class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        merge = x ^ y
        count = 0
        while merge > 0:
            if merge & 1 == 1:
                count += 1
            merge = merge >> 1
        return count


print(Solution().hammingDistance(1, 4))
