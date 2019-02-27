package main

import "strings"

/*
	questions to ask:
	- empty S?
	- empty K?
	- lowercase/uppercase?

	1st approach: stack
	1. put the characters into a stack
	2. pop the stack and form the result with a limit k numbers of char per each group

	Time	O(3n)
	Space	O(n)
	224 ms, faster than 46.15%
*/

func licenseKeyFormatting(S string, K int) string {
	stack := []byte{}
	for i := 0; i < len(S); i++ {
		c := S[i]
		if c != '-' {
			stack = append(stack, c)
		}
	}
	res := ""
	cnt := 0
	for i := len(stack) - 1; i >= 0; i-- {
		if cnt == K {
			res = "-" + res
			cnt = 0
		}
		res = string(stack[i]) + res
		cnt++
	}
	return strings.ToUpper(res)
}

func main() {

}
