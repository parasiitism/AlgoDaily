package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// recursive
func postorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var result = []int{}
	if root.Left != nil {
		result = append(result, postorderTraversal(root.Left)...)
	}
	if root.Right != nil {
		result = append(result, postorderTraversal(root.Right)...)
	}
	result = append(result, root.Val)
	return result
}

// iterative
// this is so tricky:
// reverse the pre-order traversal
func postorderTraversal1(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var stack []*TreeNode
	stack = append(stack, root)
	var result = []int{}
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		// reverse the result, add new item to its head, e.g. index=0
		result = append([]int{pop.Val}, result...)
		// left and then right
		// reminder: pre-order goes right and then left
		if pop.Left != nil {
			stack = append(stack, pop.Left)
		}
		if pop.Right != nil {
			stack = append(stack, pop.Right)
		}
	}
	return result
}

func main() {

}
