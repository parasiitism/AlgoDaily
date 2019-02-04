package main

import "fmt"

/*
	Write		O(M)
	Find		O(logn)
	Union		O(N)
	Overall	O(MN) ...worst case
*/

type UnionFind struct {
	Count int
	Ids   []int
	Caps  []int
}

func Constructor(n int) UnionFind {
	ids := []int{}
	for i := 0; i < n; i++ {
		ids = append(ids, i)
	}
	caps := []int{}
	for i := 0; i < n; i++ {
		caps = append(caps, i)
	}
	return UnionFind{n, ids, caps}
}

func (this *UnionFind) GetCount() int {
	return this.Count
}

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

// union to the bigger tree
func (this *UnionFind) Union(p int, q int) {
	if p < 0 || p+1 > len(this.Ids) || q < 0 || q+1 > len(this.Ids) {
		return
	}
	pId := this.Find(p)
	qId := this.Find(q)
	if pId == qId {
		return
	}

	if this.Caps[p] < this.Caps[q] {
		this.Ids[p] = qId
		this.Caps[q] += this.Caps[p]
	} else {
		this.Ids[q] = pId
		this.Caps[p] += this.Caps[q]
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
