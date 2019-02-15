package main

import (
	"container/heap"
	"fmt"
	"sort"
)

/*
	1st approach
	- easiest way

	Time		O(nlogn)
	Space		O(n)
	8 ms, faster than 100%
*/
func findKthLargest(nums []int, k int) int {
	sort.Ints(nums)
	return nums[len(nums)-k]
}

/*
	2nd approach
	- heap

	Time		O(nlogn)
	Space		O(n)
	12 ms, faster than 62.59%
*/

// An IntHeap is a max-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
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

func findKthLargest1(nums []int, k int) int {
	pq := &IntHeap{}
	heap.Init(pq)
	for _, num := range nums {
		heap.Push(pq, num)
	}
	i := 1
	for pq.Len() > 0 && i < k {
		heap.Pop(pq)
		i++
	}
	return heap.Pop(pq).(int)
}

/*
	follow up: if the range of the nums are known, we can use bucket sort to achieve O(n)
*/

func main() {
	fmt.Println(findKthLargest1([]int{3, 2, 1, 5, 6, 4}, 2))
	fmt.Println(findKthLargest1([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4))
	fmt.Println(findKthLargest1([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 9))
}
