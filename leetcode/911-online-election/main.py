"""
    1st approach: hashtable + binary search
    - precompute the winner for each round using a hashtable
    - when q(), do binary search to find the time that <= the input time

    Time of init()   O(n)
    Time of q()      O(qlogn)
    Space            O(n)
    948 ms, faster than 34.82%
"""


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        winners = []
        hs = {}
        maxOcurr = 0
        curwinner = []
        for person in persons:
            # count occurence
            if person not in hs:
                hs[person] = 1
            else:
                hs[person] += 1
            # compute the winner(s) for each round
            if hs[person] > maxOcurr:
                maxOcurr = hs[person]
                curwinner = [person]
            elif hs[person] == maxOcurr:
                curwinner.append(person)
            # append the winner(s) for each round
            winners.append(curwinner[:])
        self.winners = winners
        self.persons = persons
        self.times = times

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        idx = self.bsearch(self.times, t)
        if idx < 0:
            return -1
        winner = self.winners[idx]
        return winner[-1]

    def bsearch(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return right


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
