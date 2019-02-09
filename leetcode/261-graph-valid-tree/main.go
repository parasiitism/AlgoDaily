package main

/*
	Questions to ask:
	- duplicate edges?
	- directed / undirected ?
	- will there will numbers out of range?
	- no malformed input? e.g. no float, characters?
*/

/*
	1st approach
	- the question states that there will be no duplicate edges and the graph is undirected,
	the best approach for the question is to use Union Find

	Time    O(nlogn) in each iteration, union find takes O(logn)
	Space   O(n)
	12ms beats 100%
*/
func validTree(n int, edges [][]int) bool {
	uf := UnionFindConstructor(n)
	for _, edge := range edges {
		aId := uf.Find(edge[0])
		bId := uf.Find(edge[1])
		if aId != bId {
			uf.Union(edge[0], edge[1])
		} else {
			return false
		}
	}
	if uf.GetCount() == 1 {
		return true
	}
	return false
}

type UnionFind struct {
	Count int
	Ids   []int
	Caps  []int
}

func UnionFindConstructor(n int) UnionFind {
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

}
