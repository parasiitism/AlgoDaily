package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Cnt   int
	Left  *TreeNode
	Right *TreeNode
}

type KthLargest struct {
	Bst *TreeNode
	K   int
}

func Constructor(k int, nums []int) KthLargest {
	// array to BST
	var temp *TreeNode
	for i := 0; i < len(nums); i++ {
		temp = insertIntoBST(temp, nums[i])
	}
	return KthLargest{temp, k}
}

// it allows duplicate child on the left-handed side, <=
func insertIntoBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return &TreeNode{val, 1, nil, nil}
	}
	curr := root
	for true {
		if val > curr.Val {
			if curr.Right != nil {
				curr.Cnt++
				curr = curr.Right
			} else {
				curr.Right = &TreeNode{val, 1, nil, nil}
				curr.Cnt++
				break
			}
		} else { // it includes < and =
			if curr.Left != nil {
				curr.Cnt++
				curr = curr.Left
			} else {
				curr.Left = &TreeNode{val, 1, nil, nil}
				curr.Cnt++
				break
			}
		}
	}
	return root
}

// suggested solution 1: BST
func (this *KthLargest) Add(val int) int {
	// 1. insert
	this.Bst = insertIntoBST(this.Bst, val)
	// 2. search kth largest in a BST using Cnt
	count := this.K
	curr := this.Bst

	for count > 0 {
		pos := 1
		if curr.Right != nil {
			pos = pos + curr.Right.Cnt
		}
		if count == pos {
			break
		} else if count > pos {
			count = count - pos
			curr = curr.Left
		} else {
			curr = curr.Right
		}
	}
	return curr.Val
}

// Time Limit Exceeded
// func (this *KthLargest) Add(val int) int {
// 	// 1. insert
// 	this.Bst = insertIntoBST(this.Bst, val)
// 	// 2. search kth largest in a BST
// 	var arr []int
// 	var inorder func(node *TreeNode)
// 	inorder = func(node *TreeNode) {
// 		if node == nil {
// 			return
// 		}
// 		inorder(node.Left)
// 		arr = append(arr, node.Val)
// 		inorder(node.Right)
// 	}
// 	inorder(this.Bst)

// 	return arr[len(arr)-this.K]
// }

//
func main() {
	temp := Constructor(3, []int{5, 7, 3, 8, 1, 9})
	res := temp.Add(2)
	fmt.Println(res)
}
