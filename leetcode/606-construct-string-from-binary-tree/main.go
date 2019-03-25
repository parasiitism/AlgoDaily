package main

import (
	"fmt"
	"strconv"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	followup: leetcode 606
*/

func tree2str(t *TreeNode) string {
	if t == nil {
		return ""
	}
	val := strconv.Itoa(t.Val)
	left := tree2str(t.Left)
	right := tree2str(t.Right)
	if left == "" && right == "" {
		return val
	} else if right == "" {
		return val + "(" + left + ")"
	} else if left == "" {
		return val + "()(" + right + ")"
	} else {
		return val + "(" + left + ")(" + right + ")"
	}
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
	ans := tree2str(root)
	fmt.Println(ans)
	// 		5
	//	2		8
	// n 3 7	n
	root = &TreeNode{5,
		&TreeNode{2,
			nil,
			&TreeNode{3, nil, nil},
		},
		&TreeNode{8,
			&TreeNode{7, nil, nil},
			nil,
		},
	}
	ans = tree2str(root)
	fmt.Println(ans)
}
