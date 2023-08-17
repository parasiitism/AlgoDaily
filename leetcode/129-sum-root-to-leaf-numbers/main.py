class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root, 0)]
        while len(stack) > 0:
            node, total = stack.pop()
            total = total*10 + node.val

            if node.left == None and node.right == None:
                res += total

            if node.left:
                stack.append((node.left, total))
            if node.right:
                stack.append((node.right, total))
        return res
