package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	Decent iterative approach:
	1. if the current node.val > target, pass down and update successor with node
	2. if the current node.val <= target, pass down
	3. do 1 & 2 intil current node is null

	Time	O(logn)
	Space	O(h)
	24 ms, faster than 100.00%
*/
func inorderSuccessor(root *TreeNode, p *TreeNode) *TreeNode {
	var successor *TreeNode
	node := root
	for node != nil {
		if p.Val < node.Val {
			successor = node
			node = node.Left
		} else {
			node = node.Right
		}
	}
	return successor
}

// another:
// 1. in order traverse through the tree and save each node into an array
// 2. return the array[target+1]
// complexity: O(2n) so i wont implement it

func main() {

}
