package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// dfs, iterative

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

// dfs, recursive

func maxDepth1(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := maxDepth1(root.Left)
	right := maxDepth1(root.Right)
	if left > right {
		return left + 1
	}
	return right + 1
}

// bfs, iterative

type Queue struct {
	Node  *TreeNode
	Depth int
}

func maxDepth2(root *TreeNode) int {
	if root == nil {
		return 0
	}
	maxDepth := 0
	var queue []*Queue
	queue = append(queue, &Queue{root, 1})
	for len(queue) > 0 {
		n := len(queue)
		for i := 0; i < n; i++ {
			head := queue[0]
			queue = queue[1:len(queue)]
			if head.Depth > maxDepth {
				maxDepth = head.Depth
			}
			if head.Node.Left != nil {
				queue = append(queue, &Queue{head.Node.Left, head.Depth + 1})
			}
			if head.Node.Right != nil {
				queue = append(queue, &Queue{head.Node.Right, head.Depth + 1})
			}
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
	ans = maxDepth1(root)
	fmt.Println(ans)
	ans = maxDepth2(root)
	fmt.Println(ans)
}
