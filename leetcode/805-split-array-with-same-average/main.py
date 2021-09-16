"""
    1st: brute force
    - try every possibilty

    Time    O(2^N) the recursion tree
    Space   O(2^N)

    LTE
    55 / 92 test cases passed.
    A = [12,19,17,9,9,2,9,4,7]
"""


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        return self.dfs(A, 0, 0)

    def dfs(self, A, cur, count):
        if len(A) > 0 and count > 0:
            print(A)
            if sum(A)/len(A) == cur/count:
                return True
        for i in range(len(A)):
            if self.dfs(A[:i] + A[i+1:], cur + A[i], count + 1):
                return True
        return False


"""
    2nd: dynamic programming
    - learned from others, this is an N sum problem
    
    Sbservations:
    - the question can be deducted as
        total / N = sumA / L = sumB / (N - L)
        so,
        total / N = sumA / L
        total * L / N = sumA <- it must be an integer, this also applies for sumB

    - an item can only with either in groupA or groupB
    - the dataset can be only divided in
        - 2 groups of the same length
        - 1 bigger group, 1 smaller group
        so we just need to try the length from 1 to N//2+1
    - use a hashtable to avoid redundant calculation

    Time    O(2^N) worst
    Space   O(2^N)
    165 ms, faster than 73.20%
"""


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        N = len(A)
        total = sum(A)

        ht = {}

        def dfs(target, L, i):
            if L == 0:
                return target == 0
            # total length <= N
            if L + i > N:
                return False

            key = (target, L, i)
            if key in ht:
                return ht[key]

            # select or not select
            ht[key] = dfs(target - A[i], L - 1, i + 1) or dfs(target, L, i + 1)

            return ht[key]

        # try all the length from 1 to N//2+1
        for L in range(1, N//2+1):
            # sumA or sumB must be an integer
            if total * L % N == 0:
                if dfs(total * L // N, L, 0):
                    return True
        return False
