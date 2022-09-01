"""
    greedy
    - first, count the pickup_time by using a hashtable
    - second, count the travel_time by using the last index of every garbage occurrence

    Time    O(N)
    Space   O(N)
    3617 ms, faster than 25.00%
"""


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        pickup_time = 0
        last_mpg_idx = {
            'M': 0,
            'P': 0,
            'G': 0
        }
        for i in range(len(garbage)):
            mpg = garbage[i]
            ctr = Counter(mpg)
            pickup_time += ctr['M']
            pickup_time += ctr['P']
            pickup_time += ctr['G']
            if 'M' in mpg:
                last_mpg_idx['M'] = i
            if 'P' in mpg:
                last_mpg_idx['P'] = i
            if 'G' in mpg:
                last_mpg_idx['G'] = i
        travel_time = 0
        for i in range(len(travel)):
            t = travel[i]
            if i+1 <= last_mpg_idx['M']:
                travel_time += t
            if i+1 <= last_mpg_idx['P']:
                travel_time += t
            if i+1 <= last_mpg_idx['G']:
                travel_time += t

        return pickup_time + travel_time
