package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach
	- convert bst into a sorted array
	- the min diff is actually the min diff between 2 adjacent elements
	Time	O(2n)
	Space O(n)
*/
func getMinimumDifference(root *TreeNode) int {
	arr := []int{}
	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		arr = append(arr, node.Val)
		inorder(node.Right)
	}
	inorder(root)
	min := math.MaxInt64
	for i := 0; i < len(arr)-1; i++ {
		if arr[i+1]-arr[i] < min {
			min = arr[i+1] - arr[i]
		}
	}
	return min
}

func main() {
	// 			7
	//		3		11
	// 0	 6 8  15
	root := &TreeNode{7,
		&TreeNode{3,
			&TreeNode{0,
				nil,
				nil,
			},
			&TreeNode{6,
				nil,
				nil,
			},
		},
		&TreeNode{11,
			&TreeNode{8,
				nil,
				nil,
			},
			&TreeNode{15,
				nil,
				nil,
			},
		},
	}
	fmt.Println(getMinimumDifference(root))
}
