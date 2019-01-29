package main

import (
	"fmt"
	"strings"
)

/*
	1st approach
	- 2A must contain a rotated string
	Time	O(n) indexOf
	Space	O(n)
	0ms beats 100%
*/
func rotateString(A string, B string) bool {
	C := A + A
	return strings.Index(C, B) > -1 && len(B) == len(A)
}

func main() {
	a := "abcdeabcde"
	fmt.Println(strings.Index(a, "abced"))
}
