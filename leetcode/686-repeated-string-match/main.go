package main

import (
	"fmt"
	"strings"
)

/*
	questions to ask:
	- empty string A, B?
*/

/*
	1st approach: string indexing
	- each time when we multiply the A, check if the kA contains B
	- the max number of A is B/A+2
		e.g. abc, ccabcabcab
		there will be at most 4abc to construct ccabcabcab because bc|abc|abc|ab

	Time	O(B/A*kA) = O(kB)
	Space	O(n)
	12 ms, faster than 71.43%
*/
func repeatedStringMatch(A string, B string) int {
	if len(A) == 0 && len(B) == 0 {
		return 1
	} else if len(A) == 0 || len(B) == 0 {
		return 0
	}
	s := A
	i := 0
	maxLimit := len(B)/len(A) + 2
	for i < maxLimit {
		if strings.Index(s, B) > -1 {
			return i + 1
		}
		s += A
		i++
	}
	return -1
}

func main() {
	fmt.Println(repeatedStringMatch("", ""))
	fmt.Println(repeatedStringMatch("a", "a"))
	fmt.Println(repeatedStringMatch("a", "b"))
	fmt.Println(repeatedStringMatch("aa", "a"))
	fmt.Println(repeatedStringMatch("abcd", "cdabcdab"))
	fmt.Println(repeatedStringMatch("abcd", "bcdabcdab"))
	fmt.Println(repeatedStringMatch("abcd", "ccdabcdab"))
	fmt.Println(repeatedStringMatch("abcabcabcabc", "abac"))
	fmt.Println(repeatedStringMatch("bb", "bbbbbbb"))
}
