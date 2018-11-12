package main

import (
	"fmt"
)

type WordDictionary struct {
	Char     string
	Children map[string]*WordDictionary
	Depth    int
	IsWord   bool
}

/** Initialize your data structure here. */
func Constructor() WordDictionary {
	return WordDictionary{"", make(map[string]*WordDictionary), 0, false}
}

/** Adds a word into the data structure. */
func (this *WordDictionary) AddWord(word string) {
	current := this
	for i := 0; i < len(word); i++ {
		charactor := string(word[i])
		var temp *WordDictionary
		if value, existed := current.Children[charactor]; existed {
			temp = value
		} else {
			temp = &WordDictionary{charactor, make(map[string]*WordDictionary), i, false}
		}
		if i == len(word)-1 {
			temp.IsWord = true
		}
		current.Children[charactor] = temp
		current = temp
	}
}

/**
Returns if the word is in the data structure.
A word could contain the dot character '.' to represent any one letter.
*/
// dfs
func (this *WordDictionary) Search(word string) bool {
	var stack []*WordDictionary
	for _, value := range this.Children {
		stack = append(stack, value)
	}
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if pop.Depth < len(word) && (pop.Char == string(word[pop.Depth]) || string(word[pop.Depth]) == ".") {
			if pop.IsWord == true && pop.Depth+1 == len(word) {
				return true
			} else {
				for _, value := range pop.Children {
					stack = append(stack, value)
				}
			}
		}
	}
	return false
}

func main() {
	c := Constructor()
	c.AddWord("dad")
	c.AddWord("bad")
	c.AddWord("app")
	c.AddWord("apple")

	fmt.Println(c.Search("dad"))
	fmt.Println(c.Search("bad"))
	fmt.Println(c.Search("app"))
	fmt.Println(c.Search("apple"))

	fmt.Println(c.Search(".ad"))
	fmt.Println(c.Search(".a."))
	fmt.Println(c.Search(".b."))
	fmt.Println(c.Search(".p.."))
	fmt.Println(c.Search(".p..."))

}
