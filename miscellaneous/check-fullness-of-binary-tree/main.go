package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isFullTree(root *TreeNode) bool {
	if root == nil {
		return true
	}
	stack := []*TreeNode{root}
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if pop.Left != nil && pop.Right != nil {
			stack = append(stack, pop.Left)
			stack = append(stack, pop.Right)
		} else if pop.Left == nil && pop.Right == nil {
			// return false
		} else {
			return false
		}
	}
	return true
}

func main() {
	// 		1
	//	2		3
	// 4 5 6 7
	a := &TreeNode{1,
		&TreeNode{2,
			&TreeNode{4, nil, nil},
			&TreeNode{5, nil, nil},
		},
		&TreeNode{3,
			&TreeNode{6, nil, nil},
			&TreeNode{7, nil, nil},
		},
	}
	fmt.Println(isFullTree(a))

	// 		1
	//	2		3
	// 4 5
	a = &TreeNode{1,
		&TreeNode{2,
			&TreeNode{4, nil, nil},
			&TreeNode{5, nil, nil},
		},
		&TreeNode{3, nil, nil},
	}
	fmt.Println(isFullTree(a))

	// 		1
	//	2		3
	// 4 5 6
	a = &TreeNode{1,
		&TreeNode{2,
			&TreeNode{4, nil, nil},
			&TreeNode{5, nil, nil},
		},
		&TreeNode{3,
			&TreeNode{6, nil, nil},
			nil,
		},
	}
	fmt.Println(isFullTree(a))
}
