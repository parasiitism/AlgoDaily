package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// dfs, iterative
type Stack struct {
	Node    *TreeNode
	current int
}

func hasPathSum(root *TreeNode, sum int) bool {
	if root == nil {
		return false
	}
	var stack []*Stack
	stack = append(stack, &Stack{root, root.Val})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[0 : len(stack)-1]
		node := pop.Node
		current := pop.current
		// keep in mind that it is legit only when it adds up to the leafs
		if node.Left == nil && node.Right == nil && sum-current == 0 {
			return true
		}
		if node.Left != nil {
			stack = append(stack, &Stack{node.Left, current + node.Left.Val})
		}
		if node.Right != nil {
			stack = append(stack, &Stack{node.Right, current + node.Right.Val})
		}
	}
	return false
}

func main() {
	// 		1
	//	2		2
	// 3 4 4 3
	root := &TreeNode{1,
		&TreeNode{2,
			&TreeNode{3, nil, nil},
			&TreeNode{4, nil, nil},
		},
		&TreeNode{2,
			&TreeNode{4, nil, nil},
			&TreeNode{3, nil, nil},
		},
	}
	ans := hasPathSum(root, 7)
	fmt.Println(ans)
	// 		1
	// 2
	root = &TreeNode{1,
		&TreeNode{2, nil, nil},
		nil,
	}
	ans = hasPathSum(root, 1)
	fmt.Println(ans)
}
