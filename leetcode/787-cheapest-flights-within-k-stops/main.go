package main

import (
	"container/heap"
	"fmt"
	"math"
)

/*
	1st approach
	- BFS
	TLE
*/

type Route struct {
	Cost     int
	Stops    int
	Visited  map[int]bool
	Location int
}

func findCheapestPrice0(n int, flights [][]int, src int, dst int, K int) int {

	// put flights into a hashtable for lookup
	flightsMap := make(map[int][][]int)
	for _, flight := range flights {
		from := flight[0]
		if _, x := flightsMap[from]; x {
			flightsMap[from] = append(flightsMap[from], flight)
		} else {
			flightsMap[from] = [][]int{flight}
		}
	}

	// bfs
	min := math.MaxInt64
	var queue []Route
	queue = append(queue, Route{0, 0, make(map[int]bool), src})
	for len(queue) > 0 {
		n := len(queue)
		for i := 0; i < n; i++ {
			head := queue[0]
			queue = queue[1:]

			if head.Location == dst && head.Stops <= K+1 && head.Cost < min {
				min = head.Cost
				continue
			}

			if head.Stops == K+1 {
				continue
			}

			candidates := flightsMap[head.Location]
			for _, flight := range candidates {
				if _, x := head.Visited[flight[1]]; x {
					continue
				}
				// copy visited
				newVisited := make(map[int]bool)
				for k, v := range head.Visited {
					newVisited[k] = v
				}
				newVisited[flight[1]] = true
				// create new route
				r := Route{head.Cost + flight[2], head.Stops + 1, newVisited, flight[1]}
				queue = append(queue, r)
			}
		}
	}
	if min == math.MaxInt64 {
		return -1
	}
	return min
}

/*
	2nd approach
	- Depth-limied Dijkstra's Algorithm
*/

// Implement Priority Queue
type Item struct {
	Cost     int // The priority of the item in the queue.
	Location int // The value of the item; arbitrary.
	Steps    int // The value of the item; arbitrary.
	// The index is needed by update and is maintained by the heap.Interface methods.
	Index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].Cost < pq[j].Cost
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
func (pq *PriorityQueue) update(item *Item, cost int, location int, steps int) {
	item.Cost = cost
	item.Location = location
	item.Steps = steps
	heap.Fix(pq, item.Index)
}

// the func
func findCheapestPrice(n int, flights [][]int, src int, dst int, K int) int {

	// put flights into a hashtable for lookup
	flightsMap := make(map[int][][]int)
	for _, flight := range flights {
		from := flight[0]
		if _, x := flightsMap[from]; x {
			flightsMap[from] = append(flightsMap[from], flight)
		} else {
			flightsMap[from] = [][]int{flight}
		}
	}
	// dijkstra's
	pq := &PriorityQueue{}
	heap.Init(pq)
	heap.Push(pq, &Item{0, src, 0, 0})
	for pq.Len() > 0 {
		item := heap.Pop(pq).(*Item)

		// this is the trickiest part:
		// since the item has the least cost(prioirty queue),
		// even though we might have pushed the path directed destination(HIGHER COST PATH) in the queue,
		// as long as there are paths have cost less then the HIGHER COST PATH,
		// the HIGHER COST PATH would be poped.
		// it means that, instead, only the path with the least cost to the destination will be popped first!!!
		if item.Location == dst {
			return item.Cost
		}

		if item.Steps-1 == K {
			continue
		}

		if _, x := flightsMap[item.Location]; x {
			candidates := flightsMap[item.Location]
			for _, can := range candidates {
				i := pq.Len()
				heap.Push(pq, &Item{item.Cost + can[2], can[1], item.Steps + 1, i})
			}
		}
	}
	return -1
}

func main() {

	// test the trickiest part: first item
	f := [][]int{
		{1, 2, 10},
		{1, 3, 20},
		{2, 4, 100},
		{3, 4, 1},
	}
	fmt.Println(findCheapestPrice(5, f, 1, 4, 1)) // 21

	f = [][]int{
		{0, 1, 100},
		{1, 2, 100},
		{0, 2, 500},
	}
	fmt.Println(findCheapestPrice(3, f, 0, 2, 0)) // 500

	f = [][]int{
		{0, 1, 100},
		{1, 2, 100},
		{0, 2, 500},
	}
	fmt.Println(findCheapestPrice(3, f, 0, 2, 1)) // 200

	f = [][]int{
		{0, 1, 100},
		{0, 3, 50},
		{0, 2, 500},
		{1, 2, 100},
		{1, 4, 400},
		{2, 3, 1},
		{2, 4, 10},
		{3, 4, 350},
	}
	fmt.Println(findCheapestPrice(5, f, 0, 4, 5)) // 210

	f = [][]int{
		{4, 1, 1},
		{1, 2, 3},
		{0, 3, 2},
		{0, 4, 10},
		{3, 1, 1},
		{1, 4, 3},
	}
	fmt.Println(findCheapestPrice(5, f, 2, 1, 1)) //-1

	f = [][]int{
		{0, 1, 1}, {0, 2, 5}, {1, 2, 1}, {2, 3, 1},
	}
	fmt.Println(findCheapestPrice(4, f, 0, 3, 1)) //-1

	f = [][]int{
		{0, 12, 28}, {5, 6, 39}, {8, 6, 59}, {13, 15, 7}, {13, 12, 38}, {10, 12, 35}, {15, 3, 23}, {7, 11, 26}, {9, 4, 65}, {10, 2, 38}, {4, 7, 7}, {14, 15, 31}, {2, 12, 44}, {8, 10, 34}, {13, 6, 29}, {5, 14, 89}, {11, 16, 13}, {7, 3, 46}, {10, 15, 19}, {12, 4, 58}, {13, 16, 11}, {16, 4, 76}, {2, 0, 12}, {15, 0, 22}, {16, 12, 13}, {7, 1, 29}, {7, 14, 100}, {16, 1, 14}, {9, 6, 74}, {11, 1, 73}, {2, 11, 60}, {10, 11, 85}, {2, 5, 49}, {3, 4, 17}, {4, 9, 77}, {16, 3, 47}, {15, 6, 78}, {14, 1, 90}, {10, 5, 95}, {1, 11, 30}, {11, 0, 37}, {10, 4, 86}, {0, 8, 57}, {6, 14, 68}, {16, 8, 3}, {13, 0, 65}, {2, 13, 6}, {5, 13, 5}, {8, 11, 31}, {6, 10, 20}, {6, 2, 33}, {9, 1, 3}, {14, 9, 58}, {12, 3, 19}, {11, 2, 74}, {12, 14, 48}, {16, 11, 100}, {3, 12, 38}, {12, 13, 77}, {10, 9, 99}, {15, 13, 98}, {15, 12, 71}, {1, 4, 28}, {7, 0, 83}, {3, 5, 100}, {8, 9, 14}, {15, 11, 57}, {3, 6, 65}, {1, 3, 45}, {14, 7, 74}, {2, 10, 39}, {4, 8, 73}, {13, 5, 77}, {10, 0, 43}, {12, 9, 92}, {8, 2, 26}, {1, 7, 7}, {9, 12, 10}, {13, 11, 64}, {8, 13, 80}, {6, 12, 74}, {9, 7, 35}, {0, 15, 48}, {3, 7, 87}, {16, 9, 42}, {5, 16, 64}, {4, 5, 65}, {15, 14, 70}, {12, 0, 13}, {16, 14, 52}, {3, 10, 80}, {14, 11, 85}, {15, 2, 77}, {4, 11, 19}, {2, 7, 49}, {10, 7, 78}, {14, 6, 84}, {13, 7, 50}, {11, 6, 75}, {5, 10, 46}, {13, 8, 43}, {9, 10, 49}, {7, 12, 64}, {0, 10, 76}, {5, 9, 77}, {8, 3, 28}, {11, 9, 28}, {12, 16, 87}, {12, 6, 24}, {9, 15, 94}, {5, 7, 77}, {4, 10, 18}, {7, 2, 11}, {9, 5, 41},
	}
	fmt.Println(findCheapestPrice(17, f, 13, 4, 13)) // 47
}
