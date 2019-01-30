package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach
	- recursive dfs + prefix sum
	Time	O(n)
	Space	O(h) call stack
	0ms beats 100%
	30jan2019
*/
func sumNumbers(root *TreeNode) int {
	res := 0
	var dfs func(node *TreeNode, sum int)
	dfs = func(node *TreeNode, sum int) {
		if node == nil {
			return
		}
		sum = sum*10 + node.Val
		if node.Left == nil && node.Right == nil {
			res += sum
		}
		dfs(node.Left, sum)
		dfs(node.Right, sum)
	}
	dfs(root, 0)
	return res
}

/*
	2nd approach
	- iterative dfs + prefix sum
	Time	O(n)
	Space	O(h*length of children) the stack
	0ms beats 100%
	30jan2019
*/
func sumNumbers1(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	var stack []*Item
	stack = append(stack, &Item{root, 0})
	for len(stack) > 0 {
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		sum := top.Sum*10 + top.Node.Val
		if top.Node.Left == nil && top.Node.Right == nil {
			res += sum
		}
		if top.Node.Left != nil {
			stack = append(stack, &Item{top.Node.Left, sum})
		}
		if top.Node.Right != nil {
			stack = append(stack, &Item{top.Node.Right, sum})
		}
	}
	return res
}

type Item struct {
	Node *TreeNode
	Sum  int
}

func main() {
	// 		1
	//	2		3
	// 4 5
	root := &TreeNode{1,
		&TreeNode{2,
			&TreeNode{4, nil, nil},
			&TreeNode{5, nil, nil},
		},
		&TreeNode{3,
			nil,
			nil,
		},
	}
	fmt.Println(sumNumbers1(root))
}
