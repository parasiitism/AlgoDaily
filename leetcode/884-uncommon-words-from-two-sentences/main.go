package main

import "strings"

/*
	naive approach
	- for word, search for it occurence in the rest the string
	Time 	O(n^2)
	Space	O(1)
*/

/*
	1st approach
	- hashtable
	Time 	O(2n)
	Space	O(n)
	0ms beats 100%
*/
func uncommonFromSentences(A string, B string) []string {
	C := A + " " + B
	words := strings.Fields(C)
	ht := make(map[string]int)
	for _, w := range words {
		if _, x := ht[w]; x {
			ht[w]++
		} else {
			ht[w] = 1
		}
	}

	res := []string{}
	for k, v := range ht {
		if v == 1 {
			res = append(res, k)
		}
	}
	return res
}

func main() {

}
