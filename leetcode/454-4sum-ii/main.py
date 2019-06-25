"""
    1st approach: hashtable, wrap 3sum with one more loop
	1. put the numbers of D in a hashtable, num:occurence as key:value
	2. for each A[i] + B[j] + C[k], find out the num from the hashtable that they sum up to zero
	3. since there are duplicate in D and we save occurence of each number in D, we can use res += m[target] to find the total count

	Time	O(n^3)
	Space	O(n)
	LTE in python
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ht = {}
        for d in D:
            if d not in ht:
                ht[d] = 1
            else:
                ht[d] += 1
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    remain = -A[i] - B[j] - C[k]
                    if remain in ht:
                        res += ht[remain]
        return res


"""
    2nd approach: better hashtable
	- since unlike traditional 4sum, the numbers here are separate,
	so we can get all the A[i]+B[j] first, check if each C[k]+D[l] presents in the hashtable

	Time	O(n^2)
	Space	O(n)
	292 ms, faster than 68.73%
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ht = {}
        for i in range(len(A)):
            for j in range(len(B)):
                temp = A[i] + B[j]
                if temp not in ht:
                    ht[temp] = 1
                else:
                    ht[temp] += 1
        res = 0
        for i in range(len(C)):
            for j in range(len(D)):
                remain = -C[i]-D[j]
                if remain in ht:
                    res += ht[remain]
        return res
