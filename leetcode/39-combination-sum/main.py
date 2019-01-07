"""
    1st attempt:
    - bottom-up dynamic programming approch
    - use a hashtable to avoid duplicates
    e.g. candidates = [2,3,5], target = 8
    f[0] = []
    f[1] = []
    f[2] = [[2]]
    f[3] = [[3]]
    f[4] = [[2,2]]
    f[5] = [[2,3],[5]]
    f[6] = [[2,2,2],[3,3]]
    f[7] = [[2,2,3],[2,5]]
    f[8] = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    beats 15.56%
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(target+1):
            result.append([])
        for i in range(target+1):
            future_result = []
            seen = {}
            for candidate in candidates:
                cur = i - candidate
                if cur < 0:
                    continue
                that_results = result[cur]
                if len(that_results) == 0 and cur == 0:
                    future_result.append([candidate])
                else:
                    for that_result in that_results:
                        temp = that_result + [candidate]
                        temp = sorted(temp)
                        key = "".join(str(n) for n in temp)
                        if key in seen:
                            continue
                        seen[key] = True
                        future_result.append(temp)

            result[i] = future_result

        return result[target]


print(Solution().combinationSum([2, 3, 5], 8))
print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([1, 2, 3, 4], 15))
