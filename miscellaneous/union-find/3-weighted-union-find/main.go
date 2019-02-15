package main

import "fmt"

/*
	Write		O(M)
	Find		O(logn)
	Union		O(N)
	Overall	O(MlogN)
*/

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

func (this *UnionFind) IsConnect(p int, q int) bool {
	if p < 0 || p+1 > len(this.Ids) || q < 0 || q+1 > len(this.Ids) {
		return false
	}
	return this.Find(p) == this.Find(q)
}

func main() {
	c := Constructor(10)
	c.Union(2, 3)
	c.Union(3, 4)
	fmt.Println(c.Ids)
	fmt.Println(c.Find(3))
	fmt.Println(c.Find(4))
	fmt.Println(c.IsConnect(2, 3))
	fmt.Println(c.IsConnect(3, 4))
	fmt.Println(c.GetCount())
}
