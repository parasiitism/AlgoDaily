"""
    1st: brute-force hashtable

    Time    O(N^2)
    Space   O(N) 
"""


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen = Counter()
        res = []
        for i in range(n):
            seen[A[i]] += 1
            seen[B[i]] += 1
            cnt = 0
            for key in seen:
                if seen[key] > 1:
                    cnt += 1
            res.append(cnt)
        return res


"""
    2nd: hashset with math
    - since every item will only appear once, we can remove duplicate, and then count the number of removal along iteration

    Time    O(N)
    Space   O(N/2)
"""


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen = set()
        res = []
        remove_count = 0
        for i in range(n):
            a, b = A[i], B[i]

            if a in seen:
                seen.remove(a)
                remove_count += 1
            else:
                seen.add(a)

            if b in seen:
                seen.remove(b)
                remove_count += 1
            else:
                seen.add(b)

            res.append(remove_count)
        return res
