package main

import "fmt"

func wordBreak(s string, wordDict []string) bool {
	wordSet := make(map[string]bool)
	maxLength := 0
	for _, w := range wordDict {
		if len(w) > maxLength {
			maxLength = len(w)
		}
		wordSet[w] = true
	}
	m := make(map[string]bool)
	return find(s, wordSet, m, maxLength)
}

func find(s string, wordSet, m map[string]bool, maxLength int) bool {
	if len(s) == 0 {
		return true
	}
	if v, x := m[s]; x {
		return v
	}
	ifAnyTrue := false
	for i := 1; i <= len(s) && i <= maxLength; i++ {
		w := s[:i]
		if _, x := wordSet[w]; x {
			temp := find(s[i:], wordSet, m, maxLength)
			ifAnyTrue = ifAnyTrue || temp
		}
	}
	m[s] = ifAnyTrue
	return ifAnyTrue
}

func main() {
	s := "applepenapple"
	d := []string{"apple", "pen"}
	fmt.Println(wordBreak(s, d))

	s = "catsandog"
	d = []string{"cats", "dog", "sand", "and", "cat"}
	fmt.Println(wordBreak(s, d))

	s = "catsanddog"
	d = []string{"cats", "dog", "sand", "and", "cat"}
	fmt.Println(wordBreak(s, d))

	s = "catsandog"
	d = []string{"cats", "dog", "sand", "and", "cat", "og"}
	fmt.Println(wordBreak(s, d))

	s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
	d = []string{"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
		"aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"}
	fmt.Println(wordBreak(s, d))
}
