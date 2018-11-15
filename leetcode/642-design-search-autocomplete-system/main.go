package main

import (
	"fmt"
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
	sentence := this.UserInput
	current := this.UserTrie
	var targetNode *Trie
	for i := 0; i < len(sentence); i++ {
		charactor := sentence[i]
		if value, existed := current.Children[charactor]; existed {
			current = value
			if i == len(sentence)-1 {
				targetNode = value
			}
		}
	}
	if targetNode == nil {
		return []string{}
	}
	// iterate the target node children
	var results []string
	//dfs
	var stack []*Stack
	stack = append(stack, &Stack{"", targetNode})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if len(pop.trie.Children) == 0 {
			results = append(results, pop.prefix)
		}
		// add children into stack
		for key, value := range pop.trie.Children {
			stack = append(stack, &Stack{pop.prefix + string(key), value})
		}
	}
	return results
}

type Stack struct {
	prefix string
	trie   *Trie
}

func main() {
	sentences := []string{"i love you", "island", "iroman", "i love leetcode"}
	times := []int{5, 3, 2, 2}
	obj := Constructor(sentences, times)
	obj.Input('a')
	obj.Input('b')
	obj.Input('c')
	obj.Input('#')
	fmt.Println(obj.UserTrie.Children['a'])
	fmt.Println(obj.Input('a'))
	fmt.Println(obj.Input('b'))
}
