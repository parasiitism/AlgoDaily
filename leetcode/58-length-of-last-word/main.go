package main

import (
	"fmt"
	"strings"
)

/*
	- trim the string
	- iterate from the back until it reaches an empty string
	- not a good question actually
	Time		O(n)
	Space		O(1)
	18jan2019
*/
func lengthOfLastWord(s string) int {
	a := strings.Trim(s, " ")
	cnt := 0
	for i := len(a) - 1; i >= 0; i-- {
		if a[i] == ' ' {
			break
		}
		cnt++
	}
	return cnt
}

func main() {
	fmt.Println(lengthOfLastWord("Hello World"))
	fmt.Println(lengthOfLastWord("Hello World "))
	fmt.Println(lengthOfLastWord(""))
	fmt.Println(lengthOfLastWord(" "))
	fmt.Println(lengthOfLastWord("Hello World a "))
	fmt.Println(lengthOfLastWord("Hello World a"))
}
