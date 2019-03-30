package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach:
	- store the nodes' values
	- add the values back to the linked list

	Time    O(2n)
	Space   O(n)
	4 ms, faster than 100.00%
*/

func flatten(root *TreeNode) {
	nums := []int{}
	var preOrder func(node *TreeNode)
	preOrder = func(node *TreeNode) {
		if node == nil {
			return
		}
		nums = append(nums, node.Val)
		preOrder(node.Left)
		preOrder(node.Right)
	}
	preOrder(root)
	cur := root
	for i, num := range nums {
		cur.Val = num
		cur.Left = nil
		if i+1 < len(nums) {
			cur.Right = &TreeNode{}
		} else {
			cur.Right = nil
		}
		cur = cur.Right
	}
}

func main() {

}
