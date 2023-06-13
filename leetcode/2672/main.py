"""
    1st: brute-force

    Time    O(QN)
    Space   O(N)
"""


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        A = n * [0]
        res = []
        for i, c in queries:
            A[i] = c
            cnt = 0
            for j in range(len(A)-1):
                if A[j] == 0:
                    continue
                if A[j] == A[j+1]:
                    cnt += 1
            res.append(cnt)
        return res


"""
    2nd: counting the adjacent neighours at every query
    
    Observation to optimize the 1st approach:
    - we only mutate the color of a cell one at a time, so for every query we dont need to process the whole array

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        A = n * [0]
        cnt = 0
        for i, c in queries:
            if A[i] != 0:
                if i-1 >= 0 and A[i-1] == A[i]:
                    cnt -= 1
                if i+1 < n and A[i+1] == A[i]:
                    cnt -= 1
            A[i] = c
            if i-1 >= 0 and A[i-1] == A[i]:
                cnt += 1
            if i+1 < n and A[i+1] == A[i]:
                cnt += 1
            res.append(cnt)
        return res
