package main

import "fmt"

/*
	1st approach: union find
	1. put all the words into the union set
	2. establish connections between those words using quick uinion
	3. check if words1[i] and words2[i] are similar using union find

	Time		O(nlogn) union.find() takes O(nlogn) on average
	Space		O(n) unino set stores all the words from words1, words2, pairs
	116 ms, faster than 92.31%
*/
func areSentencesSimilarTwo(words1 []string, words2 []string, pairs [][]string) bool {
	if len(words1) != len(words2) {
		return false
	}
	// put all the words into the union set
	wordset := make(map[string]bool)
	for _, word := range words1 {
		wordset[word] = true
	}
	for _, word := range words2 {
		wordset[word] = true
	}
	for _, pair := range pairs {
		wordset[pair[0]] = true
		wordset[pair[1]] = true
	}
	words := []string{}
	for key := range wordset {
		words = append(words, key)
	}
	uf := Constructor(words)
	// establish connections between those words
	for _, pair := range pairs {
		uf.Union(pair[0], pair[1])
	}
	// check if words1[i] and words2[i] are similar using union find
	for i := 0; i < len(words1); i++ {
		a := words1[i]
		b := words2[i]
		if uf.IsConnect(a, b) == false {
			return false
		}
	}
	return true
}

type UnionFind struct {
	Count int
	Ids   map[string]string
	Caps  map[string]int
}

func Constructor(nodes []string) UnionFind {
	ids := make(map[string]string)
	caps := make(map[string]int)
	for _, node := range nodes {
		ids[node] = node
		caps[node] = 1
	}
	return UnionFind{len(nodes), ids, caps}
}

func (this *UnionFind) GetCount() int {
	return this.Count
}

// O(logN): it takes O(nlogn) to find the root on average
func (this *UnionFind) Find(key string) string {
	cur := key
	for cur != this.Ids[cur] {
		cur = this.Ids[cur]
	}
	return cur
}

// union to the bigger tree, O(N)
func (this *UnionFind) Union(p string, q string) bool {
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

func (this *UnionFind) IsConnect(p string, q string) bool {
	return this.Find(p) == this.Find(q)
}

func main() {
	a := []string{"great", "acting", "skills"}
	b := []string{"fine", "drama", "talent"}
	p := [][]string{{"great", "good"}, {"fine", "good"}, {"acting", "drama"}, {"skills", "talent"}}
	fmt.Println(areSentencesSimilarTwo(a, b, p))

	a = []string{"great", "acting", "skills"}
	b = []string{"fine", "drama", "talent"}
	p = [][]string{{"great", "good"}, {"acting", "drama"}, {"skills", "talent"}}
	fmt.Println(areSentencesSimilarTwo(a, b, p))

	a = []string{"great"}
	b = []string{"great"}
	p = [][]string{}
	fmt.Println(areSentencesSimilarTwo(a, b, p))

	a = []string{"great", "acting", "skills"}
	b = []string{"fine", "drama"}
	p = [][]string{}
	fmt.Println(areSentencesSimilarTwo(a, b, p))
}
