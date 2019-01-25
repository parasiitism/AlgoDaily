package main

import "fmt"

/*
	Questions to ask
	- empty string?
	- so if abababa, the result is 7?
*/

/*
	1st attempt
	- hashtable
	- loop to find out the occurence of previous charactor
	Time	O(n*m) m=continuous substr
	Space	O(1)
	12ms beats 17.65%
	25jan2019
*/
func lengthOfLongestSubstringTwoDistinct(s string) int {
	ht := make(map[byte]int)
	max := 0

	var check func()
	check = func() {
		sum := 0
		for _, v := range ht {
			sum += v
		}
		if sum > max {
			max = sum
		}
	}

	for i := 0; i < len(s); i++ {
		c := s[i]
		if _, x := ht[c]; x {
			ht[c]++
		} else {
			if len(ht) == 2 {
				// check if
				check()
				// delete the farther char
				prev := s[i-1]
				cnt := 0
				for j := i - 1; i >= 0; j-- {
					if s[j] != prev {
						break
					}
					cnt++
				}
				ht = make(map[byte]int)
				ht[prev] = cnt
			}
			ht[c] = 1
		}
	}
	check()
	return max
}

/*
	2nd attempt
	- hashtable
	- use a poiner to indicate the start point of a continuous charactors stream
	Time	O(n)
	Space	O(1)
	12ms beats 17.65% <- it could have been faster 🤔
	25jan2019
*/
func lengthOfLongestSubstringTwoDistinct1(s string) int {
	ht := make(map[byte]int)
	max := 0
	start := 0

	// check if sum > max
	var check func()
	check = func() {
		sum := 0
		for _, v := range ht {
			sum += v
		}
		if sum > max {
			max = sum
		}
	}

	for i := 0; i < len(s); i++ {
		c := s[i]
		if _, x := ht[c]; x {
			ht[c]++
			if c != s[i-1] {
				start = i
			}
		} else {
			if len(ht) == 2 {
				check()
				// delete the farther char
				prev := s[i-1]
				ht = make(map[byte]int)
				ht[prev] = i - start
			}
			ht[c] = 1
			start = i
		}
	}
	check()
	return max
}

func main() {
	fmt.Println(lengthOfLongestSubstringTwoDistinct(""))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("aaa"))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("aab"))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("abaccc"))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("eceba"))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("ccaabbb"))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("ccaaabbaabab"))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("ccaababab"))
}
