package main

import (
	"fmt"
	"sort"
)

type Trie struct {
	Cnt      int
	IsWord   bool
	Children map[byte]*Trie
}

type AutocompleteSystem struct {
	UserTrie  *Trie
	UserInput string
}

func Constructor(sentences []string, times []int) AutocompleteSystem {
	userTrie := &Trie{0, false, make(map[byte]*Trie)}
	for i := 0; i < len(sentences); i++ {
		sentence := sentences[i]
		insert(userTrie, sentence, times[i])
	}
	return AutocompleteSystem{userTrie, ""}
}

func (this *AutocompleteSystem) Input(c byte) []string {
	// add sentence
	if c == '#' {
		insert(this.UserTrie, this.UserInput, 0)
		this.UserInput = ""
		return []string{}
	}
	// search
	this.UserInput += string(c)
	return this.search()
}

// helpers
func insert(userTrie *Trie, sentence string, time int) {
	current := userTrie
	for i := 0; i < len(sentence); i++ {
		charactor := sentence[i]
		var temp *Trie
		if value, existed := current.Children[charactor]; existed {
			temp = value
		} else {
			temp = &Trie{0, false, make(map[byte]*Trie)}
		}
		if i == len(sentence)-1 {
			temp.IsWord = true
			if time == 0 {
				temp.Cnt++
			} else {
				temp.Cnt = time
			}
		}
		current.Children[charactor] = temp
		current = temp
	}
}

func (this *AutocompleteSystem) search() []string {
	// find the target node
	query := this.UserInput
	current := this.UserTrie
	var targetNode *Trie
	for i := 0; i < len(query); i++ {
		charactor := query[i]
		if value, existed := current.Children[charactor]; existed {
			current = value
			if i == len(query)-1 {
				targetNode = value
			}
		}
	}
	if targetNode == nil {
		return []string{}
	}
	// iterate the target node children
	var results []Result
	// dfs
	var stack []*Stack
	stack = append(stack, &Stack{"", targetNode})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if pop.trie.IsWord {
			temp := Result{query + pop.prefix, pop.trie.Cnt}
			results = append(results, temp)
		}
		// add children into stack
		for key, value := range pop.trie.Children {
			stack = append(stack, &Stack{pop.prefix + string(key), value})
		}
	}
	// sort
	descendingOccurence := func(r1, r2 *Result) bool {
		return r1.Occurence > r2.Occurence
	}
	acendingAlphabet := func(r1, r2 *Result) bool {
		return r1.Str < r2.Str
	}
	OrderedBy(descendingOccurence, acendingAlphabet).Sort(results)
	var sortedResults []string
	for i := 0; i < len(results) && i < 3; i++ {
		sortedResults = append(sortedResults, results[i].Str)
	}
	return sortedResults
}

type Stack struct {
	prefix string
	trie   *Trie
}

type Result struct {
	Str       string
	Occurence int
}

// sort by multiple keys
type lessFunc func(p1, p2 *Result) bool
type multiSorter struct {
	results []Result
	less    []lessFunc
}

func (ms *multiSorter) Sort(results []Result) {
	ms.results = results
	sort.Sort(ms)
}
func OrderedBy(less ...lessFunc) *multiSorter {
	return &multiSorter{
		less: less,
	}
}

// interface
func (ms *multiSorter) Len() int {
	return len(ms.results)
}
func (ms *multiSorter) Swap(i, j int) {
	ms.results[i], ms.results[j] = ms.results[j], ms.results[i]
}
func (ms *multiSorter) Less(i, j int) bool {
	p, q := &ms.results[i], &ms.results[j]
	var k int
	for k = 0; k < len(ms.less)-1; k++ {
		less := ms.less[k]
		switch {
		case less(p, q):
			return true
		case less(q, p):
			return false
		}
	}
	return ms.less[k](p, q)
}

func main() {
	sentences := []string{"abc", "abbc", "a"}
	times := []int{3, 3, 3}
	obj := Constructor(sentences, times)
	obj.Input('b')
	obj.Input('c')
	obj.Input('#')
	fmt.Println(obj.Input('c'))
	// fmt.Println(obj.UserTrie.Children['a'])
}
