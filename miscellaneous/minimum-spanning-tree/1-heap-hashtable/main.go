package main

import (
	"container/heap"
	"fmt"
)

/*
	Minimum Spanning Tree: find the edges which connect all the nodes with minimum cost

	This appraoch is an eclectic implementation using a heap and a list of hashable(see 2. for the Union Find version)
	1. basically we sort the input edges
	2. pop the edges one by one with minimum cost and put them in its corresponding cluster(hashtable)
	3. merge the clusters if there is a connection
	4. ignore the edges which are present in one cluster(since the edges with min cost come first, we can ignore the later edges)
	5. the "considered" edges are the result

	Time		O(nlogn)
	Space		O(n)
*/
func miniumSpanningTree(edges [][]int) [][]int {
	var res [][]int
	var hts []map[int]bool

	pq := &PriorityQueue{}
	heap.Init(pq)

	for _, e := range edges {
		edge := &Edge{e[0], e[1], e[2]}
		heap.Push(pq, edge)
	}

	for pq.Len() > 0 {
		edge := heap.Pop(pq).(*Edge)
		// find edge
		clusterIdx1 := -1
		for i, ht := range hts {
			if _, x := ht[edge.Vertex1]; x {
				clusterIdx1 = i
			}
		}
		clusterIdx2 := -1
		for i, ht := range hts {
			if _, x := ht[edge.Vertex2]; x {
				clusterIdx2 = i
			}
		}
		if clusterIdx1 > -1 && clusterIdx2 > -1 {
			if clusterIdx1 == clusterIdx2 {
				continue
			}
			hta := hts[clusterIdx1]
			for k, v := range hts[clusterIdx2] {
				hta[k] = v
			}
			hts = append(hts[:clusterIdx2], hts[clusterIdx2+1:]...)
		} else if clusterIdx1 > -1 {
			hta := hts[clusterIdx1]
			hta[edge.Vertex2] = true
		} else if clusterIdx2 > -1 {
			htb := hts[clusterIdx2]
			htb[edge.Vertex1] = true
		} else {
			ht := make(map[int]bool)
			ht[edge.Vertex1] = true
			ht[edge.Vertex2] = true
			hts = append(hts, ht)
		}
		res = append(res, []int{edge.Vertex1, edge.Vertex2, edge.Weight})
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
