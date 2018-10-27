package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// dfs, iterative
type Stack struct {
	Node  *TreeNode
	Route []int
}

func rightSideView(root *TreeNode) []int {
	result := []int{}
	if root == nil {
		return result
	}
	stack := []*Stack{}
	stack = append(stack, &Stack{root, []int{root.Val}})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		node := pop.Node
		route := pop.Route
		if node.Left == nil && node.Right == nil && len(route) > len(result) {
			result = append(result, route[len(result):]...)
		}
		if node.Left != nil {
			stack = append(stack, &Stack{node.Left, append(route, node.Left.Val)})
		}
		if node.Right != nil {
			stack = append(stack, &Stack{node.Right, append(route, node.Right.Val)})
		}
	}
	return result
}

func main() {
	// 		5
	//	2		8
	// 1 3 7 9
	//10
	root := &TreeNode{5,
		&TreeNode{2,
			&TreeNode{1,
				&TreeNode{10, nil, nil},
				nil,
			},
			&TreeNode{3, nil, nil},
		},
		&TreeNode{8,
			&TreeNode{7, nil, nil},
			&TreeNode{9, nil, nil},
		},
	}
	ans := rightSideView(root)
	fmt.Println(ans)
}
