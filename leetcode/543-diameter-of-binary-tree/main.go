package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: dfs in recursion
	- for each node, compare the depths of left and right subtree
	- and compare and assign the result
	- in each node, just return the max depth of either left or right subtree

	Time  O(n)
	Space O(h)
	4 ms, faster than 100.00%
*/
func diameterOfBinaryTree(root *TreeNode) int {
	res := 0
	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		temp := left + right
		if temp > res {
			res = temp
		}
		if left > right {
			return left + 1
		}
		return right + 1
	}
	dfs(root)
	return res
}

func main() {

}
