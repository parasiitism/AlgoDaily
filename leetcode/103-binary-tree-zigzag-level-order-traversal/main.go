package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: bfs
	- classic level order traversal

	Time	O(n)
	Space	O(2w) put the nodes into the queue level by level,
	0 ms, faster than 100.00%
*/
func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	res := [][]int{}
	queue := []*TreeNode{root}
	levelCount := 0
	for len(queue) > 0 {
		n := len(queue)
		temp := []int{}
		for i := 0; i < n; i++ {
			head := queue[0]
			queue = queue[1:]

			if levelCount%2 == 0 {
				temp = append(temp, head.Val)
			} else {
				temp = append([]int{head.Val}, temp...)
			}

			if head.Left != nil {
				queue = append(queue, head.Left)
			}
			if head.Right != nil {
				queue = append(queue, head.Right)
			}
		}
		res = append(res, temp)
		levelCount++
	}
	return res
}

func main() {

}
