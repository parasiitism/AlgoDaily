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
// this is also the way that transforms a BST to an sorted array
func InorderRecursive(root *TreeNode) {
	if root.Left != nil {
		InorderRecursive(root.Left)
	}
	fmt.Println(root.Val)
	if root.Right != nil {
		InorderRecursive(root.Right)
	}
}

// iterative in-order traversal on BST
// this is also the way that transforms a BST to an sorted array
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

// pre-order traversal on BST
func PreorderRecursive(root *TreeNode) {
	fmt.Println(root.Val)
	if root.Left != nil {
		PreorderRecursive(root.Left)
	}
	if root.Right != nil {
		PreorderRecursive(root.Right)
	}
}

// post-order traversal on BST
func PostorderRecursive(root *TreeNode) {
	if root.Left != nil {
		PostorderRecursive(root.Left)
	}
	if root.Right != nil {
		PostorderRecursive(root.Right)
	}
	fmt.Println(root.Val)
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
	InorderRecursive(root)
	fmt.Println(",")
	InorderIterative(root)
	fmt.Println(",")
	PreorderRecursive(root)
	fmt.Println(",")
	PostorderRecursive(root)
}
