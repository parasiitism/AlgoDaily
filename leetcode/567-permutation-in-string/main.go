package main

import (
	"fmt"
)

/*
	1st approach
	- learned from others https://leetcode.com/problems/permutation-in-string/solution/
	1. use a hashtable
	2. for each substring in s2, check if it has the same characters' freq with s1
	Time		O(n^2)
	Space		O(n)
	2476ms beats 0%
*/
func checkInclusion1(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}
	s1ht := make(map[byte]int)
	// put keywords into a hashtable with key: freq
	for i := 0; i < len(s1); i++ {
		key := s1[i]
		if _, x := s1ht[key]; x {
			s1ht[key]++
		} else {
			s1ht[key] = 1
		}
	}
	// itereate the s2: for each iterate, check if substr of s2 has the same characters freq of s1
	for i := 0; i <= len(s2)-len(s1); i++ {
		s2ht := make(map[byte]int)
		for j := i; j < i+len(s1); j++ {
			key := s2[j]
			if _, x := s2ht[key]; x {
				s2ht[key]++
			} else {
				s2ht[key] = 1
			}
		}
		// check if the key : freq equal
		found := true
		for k, f1 := range s1ht {
			if f2, x := s2ht[k]; x {
				if f1 != f2 {
					found = false
					break
				}
			} else {
				found = false
				break
			}
		}
		if found {
			return true
		}
	}
	return false
}

/*
	2nd approach
	- optimize the 1st appraoch with a [26]int{}
	Time		O(n^2)
	Space		O(n)
	72ms beats 40%
*/
func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}
	s1ht := [26]int{}
	// put keywords into a hashtable with key: freq
	for i := 0; i < len(s1); i++ {
		key := s1[i] - 'a'
		s1ht[key]++
	}
	// itereate the s2: for each iterate, check if substr of s2 has the same characters freq of s1
	for i := 0; i <= len(s2)-len(s1); i++ {
		s2ht := [26]int{}
		for j := i; j < i+len(s1); j++ {
			key := s2[j] - 'a'
			s2ht[key]++
		}
		// check if the key : freq equal
		found := true
		for k, f1 := range s1ht {
			if s2ht[k] > 0 && s2ht[k] != f1 {
				found = false
				break
			}
		}
		if found {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(checkInclusion("a", "a"))
	fmt.Println(checkInclusion("a", "eab"))
	fmt.Println(checkInclusion("eab", "a"))
	fmt.Println(checkInclusion("ab", "eidbaooo"))
	fmt.Println(checkInclusion("ab", "eidboaooo"))
	fmt.Println(checkInclusion("aba", "eidbaaooo"))
	fmt.Println(checkInclusion("abao", "eidbaaooo"))
	fmt.Println(checkInclusion("oabao", "oidbaao"))
}
