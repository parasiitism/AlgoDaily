"""
    1st: brute-force
    - Try all the possibilities to pick the remaining numbers (the selection sequence), there are N! possibilities

    Observation
    - In the recursive function, we don't need to indicate which use is playing, because we must start from playerA, so the next must be the playerB, ABABAB...so on. 
    - As long as the current player find a way to win (make opponent lose), this is the optimal stragegy
    - this is also known the minmax problem: min loss -> max gain

    Time    O(N!)
    Space   O(N!)
"""


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        # if we sum up all the numbers but still < desiredTotal, it means playerA cannot force a win
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        # if desiredTotal is small, playerA
        if desiredTotal <= maxChoosableInteger:
            return True

        # an array to indicate which integers are used
        chosen = (maxChoosableInteger + 1) * [False]
        return self.dfs(chosen, desiredTotal)

    def dfs(self, chosen, remainingTotal):

        # it means the previous person found an integer that made the total becomes 0, so the current person lost
        if remainingTotal <= 0:
            return False

        for i in range(1, len(chosen)):
            if chosen[i] == False:
                chosen[i] = True
                # if the current person found a number to make the next person lose,
                # this person wins and that is the optimal selection then we can return immediately
                if self.dfs(chosen, remainingTotal - i) == False:
                    chosen[i] = False
                    return True
                chosen[i] = False

        return False


"""
    2nd: optimize with cache
    - actually the selection sequence doesn't matter, as the remaining total is the same, and for every reach to that total who will wins
        i.e.
        2,3,4....
        4,3,2....
        In this example, playerA picked 2,4 and playerB picked 3
    , so we can cache the used integers, and when we travese in another permutation and see the used integers before, it means we explored that node
    

    Time    O(2^N)
    Space   O(2^N)
"""


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        if desiredTotal <= maxChoosableInteger:
            return True

        chosen = (maxChoosableInteger + 1) * [False]
        seen = {}
        return self.dfs(chosen, desiredTotal, seen)

    def dfs(self, chosen, remainingTotal, seen):
        if remainingTotal <= 0:
            return False
        key = tuple(chosen)
        if key in seen:
            return seen[key]
        for i in range(1, len(chosen)):
            if chosen[i] == False:
                chosen[i] = True
                if self.dfs(chosen, remainingTotal - i, seen) == False:
                    chosen[i] = False
                    seen[key] = True
                    return True
                chosen[i] = False
        seen[key] = False
        return False
