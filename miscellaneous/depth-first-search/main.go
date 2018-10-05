package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// depth first search = pre-order traversal
// iterative
func dfs(root *TreeNode) {
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		fmt.Println(pop.Val)
		if pop.Right != nil {
			stack = append(stack, pop.Right)
		}
		if pop.Left != nil {
			stack = append(stack, pop.Left)
		}
	}
}

// recursive
// pre-order
func dfsRecursivePreorder(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Println(root.Val)
	dfsRecursivePreorder(root.Left)
	dfsRecursivePreorder(root.Right)
}

// recursive
// in-order
func dfsRecursiveInorder(root *TreeNode) {
	if root == nil {
		return
	}
	dfsRecursiveInorder(root.Left)
	fmt.Println(root.Val)
	dfsRecursiveInorder(root.Right)
}

// recursive
// post-order
func dfsRecursivePostorder(root *TreeNode) {
	if root == nil {
		return
	}
	dfsRecursivePostorder(root.Left)
	dfsRecursivePostorder(root.Right)
	fmt.Println(root.Val)
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

	dfs(root)

	dfsRecursivePreorder(root)
	dfsRecursiveInorder(root)
	dfsRecursivePostorder(root)
}
