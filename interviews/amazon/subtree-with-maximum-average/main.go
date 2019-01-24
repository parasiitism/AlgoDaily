package main

type NaryNode struct {
	Val      int
	Children []*NaryNode
}

func findMaxAverageSubtree(root *NaryNode) *NaryNode {
	maxAvr := 0.0
	var res *NaryNode
	var dfs func(node *NaryNode)
	dfs = func(node *NaryNode) {
		acc := 0
		for _, child := range node.Children {
			acc += child.Val
		}
		if len(node.Children) > 0 {
			avr := float64(acc) / float64(len(node.Children))
			if avr > maxAvr {
				maxAvr = avr
				res = node
			}
		}
		for _, child := range node.Children {
			dfs(child)
		}

	}
	dfs(root)
	return res
}

func main() {

}
