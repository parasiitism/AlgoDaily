package main

import "fmt"

/*
	1st approach: Union Find
	- implement an Union Find
	- for each edge, union the node if they are not connected
	- but if they both present in the union set, put it into the result

	The purpose of this question is to practice Union Find, I am gonna do it in other ways

	Time    O(nlogn) iterate the edges, in each iteration the Find() operation is O(logn)
	Space   O(n) the set
	8 ms, faster than 53.57%
*/
func findRedundantConnection(edges [][]int) []int {
	nodesSet := make(map[int]bool)
	for _, edge := range edges {
		nodesSet[edge[0]] = true
		nodesSet[edge[1]] = true
	}
	nodes := []int{}
	for key := range nodesSet {
		nodes = append(nodes, key)
	}
	uf := Constructor(nodes)
	res := []int{}
	for _, edge := range edges {
		temp := uf.Union(edge[0], edge[1])
		if temp == false {
			res = edge
		}
	}
	if uf.GetCount() > 1 {
		return []int{}
	}
	return res
}

type UnionFind struct {
	Count int
	Ids   map[int]int
	Caps  map[int]int
}

func Constructor(nodes []int) UnionFind {
	ids := make(map[int]int)
	caps := make(map[int]int)
	for _, node := range nodes {
		ids[node] = node
		caps[node] = 1
	}
	return UnionFind{len(nodes), ids, caps}
}

func (this *UnionFind) GetCount() int {
	return this.Count
}

// O(logN): loop to find to ultimate root
func (this *UnionFind) Find(key int) int {
	cur := key
	for cur != this.Ids[cur] {
		cur = this.Ids[cur]
	}
	return cur
}

// union to the bigger tree, O(N)
func (this *UnionFind) Union(p int, q int) bool {
	pId := this.Find(p)
	qId := this.Find(q)
	if pId == qId {
		return false
	}
	if this.Caps[pId] < this.Caps[qId] {
		this.Ids[pId] = qId
		this.Caps[qId] += this.Caps[pId]
	} else {
		this.Ids[qId] = pId
		this.Caps[pId] += this.Caps[qId]
	}
	this.Count--
	return true
}

func (this *UnionFind) IsConnect(p int, q int) bool {
	return this.Find(p) == this.Find(q)
}

func main() {
	a := [][]int{
		{1, 2}, {1, 3}, {2, 3},
	}
	fmt.Println(findRedundantConnection(a))

	a = [][]int{
		{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5},
	}
	fmt.Println(findRedundantConnection(a))

	a = [][]int{
		{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}, {4, 5},
	}
	fmt.Println(findRedundantConnection(a))

	a = [][]int{
		{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}, {6, 7},
	}
	fmt.Println(findRedundantConnection(a))
}
