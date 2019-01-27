package main

import (
	"container/heap"
	"fmt"
)

/*
	Implement Priority Queue
*/

type Item struct {
	Weight   int // The priority of the item in the queue.
	Location int // The value of the item; arbitrary.
	// The index is needed by update and is maintained by the heap.Interface methods.
	Index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].Weight < pq[j].Weight
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
func (pq *PriorityQueue) update(item *Item, priority int, value int) {
	item.Weight = priority
	item.Location = value
	heap.Fix(pq, item.Index)
}

/*
	It can be solved by DFS, but the main purpose of this attempt is to understand Dijkstra's Algorithm
	- Time  O(NlogN) logN due to the heap
	- Space O(N) result dict
	116ms beats 61.11%
	27jan2019
*/
func networkDelayTime(times [][]int, N int, K int) int {

	// put times into a hashtable for lookup, time = (from, to, weight)
	timesMap := make(map[int][][]int)
	for _, time := range times {
		key := time[0]
		if _, x := timesMap[key]; x {
			timesMap[key] = append(timesMap[key], time)
		} else {
			timesMap[key] = [][]int{time}
		}
	}

	// dijkstra's
	h := &PriorityQueue{}
	heap.Init(h)
	heap.Push(h, &Item{0, K, 0})
	seen := make(map[int]int)
	for h.Len() > 0 {
		item := heap.Pop(h).(*Item)

		if _, x := seen[item.Location]; x {
			continue
		}
		seen[item.Location] = item.Weight

		if _, x := timesMap[item.Location]; x {
			candidates := timesMap[item.Location]
			for _, can := range candidates {
				if _, x := seen[can[1]]; !x {
					i := h.Len()
					heap.Push(h, &Item{item.Weight + can[2], can[1], i})
				}
			}
		}
	}

	// the max travel time is the result
	max := 0
	for i := 1; i <= N; i++ {
		if _, x := seen[i]; !x {
			return -1
		}
		if seen[i] > max {
			max = seen[i]
		}
	}
	return max
}

func main() {
	a := [][]int{
		{2, 1, 1},
		{2, 3, 1},
		{3, 4, 1},
	}
	fmt.Println(networkDelayTime(a, 4, 2))

	a = [][]int{
		{2, 1, 1}, {2, 3, 1}, {1, 4, 3}, {2, 4, 7},
	}
	fmt.Println(networkDelayTime(a, 4, 2))

	a = [][]int{
		{1, 2, 3},
		{3, 4, 5},
	}
	fmt.Println(networkDelayTime(a, 4, 1))
}
