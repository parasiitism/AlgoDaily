"""
    1st approach: bit op + hashtable
    - count the occurence of each digit in N
    - compare the signature(occurence of digits) to 2^i where 0 <= i < 32

    e.g.
    N = 4210
    signature = [1,1,1,0,1,0,0,0]
    then we iterate the power of 2 from 1 to 2^32, we see that 1024 has the same signature

    Time    O(logn + 32logn) log base = 10
    Space   O(logn)
    36 ms, faster than 28.44%
"""


class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        target = self.signature(N)
        for i in range(32):
            if self.signature(1 << i) == target:
                return True
        return False

    def signature(self, num):
        m = 10 * [0]
        while num > 0:
            m[num % 10] += 1
            num /= 10
        return tuple(m)


"""
    2nd: hashtable
    - build a hashtable to store the parent relation of every node
    - BFS to find all the nodes which are k-distance away from target

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parents = {}

        def dfs(node, prev):
            if node == None:
                return
            parents[node] = prev
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        res = []
        q = [(target, 0)]
        seen = set()
        while len(q) > 0:
            node, steps = q.pop(0)
            if node == None:
                continue
            if node in seen:
                continue
            seen.add(node)
            if steps == k:
                res.append(node.val)
            else:
                q.append((node.left, steps + 1))
                q.append((node.right, steps + 1))
                q.append((parents[node], steps + 1))
        return res
