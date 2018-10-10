package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}
	nadir := math.MaxInt64
	peak := 0
	fmt.Println(nadir, peak)
	var dfs func(node *TreeNode, floor int)
	dfs = func(node *TreeNode, floor int) {
		if node.Left == nil && node.Right == nil {
			// leaf
			if floor < nadir {
				nadir = floor
			} else if floor > peak {
				peak = floor
			}
		}
		if node.Left != nil {
			dfs(node.Left, floor+1)
		}
		if node.Right != nil {
			dfs(node.Right, floor+1)
		}
	}
	dfs(root, 1)
	fmt.Println(nadir, peak)
	return peak-nadir < 2
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
