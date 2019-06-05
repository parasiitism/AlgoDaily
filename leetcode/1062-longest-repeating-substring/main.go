package main

/*
	1st approach: hashtable
	- generate all the substrings and count the occurence of each
	- the result is the substring with max length and appears more than once

	Time	O(n^2)
	Space	O(n^2)
	1392 ms, faster than 100.00%
*/
func longestRepeatingSubstring(S string) int {
	ht := make(map[string]int)
	for i := 0; i < len(S); i++ {
		for j := i; j < len(S); j++ {
			sub := S[i : j+1]
			if _, x := ht[sub]; x {
				ht[sub] += 1
			} else {
				ht[sub] = 1
			}
		}
	}
	res := 0
	for key := range ht {
		if ht[key] > 1 && len(key) > res {
			res = len(key)
		}
	}
	return res
}

func main() {

}
