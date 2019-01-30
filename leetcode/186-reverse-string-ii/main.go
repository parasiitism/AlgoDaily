package main

import "fmt"

/*
	1st approach
	1. reverse the whole string
	2. iterate forward, reverse a word in the back if encounter a space/end of a string
	Time	O(n) 2n->n
	Space	O(1) in-place
	1096ms beats 100%
*/

func reverseWords(str []byte) {
	reverseInplace(str, 0, len(str)-1)
	start := 0
	for i := 0; i < len(str); i++ {
		if str[i] == ' ' {
			reverseInplace(str, start, i-1)
			start = i + 1
		} else if i == len(str)-1 {
			reverseInplace(str, start, i)
			start = i + 1
		}
	}
}

func reverseInplace(str []byte, start, end int) {
	for start < end {
		str[start], str[end] = str[end], str[start]
		start++
		end--
	}
}

func main() {
	a := []byte{'a', 'b', ' ', 'c', 'd'}
	reverseWords(a)
	fmt.Println(a)
}
