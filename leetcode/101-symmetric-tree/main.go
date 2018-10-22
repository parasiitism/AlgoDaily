package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// iterative
func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	var stackA []*TreeNode
	var stackB []*TreeNode
	stackA = append(stackA, root.Left)
	stackB = append(stackB, root.Right)
	// consider nil pointer error, use &&
	for len(stackA) > 0 && len(stackB) > 0 {
		popA := stackA[len(stackA)-1]
		popB := stackB[len(stackB)-1]
		stackA = stackA[0 : len(stackA)-1]
		stackB = stackB[0 : len(stackB)-1]
		// take care of nil pointer error on stack push operations
		if popA != nil && popB != nil {
			if popA.Val != popB.Val {
				return false
			}
			stackA = append(stackA, popA.Left)
			stackA = append(stackA, popA.Right)

			stackB = append(stackB, popB.Right)
			stackB = append(stackB, popB.Left)
		} else {
			// check ni here so that i can write less 'if clause' for the above 4 stack push operations
			if popA == nil && popB != nil || popA != nil && popB == nil {
				return false
			}
		}
	}
	return true
}

func main() {
	// 		1
	//	2		2
	// 3 4 4 4
	root := &TreeNode{1,
		&TreeNode{2,
			&TreeNode{3, nil, nil},
			&TreeNode{4, nil, nil},
		},
		&TreeNode{2,
			&TreeNode{4, nil, nil},
			nil,
		},
	}
	ans := isSymmetric(root)
	fmt.Println(ans)
}
