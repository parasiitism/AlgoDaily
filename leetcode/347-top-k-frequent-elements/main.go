package main

import (
	"container/heap"
	"fmt"
)

/*
	Questions to ask:
	- will there will element has the same frequency?
	- does the order matter in the result?
*/

/*
	1st approach
	- count num: freq into a hashtable
	- put the hashtable key&value into a priority queue
	- the first k elements are the top k elements in the priority queue


	Time	O(nlogn)
	Space	O(n)
	20ms beats 64.29%
	1feb2019
*/
func topKFrequent(nums []int, k int) []int {
	if k > len(nums) {
		return []int{}
	}
	ht := make(map[int]int)
	pq := &PriorityQueue{}
	heap.Init(pq)
	// count the freq for each num
	for _, num := range nums {
		if _, x := ht[num]; x {
			ht[num]++
		} else {
			ht[num] = 1
		}
	}
	// put the num: freq into a prioroity queue
	for key, value := range ht {
		heap.Push(pq, &Item{value, key, pq.Len()})
	}
	// pop the first k element from the priority queue
	res := []int{}
	for i := 0; i < k; i++ {
		item := heap.Pop(pq).(*Item)
		res = append(res, item.Num)
	}
	return res
}

/*
	Implement Priority Queue
*/

type Item struct {
	Freq int // The priority of the item in the queue.
	Num  int // The value of the item; arbitrary.
	// The index is needed by update and is maintained by the heap.Interface methods.
	Index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].Freq > pq[j].Freq
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

// update modifies the priority and value of an Item in the queue.
func (pq *PriorityQueue) update(item *Item, freq int, num int) {
	item.Freq = freq
	item.Num = num
	heap.Fix(pq, item.Index)
}

/*
	2nd approach
	- similar to approach 1 but use bucket sort concept O(n) instead of a heap O(logn)

	Time	O(n)
	Space	O(n)
	20ms beats 64.29%
	1feb2019
*/
func topKFrequent1(nums []int, k int) []int {
	if k > len(nums) {
		return []int{}
	}
	ht := make(map[int]int)
	maxOccur := 0
	// count the freq for each num
	for _, num := range nums {
		if _, x := ht[num]; x {
			ht[num]++
		} else {
			ht[num] = 1
		}
		if ht[num] > maxOccur {
			maxOccur = ht[num]
		}
	}
	// create a bucket, the index is the freq of nums
	bucket := make([][]int, maxOccur+1)
	for key, freq := range ht {
		bucket[freq] = append(bucket[freq], key)
	}
	// get the most frequent k
	res := []int{}
	j := 0
	for i := len(bucket) - 1; i >= 0; i-- {
		b := bucket[i]
		for _, x := range b {
			if j < k {
				res = append(res, x)
				j++
			}
		}
	}

	return res
}

func main() {
	maxOccur := 5
	bucket := make([][]int, maxOccur)
	fmt.Println(bucket)

	fmt.Println(topKFrequent1([]int{1, 1, 1, 2, 2, 3}, 2))
	fmt.Println(topKFrequent1([]int{1, 1, 1, 2, 2, 3, 4, 1, 2, 1, 3, 3, 4, 3}, 2))
}
