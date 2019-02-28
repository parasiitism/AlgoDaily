package main

import (
	"container/heap"
	"fmt"
)

/*
	1st approach: classic dp problem
	- keep the bay when we traverse the list
	- when there is a new peak and the current diff is larger than the previous diff, update the diff

	Time    O(n)
	Space   O(1)
	20 ms, faster than 100.00%
*/
func maxProfit(prices []int) int {
	if len(prices) < 2 {
		return 0
	}
	bay := prices[0]
	diff := 0
	for i := 0; i < len(prices); i++ {
		price := prices[i]
		if price-bay > diff {
			diff = price - bay
		}
		if price < bay {
			bay = price
		}
	}
	return diff
}

/*
	2nd approach: priority queue
	- keep pushing the number into the priority
	- in each iteration, if each price - min(priority queue) is larger than the result, update the result

	Time    O(nlogn)
	Space   O(n) heap
	8 ms, faster than 34.66%
*/
func maxProfit1(prices []int) int {
	if len(prices) < 2 {
		return 0
	}
	h := &IntHeap{}
	heap.Init(h)
	diff := 0
	for i := 0; i < len(prices); i++ {
		price := prices[i]
		heap.Push(h, price)
		if price-(*h)[0] > diff {
			diff = price - (*h)[0]
		}
	}
	return diff
}

// heap implementation
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func main() {
	fmt.Println(maxProfit1([]int{7, 1, 5, 3, 6, 4}))
	fmt.Println(maxProfit1([]int{7, 6, 4, 3, 1}))
	fmt.Println(maxProfit1([]int{2, 4}))
	fmt.Println(maxProfit1([]int{2, 4, 1}))
	fmt.Println(maxProfit1([]int{2, 4, 1, 4}))
}
