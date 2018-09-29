package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func searchBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}
	if val > root.Val {
		temp := searchBST(root.Right, val)
		if temp != nil {
			return temp
		}
	} else if val < root.Val {
		temp := searchBST(root.Left, val)
		if temp != nil {
			return temp
		}
	} else {
		return root
	}
	return nil
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
	ans := searchBST(root, 5)
	fmt.Println(ans)
}
