package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// way of search, iteratively
func insertIntoBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return &TreeNode{val, nil, nil}
	}
	var curr *TreeNode
	curr = root
	for true {
		if val > curr.Val {
			if curr.Right != nil {
				curr = curr.Right
			} else {
				curr.Right = &TreeNode{val, nil, nil}
				break
			}
		} else {
			if curr.Left != nil {
				curr = curr.Left
			} else {
				curr.Left = &TreeNode{val, nil, nil}
				break
			}
		}
	}
	return root
}

// another way:
// unfold the tree into an array,
// construct an binary tree based on the array
// PS1 the tree might be resulted in a different structure
// PS2 too tedious wont implement

func main() {
	// 		4
	//	2		7
	// 1 3
	root := &TreeNode{4,
		&TreeNode{2,
			&TreeNode{1, nil, nil},
			&TreeNode{3, nil, nil},
		},
		&TreeNode{7, nil, nil},
	}
	ans := insertIntoBST(root, 5)
	println(ans.Right.Left.Val)
}
