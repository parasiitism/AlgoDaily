package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach
	- delete the leafs(and put the leafs to the result) until the node becomes empty
	Time	O(h*n)
	Space	O(h)
	0ms beats 100%
	30jan2019
*/
func findLeaves(root *TreeNode) [][]int {
	dumpHead := &TreeNode{0, root, nil}

	res := [][]int{}
	temp := []int{}

	var dfs func(node *TreeNode, parent *TreeNode, isLeft bool)
	dfs = func(node *TreeNode, parent *TreeNode, isLeft bool) {
		if node == nil {
			return
		}
		if node.Left == nil && node.Right == nil {
			temp = append(temp, node.Val)
			if isLeft {
				parent.Left = nil
			} else {
				parent.Right = nil
			}
		}
		dfs(node.Left, node, true)
		dfs(node.Right, node, false)
	}

	for dumpHead.Left != nil {
		dfs(dumpHead.Left, dumpHead, true)
		res = append(res, temp)
		temp = []int{}
	}
	return res
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
	fmt.Println(findLeaves(root))

	// 			  1
	//	  2			 3
	// 4   5 		8
	//6 7
	root = &TreeNode{1,
		&TreeNode{2,
			&TreeNode{4,
				&TreeNode{6, nil, nil},
				&TreeNode{7, nil, nil},
			},
			&TreeNode{5, nil, nil},
		},
		&TreeNode{3,
			&TreeNode{8, nil, nil},
			nil,
		},
	}
	fmt.Println(findLeaves(root))
}
