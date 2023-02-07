"""
    BFS

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def distinctIntegers(self, n: int) -> int:
        cands = [n]
        seen = set()
        while len(cands) > 0:
            num = cands.pop(0)
            if num in seen:
                continue
            seen.add(num)
            for i in range(1, num+1):
                if num % i == 1:
                    cands.append(i)
        return len(seen)


"""
    Brain teaser
    - for any N, u will get 2, 3, 4...N

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def distinctIntegers(self, n: int) -> int:
        return max(n-1, 1)
