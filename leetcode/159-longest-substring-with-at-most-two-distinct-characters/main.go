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
	Time	O(n*m) m=continuous substr
	Space	O(2)
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

func main() {
	fmt.Println(lengthOfLongestSubstringTwoDistinct(""))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("aaa"))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("aab"))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("eceba"))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("ccaabbb"))
	fmt.Println(lengthOfLongestSubstringTwoDistinct("ccaababab"))
}
