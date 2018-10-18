package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// bfs, iterative
func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	var result [][]int
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		lengthOnSameLevel := len(queue)
		nodesOnSameLevel := []int{}
		for i := 0; i < lengthOnSameLevel; i++ {
			head := queue[0]
			queue = queue[1:len(queue)]
			nodesOnSameLevel = append(nodesOnSameLevel, head.Val)
			if head.Left != nil {
				queue = append(queue, head.Left)
			}
			if head.Right != nil {
				queue = append(queue, head.Right)
			}
		}
		result = append(result, nodesOnSameLevel)
	}
	return result
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
	ans := levelOrder(root)
	fmt.Println(ans)
}
