class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        count = 0
        notPrime = n*[False]
        for i in range(2, n):
            if notPrime[i] == False:
                count += 1
                j = 2
                while i*j < n:
                    notPrime[i*j] = True
                    j += 1
        return count


print(Solution().countPrimes(10))
