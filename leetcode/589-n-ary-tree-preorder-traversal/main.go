// leetcode doesn't support go submission, i did this in python

package main

type NaryNode struct {
	Val      int
	Children []*NaryNode
}

// iterative
func preorder(root *NaryNode) []int {
	if root == nil {
		return []int{}
	}
	var result []int
	var stack []*NaryNode
	stack = append(stack, root)
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, pop.Val)
		for i := len(pop.Children) - 1; i >= 0; i-- {
			stack = append(stack, pop.Children[i])
		}
	}
	return result
}

// i am too lazy, read .py for the recursive one

func main() {

}
