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

/*
	2nd approach: recursion
	- basically we save the item in an post-order sequence
	- and then append the prev item to the right child and set left child as null
	- recursively
	- see idea.jpeg

	learned from others:
	- https://www.youtube.com/watch?v=NHdrzNpt1ZI
	- https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/My-short-post-order-traversal-Java-solution-for-share

	Time    O(n)
	Space   O(n)
	4 ms, faster than 100.00%
*/
func flatten1(root *TreeNode) {
	var prev *TreeNode
	var helper func(node *TreeNode)
	helper = func(node *TreeNode) {
		if node == nil {
			return
		}
		helper(node.Right)
		helper(node.Left)
		node.Right = prev
		node.Left = nil
		prev = node
	}
	helper(root)
}

func main() {

}
