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
}
