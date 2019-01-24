package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	Questions to ask:
	- will there be empty nodes s or t ?
	- if both empty, what should i return?
	- so what i need to check is whether the trees have the same structure and values, but not the addresses/pointers of the nodes?
	amazon OA: https://wdxtub.com/interview/14520850399861.html
*/

/*
	1st approach
	1. dfs to look for the node having the same value with target root
	2. if yes, check the left and right subtrees are identical to the target
	Time	O(n^2) for each node, check its children
	Space	O(h)
	24ms beats 100%
	24jan2019
*/
func isSubtree(s *TreeNode, t *TreeNode) bool {
	if s == nil && t == nil {
		return true
	} else if s == nil || t == nil {
		return false
	}

	if s.Val == t.Val {
		if isIdentical(s, t) == true {
			return true
		}
	}
	left := isSubtree(s.Left, t)
	right := isSubtree(s.Right, t)
	return left || right
}

func isIdentical(a *TreeNode, b *TreeNode) bool {
	if a == nil && b == nil {
		return true
	} else if a == nil || b == nil {
		return false
	}
	mid := a.Val == b.Val
	left := isIdentical(a.Left, b.Left)
	right := isIdentical(a.Right, b.Right)
	return mid && left && right
}

func main() {

}
