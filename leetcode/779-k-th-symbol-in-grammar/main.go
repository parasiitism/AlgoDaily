package main

import "fmt"

/*
	1st approach: better brute force
	Time	O(2^n)
	Space	O(1)
	TLE
*/
func kthGrammar0(N int, K int) int {
	s := "0"
	i := 0
	for i < N {
		temp := ""
		for j := 0; j < len(s); j++ {
			c := s[j]
			if c == '0' {
				temp += "01"
			} else {
				temp += "10"
			}
			// actually it doesn't help when K is big
			if len(temp) >= K {
				s = temp
				i++
				break
			}
		}
		s = temp
		i++
	}
	return int(s[K-1] - '0')
}

/*
	suggested solution: tricky recursion
	- see ./idea.jpeg
	- http://www.cnblogs.com/grandyang/p/9027098.html
	- https://leetcode.com/articles/k-th-symbol-in-grammar/

	Time	O(n)
	Space	O(h)
*/
func kthGrammar(N int, K int) int {
	if N == 1 {
		return 0
	}
	// if K is an even
	if K%2 == 0 {
		// if parent is zero
		if kthGrammar(N-1, K/2) == 0 {
			return 1
		} else {
			// if parent is 1
			return 0
		}
	} else { // if K is an odd
		// if parent is zero
		if kthGrammar(N-1, (K+1)/2) == 0 {
			return 0
		} else {
			// if parent is 1
			return 1
		}
	}
}

func main() {
	fmt.Println(kthGrammar(1, 1))
	fmt.Println(kthGrammar(2, 1))
	fmt.Println(kthGrammar(2, 2))
	fmt.Println(kthGrammar(4, 5))
	fmt.Println(kthGrammar(5, 5))
	fmt.Println(kthGrammar(30, 536870912))
}
