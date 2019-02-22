package main

import "fmt"

/*
	1st approach: hashtable

	Time	O(n)
	Space	O(n)
	32 ms, faster than 36.23%
*/
func findRepeatedDnaSequences(s string) []string {
	if len(s) < 10 {
		return []string{}
	}
	m := make(map[string]int)
	// put key into the hashtable and count the occurence of each substring
	for i := 10; i <= len(s); i++ {
		sub := s[i-10 : i]
		if _, x := m[sub]; !x {
			m[sub] = 1
		} else {
			m[sub]++
		}
	}
	// result are the key which present more than once
	res := []string{}
	for k, v := range m {
		if v > 1 {
			res = append(res, k)
		}
	}
	return res
}

func main() {
	fmt.Println(findRepeatedDnaSequences("A"))
	fmt.Println(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
	fmt.Println(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCAAAAAGGGTTT"))
}
