package main

import "fmt"

/*
	Write		O(M)
	Find		O(logN)
	Union		O(N)
	Overall	O(MlogN)
*/

type QuickFind struct {
	Count int
	Ids   []int
}

func Constructor(n int) QuickFind {
	ids := []int{}
	for i := 0; i < n; i++ {
		ids = append(ids, i)
	}
	return QuickFind{n, ids}
}

func (this *QuickFind) GetCount() int {
	return this.Count
}

func (this *QuickFind) Find(key int) int {
	if key < len(this.Ids) {
		return this.Ids[key]
	}
	return -1
}

// add set q to set q
func (this *QuickFind) Union(p int, q int) {
	if p < 0 || p+1 > len(this.Ids) || q < 0 || q+1 > len(this.Ids) {
		return
	}
	pId := this.Find(p)
	qId := this.Find(q)

	// iterate through the set, set the numbers(with qId) belongs to pId
	for i := 0; i < len(this.Ids); i++ {
		if this.Find(i) == qId {
			this.Ids[i] = pId
		}
	}
	this.Count--
}

func (this *QuickFind) IsConnect(p int, q int) bool {
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
