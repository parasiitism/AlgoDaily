package main

import (
	"fmt"
)

/*
	approach 1: hash table
*/

// type but, in my opinion, it is a class
type Trie struct {
	IsWord   bool
	Children map[byte]*Trie
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{false, make(map[byte]*Trie)}
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	current := this
	for i := 0; i < len(word); i++ {
		charactor := word[i]
		var temp *Trie
		if value, existed := current.Children[charactor]; existed {
			temp = value
		} else {
			temp = &Trie{false, make(map[byte]*Trie)}
		}
		if i == len(word)-1 {
			temp.IsWord = true
		}
		current.Children[charactor] = temp
		current = temp
	}
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	current := this
	for i := 0; i < len(word); i++ {
		charactor := word[i]
		if value, existed := current.Children[charactor]; existed {
			if i == len(word)-1 && value.IsWord {
				return true
			}
			current = value
		} else {
			return false
		}
	}
	return false
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	current := this
	for i := 0; i < len(prefix); i++ {
		charactor := prefix[i]
		if value, existed := current.Children[charactor]; existed {
			if i == len(prefix)-1 {
				return true
			}
			current = value
		} else {
			return false
		}
	}
	return false
}

func main() {
	t := Constructor()
	t.Insert("abc")
	t.Insert("app")
	fmt.Println(t)
	fmt.Println(t.Search("appp"))
	fmt.Println(t.StartsWith("a"))
}
