package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

// 1st attempt: hashtable
// 1 pass for iterating the words and put the words into corresponding hashtable
// 1 pass for grouping the values from hashtable into the result
// Time O(n*klogk) n:number of words, k:length of charactors, klogk is due to the sorting
// Space O(k*n)
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

// 2nd attempt: hashtable but base on charactor count
// although it doesnt sort(nlogn), it runs slower than the 1st due to the string manipulation
// Time O(n*2m) n:number of words, k:length of charactors, klogk is due to the sorting
// Space O(k*n)
// beats 89.66%
func groupAnagrams1(strs []string) [][]string {
	hash := make(map[string][]string)
	for i := 0; i < len(strs); i++ {
		word := strs[i]
		key := charCount(strs[i])
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

func charCount(s string) string {
	charCnt := [26]int{}
	for i := 0; i < len(s); i++ {
		charCnt[s[i]-'a']++
	}
	result := ""
	for i := 0; i < len(charCnt); i++ {
		result += strconv.Itoa(charCnt[i]) + ","
	}
	return result
}

func main() {
	a := []string{
		"eat", "tea", "tan", "ate", "nat", "bat",
	}
	fmt.Println(groupAnagrams1(a))
}
