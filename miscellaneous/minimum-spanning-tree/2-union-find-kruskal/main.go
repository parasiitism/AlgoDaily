package main

import (
	"fmt"
	"sort"
)

/*
	Minimum Spanning Tree: find the edges which connect all the nodes with minimum cost

	This appraoch is a classic approach using Union Find, aka. Kruskal Algorithm, to merge the edges with minimum weight
	1. basically we sort the input edges
	2. pop the edges one by one from minimum
	3. union the vertexs and put the vertexs in the result set if the vertexs are not connected
	5. the edges in the set are the result

	Optimization
	- if the weights are dicrete and the range is known, sort the edges with a bucket-sort in linear time O(n)

	⭐️ Kruskal vs Prim, we should use Kruskal
	- when the graph is sparse, number of edges(E) ~= number of vertexes(V) ,like E ~= V
	- when the edges are already sorted or if we can sort them in linear time

	Time		O(E log E) E: number of edges
	Space		O(E) edges in the heap
	ref: https://www.youtube.com/watch?v=5xosHRdxqHA
*/
func miniumSpanningTree(n int, edges [][]int) [][]int {
	// sort, O(nlogn)
	sort.Slice(edges, func(i, j int) bool {
		return edges[i][2] < edges[j][2]
	})
	// make disjoint set, O(n)
	c := Constructor(n)
	res := [][]int{}
	// for each edge, union if v1's set and v2's set are different, O(nlogn)
	for i := 0; i < len(edges); i++ {
		edge := edges[i]
		c1 := c.Find(edge[0])
		c2 := c.Find(edge[1])
		if c1 != c2 {
			c.Union(edge[0], edge[1])
			res = append(res, edge)
		}
	}
	return res
}

// Union Find class
type UnionFind struct {
	Count int
	Ids   []int
	Caps  []int
}

// O(n)
func Constructor(n int) UnionFind {
	ids := []int{}
	caps := []int{}
	for i := 0; i < n; i++ {
		ids = append(ids, i)
		caps = append(caps, 1)
	}
	return UnionFind{n, ids, caps}
}

func (this *UnionFind) GetCount() int {
	return this.Count
}

// O(logn)
func (this *UnionFind) Find(key int) int {
	if key < len(this.Ids) {
		// loop to find to ultimate root
		cur := key
		for cur != this.Ids[cur] {
			cur = this.Ids[cur]
		}
		return cur
	}
	return -1
}

// O(n)
func (this *UnionFind) Union(p int, q int) {
	if p < 0 || p+1 > len(this.Ids) || q < 0 || q+1 > len(this.Ids) {
		return
	}
	pId := this.Find(p)
	qId := this.Find(q)
	if pId == qId {
		return
	}

	if this.Caps[pId] < this.Caps[qId] {
		this.Ids[pId] = qId
		this.Caps[qId] += this.Caps[pId]
	} else {
		this.Ids[qId] = pId
		this.Caps[pId] += this.Caps[qId]
	}
	this.Count--
}

func (this *UnionFind) IsConnect(p int, q int) bool {
	if p < 0 || p+1 > len(this.Ids) || q < 0 || q+1 > len(this.Ids) {
		return false
	}
	return this.Find(p) == this.Find(q)
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
	fmt.Println(miniumSpanningTree(7, edges))
}
