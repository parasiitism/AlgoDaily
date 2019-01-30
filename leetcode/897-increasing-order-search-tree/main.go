package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach
	1. dfs all the nodes, and put the node.val into the result tree leaf.right
	Time		O(n)
	Space		O(n) recursion
	32ms beats 100%
*/
func increasingBST(root *TreeNode) *TreeNode {
	dump := &TreeNode{0, nil, root}
	cur := dump
	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		newNode := &TreeNode{node.Val, nil, nil}
		cur.Right = newNode
		cur = cur.Right
		inorder(node.Right)
	}
	inorder(root)
	return dump.Right
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
	a := increasingBST(root)
	fmt.Println(a)
}
