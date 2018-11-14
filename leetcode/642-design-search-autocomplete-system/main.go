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
		return []string{}
	}
	// search
	this.UserInput += string(c)
	return []string{}
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

// func (this *AutocompleteSystem) search(c byte) []string {

// }

func main() {
	sentences := []string{"i love you", "island", "iroman", "i love leetcode"}
	times := []int{5, 3, 2, 2}
	obj := Constructor(sentences, times)
	fmt.Println(obj.UserTrie)
	obj.Input('a')
	obj.Input('b')
	obj.Input('#')
	fmt.Println(obj.UserTrie.Children['a'])
}
