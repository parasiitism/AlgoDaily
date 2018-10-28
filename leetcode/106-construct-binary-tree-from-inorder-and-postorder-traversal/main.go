package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// recursive
func buildTree(inorder []int, postorder []int) *TreeNode {
	if len(inorder) == 0 || len(postorder) == 0 {
		return nil
	}
	root_val := postorder[len(postorder)-1]
	root := &TreeNode{root_val, nil, nil}
	left_in := []int{}
	left_post := []int{}
	right_in := []int{}
	right_post := []int{}
	for i := 0; i < len(inorder); i++ {
		if inorder[i] == root_val {
			left_in = inorder[:i]
			left_post = postorder[:i]
			if i+1 < len(inorder) {
				right_in = inorder[i+1:]
				right_post = postorder[i : len(postorder)-1]
			}
		}
	}
	root.Left = buildTree(left_in, left_post)
	root.Right = buildTree(right_in, right_post)
	return root
}

func main() {
	// no test
	// cos i just got passed against the online judge without further modication
}
