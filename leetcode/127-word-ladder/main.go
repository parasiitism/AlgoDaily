package main

import "fmt"

/*
	2nd approach: BFS + hashset to avoid loop
	- but this time we change the word to get the next combination instead of finding it from the wordList,
	because there might be a lot of words in the wordList which just have 1 digit difference

	Time    O(n^26*wordLength) for each word, traverse the similar words
	Space   O(n)
	156 ms, faster than 72.48%
*/
func ladderLength(beginWord string, endWord string, wordList []string) int {
	wordListSet := make(map[string]bool)
	for _, word := range wordList {
		wordListSet[word] = true
	}
	q := []Item{}
	q = append(q, Item{beginWord, 1})
	seen := make(map[string]bool)
	alphabets := "abcdefghijklmnopqrstuvwxyz"
	for len(q) > 0 {
		item := q[0]
		q = q[1:]
		word := item.Word
		level := item.Level
		if word == endWord {
			return level
		}
		for i := 0; i < len(word); i++ {
			for j := 0; j < 26; j++ {
				c := string(alphabets[j])
				newWord := word[:i] + c + word[i+1:]
				if _, x := wordListSet[newWord]; x {
					if _, x1 := seen[newWord]; !x1 {
						q = append(q, Item{newWord, level + 1})
						seen[newWord] = true
					}
				}
			}
		}
	}
	return 0
}

type Item struct {
	Word  string
	Level int
}

func main() {
	a := "hit"
	b := "cog"
	c := []string{"hot", "dot", "dog", "lot", "log", "cog"}
	fmt.Println(ladderLength(a, b, c))
}
