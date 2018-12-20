package main

import (
	"fmt"
	"sort"
	"strings"
)

// 1st attempt: hashtable
// 1 pass for iterating the words and put the words into corresponding hashtable
// 1 pass for grouping the values from hashtable into the result
// Time O(n) n:number of characters
// Space O(m*n) m:number of keys, it depends on the characters composition in the input
// beats 96.55%
func groupAnagrams(strs []string) [][]string {
	hash := make(map[string][]string)
	for i := 0; i < len(strs); i++ {
		word := strs[i]
		key := SortString(strs[i])
		if _, x := hash[key]; x {
			hash[key] = append(hash[key], word)
		} else {
			hash[key] = []string{word}
		}
	}
	result := [][]string{}
	for key := range hash {
		result = append(result, hash[key])
	}
	return result
}

func SortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func main() {
	a := []string{
		"eat", "tea", "tan", "ate", "nat", "bat",
	}
	fmt.Println(groupAnagrams(a))
}
