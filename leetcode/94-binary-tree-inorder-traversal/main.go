package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// recursive
func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	result := []int{}
	if root.Left != nil {
		left := inorderTraversal(root.Left)
		result = append(result, left...)
	}
	result = append(result, root.Val)
	if root.Right != nil {
		right := inorderTraversal(root.Right)
		result = append(result, right...)
	}
	return result
}

// iterative
// 1. put left child into stack recusively
// 2. when we pop a stack, set current to the pop.right such that we will not consider any node which was in the stack(avoid duplicate)
func inorderTraversal1(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var result []int
	var stack []*TreeNode
	curr := root
	for curr != nil || len(stack) > 0 {
		// get to the left-most node
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}
		// put the node in to the result
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, pop.Val)
		// consider the right node
		curr = pop.Right
	}
	return result
}

func main() {
	// 		1
	//	2		3
	// 4 5 6 7
	root := &TreeNode{1,
		&TreeNode{2,
			&TreeNode{4, nil, nil},
			&TreeNode{5, nil, nil},
		},
		&TreeNode{3,
			&TreeNode{6, nil, nil},
			&TreeNode{7, nil, nil},
		},
	}
	ans := inorderTraversal1(root)
	fmt.Println(ans)
}
