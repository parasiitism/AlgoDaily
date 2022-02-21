"""
    1st: backtracking
    - learnt from the others

    Time    O(at most 4^6?) hard to determine due to backtracking but every pair has 6 possible operations
    Space   O(at most 4^6?)
    144 ms, faster than 55.39%
"""


from collections import *


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.backtracking(cards)

    def backtracking(self, nums):
        n = len(nums)
        if n == 1:
            return abs(nums[0] - 24) <= 0.001
        # randomly select 2 numbers to do +-*/
        # due to randomness, it works like using (,)
        for i in range(n):
            for j in range(i):
                # remove the numbers from the current array
                a = nums.pop(i)
                b = nums.pop(j)
                # use the operands
                cands = [a+b, a-b, b-a, a*b]
                if abs(a) > 0.001:
                    cands.append(float(b)/float(a))
                if abs(b) > 0.001:
                    cands.append(float(a)/float(b))
                # for every possibilty, move forward to the next recursive function
                for x in cands:
                    nums.append(x)
                    if self.backtracking(nums):
                        return True
                    # backtrack the possibilty
                    nums.pop()
                # backtrack the pops
                nums.insert(j, b)
                nums.insert(i, a)
        return False


"""
    2nd: BFS
    - very similar to 1st
    - but clone an current array instead of mutating the array

    Time    O(at most 4^6?) hard to determine due to backtracking but every pair has 6 possible operations
    Space   O(at most 4^6?)
    144 ms, faster than 55.39%
"""


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        q = deque()
        q.append(cards)
        seen = set()
        # BFS
        while len(q) > 0:
            nums = q.popleft()
            if len(nums) == 1 and abs(nums[0] - 24) <= 0.001:
                return True

            # since we do BFS, it is possible to see redundant possibilities, see 3rd)
            key = tuple(nums)
            if key in seen:
                continue
            seen.add(key)

            # like 1st, randomly select 2 numbers to do +-*/ to similate using (,)
            # but we do array copy here because we are doing BFS
            for i in range(len(nums)):
                a = nums[i]
                clone1 = nums[:i] + nums[i+1:]
                for j in range(len(clone1)):
                    b = clone1[j]
                    clone2 = clone1[:j] + clone1[j+1:]
                    # use the operands
                    cands = [a+b, a-b, b-a, a*b]
                    if abs(a) > 0.001:
                        cands.append(float(b)/float(a))
                    if abs(b) > 0.001:
                        cands.append(float(a)/float(b))
                    # move to the next iteration
                    for x in cands:
                        q.append(clone2 + [x])
        return False


"""
    3rd: BFS without hashtable

    1383 ms, faster than 5.02%
"""


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        q = deque()
        q.append(cards)
        # seen = set()
        # BFS
        while len(q) > 0:
            nums = q.popleft()
            if len(nums) == 1 and abs(nums[0] - 24) <= 0.001:
                return True
            # key = tuple(nums)
            # if key in seen:
            #     continue
            # seen.add(key)
            for i in range(len(nums)):
                a = nums[i]
                clone1 = nums[:i] + nums[i+1:]
                for j in range(len(clone1)):
                    b = clone1[j]
                    clone2 = clone1[:j] + clone1[j+1:]

                    cands = [a+b, a-b, b-a, a*b]
                    if abs(a) > 0.001:
                        cands.append(float(b)/float(a))
                    if abs(b) > 0.001:
                        cands.append(float(a)/float(b))

                    for x in cands:
                        q.append(clone2 + [x])
        return False
