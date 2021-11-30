from collections import *

"""
    1st: hashtable
    - very annoying if-clause

    Time    O(N)
    Space   O(N)
    308 ms, faster than 14.29%
"""


class Solution:
    def minimumBuckets(self, street: str) -> int:
        Hs = set()
        n = len(street)
        for i in range(n):
            c = street[i]
            if c == 'H':
                Hs.add(i)
        covered = set()
        buckets = Counter()
        for i in range(n):
            c = street[i]
            if c == 'H':
                continue
            # for all . which both left and right are houses
            if i-1 in Hs and i+1 in Hs:
                # remove the previous bucket if that bucket only collect 1 house' water
                if i-2 in buckets and buckets[i-2] == 1:
                    del buckets[i-2]
                    covered.remove(i-1)
                # if left house is not covered, add a bucket
                if i-1 not in covered:
                    covered.add(i-1)
                    buckets[i] += 1
                # if right house is not covered, add a bucket
                if i+1 not in covered:
                    covered.add(i+1)
                    buckets[i] += 1
            elif i-1 in Hs and i-1 not in covered:
                # add a bucket for the left house
                covered.add(i-1)
                buckets[i] += 1
            elif i+1 in Hs and i+1 not in covered:
                # add a bucket for the right house
                covered.add(i+1)
                buckets[i] += 1
        # make sure all the houses are covered
        if len(Hs) != len(covered):
            return -1
        return len(buckets)
