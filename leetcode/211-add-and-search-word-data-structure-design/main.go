package main

type WordDictionary struct {
	IsWord   bool
	Children map[string]*WordDictionary
}

/** Initialize your data structure here. */
func Constructor() WordDictionary {
	return WordDictionary{false, make(map[string]*WordDictionary)}
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
			temp = &WordDictionary{false, make(map[string]*WordDictionary)}
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
	// need depth and key in the WordDictionary
}

func main() {

}
