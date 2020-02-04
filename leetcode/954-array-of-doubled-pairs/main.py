from collections import defaultdict

"""
    1st: sort + hashtable
    e.g. [-4,-2,2,3,4,6,2,4]

    (key: indeces) equals to
    
    negatives:
    -2: [1]
    -4: [0]
    positives:
    2: [2, 6]
    3: [4]
    4: [3, 7]
    6: [5]

    1. for example of key 2, we remove [3] from key 4, as well as [2] from key 2 since 2*2 = 4
    
    negatives:
    -2: [1]
    -4: [0]
    positives:
    2: [6]
    3: [4]
    4: [7]
    6: [5]

    2. for example of key 3, we remove [5] from key 7, as well as [4] from key 3 since 2*3 = 6

    negatives:
    -2: [1]
    -4: [0]
    positives:
    2: [6]
    4: [7]

    continue the process until we dont have any thing our hashtable then return True

    Time    O(NlogN+N)
    Space   O(N)
"""


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        negs = []
        for x in A:
            if x < 0:
                negs.append(x)
        negs = sorted(negs, reverse=True)

        pos = []
        for x in A:
            if x >= 0:
                pos.append(x)
        pos = sorted(pos)

        a = self.check(negs)
        b = self.check(pos)
        return (a and b) == True

    def check(self, nums):
        ht = defaultdict(list)

        for i in range(len(nums)):
            x = nums[i]
            ht[x].append(i)

        visited = len(nums) * [False]

        for i in range(len(nums)):

            if visited[i] == True:
                continue

            num = nums[i]
            target = nums[i] * 2

            if target in ht:
                ht[num].pop(0)
                if len(ht[target]) == 0:
                    return False
                idx = ht[target].pop(0)

                visited[i] = True
                visited[idx] = True
                if len(ht[num]) == 0:
                    del ht[num]
                if len(ht[target]) == 0:
                    del ht[target]
            else:
                return False
        return True


s = Solution()

a = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
print(s.canReorderDoubled(a))


"""
    2nd: sort + hashtable
    - similar to the 1st but sort by abs()

    Time    O(NlogN+N)
    Space   O(N)
    968 ms, faster than 10.00% 
"""


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        arr = sorted(A, key=abs)
        return self.check(arr)

    def check(self, nums):
        ht = defaultdict(list)

        for i in range(len(nums)):
            x = nums[i]
            ht[x].append(i)

        visited = len(nums) * [False]

        for i in range(len(nums)):

            if visited[i] == True:
                continue

            num = nums[i]
            target = nums[i] * 2

            if target in ht:
                ht[num].pop(0)
                if len(ht[target]) == 0:
                    return False
                idx = ht[target].pop(0)

                visited[i] = True
                visited[idx] = True
                if len(ht[num]) == 0:
                    del ht[num]
                if len(ht[target]) == 0:
                    del ht[target]
            else:
                return False
        return True


"""
    3rd: sort + hashtable, too concise, learned from others
    - similar logic as 1st, 2nd
    - but use counts instead of indeces

    ref:
    - https://leetcode.com/problems/array-of-doubled-pairs/discuss/203183/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100

    Time    O(NlogN+N)
    Space   O(N)
    536 ms, faster than 98.57%
"""


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        ht = defaultdict(int)
        for x in A:
            ht[x] += 1

        for x in sorted(ht, key=abs):
            if ht[x] > ht[2*x]:
                return False
            ht[2*x] -= ht[x]
        return True
