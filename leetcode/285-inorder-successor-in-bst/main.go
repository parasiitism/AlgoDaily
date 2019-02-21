package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	leetcode doesn't support go for this question, i did it in python
	my first intuitve workable attempt: see main.py
	suggested solution by leetcoders: O(logn)
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
