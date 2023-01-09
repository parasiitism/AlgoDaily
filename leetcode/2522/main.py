"""
    2 pointers

    Time    O(S)
    Space   O(S) my 'nums' is unnecessary
"""


class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        nums = []
        i = 0
        while i < len(s):
            j = i
            cur = s[j]
            if int(cur) > k:
                return -1
            while j+1 < len(s) and int(cur+s[j+1]) <= k:
                cur += s[j+1]
                j += 1
            nums.append(int(cur))
            i = j+1
        return len(nums)
