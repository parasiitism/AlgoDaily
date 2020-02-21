from collections import defaultdict
from collections import Counter

"""
    1st: binary search + hashtable

    Time of addScore()      O(k), it can be O(logN) depends on language becos of array.insert()
    Time of top()           O(k)
    Time of reset()         O(N) binary search + linear search
    Space                   O(2N)
    60 ms, faster than 77.46%
"""


class Leaderboard:

    def __init__(self):
        self.ht = defaultdict(int)
        self.nums = []

    def _upperBsearch(self, nums, target):
        # nums = [(player0, score0), (player1, score1)....]
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid][1]:
                left = mid + 1
            else:
                right = mid
        return right

    def findPersonFromTheRight(self, nums, idx, playerId):
        while nums[idx][0] != playerId:
            idx -= 1
        return idx

    def addScore(self, playerId: int, score: int) -> None:
        idxToInsert = self._upperBsearch(self.nums, score)
        if playerId in self.ht:
            idxToInsert -= 1
            targetIdx = self.findPersonFromTheRight(
                self.nums, idxToInsert, playerId)
            # get the new score
            newScore = self.nums[targetIdx][1] + score
            # remove
            self.nums = self.nums[:targetIdx] + self.nums[targetIdx+1:]
            # add back
            idxToInsert = self._upperBsearch(self.nums, newScore)
            self.nums.insert(idxToInsert, (playerId, newScore))
            self.ht[playerId] = newScore
        else:
            self.nums.insert(idxToInsert, (playerId, score))
            self.ht[playerId] = score

    def top(self, K: int) -> int:
        total = 0
        for i in range(len(self.nums)-1, len(self.nums)-K-1, -1):
            total += self.nums[i][1]
        return total

    def reset(self, playerId: int) -> None:
        if playerId not in self.ht:
            return
        # find out the score
        score = self.ht[playerId]
        # binary search the (player, score) with the same score O(logN)
        rightMostIdx = self._upperBsearch(self.nums, score) - 1
        # linear search the player
        targetIdx = self.findPersonFromTheRight(
            self.nums, rightMostIdx, playerId)
        # remove it from the list
        self.nums = self.nums[:targetIdx] + self.nums[targetIdx+1:]
        del self.ht[playerId]


"""
    2nd: just use a hashtable

    ref:
    - https://leetcode.com/problems/design-a-leaderboard/discuss/418866/Python-Counter-1-line-Each

    Time of addScore()      O(1)
    Time of top()           O(N) -> O(NlogK)
    Time of reset()         O(1)
    Space                   O(1)
    112 ms, faster than 23.24%
"""


class Leaderboard(object):

    def __init__(self):
        self.A = Counter()

    def addScore(self, playerId, score):
        self.A[playerId] += score

    def top(self, K):
        return sum(v for i, v in self.A.most_common(K))

    def reset(self, playerId):
        self.A[playerId] = 0
