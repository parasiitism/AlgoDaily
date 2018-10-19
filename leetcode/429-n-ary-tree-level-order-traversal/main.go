package main

type NaryNode struct {
	Val      int
	Children []*NaryNode
}

// bfs, iterative
func levelOrder(root *NaryNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	var result [][]int
	queue := []*NaryNode{root}
	for len(queue) > 0 {
		lengthOnSameLevel := len(queue)
		nodesOnSameLevel := []int{}
		for i := 0; i < lengthOnSameLevel; i++ {
			head := queue[0]
			queue = queue[1:len(queue)]
			nodesOnSameLevel = append(nodesOnSameLevel, head.Val)
			for j := 0; j < len(head.Children); j++ {
				if head.Children[j] != nil {
					queue = append(queue, head.Children[j])
				}
			}
		}
		result = append(result, nodesOnSameLevel)
	}
	return result
}

func main() {

}
