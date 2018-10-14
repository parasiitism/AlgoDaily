package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// iterative
func preorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var result []int
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, pop.Val)
		if pop.Right != nil {
			stack = append(stack, pop.Right)
		}
		if pop.Left != nil {
			stack = append(stack, pop.Left)
		}
	}
	return result
}

// recursive
func preorderTraversal1(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	result := []int{root.Val}
	if root.Left != nil {
		result = append(result, preorderTraversal1(root.Left)...)
	}
	if root.Right != nil {
		result = append(result, preorderTraversal1(root.Right)...)
	}
	return result
}

func main() {

}
