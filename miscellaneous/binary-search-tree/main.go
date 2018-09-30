package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// recursive in-order traversal on BST
func BST2SortedArray(root *TreeNode) {
	if root.Left != nil {
		BST2SortedArray(root.Left)
	}
	fmt.Println(root.Val)
	if root.Right != nil {
		BST2SortedArray(root.Right)
	}
}

// iterative in-order traversal on BST
func InorderIterative(root *TreeNode) {
	var stack []*TreeNode
	curr := root
	for curr != nil || len(stack) > 0 {
		// all the way down to the left most leaf
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}
		// pop the item from the stack
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		// do something on the popped node
		fmt.Println(pop.Val)
		// take the nearest right sibling then iterate again
		if pop.Right != nil {
			stack = append(stack, pop.Right)
		}
	}
}

func main() {
	// 		5
	//	2		8
	// 1 3 7 9
	root := &TreeNode{5,
		&TreeNode{2,
			&TreeNode{1, nil, nil},
			&TreeNode{3, nil, nil},
		},
		&TreeNode{8,
			&TreeNode{7, nil, nil},
			&TreeNode{9, nil, nil},
		},
	}
	BST2SortedArray(root)
	fmt.Println(",")
	InorderIterative(root)
}
