package main

import (
	"fmt"
	"strconv"
)

/*
	1st approach is in python
*/

/*
	2nd approach: brute force, bottom up with memorization
	1. go through all the paths
	2. for each path, when it comes to an end return 1
	3. memorize the substrings and their "ways" to avoid duplicate calculations
	3. the result is the sum of recursion

	Time    O(n) the length of the string, we use map to avoid duplicate substring
	Space   O(h) the height of recursion
	0 ms, faster than 100%
*/
func numDecodings(s string) int {
	seen := make(map[string]int)
	return helper(s, seen)
}

func helper(sub string, seen map[string]int) int {
	if v, x := seen[sub]; x {
		return v
	}
	if len(sub) == 0 {
		return 1
	}
	left := 0
	right := 0
	a := sub[0] - '0'
	if a > 0 {
		left = helper(sub[1:], seen)
	}
	if len(sub) > 1 {
		b, _ := strconv.Atoi(sub[:2])
		if b < 27 {
			right = helper(sub[2:], seen)
		}
	}
	seen[sub] = left + right
	return left + right
}

func main() {
	fmt.Println(numDecodings("12"))
	fmt.Println(numDecodings("226"))
	fmt.Println(numDecodings("1212"))
	fmt.Println(numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
}
