package main

import (
	"fmt"
	"math"
)

/*
	Questions to ask:
	- what if there are duplicate node.vals?
	- what if the integraer range of node.val? -2^32 -> 2^32-1 ?
*/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach:
	- for each node, check if the subtree is a valid BST
	Time		O(n^2)
	Space		O(h)
	12ms beats 100%
*/
func largestBSTSubtree(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		isValid, cnt := isValidBST(pop, math.MinInt64, math.MaxInt64)
		if isValid && cnt > res {
			res = cnt
		}
		if pop.Left != nil {
			stack = append(stack, pop.Left)
		}
		if pop.Right != nil {
			stack = append(stack, pop.Right)
		}
	}
	return res
}

func isValidBST(node *TreeNode, min, max int) (bool, int) {
	if node == nil {
		return true, 0
	}
	if node.Val <= min || node.Val >= max {
		return false, 0
	}
	left, leftCnt := isValidBST(node.Left, min, node.Val)
	right, rightCnt := isValidBST(node.Right, node.Val, max)
	return left && right, leftCnt + rightCnt + 1
}

func main() {
	// 		10
	//	5		15
	// 1 8 6 7
	root := &TreeNode{10,
		&TreeNode{5,
			&TreeNode{1, nil, nil},
			&TreeNode{8, nil, nil},
		},
		&TreeNode{15,
			&TreeNode{6, nil, nil},
			&TreeNode{7, nil, nil},
		},
	}
	fmt.Println(largestBSTSubtree(root))
}
