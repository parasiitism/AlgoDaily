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
func inorderTraversal1(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var result []int
	var stack []*TreeNode
	curr := root
	for curr != nil || len(stack) > 0 {
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, pop.Val)
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
