package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	idea similar to binary search
	- if p and q < current node, move the current to the left
	- if p and q > current node, move the current to the right
	- if current node is between p and q, this is the answer

	Time	O(logn) -> O(n). O(logn) if the tree is complete, O(n) if the tree is like a linked list
	Space O(h)

	28 ms, faster than 98.46%
*/
func LowestCommonAncestor(root *TreeNode, p *TreeNode, q *TreeNode) *TreeNode {
	parent := root
	for true {
		if p.Val < parent.Val && q.Val < parent.Val {
			parent = parent.Left
		} else if p.Val > parent.Val && q.Val > parent.Val {
			parent = parent.Right
		} else {
			break
		}
	}
	return parent
}

func main() {

}
