package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func constructFromPrePost(pre []int, post []int) *TreeNode {
	if len(pre) == 0 || len(post) == 0 {
		return nil
	}
	node := &TreeNode{pre[0], nil, nil}
	if len(pre) == 1 || len(post) == 1 {
		return node
	}
	left_node_val := pre[1]
	left_pre := []int{}
	left_post := []int{}
	right_pre := []int{}
	right_post := []int{}
	for i := 0; i < len(post); i++ {
		if post[i] == left_node_val {
			left_pre = pre[1 : i+2]
			left_post = post[:i+1]
			if i+2 < len(pre) {
				right_pre = pre[i+2:]
				right_post = post[i+1 : len(post)-1]
			}
		}
	}
	node.Left = constructFromPrePost(left_pre, left_post)
	node.Right = constructFromPrePost(right_pre, right_post)
	return node
}

func main() {
}
