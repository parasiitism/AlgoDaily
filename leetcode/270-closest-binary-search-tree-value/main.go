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

// depth first search O(n)
// This a not a good way to do dfs cos it is nested
func closestValue(root *TreeNode, target float64) int {
	closest := root.Val
	var dfs func(cur *TreeNode)
	dfs = func(cur *TreeNode) {
		diff := math.Abs(target - float64(closest))
		cur_diff := math.Abs(target - float64(cur.Val))
		if cur_diff < diff {
			closest = cur.Val
		}
		if cur.Left != nil {
			dfs(cur.Left)
		}
		if cur.Right != nil {
			dfs(cur.Right)
		}
	}

	dfs(root)

	return closest
}

func main() {
	root := &TreeNode{4,
		&TreeNode{2,
			&TreeNode{1, nil, nil},
			&TreeNode{3, nil, nil},
		},
		&TreeNode{5, nil, nil},
	}
	ans := closestValue(root, -2.1)
	fmt.Println(ans)

	root = &TreeNode{4,
		&TreeNode{2,
			&TreeNode{1, nil, nil},
			nil,
		},
		&TreeNode{5, nil, nil},
	}
	ans = closestValue(root, 1.1)
	fmt.Println(ans)
}
