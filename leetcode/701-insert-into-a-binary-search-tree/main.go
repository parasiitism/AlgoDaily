package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// iterative search
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

// recursive search
func insertIntoBST1(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return &TreeNode{val, nil, nil}
	}
	var recursion func(curr *TreeNode)
	recursion = func(curr *TreeNode) {
		if val > curr.Val {
			if curr.Right != nil {
				recursion(curr.Right)
			} else {
				curr.Right = &TreeNode{val, nil, nil}
			}
		} else {
			if curr.Left != nil {
				recursion(curr.Left)
			} else {
				curr.Left = &TreeNode{val, nil, nil}
			}
		}
	}
	recursion(root)
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
	ans := insertIntoBST1(root, 5)
	println(ans.Right.Left.Val)
}
