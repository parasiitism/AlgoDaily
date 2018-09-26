package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// suggested
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

// another: see main.py

// another:
// first, in order traverse through the tree and save each node into an array
// second, return the array[target+1]
// complexity: O(2n) so i wont implement it

func main() {

}
