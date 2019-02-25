package main

import (
	"container/heap"
	"fmt"
)

/*
	3rd approach: 2 heaps
	- minheap for right half
	- maxheap for left half
	- therefore the mean will always be the max of maxheap and the min of minheap
	- https://leetcode.com/articles/find-median-from-data-stream/

	TimeAddNum() 				O(5*logn)
	Time FindMedian() 	O(1)
	132 ms, faster than 80.65%
*/

type MedianFinder struct {
	maxHeap *MaxHeap
	minHeap *MinHeap
}

/** initialize your data structure here. */
func Constructor() MedianFinder {
	left := &MaxHeap{}
	right := &MinHeap{}
	return MedianFinder{left, right}
}

func (this *MedianFinder) AddNum(num int) {
	heap.Push(this.minHeap, num)
	m := heap.Pop(this.minHeap)
	heap.Push(this.maxHeap, m)
	if this.minHeap.Len() < this.maxHeap.Len() {
		n := heap.Pop(this.maxHeap)
		heap.Push(this.minHeap, n)
	}
}

func (this *MedianFinder) FindMedian() float64 {
	fmt.Println(this.maxHeap)
	fmt.Println(this.minHeap)
	if this.minHeap.Len() != this.maxHeap.Len() {
		return float64((*this.minHeap)[0])
	}
	return (float64((*this.minHeap)[0]) + float64((*this.maxHeap)[0])) / 2.0
}

// min heap
type MinHeap []int

func (h MinHeap) Len() int            { return len(h) }
func (h MinHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// max heap
type MaxHeap []int

func (h MaxHeap) Len() int            { return len(h) }
func (h MaxHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func main() {

	obj := Constructor()
	obj.AddNum(1)
	obj.AddNum(2)
	fmt.Println(obj.FindMedian())

	obj = Constructor()
	obj.AddNum(5)
	obj.AddNum(3)
	obj.AddNum(4)
	obj.AddNum(3)
	obj.AddNum(1)
	obj.AddNum(2)
	obj.AddNum(6)
	fmt.Println(obj.FindMedian())
}
