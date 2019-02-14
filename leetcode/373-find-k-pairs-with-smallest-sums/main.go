package main

import (
	"container/heap"
	"fmt"
	"sort"
)

/*
	1st approach
	- use a priority queue

	Time 	O(nlogn)
	Space	O(n)
	188 ms, faster than 18.75%
*/
func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
	pq := &PriorityQueue{}
	heap.Init(pq)
	cnt := 0
	for _, a := range nums1 {
		for _, b := range nums2 {
			heap.Push(pq, &Item{a + b, a, b, cnt})
			cnt++
		}
	}
	i := 0
	min := 0
	if pq.Len() < k {
		min = pq.Len()
	} else {
		min = k
	}
	res := [][]int{}
	for i < min {
		pop := heap.Pop(pq).(*Item)
		res = append(res, []int{pop.Nums1, pop.Nums2})
		i++
	}
	return res
}

/*
	Implement Priority Queue
*/

type Item struct {
	Product int // The priority of the item in the queue.
	Nums1   int
	Nums2   int
	// The index is needed by update and is maintained by the heap.Interface methods.
	Index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].Product < pq[j].Product
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].Index = i
	pq[j].Index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.Index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.Index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

/*
	2nd approach
	- use built-in sort

	Time 	O(nlogn)
	Space	O(n)
	192 ms, faster than 12.50%
*/
func kSmallestPairs1(nums1 []int, nums2 []int, k int) [][]int {
	arr := []*Item{}
	for _, a := range nums1 {
		for _, b := range nums2 {
			o := &Item{a + b, a, b, 0}
			arr = append(arr, o)
		}
	}
	sort.Slice(arr, func(i, j int) bool {
		return arr[i].Product < arr[j].Product
	})
	min := 0
	if len(arr) < k {
		min = len(arr)
	} else {
		min = k
	}
	res := [][]int{}
	i := 0
	for i < min {
		res = append(res, []int{arr[i].Nums1, arr[i].Nums2})
		i++
	}
	return res
}

func main() {
	nums1 := []int{1, 7, 11}
	nums2 := []int{2, 4, 6}
	fmt.Println(kSmallestPairs(nums1, nums2, 3))
	fmt.Println(kSmallestPairs1(nums1, nums2, 3))
}
