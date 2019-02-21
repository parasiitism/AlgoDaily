package main

import (
	"container/heap"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach:
	1. dfs and put all the diff, values into a priority queue
	2. pop k values from the pq

	Time	O(nlogn)
	Space	O(n)
	24 ms, faster than 100.00%
*/
func closestKValues(root *TreeNode, target float64, k int) []int {
	pq := &PriorityQueue{}
	heap.Init(pq)
	// dfs iteratively
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		value := math.Abs(target - float64(pop.Val))
		heap.Push(pq, &Item{value, pop.Val})
		if pop.Left != nil {
			stack = append(stack, pop.Left)
		}
		if pop.Right != nil {
			stack = append(stack, pop.Right)
		}
	}
	// pop the item from the pq
	res := []int{}
	for i := 0; i < pq.Len(); i++ {
		item := heap.Pop(pq).(*Item)
		res = append(res, item.Val)
	}
	return res
}

type Item struct {
	Diff float64
	Val  int
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].Diff > pq[j].Diff
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	item := x.(*Item)
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

func main() {

}
