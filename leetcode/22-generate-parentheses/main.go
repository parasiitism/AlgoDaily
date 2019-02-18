package main

import "fmt"

/*
	1st approach: brute force
	1. generate all the posibilities
	2. check if each of the posibilities is a valid parentheses string

	Time	O(2^(2*n)) there are 2 possibilities for each node
	Space	O(2*n) height of recursion
	28 ms, faster than 5.34%
*/
func generateParenthesis(n int) []string {
	if n <= 0 {
		return []string{}
	}
	res := []string{}
	var permuate func(s string, i, k int)
	permuate = func(s string, i, k int) {
		if i == k {
			if isValid(s) == true {
				res = append(res, s)
			}
			return
		}
		permuate(s+"(", i+1, k)
		permuate(s+")", i+1, k)
	}
	permuate("", 0, 2*n)
	return res
}

func isValid(s string) bool {
	if len(s) == 0 {
		return true
	}
	stack := []string{}
	for i := 0; i < len(s); i++ {
		c := string(s[i])
		if c == "(" {
			stack = append(stack, c)
		} else if c == ")" {
			if len(stack) > 0 && stack[len(stack)-1] == "(" {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		}
	}
	return len(stack) == 0
}

func main() {
	fmt.Println(generateParenthesis(-1))
	fmt.Println(generateParenthesis(0))
	fmt.Println(generateParenthesis(1))
	fmt.Println(generateParenthesis(2))
	fmt.Println(generateParenthesis(3))
	fmt.Println(generateParenthesis(4))
}
