package main

import (
	"container/heap"
	"fmt"
)

// suggested solution 1: BST
// -----------------------------------------------------------------------------------
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

/*
// my first attempt: unfold the BST into an sorted array, return the arr[n-k], O(n)
// failed: Time Limit Exceeded
func (this *KthLargest) Add(val int) int {
	// 1. insert
	this.Bst = insertIntoBST(this.Bst, val)
	// 2. search kth largest in a BST
	var arr []int
	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		arr = append(arr, node.Val)
		inorder(node.Right)
	}
	inorder(this.Bst)

	return arr[len(arr)-this.K]
}
*/

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

// Suggested solution: min heap
// -----------------------------------------------------------------------------------

// heap implementation
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// real thing
type KthLargest1 struct {
	Nums *IntHeap
	K    int
}

func Constructor1(k int, nums []int) KthLargest1 {
	// array to BST
	h := &IntHeap{}
	heap.Init(h)
	// push all elements to the heap
	for i := 0; i < len(nums); i++ {
		heap.Push(h, nums[i])
	}
	// remove the smaller elements from the heap such that only the k largest elements are in the heap
	for len(*h) > k {
		heap.Pop(h)
	}
	return KthLargest1{h, k}
}

func (this *KthLargest1) Add1(val int) int {
	if len(*this.Nums) < this.K {
		heap.Push(this.Nums, val)
	} else if val > (*this.Nums)[0] {
		heap.Push(this.Nums, val)
		heap.Pop(this.Nums)
	}
	return (*this.Nums)[0]
}

func main() {
	temp := Constructor1(3, []int{5, 7, 3, 8, 1, 9})
	res := temp.Add1(2)
	res = temp.Add1(10)
	fmt.Println(res)
}
