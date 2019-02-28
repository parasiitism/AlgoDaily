package main

import "fmt"

/*
	1st approach: dfs
	- recursively go through all the possibilities
	- avoid duplicate computing by using a set
	Time	O(2^n)
	Space	O(2^n)
	112 ms, faster than 98.68%
*/
func letterCasePermutation(S string) []string {
	seen := make(map[string]bool)
	var dfs func(s string, curIdx int)
	dfs = func(s string, curIdx int) {
		if _, x := seen[s]; x {
			return
		}
		seen[s] = true
		for i := curIdx; i < len(s); i++ {
			if s[i] >= 97 && s[i] <= 122 {
				// clone
				clone := ""
				clone += s[:i]
				clone += string(s[i] - 32)
				clone += s[i+1:]
				dfs(clone, curIdx+1)
			} else if s[i] >= 65 && s[i] <= 90 {
				// clone
				clone := ""
				clone += s[:i]
				clone += string(s[i] + 32)
				clone += s[i+1:]
				dfs(clone, curIdx+1)
			} else {
				dfs(s, curIdx+1)
			}
		}
	}
	dfs(S, 0)
	res := []string{}
	for key := range seen {
		res = append(res, key)
	}
	return res
}

/*
	2nd approach: dfs
	- recursively go through all the possibilities
	- avoid duplicates by appending forward (curIdx), instead of iterating through a for loop in 1st approach

	Time	O(2^n)
	Space	O(2^n)
	108 ms, faster than 100.00%
*/
func letterCasePermutation1(S string) []string {
	res := []string{}
	var dfs func(s []byte, curIdx int)
	dfs = func(s []byte, curIdx int) {
		if curIdx == len(S) {
			res = append(res, string(s))
			return
		}
		if S[curIdx] >= 65 && S[curIdx] <= 90 {
			dfs(append(s, S[curIdx]), curIdx+1)
			dfs(append(s, S[curIdx]+32), curIdx+1)
		} else if S[curIdx] >= 97 && S[curIdx] <= 122 {
			dfs(append(s, S[curIdx]), curIdx+1)
			dfs(append(s, S[curIdx]-32), curIdx+1)
		} else {
			dfs(append(s, S[curIdx]), curIdx+1)
		}
	}
	dfs([]byte{}, 0)
	return res
}

func main() {
	fmt.Println(letterCasePermutation1(""))
	fmt.Println(letterCasePermutation1("C"))
	fmt.Println(letterCasePermutation1("3z4"))
	fmt.Println(letterCasePermutation1("12345"))
	fmt.Println(letterCasePermutation1("a1b2"))
	fmt.Println(letterCasePermutation1("OD7En5wEUJiP"))
}
