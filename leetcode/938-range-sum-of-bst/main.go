package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	questions to ask:
	- can i assume that L < R all the time? yes
	- will there be null root? yes
	- how deep is the depth of the tree? it depends
	- can i assume that the depth wont exceed the call stack size? yes, for now
	- can i assume that the result wont exceed int32 upper bound? yes for now
*/

/*
	1st approach: recursively dfs all the nodes, and sum sup the values within the ranges

	Time    O(n)
	Space   O(h)
	108 ms, faster than 98.54%
*/
func rangeSumBST(root *TreeNode, L int, R int) int {
	res := 0
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		if L <= node.Val && node.Val <= R {
			res += node.Val
		}
		dfs(node.Left)
		dfs(node.Right)
	}
	dfs(root)
	return res
}

/*
	2nd approach: iteratively dfs all the nodes, and sum sup the values within the ranges

	Time    O(n)
	Space   O(h)
	108 ms, faster than 98.54%
*/
func rangeSumBST1(root *TreeNode, L int, R int) int {
	res := 0
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if L <= pop.Val && pop.Val <= R {
			res += pop.Val
		}
		if pop.Left != nil {
			stack = append(stack, pop.Left)
		}
		if pop.Right != nil {
			stack = append(stack, pop.Right)
		}
	}
	return res
}

func main() {

}
