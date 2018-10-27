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
		// put left child to the stack first, since we want to read right child in the next iteration
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

// recursive
func rightSideView1(root *TreeNode) []int {
	result := []int{}
	if root == nil {
		return result
	}
	var dfs func(root *TreeNode, route []int)
	dfs = func(root *TreeNode, route []int) {
		if root != nil {
			if root.Left == nil && root.Right == nil && len(route) > len(result) {
				result = append(result, route[len(result):]...)
			}
			// put right child first, since we want the right first
			if root.Right != nil {
				dfs(root.Right, append(route, root.Right.Val))
			}
			if root.Left != nil {
				dfs(root.Left, append(route, root.Left.Val))
			}
		}
	}
	dfs(root, []int{root.Val})
	return result
}

func main() {
	// 		5
	//	2		8
	// 1 3 7
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
			nil,
		},
	}
	ans := rightSideView(root)
	fmt.Println(ans)
	ans = rightSideView1(root)
	fmt.Println(ans)
}
