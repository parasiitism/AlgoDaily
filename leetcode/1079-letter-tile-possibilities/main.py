"""
    1st: subsets + permutations + hashtable optimization
    1. sort the input characters, create a sorted string
    2. generate all the distinct subsets, use a hashtbale to avoid redundant calculation
    3. generate all the permutations of each subset, use hashtbale to avoid redundant calculation

    Time    O(2^n * n!) 2^n for subsets, n! for permutation
    140 ms, faster than 27.32%
"""


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        # hashtable
        ht = 26 * [0]
        for c in tiles:
            idx = ord(c) - ord('A')
            ht[idx] += 1
        s = ''
        alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(26):
            s += ht[i] * alphabets[i]

        # subset
        self.hs = set()
        self.genSubsets(s, "")

        # permuations
        self.hs2 = set()
        for key in self.hs:
            self.genPermutation(key, '')
        return len(self.hs2)

    def genSubsets(self, cands, chosen):
        if chosen != '':
            self.hs.add(chosen)
        for i in range(len(cands)):
            newChosen = chosen+cands[i]
            if newChosen in self.hs:
                continue
            self.genSubsets(cands[i+1:], newChosen)

    def genPermutation(self, cands, chosen):
        if len(cands) == 0:
            self.hs2.add(chosen)
        for i in range(len(cands)):
            if i == 0 or cands[i-1] != cands[i]:
                self.genPermutation(cands[:i] + cands[i+1:], chosen + cands[i])


s = Solution()

a = 'AAB'
print(s.numTilePossibilities(a))

a = 'AAABBC'
print(s.numTilePossibilities(a))

a = 'ABACAB'
print(s.numTilePossibilities(a))

a = 'EFGABCD'
print(s.numTilePossibilities(a))
