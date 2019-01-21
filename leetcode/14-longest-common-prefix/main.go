package main

import "fmt"

/*
	questions to ask:
	- empty array?
	- empty string?
*/

/*
	1st approach:
	- append charactors
	Time		O(n*m)
	Space		O(m)
	4ms beats 12.9%
	21jan2019
*/
func longestCommonPrefix1(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	res := strs[0]
	for i := 1; i < len(strs); i++ {
		temp := ""
		for j := 0; j < len(strs[i]); j++ {
			if j < len(res) && strs[i][j] == res[j] {
				temp += string(res[j])
			} else {
				break
			}
		}
		res = temp
	}
	return res
}

/*
	2nd approach:
	- instead of appending charactors so many times, slice the end
	Time		O(n*m)
	Space		O(m)
	0ms beats 100%
	21jan2019
*/
func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	res := strs[0]
	for i := 1; i < len(strs); i++ {
		for j := 0; j < len(strs[i]); j++ {
			if j < len(res) && strs[i][j] != res[j] {
				res = res[:j]
				break
			}
		}
		if len(res) > len(strs[i]) {
			res = res[:len(strs[i])]
		}
	}
	return res
}

func main() {
	a := []string{
		"flower",
		"flow",
		"flight",
	}
	fmt.Println(longestCommonPrefix(a))
	a = []string{
		"dog",
		"racecar",
		"car",
	}
	fmt.Println(longestCommonPrefix(a))
	a = []string{
		"aa",
		"a",
	}
	fmt.Println(longestCommonPrefix(a))
	a = []string{
		"ca",
		"c",
	}
	fmt.Println(longestCommonPrefix(a))
	a = []string{
		"ca",
		"a",
	}
	fmt.Println(longestCommonPrefix(a))
	a = []string{
		"aca",
		"cba",
	}
	fmt.Println(longestCommonPrefix(a))
}
