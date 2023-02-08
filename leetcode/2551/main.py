"""
    1st: Sort
    - at the 1st glance, it looks like a DP knapsack problem, but thought through it is a sorting problem
    - keep in mind that in an subarray we only care about the left and right
    - we just need to find k-1 location to cut the array with the min&max scores
    e.g.
        (A[0] + A[i1]) + (A[i2] + A[i3]) + (A[i4] + ..... + A[i(k-1)) + (A[ik] + A[n-1])
             * *                * *              * *     * *                  * *
    =   A[0] + (A[i1]) + A[i2]) + (A[i3] + A[i4)] +..... + (A[i(k-1)] + A[ik]) + A[n-1])
          *           * *               * *                          * *            *
        
    Time    O(NlogN)
    Space   O(N)
"""


from heapq import *


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        buckets_min = []
        buckets_max = []
        for i in range(1, n):
            buckets_min.append(weights[i-1] + weights[i])
            buckets_max.append(weights[i-1] + weights[i])
        buckets_min = sorted(buckets_min)[:k-1]
        buckets_max = sorted(buckets_max, reverse=True)[:k-1]
        score_min = weights[0] + weights[-1] + sum(buckets_min)
        score_max = weights[0] + weights[-1] + sum(buckets_max)
        return score_max - score_min


"""
    2nd: Same logic as 1st
    - but just use min&max heaps for optimization
        
    Time    O(Nlog(K-1))
    Space   O(K-1)
"""


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        buckets_min = []
        buckets_max = []
        for i in range(1, n):
            heappush(buckets_min, -(weights[i-1] + weights[i]))
            if len(buckets_min) > k-1:
                heappop(buckets_min)
            heappush(buckets_max, weights[i-1] + weights[i])
            if len(buckets_max) > k-1:
                heappop(buckets_max)
        score_min = weights[0] + weights[-1] - sum(buckets_min)
        score_max = weights[0] + weights[-1] + sum(buckets_max)
        return score_max - score_min
