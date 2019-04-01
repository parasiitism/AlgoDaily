package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	2nd approach: iterative dfs

	Time  O(n)
	Space O(h)
	8 ms, faster than 70.71%
*/

type StackItem struct {
	Node      *TreeNode
	PrefixSum int
	Path      []int
}

func pathSum(root *TreeNode, sum int) [][]int {
	if root == nil {
		return [][]int{}
	}
	res := [][]int{}
	stack := []*StackItem{}
	stack = append(stack, &StackItem{root, 0, []int{}})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		node := pop.Node

		cur := pop.PrefixSum + node.Val

		path := []int{}
		path = append(path, pop.Path...)
		path = append(path, node.Val)

		if node.Left == nil && node.Right == nil && cur == sum {
			res = append(res, path)
		}
		if node.Left != nil {
			stack = append(stack, &StackItem{node.Left, cur, path})
		}
		if node.Right != nil {
			stack = append(stack, &StackItem{node.Right, cur, path})
		}
	}
	return res
}

func main() {

}
