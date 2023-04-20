"""
    Math + hashtable + prefix sum
    1. use a hashtable to calculate the number: [indices]
        {
            1: [0, 2, 3]
            2: [4]
            3: [1]
        }
    2. then for each key, basically we can narrow down the question to: Calculate the absolute diffs amongst all numbers
    
    e.g. [0, 2, 3, 9, 11]

    If we brute-force in O(N^2)
    At idx=0, |3-0| + |2-0| + |9-0| + |11-0| = 25
    At idx=1, |0-2| + |3-2| + |9-2| + |11-2| = 19
    At idx=2, |0-3| + |2-3| + |9-3| + |11-3| = 18
    At idx=3, |0-9| + |3-9| + |2-9| + |11-9| = 24
    At idx=4, |0-11| + |3-11| + |2-11| + |9-11| = 30
    
    But if the numbers are sorted, we can transform the formala to make the calculation O(N)
        |A[0] - A[i]| + |A[1] - A[i]| + ...... |A[i] - A[i]| + ...... + |A[n-2] - A[i]| + |A[n-1] - A[i]|
    =   (A[i] - A[0]) + (A[i] - A[1]) + ...... (A[i] - A[i]) + ...... + (A[n-2] - A[i]) + (A[n-1] - A[i])
    

    Time    O(N)    837 ms
    Space   O(N)
"""


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_indices = defaultdict(list)
        for i in range(n):
            x = nums[i]
            num_indices[x].append(i)
        res = n * [0]
        for k in num_indices:
            A = num_indices[k]
            total = sum(A)
            pfss = []
            pfs = 0
            for x in A:
                pfs += x
                pfss.append(pfs)
            m = len(A)
            for i in range(m):
                left = (i + 1) * A[i] - pfss[i]
                right = total - pfss[i] - (m - i - 1) * A[i]
                idx = A[i]
                res[idx] = left + right
        return res
