package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	return treeHeight(root) != -1
}

/*
	a tree is balanced if 2 of its subtreees are balanced
	for every subtree
	if treeHeight() == -1, then this is unbalanced
*/
func treeHeight(node *TreeNode) int {
	if node == nil {
		return 0
	}
	h_left := treeHeight(node.Left)
	h_right := treeHeight(node.Right)

	// just report "unbalanced" to parent that if any one of the subtrees is unbalanced
	if h_left == -1 || h_right == -1 {
		return -1
	}

	// if the height diff is > 1, then this subtree is unbalanced
	if h_left-h_right > 1 || h_right-h_left > 1 {
		return -1
	}

	// height increment on the greater
	if h_left > h_right {
		return h_left + 1
	}
	return h_right + 1
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
	ans := isBalanced(root)
	fmt.Println(ans)
}
