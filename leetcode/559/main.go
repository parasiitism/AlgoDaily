package main

type NaryNode struct {
	Val      int
	Children []*NaryNode
}

type Stack struct {
	Node  *NaryNode
	Depth int
}

func maxDepth(root *NaryNode) int {
	if root == nil {
		return 0
	}
	result := 0
	var stack []*Stack
	stack = append(stack, &Stack{root, 0})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if pop.Depth > result {
			result = pop.Depth
		}
		for i := 0; i < len(pop.Node.Children); i++ {
			stack = append(stack, &Stack{pop.Node, pop.Depth + 1})
		}
	}
	return result
}

func main() {

}
