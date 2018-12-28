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
	fmt.Print(root.Val)
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
		fmt.Print(pop.Val)
		curr = pop.Right
	}
}

// pre-order traversal on BST
func PreorderRecursive(root *TreeNode) {
	fmt.Print(root.Val)
	if root.Left != nil {
		PreorderRecursive(root.Left)
	}
	if root.Right != nil {
		PreorderRecursive(root.Right)
	}
}

func PreorderIterative(root *TreeNode) {
	stack := []*TreeNode{}
	stack = append(stack, root)
	for len(stack) > 0 {
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		fmt.Print(top.Val)
		if top.Right != nil {
			stack = append(stack, top.Right)
		}
		if top.Left != nil {
			stack = append(stack, top.Left)
		}
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
	fmt.Print(root.Val)
}

func PostorderIterative(root *TreeNode) {
	stack := []*TreeNode{}
	stack = append(stack, root)
	arr := []*TreeNode{}
	for len(stack) > 0 {
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		arr = append(arr, top)
		if top.Left != nil {
			stack = append(stack, top.Left)
		}
		if top.Right != nil {
			stack = append(stack, top.Right)
		}
	}
	for i := len(arr) - 1; i >= 0; i-- {
		fmt.Print(arr[i].Val)
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
	// in order
	InorderRecursive(root)
	fmt.Println(",")
	InorderIterative(root)
	fmt.Println(",")
	// pre order
	PreorderRecursive(root)
	fmt.Println(",")
	PreorderIterative(root)
	fmt.Println(",")
	// post order
	PostorderRecursive(root)
	fmt.Println(",")
	PostorderIterative(root)
	fmt.Println(",")
}
