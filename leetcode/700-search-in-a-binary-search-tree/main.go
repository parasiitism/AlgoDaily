package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: recursive bst dfs

	Time	O(h)
	Space	O(h)
	36 ms, faster than 31.62%
*/
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

/*
	2nd approach: iterative bst dfs

	Time	O(h)
	Space	O(1)
	24 ms, faster than 100.00%
*/
func searchBST1(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}
	cur := root
	for cur != nil {
		if val > cur.Val {
			cur = cur.Right
		} else if val < cur.Val {
			cur = cur.Left
		} else {
			return cur
		}
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
	ans := searchBST1(root, 8)
	fmt.Println(ans)
}
