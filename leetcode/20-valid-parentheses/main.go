package main

import (
	"fmt"
)

func isValid(s string) bool {
	parentheses := map[string]string{
		"}": "{",
		"]": "[",
		")": "(",
	}
	var stack []string
	for i := 0; i < len(s); i++ {
		curr := string(s[i])
		if curr == "{" || curr == "[" || curr == "(" {
			stack = append(stack, curr)
		} else if len(stack) == 0 {
			return false
		} else if parentheses[curr] != stack[len(stack)-1] {
			return false
		} else {
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}

func main() {
	fmt.Println(isValid(""))
	fmt.Println(isValid("()"))
	fmt.Println(isValid("("))
	fmt.Println(isValid(")"))
	fmt.Println(isValid("(}"))
	fmt.Println(isValid("([)]"))
	fmt.Println(isValid("{[]}"))
	fmt.Println(isValid("{[[]}"))
}
