package main

import (
	"math"
	"sort"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: inorder+sort
	- actually the inorder traversal of a BST is suppoed to be a sorted list of a valid
	1. so we can just get the inorder list
	2. clone the list and sort it, then compare with the inorder list we get from the inroder traversal to get that 2 nodes
	3. traverse again the tree, coorect that 2 nodes

	Time	O(nlogn+2n)
	Space	O(n)
	24 ms, faster than 70.21%
*/
func recoverTree(root *TreeNode) {
	if root == nil {
		return
	}
	// get the in order traversal list, it is supposed to be a sorted list
	arr := InorderRecursive(root)
	// clone
	clone := make([]int, len(arr))
	sort.Ints(clone)
	// check diff
	a := math.MinInt64
	b := math.MinInt64
	for i := 0; i < len(arr); i++ {
		if clone[i] != arr[i] {
			a = arr[i]
			b = clone[i]
			break
		}
	}
	// swap the node val
	stack := []*TreeNode{}
	stack = append(stack, root)
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if pop.Val == a {
			pop.Val = b
		} else if pop.Val == b {
			pop.Val = a
		}
		if pop.Left != nil {
			stack = append(stack, pop.Left)
		}
		if pop.Right != nil {
			stack = append(stack, pop.Right)
		}
	}
}

func InorderRecursive(root *TreeNode) []int {
	arr := []int{}
	if root.Left != nil {
		left := InorderRecursive(root.Left)
		arr = append(arr, left...)
	}
	arr = append(arr, root.Val)
	if root.Right != nil {
		right := InorderRecursive(root.Right)
		arr = append(arr, right...)
	}
	return arr
}

/*
	2nd approach: inorder
	- actually the inorder traversal of a BST is suppoed to be a sorted list of a valid
	- so in the traversal, if the prev node >= current node, we found the swap nodes

	learned from others
	- https://www.youtube.com/watch?v=2rsGbHnIDV0

	Time	O(n)
	Space	O(n)
	20 ms, faster than 100.00%
*/
func recoverTree1(root *TreeNode) {
	if root == nil {
		return
	}
	var a *TreeNode
	var b *TreeNode
	var prev *TreeNode

	// 1,2,3,4,5,6,7
	// 1,7,3,4,5,6,2
	//	 ^ ^     ^ ^ there are 2 times that prev>=curr
	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		if prev != nil && prev.Val >= node.Val {
			if a == nil {
				a = prev
			}
			b = node
		}
		prev = node
		inorder(node.Right)
	}
	inorder(root)

	a.Val, b.Val = b.Val, a.Val
}

func main() {

}
