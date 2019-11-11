from collections import defaultdict
from itertools import product

"""
    1st: brute force
    - try all the possibilities with BFS 

    Time    O(B(B+1)/2 * 2^A) at max
    Space   O(?)
    TLE
"""


class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        allowed = set(allowed)
        ht = defaultdict(str)
        for s in allowed:
            prefix = s[0] + s[1]
            ht[prefix] += s[2]

        q = [bottom]
        while len(q) > 0:
            head = q.pop(0)
            if len(head) == 1:
                return True
            n = len(head)
            candidates = []
            isBroken = False
            for i in range(1, len(head)):
                prefix = head[i-1] + head[i]
                if prefix not in ht:
                    isBroken = True
                    break
                candidates.append(ht[prefix])
            if isBroken:
                continue
            # nextLayers = self.generateNextLayers(candidates)
            nextLayers = product(*candidates)
            for nl in nextLayers:
                if len(nl) == n-1:
                    q.append(nl)
        return False

    def generateNextLayers(self, layers):
        """
            layers = [AB, CDE]
            res = AC, AD, AE, BC, BD, BE
            its what actually itertools.product does
        """
        res = []
        def f(layers, idx, cur):
            if idx == len(layers):
                res.append(cur)
                return
            for i in range(len(layers[idx])):
                f(layers, idx + 1, cur + layers[idx][i])
        f(layers, 0, '')
        return res


s = Solution()

a = "BCD"
b = ["BCG", "CDE", "GEA", "FFF"]
print(s.pyramidTransition(a, b))

a = "BCD"
b = ["BCG", "CDE", "GEA", "FFF", "BCX", "CDY", "XYZ"]
print(s.pyramidTransition(a, b))


a = "AABA"
b = ["AAA", "AAB", "ABA", "ABB", "BAC"]
print(s.pyramidTransition(a, b))

a = "BDBBA"
b = ["ACB","ACA","AAA","ACD","BCD","BAA","BCB","BCC","BAD","BAB","BAC","CAB","CCD","CAA","CCA","CCC","CAD","DAD","DAA","DAC","DCD","DCC","DCA","DDD","BDD","ABB","ABC","ABD","BDB","BBD","BBC","BBA","ADD","ADC","ADA","DDC","DDB","DDA","CDA","CDD","CBA","CDB","CBD","DBA","DBC","DBD","BDA"]
print(s.pyramidTransition(a, b))

a = "BDBBAA"
b = ["ACB","ACA","AAA","ACD","BCD","BAA","BCB","BCC","BAD","BAB","BAC","CAB","CCD","CAA","CCA","CCC","CAD","DAD","DAA","DAC","DCD","DCC","DCA","DDD","BDD","ABB","ABC","ABD","BDB","BBD","BBC","BBA","ADD","ADC","ADA","DDC","DDB","DDA","CDA","CDD","CBA","CDB","CBD","DBA","DBC","DBD","BDA"]
# print(s.pyramidTransition(a, b))

print('-----')

"""
    2nd: brute force
    - try all the possibilities with DFS

    Why it gets LTE with BFS?
    - there might be so many possibilities on each layer(of a pyramid)
    - Given that the bottom width is just 8 unit, if we do DFS, we can reach to any one of the top and skip all other calculations

    Time    O(B(B+1)/2 * 2^A) at max
    Space   O(?)
    20 ms, faster than 90.11%
"""
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        ht = defaultdict(str)
        for s in allowed:
            prefix = s[0] + s[1]
            ht[prefix] += s[2]

        def dfs(layer):
            if len(layer) == 2 and layer in ht:
                return True
            options = []
            for i in range(1, len(layer)):
                key = layer[i-1] + layer[i]
                if key in ht:
                    options.append(ht[key])
                else:
                    return False
            for opt in product(*options):
                nextLayer = ''.join(opt)
                if dfs(nextLayer) == True:
                    return True
            return False
        return dfs(bottom)

s = Solution()

a = "BCD"
b = ["BCG", "CDE", "GEA", "FFF"]
print(s.pyramidTransition(a, b))

a = "BCD"
b = ["BCG", "CDE", "GEA", "FFF", "BCX", "CDY", "XYZ"]
print(s.pyramidTransition(a, b))


a = "AABA"
b = ["AAA", "AAB", "ABA", "ABB", "BAC"]
print(s.pyramidTransition(a, b))

a = "BDBBA"
b = ["ACB","ACA","AAA","ACD","BCD","BAA","BCB","BCC","BAD","BAB","BAC","CAB","CCD","CAA","CCA","CCC","CAD","DAD","DAA","DAC","DCD","DCC","DCA","DDD","BDD","ABB","ABC","ABD","BDB","BBD","BBC","BBA","ADD","ADC","ADA","DDC","DDB","DDA","CDA","CDD","CBA","CDB","CBD","DBA","DBC","DBD","BDA"]
print(s.pyramidTransition(a, b))

a = "BDBBAA"
b = ["ACB","ACA","AAA","ACD","BCD","BAA","BCB","BCC","BAD","BAB","BAC","CAB","CCD","CAA","CCA","CCC","CAD","DAD","DAA","DAC","DCD","DCC","DCA","DDD","BDD","ABB","ABC","ABD","BDB","BBD","BBC","BBA","ADD","ADC","ADA","DDC","DDB","DDA","CDA","CDD","CBA","CDB","CBD","DBA","DBC","DBD","BDA"]
print(s.pyramidTransition(a, b))