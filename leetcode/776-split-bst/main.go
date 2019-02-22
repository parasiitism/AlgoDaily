package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	this question is super hard
	i gave up an read the ans
	- https://leetcode.com/articles/split-bst
	- https://leetcode.com/problems/split-bst/discuss/159985/Python-DFS-tm

	the basic idea is to split the node into 2 subtree
	1. if target < curNode, split left subtree of the curNode, and reassign the curNode's left subtree
	2. else, split the right subtree of the curNode, and reassign the curNode's right subtree
*/
func splitBST(root *TreeNode, V int) []*TreeNode {
	if root == nil {
		return []*TreeNode{nil, nil}
	}
	if V < root.Val {
		// go to left and split left subtree
		temp := splitBST(root.Left, V)
		root.Left = temp[1]
		// the left and new root
		return []*TreeNode{temp[0], root}
	} else {
		// go to left and split left subtree
		temp := splitBST(root.Right, V)
		root.Right = temp[0]
		// the left and new root
		return []*TreeNode{root, temp[1]}
	}
}

// helper
func InorderRecursive(root *TreeNode) {
	if root == nil {
		return
	}
	InorderRecursive(root.Left)
	fmt.Print(root.Val)
	InorderRecursive(root.Right)
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
	ans := splitBST(root, 5)
	InorderRecursive(ans[0])
	fmt.Println("---")
	InorderRecursive(ans[1])
}
