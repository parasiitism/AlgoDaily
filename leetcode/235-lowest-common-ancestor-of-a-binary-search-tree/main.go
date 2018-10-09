package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func LowestCommonAncestor(root *TreeNode, p *TreeNode, q *TreeNode) *TreeNode {
	curr := root
	var left *TreeNode
	var right *TreeNode
	if p.Val < q.Val {
		left = p
		right = q
	} else {
		left = q
		right = p
	}
	for true {
		if curr.Left != nil && right.Val < curr.Val {
			curr = curr.Left
		} else if curr.Right != nil && left.Val > curr.Val {
			curr = curr.Right
		} else {
			break
		}
	}
	return curr
}

func main() {

}
