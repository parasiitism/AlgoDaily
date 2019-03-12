package main

import (
	"fmt"
	"strings"
)

/*
	1st approach:
	1. space split the sentence
	2. put the wors reversly back to the result

	Time	O(n)
	Space	O(n)
	4 ms, faster than 38.10%
*/
func reverseWords(s string) string {
	words := strings.Fields(s)
	if len(words) == 0 {
		return ""
	}
	res := words[0]
	for i := 1; i < len(words); i++ {
		res = words[i] + " " + res
	}
	return res
}

func main() {
	fmt.Println(reverseWords("the sky is blue"))
	fmt.Println(reverseWords("  hello world!  "))
	fmt.Println(reverseWords("a good   example"))
}
