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

func treeHeight(node *TreeNode) int {
	if node == nil {
		return 0
	}
	h_left := treeHeight(node.Left)
	h_right := treeHeight(node.Right)

	if h_left == -1 || h_right == -1 {
		return -1
	}

	if h_left-h_right > 1 || h_right-h_left > 1 {
		return -1
	}

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
