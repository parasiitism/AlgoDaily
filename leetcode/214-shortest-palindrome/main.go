package main

/*
	1st approach:
	- reverse str
	- append the reveresed str to the original str character by character and check if the combo is a palindrome

	Time    O(n^2)
	Space   O(n)
	308 ms, faster than 12.16%
*/
func shortestPalindrome(s string) string {
	rStr := reverseStr(s)
	for i := 0; i < len(s); i++ {
		temp := rStr[:i] + s
		if isPalindrome(temp) == true {
			return temp
		}
	}
	return ""
}

func reverseStr(s string) string {
	res := ""
	for i := 0; i < len(s); i++ {
		res = string(s[i]) + res
	}
	return res
}

func isPalindrome(s string) bool {
	left := 0
	right := len(s) - 1
	for left < right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}
	return true
}

func main() {

}
