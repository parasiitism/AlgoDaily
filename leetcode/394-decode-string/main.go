package main

import (
	"fmt"
	"strconv"
)

type Stack struct {
	Prefix string
	Times  int
}

func decodeString(s string) string {
	stack := []Stack{}
	n := ""
	result := ""
	for i := 0; i < len(s); i++ {
		curr := string(s[i])
		num, err := strconv.Atoi(curr)
		if err == nil {
			// add digit to the number
			n += curr
		} else if curr == "[" {
			// add to stack
			num, err = strconv.Atoi(n)
			if err == nil {
				stack = append(stack, Stack{result, num})
				n = ""
				result = ""
			}
		} else if curr == "]" {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			sum := ""
			for j := 0; j < top.Times; j++ {
				sum += result
			}
			result = top.Prefix + sum
		} else {
			// for all string other than "[", "]" and numbers
			result += curr
		}
	}
	return result
}

func main() {
	fmt.Println(decodeString("3[a]2[bc]"))
	fmt.Println(decodeString("2[abc]3[cd]ef"))
	fmt.Println(decodeString("100[ab]"))
}
