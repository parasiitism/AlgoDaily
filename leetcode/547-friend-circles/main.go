package main

import "fmt"

/*
	1st approach: union find
	- put the friends connections into an union find
	- return the total 'cluster' as a result

	Time		O(nlogn)
	Space		O(n)
	28 ms, faster than 100.00%
*/
func findCircleNum(M [][]int) int {
	if len(M) == 0 || len(M[0]) == 0 {
		return 0
	}
	uf := Constructor(len(M))
	for i := 0; i < len(M); i++ {
		for j := i; j < len(M); j++ {
			if M[i][j] == 1 {
				uf.Union(i, j)
			}
		}
	}
	return uf.GetCount()
}

type UnionFind struct {
	Count int
	Ids   []int
	Caps  []int
}

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

// O(logN)
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

// union to the bigger tree, O(N)
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

func main() {
	a := [][]int{
		{1, 1, 0},
		{1, 1, 0},
		{0, 0, 1},
	}
	fmt.Println(findCircleNum(a))

	a = [][]int{
		{1, 1, 0},
		{1, 1, 1},
		{0, 1, 1},
	}
	fmt.Println(findCircleNum(a))

	a = [][]int{
		{1, 1, 0, 0},
		{1, 1, 0, 1},
		{0, 0, 1, 0},
		{0, 1, 0, 1},
	}
	fmt.Println(findCircleNum(a))
}
