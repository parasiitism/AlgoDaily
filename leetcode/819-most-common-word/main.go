package main

import (
	"fmt"
	"regexp"
	"strings"
)

/*
	1st approach
	1. put the banned words into a hashtable
	2. count the occurence of each word in the paragraph if it is not banned
	3. find the most freq word
	- takeaway: regexp.MustCompile(`[!?',;. ]`) and words := r.Split(paragraph, -1)
	Time    O(n)
	Space   O(n)
	8ms beats 10.53%
*/
func mostCommonWord(paragraph string, banned []string) string {
	bannedHt := make(map[string]bool)
	ht := make(map[string]int)
	for _, b := range banned {
		bannedHt[b] = true
	}
	r := regexp.MustCompile(`[!?',;. ]`)
	words := r.Split(paragraph, -1)
	for _, word := range words {
		w := strings.ToLower(word)
		if _, x := bannedHt[w]; x {
			continue
		}
		if w == "" {
			continue
		}
		if _, x := ht[w]; x {
			ht[w]++
		} else {
			ht[w] = 1
		}
	}
	resCnt := 0
	res := ""
	for key, val := range ht {
		if val > resCnt {
			resCnt = val
			res = key
		}
	}
	return res
}

func main() {
	a := "Bob hit a  ball, the hit BALL flew far after it was hit."
	// words := strings.Fields(a)
	// r := regexp.MustCompile(`[!?',;. ]`)
	// words := r.Split(a, -1)
	// for _, w := range words {
	// 	fmt.Println(w)
	// }
	fmt.Println(mostCommonWord(a, []string{"hit"}))

	a = "a, a, a, a, b,b,b,c, c"
	fmt.Println(mostCommonWord(a, []string{"a"}))

	a = "Bob!"
	fmt.Println(mostCommonWord(a, []string{"hit"}))
}
