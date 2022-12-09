"""
    hashtable

    Time    O(N)
    Space   O(N)
    1073 ms, faster than 53.85%
"""


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total = sum(skill)
        unit = 2 * total // n
        ctr = Counter(skill)
        res = 0
        for x in skill:
            if ctr[x] > 0:
                remain = unit - x
                if ctr[remain] == 0:
                    return -1
                res += x * remain
                ctr[x] -= 1
                ctr[remain] -= 1
        return res


"""
    2nd: sort + 2 pointers

    Time    O(NlogN)
    Space   O(1)
    709 ms, faster than 61.54%
"""


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill) - 1
        prev_unit = None
        res = 0
        while i < j:
            unit = skill[i] + skill[j]
            if prev_unit != None and unit != prev_unit:
                return -1
            prev_unit = unit
            res += skill[i] * skill[j]
            i += 1
            j -= 1
        return res
