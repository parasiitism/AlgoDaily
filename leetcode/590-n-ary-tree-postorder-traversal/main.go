// leetcode doesn't support go submission, i did this in python

package main

type NaryNode struct {
	Val      int
	Children []*NaryNode
}

// recursive
func postorder(root *NaryNode) []int {
	if root == nil {
		return []int{}
	}
	var result = []int{}
	for i := 0; i < len(root.Children); i++ {
		result = append(result, postorder(root.Children[i])...)
	}
	result = append(result, root.Val)
	return result
}

// i am too lazy, read main.py for the iterative one

func main() {

}
