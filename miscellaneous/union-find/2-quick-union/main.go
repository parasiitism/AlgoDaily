package main

import "fmt"

/*
	Write		O(M)
	Find		from O(logN) to O(N)
	Union		O(1)
	Overall	O(MN) ...worst case
*/

type QuickUnion struct {
	Count int
	Ids   []int
}

func Constructor(n int) QuickUnion {
	ids := []int{}
	for i := 0; i < n; i++ {
		ids = append(ids, i)
	}
	return QuickUnion{n, ids}
}

func (this *QuickUnion) GetCount() int {
	return this.Count
}

func (this *QuickUnion) Find(key int) int {
	if key < len(this.Ids) {
		// loop for find to ultimate root
		cur := key
		for cur != this.Ids[cur] {
			cur = this.Ids[cur]
		}
		return cur
	}
	return -1
}

// add set q to set q
func (this *QuickUnion) Union(p int, q int) {
	if p < 0 || p+1 > len(this.Ids) || q < 0 || q+1 > len(this.Ids) {
		return
	}
	pId := this.Find(p)
	qId := this.Find(q)
	if pId == qId {
		return
	}
	this.Ids[qId] = pId
	this.Count--
}

func (this *QuickUnion) IsConnect(p int, q int) bool {
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
	fmt.Println(c.IsConnect(2, 4))
	fmt.Println(c.IsConnect(3, 4))
	fmt.Println(c.GetCount())
}
