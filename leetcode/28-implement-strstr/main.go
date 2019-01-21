package main

import "fmt"

/*
	Questions to ask:
	- haystack is empty?
	- needle is empty?
	- haystack and needle are empty?
	- haystack=abc, needle=bcd not found?
*/

/*
	1st approach:
	- brute force
	- for each char, check if the later chars between haystack and needle are the same
	Time		O(n^2)
	Space		O(1)
	544ms beats 2.04%
	21jan2019
*/
func strStr1(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}
	for k := 0; k < len(haystack); k++ {
		i := k
		j := 0
		start := -1
		for i < len(haystack) && j < len(needle) {
			if haystack[i] == needle[j] {
				if j == 0 {
					start = i
				}
				if j == len(needle)-1 {
					return start
				}
				j++
			} else {
				break
			}
			i++
		}
	}
	return -1
}

/*
	1st approach:
	- brute force
	- for each char, check if the later chars between haystack and needle are the same
	Time		O(n)
	Space		O(1)
	544ms beats 100%
	21jan2019
*/
func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}
	lenN := len(needle)
	for i := 0; i < len(haystack)-lenN+1; i++ {
		if haystack[i:i+lenN] == needle {
			return i
		}
	}
	return -1
}

func main() {
	fmt.Println(strStr("", ""))
	fmt.Println(strStr("da", ""))
	fmt.Println(strStr("", "a"))
	fmt.Println(strStr("a", "a"))
	fmt.Println(strStr("hello", "ll"))
	fmt.Println(strStr("hello", "llg"))
	fmt.Println(strStr("aaaaa", "bba"))
	fmt.Println(strStr("abcdeabcde", "bc"))
	fmt.Println(strStr("abcdeabcde", "de"))
	fmt.Println(strStr("abcdeabcde", "deg"))
	fmt.Println(strStr("mississippi", "issip"))
	fmt.Println(strStr("aabaabbbaabbbbabaaab", "abaa"))
}
