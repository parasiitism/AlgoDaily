package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach dfs
	Time		O(n)
	Space		O(height of the tree)
	24ms beats 92.86%
	20jan2019
*/
func countNodes(root *TreeNode) int {
	count := 0
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		count++
		dfs(node.Left)
		dfs(node.Right)
	}
	dfs(root)
	return count
}

func main() {

}
