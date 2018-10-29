package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(inorder) == 0 || len(preorder) == 0 {
		return nil
	}
	root_val := preorder[0]
	root := &TreeNode{root_val, nil, nil}
	left_in := []int{}
	left_pre := []int{}
	right_in := []int{}
	right_pre := []int{}
	for i := 0; i < len(inorder); i++ {
		if inorder[i] == root_val {
			left_in = inorder[:i]
			left_pre = preorder[1 : i+1]
			if i+1 < len(inorder) {
				right_in = inorder[i+1:]
				right_pre = preorder[i+1:]
			}
		}
	}
	root.Left = buildTree(left_pre, left_in)
	root.Right = buildTree(right_pre, right_in)
	return root
}

func main() {
	// no test
	// cos i just got passed against the online judge without further modication
}
