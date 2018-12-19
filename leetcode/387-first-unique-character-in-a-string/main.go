package main

import "fmt"

// naive solution
// hashtable
func firstUniqChar(s string) int {
	hash := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		if _, ex := hash[s[i]]; !ex {
			hash[s[i]] = 1
		} else {
			hash[s[i]]++
		}
	}
	for i := 0; i < len(s); i++ {
		if v, _ := hash[s[i]]; v == 1 {
			return i
		}
	}
	return -1
}

func main() {
	fmt.Println(firstUniqChar("loveleetcode"))
	fmt.Println(firstUniqChar("https://leetcode.com/problems/first-unique-character-in-a-string/"))
}
