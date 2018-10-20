package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// iterative

type Stack struct {
	Node  *TreeNode
	Depth int
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	maxDepth := 0
	var stack []*Stack
	stack = append(stack, &Stack{root, 1})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[0 : len(stack)-1]
		if pop.Depth > maxDepth {
			maxDepth = pop.Depth
		}
		if pop.Node.Left != nil {
			stack = append(stack, &Stack{pop.Node.Left, pop.Depth + 1})
		}
		if pop.Node.Right != nil {
			stack = append(stack, &Stack{pop.Node.Right, pop.Depth + 1})
		}
	}
	return maxDepth
}

func main() {
	// 		5
	//	2		8
	// 1 3 7 9
	//				10
	root := &TreeNode{5,
		&TreeNode{2,
			&TreeNode{1, nil, nil},
			&TreeNode{3, nil, nil},
		},
		&TreeNode{8,
			&TreeNode{7, nil, nil},
			&TreeNode{9,
				nil,
				&TreeNode{10, nil, nil},
			},
		},
	}
	ans := maxDepth(root)
	fmt.Println(ans)
}
