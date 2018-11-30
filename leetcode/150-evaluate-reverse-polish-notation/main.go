package main

import (
	"fmt"
	"strconv"
)

func evalRPN(tokens []string) int {
	if len(tokens) == 0 {
		return 0
	}
	var stack []int
	for i := 0; i < len(tokens); i++ {
		curr := tokens[i]
		if curr != "+" && curr != "-" && curr != "*" && curr != "/" {
			v, _ := strconv.Atoi(curr)
			stack = append(stack, v)
		} else {
			a := stack[len(stack)-2]
			b := stack[len(stack)-1]
			stack = stack[:len(stack)-2]
			if curr == "+" {
				temp := a + b
				stack = append(stack, temp)
			} else if curr == "-" {
				temp := a - b
				stack = append(stack, temp)
			} else if curr == "*" {
				temp := a * b
				stack = append(stack, temp)
			} else if curr == "/" {
				temp := a / b
				stack = append(stack, temp)
			}
		}
	}
	return stack[0]
}

func main() {
	fmt.Println(evalRPN([]string{"2", "1", "+", "3", "*"}))
	fmt.Println(evalRPN([]string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}))
}
