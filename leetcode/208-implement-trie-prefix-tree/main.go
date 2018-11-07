package main

import (
	"fmt"
)

// type but, in my opinion, it is a class
type Trie struct {
	isWord   bool
	children map[string]Trie
}

/** Initialize your data structure here. */
func Constructor() Trie {
	root := Trie{false, make(map[string]Trie)}
	return root
}

// /** Inserts a word into the trie. */
// func (this *Trie) Insert(word string) {

// }

// /** Returns if the word is in the trie. */
// func (this *Trie) Search(word string) bool {

// }

// /** Returns if there is any word in the trie that starts with the given prefix. */
// func (this *Trie) StartsWith(prefix string) bool {

// }

func main() {
	var hashtable = make(map[string]string)
	fmt.Println(hashtable)
	hashtable["a"] = "calvi"
	hashtable["b"] = "calvin"
	fmt.Println(hashtable)

	// a_node := make(map[string]Trie)
	// a_node["b"] = nil
	// b := Trie{false, a_node}
	a := Trie{false, make(map[string]Trie)}
	fmt.Println(a)
	b := Trie{false, make(map[string]Trie)}
	a.children["a"] = b
	fmt.Println(a)
}
