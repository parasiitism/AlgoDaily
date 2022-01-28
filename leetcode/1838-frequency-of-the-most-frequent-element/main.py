"""
    1st: brute force
    
    Time    O(N^2)
    TLE
"""


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n-1, -1, -1):
            _k = k
            j = i
            while j >= 0:
                diff = nums[i] - nums[j]
                if _k >= diff:
                    _k -= diff
                else:
                    break
                j -= 1
            count = i - j
            res = max(res, count)
        return res


"""
    2nd: sort + sliding window
    1. sort the nums descendingly
    2. for every index, find the furthest right point it can reach
    3. during, interation, remember to add back the diffs

    e.g.
        [13, 12, 11, 10, 8, 4], k=6
    0:   i            j         k=0
    1:       i        j         k=3
    2:            i      j      k=1
    3:                i  j      k=3
    4:                   i  j   k=2
    From the above, at idx0, the diff between i and j is the largest

    Time    O(NlogN + N)
    Space   O(1)
    1648 ms, faster than 53.18%
"""


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort(key=lambda x: -x)
        res = 0
        _k = k
        j = 0
        for i in range(n):
            while j+1 < n:
                diff = nums[i] - nums[j+1]
                if _k >= diff:
                    _k -= diff
                    j += 1
                else:
                    break
            count = j - i + 1
            res = max(res, count)
            if i+1 < n:
                _k += (j - i) * (nums[i] - nums[i+1])
        return res
