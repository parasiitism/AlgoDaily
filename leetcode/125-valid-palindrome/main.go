package main

import (
	"fmt"
	"strings"
)

/*
	1st approach: classic approach
	- 2 pointers: 1 from the front, 1 from the back, and check if s[i] == s[j]

	Time		O(n)
	Space		O(1)
	4 ms, faster than 96.94%
*/
func isPalindrome(s string) bool {
	i := 0
	j := len(s) - 1
	for i <= j {
		if isAlphanumeric(s[i]) && isAlphanumeric(s[j]) {
			x := strings.ToLower(string(s[i]))
			y := strings.ToLower(string(s[j]))
			if x != y {
				return false
			}
			i++
			j--
		} else if !isAlphanumeric(s[i]) {
			i++
		} else if !isAlphanumeric(s[j]) {
			j--
		} else {
			i++
			j--
		}
	}
	return true
}

func isAlphanumeric(s byte) bool {
	return (s >= 65 && s <= 90) || (s >= 97 && s <= 122) || (s >= 48 && s <= 57)
}

func main() {
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
	fmt.Println(isPalindrome("race a car"))
	fmt.Println(isPalindrome(""))
	fmt.Println(isPalindrome(" "))
	fmt.Println(isPalindrome("0P"))
	fmt.Println(isPalindrome(".,"))
	fmt.Println(isPalindrome("`l;`` 1o1 ??;l`"))
}
