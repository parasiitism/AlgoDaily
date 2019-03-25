package main

import "strconv"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	2nd approach: iterative dfs

	Time  O(n)
	Space O(h)
	24 ms, faster than 76.92%
*/

type StackItem struct {
	Node *TreeNode
	Path string
}

func binaryTreePaths(root *TreeNode) []string {
	if root == nil {
		return []string{}
	}
	stack := []*StackItem{}
	stack = append(stack, &StackItem{root, ""})
	res := []string{}
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		node, path := pop.Node, pop.Path
		newPath := path + "->" + strconv.Itoa(node.Val)
		if node.Left == nil && node.Right == nil {
			res = append(res, newPath[2:])
		}
		if node.Left != nil {
			stack = append(stack, &StackItem{node.Left, newPath})
		}
		if node.Right != nil {
			stack = append(stack, &StackItem{node.Right, newPath})
		}
	}
	return res
}

func main() {

}
