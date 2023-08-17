"""
    1st: hashtable

    Time    O(N + K)
    Space   O(N + K)
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        hs = set(arr)
        res = []
        cur = 1
        while len(res) < k:
            if cur not in hs:
                res.append(cur)
            cur += 1
        return res[-1]


"""
    2nd: pointers

    Time    O(N)
    Space   O(1)
    48 ms, faster than 82.82%
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        cur = 1
        count = 0
        while True:
            if i < len(arr) and cur == arr[i]:
                i += 1
            else:
                count += 1
            if count == k:
                return cur
            cur += 1


"""
    3rd: binary search

    Time    O(logN)
    Space   O(1)
    48 ms, faster than 99.31%
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            missing = arr[mid] - mid - 1
            if missing < k:
                left = mid + 1
            else:
                right = mid
        return left + k
