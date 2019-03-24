package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: recursion
	- if a node is within the range, return it and REMEMBER to reset its left and right if necessary

	Time		O(n)
	Space		O(h)
	12 ms, faster than 100.00%
*/
func trimBST(root *TreeNode, L int, R int) *TreeNode {
	if root == nil {
		return nil
	}
	mid := L <= root.Val && root.Val <= R
	left := trimBST(root.Left, L, R)
	right := trimBST(root.Right, L, R)
	if left != nil && right != nil {
		root.Left = left
		root.Right = right
		return root
	} else if left != nil {
		if mid {
			root.Left = left
			root.Right = nil
			return root
		}
		return left
	} else if right != nil {
		if mid {
			root.Left = nil
			root.Right = right
			return root
		}
		return right
	}
	if mid {
		root.Left = nil
		root.Right = nil
		return root
	}
	return nil
}

/*
	2nd approach: optimize the 1st

	Time		O(n)
	Space		O(h)
	12 ms, faster than 100.00%
*/
func trimBST1(root *TreeNode, L int, R int) *TreeNode {
	if root == nil {
		return nil
	}
	left := trimBST(root.Left, L, R)
	right := trimBST(root.Right, L, R)
	if L <= root.Val && root.Val <= R {
		root.Left = left
		root.Right = right
		return root
	}
	if left != nil {
		return left
	}
	return right
}

// helpers
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
	// 			  3
	//	  0			 4
	// 	   	2
	//		 1
	root := &TreeNode{3,
		&TreeNode{0,
			nil,
			&TreeNode{2,
				&TreeNode{1, nil, nil},
				nil,
			},
		},
		&TreeNode{4, nil, nil},
	}
	ans := trimBST1(root, 1, 3)
	fmt.Println(levelOrder(ans))

	// 			  3
	//	  1			 4
	// 	   	2
	root = &TreeNode{3,
		&TreeNode{1,
			nil,
			&TreeNode{2, nil, nil},
		},
		&TreeNode{4, nil, nil},
	}
	ans = trimBST1(root, 2, 12)
	fmt.Println(levelOrder(ans))
}
