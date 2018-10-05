package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// breadth first search
// iterative
func bfs(root *TreeNode) {
	var queue []*TreeNode
	queue = append(queue, root)
	for len(queue) > 0 {
		n := len(queue)
		for i := 0; i < n; i++ {
			head := queue[0]
			queue = queue[1:]
			fmt.Println(head.Val)
			if head.Left != nil {
				queue = append(queue, head.Left)
			}
			if head.Right != nil {
				queue = append(queue, head.Right)
			}
		}
	}
}

func main() {
	// 		1
	//	2		3
	// 4 5 6 7
	root := &TreeNode{1,
		&TreeNode{2,
			&TreeNode{4, nil, nil},
			&TreeNode{5, nil, nil},
		},
		&TreeNode{3,
			&TreeNode{6, nil, nil},
			&TreeNode{7, nil, nil},
		},
	}
	// print 1234567
	bfs(root)
}
