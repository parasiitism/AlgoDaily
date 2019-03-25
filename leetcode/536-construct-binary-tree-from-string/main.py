# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    questions to ask:
    - negative numbers? yes e.g. "51(-232)(434)"
    - every number is single-digited? no, there might be "51(232)(434)"
    - will the number within 2^32? yes
"""


class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode

        1st approach: recursion
        - get every number by appending digits
        - destruct the ( and ) if any
        - repeat the steps when we encounter a (

        Time    O(n)
        Space   O(h)
        176 ms, faster than 56.04%
        """
        arr = []
        for c in s:
            arr.append(c)
        return self.dfs(arr)

    def dfs(self, arr):
        if len(arr) == 0:
            return None

        # construct number
        isNegative = False
        if arr[0] == "-":
            arr.pop(0)
            isNegative = True
        num = ""
        node = None
        while len(arr) > 0 and arr[0] != "(" and arr[0] != ")":
            num += arr.pop(0)
        if isNegative:
            node = TreeNode(-int(num))
        else:
            node = TreeNode(int(num))

        # construct nofe.left with recusively
        if len(arr) > 0 and arr[0] == "(":
            arr.pop(0)
            node.left = self.dfs(arr)

        # construct nofe.right with recusively
        if len(arr) > 0 and arr[0] == "(":
            arr.pop(0)
            node.right = self.dfs(arr)
        # remove )
        if len(arr) > 0 and arr[0] == ")":
            arr.pop(0)
        return node


t = Solution().str2tree("4(2(3)(1))(6(5))")
