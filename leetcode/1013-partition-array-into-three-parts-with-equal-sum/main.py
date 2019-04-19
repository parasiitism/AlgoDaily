class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total = sum(A)
        subTotal = total/3
        curSum = 0
        count = 0
        i = 0
        while i < len(A):
            curSum += A[i]
            if curSum == subTotal:
                count += 1
                curSum = 0
            i += 1
            if count == 2:
                break
        lastSum = sum(A[i:])
        return lastSum == subTotal and count == 2
