package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

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

func main() {

}
