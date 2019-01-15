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

/*
	Given a BST, return the invalid node if there is any.
	- assume there is only almost 1 invalid node
	- "valid" is defined as min < node.val < max
	- there will be duplicate numbers
*/

/*
	1st approach: similar to leetcode 98
	Time		O(n)
	Space		O(n) callstack
*/
func findInvalidNodeInBST(root *TreeNode) *TreeNode {
	var dfs func(node *TreeNode, min int, max int) *TreeNode
	dfs = func(node *TreeNode, min int, max int) *TreeNode {
		if node == nil {
			return nil
		}
		if node.Val <= min || node.Val >= max {
			return node
		}
		left := dfs(node.Left, min, node.Val)
		right := dfs(node.Right, node.Val, max)
		if left != nil {
			return left
		}
		if right != nil {
			return right
		}
		return nil
	}
	return dfs(root, math.MinInt64, math.MaxInt64)
}

func main() {
	// 			3
	//		1		4
	// 0	 2
	root := &TreeNode{3,
		&TreeNode{1,
			&TreeNode{0,
				nil,
				nil,
			},
			&TreeNode{2,
				nil,
				nil,
			},
		},
		&TreeNode{4, nil, nil},
	}
	fmt.Println(findInvalidNodeInBST(root))

	// 			3
	//		1		4
	// 0	 2 7 5
	root = &TreeNode{3,
		&TreeNode{1,
			&TreeNode{0,
				nil,
				nil,
			},
			&TreeNode{2,
				nil,
				nil,
			},
		},
		&TreeNode{4,
			&TreeNode{7,
				nil,
				nil,
			},
			&TreeNode{5,
				nil,
				nil,
			},
		},
	}
	fmt.Println(findInvalidNodeInBST(root))
}
