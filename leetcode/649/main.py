"""
    1st: queue
    
    Idea:
        - find the closest opponent to ban
        - to rotate, add the winner to the end of the queue by +n in the index
        - that's it

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        Rs = []
        Ds = []
        for i in range(n):
            c = senate[i]
            if c == 'R':
                Rs.append(i)
            else:
                Ds.append(i)
        while len(Rs) > 0 or len(Ds) > 0:
            if len(Rs) == 0:
                return 'Dire'
            if len(Ds) == 0:
                return 'Radiant'
            if Rs[0] < Ds[0]:
                Ds.pop(0)
                r_idx = Rs.pop(0)
                Rs.append(r_idx + n)
            elif Rs[0] > Ds[0]:
                Rs.pop(0)
                d_idx = Ds.pop(0)
                Ds.append(d_idx + n)
        return None
