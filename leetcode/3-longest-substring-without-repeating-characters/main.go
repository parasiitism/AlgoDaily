package main

import "fmt"

/*
	1st approach:
	- 2 pointers + hashtable
	- when we see a precedented char, we update the result and remove the items which values(indeces) < slow pointer

	Time	O(n^2)
	Space	O(n)
	beats 22.82%
*/
func lengthOfLongestSubstring(s string) int {
	m := make(map[string]int)
	last := 0
	res := 0
	for i := 0; i < len(s); i++ {
		c := string(s[i])
		if _, x := m[c]; !x {
			m[c] = i
		} else {
			res = max(res, i-last)
			recur := m[c]
			last = recur + 1
			m[c] = i
			for k, _ := range m {
				if m[k] < last {
					delete(m, k)
				}
			}
		}
	}
	res = max(res, len(s)-last)
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/*
	2nd approach:
	- optimize the 1st approach, hashtable
	- but we dont need to remove the item from hashtable
	- instead we can just ignore the item which index < slow pointer

	Time	O(n)
	Space	O(n)
	beats 69.67%
*/
func lengthOfLongestSubstring1(s string) int {
	m := make(map[string]int)
	last := 0
	res := 0
	for i := 0; i < len(s); i++ {
		c := string(s[i])
		if _, x := m[c]; !x {
			m[c] = i
		} else {
			recur := m[c]
			if recur >= last {
				res = max(res, i-last)
				last = recur + 1
			}
			m[c] = i
		}
	}
	res = max(res, len(s)-last)
	return res
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
	fmt.Println(lengthOfLongestSubstring("bbbbb"))
	fmt.Println(lengthOfLongestSubstring("pwwkew"))
	fmt.Println(lengthOfLongestSubstring("abcdef"))
	fmt.Println(lengthOfLongestSubstring("abcbdef"))
	fmt.Println(lengthOfLongestSubstring("abcbdee"))
	fmt.Println(lengthOfLongestSubstring("abb"))
	fmt.Println(lengthOfLongestSubstring("ab"))
	fmt.Println(lengthOfLongestSubstring("a"))

	fmt.Println("---")

	fmt.Println(lengthOfLongestSubstring1("abcabcbb"))
	fmt.Println(lengthOfLongestSubstring1("bbbbb"))
	fmt.Println(lengthOfLongestSubstring1("pwwkew"))
	fmt.Println(lengthOfLongestSubstring1("abcdef"))
	fmt.Println(lengthOfLongestSubstring1("abcbdef"))
	fmt.Println(lengthOfLongestSubstring1("abcbdee"))
	fmt.Println(lengthOfLongestSubstring1("abb"))
	fmt.Println(lengthOfLongestSubstring1("ab"))
	fmt.Println(lengthOfLongestSubstring1("a"))
}
