package main

import (
	"container/heap"
	"fmt"
)

/*
	Minimum Spanning Tree: find the edges which connect all the nodes with minimum cost

	This appraoch is a classic approach using Prim's Algorithm
	- I did it with a heap and a hashtable

	Optimization
	- use finbonacci heap to sort the edges

	️️⭐️ Kruskal vs Prim, we should use Prim
	- when the graph is dense, number of edges(E) > number of vertexes(V) ,like E > V^2

	Time	O(E log V) E: number of edges, V: number of vertexes
	Space	O(E + V) hashtable + heap
*/
func miniumSpanningTree(edges [][]int) [][]int {
	res := [][]int{}
	visited := make(map[int]bool)

	pq := &PriorityQueue{}
	heap.Init(pq)

	// pick the first vertex as a starting point
	start := edges[0][0]
	visited[start] = true
	for _, e := range edges {
		if e[0] == start || e[1] == start {
			heap.Push(pq, &Edge{e[0], e[1], e[2]})
		}
	}
	for pq.Len() > 0 {
		pop := heap.Pop(pq).(*Edge)
		found1 := false
		found2 := false
		if _, x := visited[pop.Vertex1]; x {
			found1 = true
		}
		if _, x := visited[pop.Vertex2]; x {
			found2 = true
		}
		if found1 && found2 {
			continue
		} else if found1 {
			// found vertex1, it means vertex2 is new so we should put vertex2's children into the heap
			visited[pop.Vertex2] = true
			res = append(res, []int{pop.Vertex1, pop.Vertex2, pop.Weight})
			for _, e := range edges {
				if e[0] == pop.Vertex2 || e[1] == pop.Vertex2 {
					heap.Push(pq, &Edge{e[0], e[1], e[2]})
				}
			}
		} else if found2 {
			// found vertex2, it means vertex1 is new so we should put vertex1's children into the heap
			visited[pop.Vertex1] = true
			res = append(res, []int{pop.Vertex1, pop.Vertex2, pop.Weight})
			for _, e := range edges {
				if e[0] == pop.Vertex1 || e[1] == pop.Vertex1 {
					heap.Push(pq, &Edge{e[0], e[1], e[2]})
				}
			}
		}
	}

	return res
}

// PriorityQueue deleration

type Edge struct {
	Vertex1 int
	Vertex2 int
	Weight  int
}

type PriorityQueue []*Edge

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].Weight < pq[j].Weight
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	item := x.(*Edge)
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
	edges := [][]int{
		{1, 2, 4},
		{1, 6, 2},
		{2, 6, 5},
		{2, 3, 6},
		{3, 6, 1},
		{4, 5, 2},
		{5, 6, 4},
		{3, 4, 3},
	}
	fmt.Println(miniumSpanningTree(edges))
}
