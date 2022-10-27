"""
    BFS, factorization

    Time    O(sqrt(sum(N)) + E + N)
    Space   O(N)
    4718 ms, faster than 44.26%
"""


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        total = sum(nums)
        factors = self.get_factors(total)

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(parent, node, target_sum):
            subtree_sum = nums[node]
            for nb in g[node]:
                if nb == parent:
                    continue
                subtree_sum += dfs(node, nb, target_sum)
            if subtree_sum == target_sum:
                return 0
            return subtree_sum

        for x in factors:
            if dfs(-1, 0, x) == 0:
                return total//x - 1
        return 0

    def get_factors(self, n):
        smalls = []
        bigs = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                if i == n//i:
                    smalls.append(i)
                else:
                    smalls.append(i)
                    bigs.append(n//i)
            i += 1
        return smalls + bigs[::-1]
