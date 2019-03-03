package main

import "fmt"

/*
	1st approach: combinations, dfs in recursion
	1. for 13,a->d, a->e, a->f...so on
	2. quite similar to permutation problem

	Time	O(3^n*3^m)
	Space	O(3^n*3^m)
	n: number of 3 characters digits like 1->abc
	m: number of 4 characters digits like 9->wxyz
	0 ms, faster than 100.00%
*/
func letterCombinations(digits string) []string {
	mapping := make(map[byte][]string)
	mapping['2'] = []string{"a", "b", "c"}
	mapping['3'] = []string{"d", "e", "f"}
	mapping['4'] = []string{"g", "h", "i"}
	mapping['5'] = []string{"j", "k", "l"}
	mapping['6'] = []string{"m", "n", "o"}
	mapping['7'] = []string{"p", "q", "r", "s"}
	mapping['8'] = []string{"t", "u", "v"}
	mapping['9'] = []string{"w", "x", "y", "z"}

	res := []string{}

	var dfs func(prefix string, idx int)
	dfs = func(prefix string, idx int) {
		if idx == len(digits) {
			if len(prefix) > 0 {
				res = append(res, prefix)
			}
			return
		}
		digit := digits[idx]
		if v, x := mapping[digit]; x {
			for i := 0; i < len(v); i++ {
				dfs(prefix+v[i], idx+1)
			}
		} else {
			dfs(prefix, idx+1)
		}
	}
	dfs("", 0)
	return res
}

func main() {
	fmt.Println(letterCombinations(""))
	fmt.Println(letterCombinations("23"))
	fmt.Println(letterCombinations("13"))
	fmt.Println(letterCombinations("13#4"))
}
