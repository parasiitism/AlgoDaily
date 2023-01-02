"""
    1st: binary search

    Time    O(NlogN)    Runtime 3752 ms Beats 7.47%
    Space   O(N)
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        forward, backward = [0, 0, 0], [0, 0, 0]
        # the first item [0,0,0] means that we can start from a:0,b:0,c:0
        forwards = [forward[:]]
        backwards = [backward[:]]
        for i in range(n):
            f = ord(s[i]) - ord('a')
            b = ord(s[n-i-1]) - ord('a')
            forward[f] += 1
            backward[b] += 1
            forwards.append(forward[:])
            backwards.append(backward[:])
        if any([f < k for f in forwards[-1]]):
            return -1
        res = n
        for i in range(n+1):
            a, b, c = forwards[i]
            left, right = 0, n+1
            while left < right:
                mid = (left + right) // 2
                if self.meet(backwards, mid, i, a, b, c, k):
                    right = mid
                else:
                    left = mid + 1
            total_days = i + left
            res = min(res, total_days)
        return res

    def meet(self, backwards, mid, i, a, b, c, k):
        _a, _b, _c = backwards[mid]
        if a+_a < k or b+_b < k or c+_c < k:
            return False
        return True


"""
    2nd: 2 pointers
    - rephase: find the maximum window in the middle to remove so that each of the remaining characters on both side >= k

    Time    O(N)    Runtime 424 ms Beats 64.17%
    Space   O(N)
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        ctr = Counter(s)
        if any([ctr[c] < k for c in 'abc']):
            return -1
        max_window = 0
        j = 0
        cur = Counter()
        for i in range(n):
            c = s[i]
            cur[c] += 1
            while cur[c] > ctr[c] - k:
                cur[s[j]] -= 1
                j += 1
            max_window = max(max_window, i-j+1)
        return n - max_window
