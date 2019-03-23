package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	bfs, iterative

	Time	O(n)
	Space	O(h)
	12ms beats 100%
*/
func averageOfLevels(root *TreeNode) []float64 {
	if root == nil {
		return []float64{}
	}
	var result []float64
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		lengthOnSameLevel := len(queue)
		sum := 0.0
		i := 0
		for ; i < lengthOnSameLevel; i++ {
			head := queue[0]
			queue = queue[1:len(queue)]
			sum += float64(head.Val)
			if head.Left != nil {
				queue = append(queue, head.Left)
			}
			if head.Right != nil {
				queue = append(queue, head.Right)
			}
		}
		avg := sum / float64(i)
		result = append(result, avg)
	}
	return result
}

func main() {

}
