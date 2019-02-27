package main

import (
	"fmt"
	"strings"
)

/*
	1st approach: replace string
	- for each substring, check if the remaining string will be empty if we replace the substring with empty

	Time    O(n^2)
	Space   O(1)
	716 ms, faster than 7.41%
*/
func repeatedSubstringPattern(s string) bool {
	for i := 1; i < len(s)/2+1; i++ {
		sub := s[:i]
		if check(s[i:], sub) {
			return true
		}
	}
	return false
}

func check(s, sub string) bool {
	x := strings.Replace(s, sub, "", -1)
	return len(x) == 0
}

/*
	2nd approach: WTF
	- https://www.jianshu.com/p/4406bf26366e

	e.g.1
	S = abcabc
	SS = bcabcabcab <= (S+S)[1:-1] stripe out the front and end
	check of S is in SS, bc|abcabc|ab <= return true

	e.g.2
	S = abcab
	SS = bcababca <= (S+S)[1:-1] stripe out the front and end
	check of S is in SS, return false

	Time	O(n)
	Space	O(n)
	4ms beats 100%
*/
func repeatedSubstringPattern1(s string) bool {
	ss := s + s
	ss = ss[1 : len(ss)-1]
	return strings.Index(ss, s) > -1
}

func main() {
	fmt.Println(repeatedSubstringPattern1("a"))
	fmt.Println(repeatedSubstringPattern1("ab"))
	fmt.Println(repeatedSubstringPattern1("aa"))
	fmt.Println(repeatedSubstringPattern1("aaa"))
	fmt.Println(repeatedSubstringPattern1("abab"))
	fmt.Println(repeatedSubstringPattern1("ababa"))
	fmt.Println(repeatedSubstringPattern1("abcabc"))
	fmt.Println(repeatedSubstringPattern1("abccda"))
}
