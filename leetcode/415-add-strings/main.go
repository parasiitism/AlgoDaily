package main

import (
	"fmt"
	"strconv"
)

/*
	1st approach: stack
	1. put the numbers into 2 stacks
	2. store the carry and add it to the next digit

	corner cases:
	1. 9 + 1 => 10
	2. "" => "0"

	8 ms, faster than 58.33%
*/
func addStrings(num1 string, num2 string) string {
	stack1 := []int{}
	stack2 := []int{}
	for _, c := range num1 {
		stack1 = append(stack1, int(c-'0'))
	}
	for _, c := range num2 {
		stack2 = append(stack2, int(c-'0'))
	}
	carry := 0
	res := ""
	for len(stack1) > 0 || len(stack2) > 0 {
		v1 := 0
		if len(stack1) > 0 {
			v1 = stack1[len(stack1)-1]
			stack1 = stack1[:len(stack1)-1]
		}
		v2 := 0
		if len(stack2) > 0 {
			v2 = stack2[len(stack2)-1]
			stack2 = stack2[:len(stack2)-1]
		}
		x := v1 + v2 + carry
		carry = x / 10
		x = x % 10
		res = strconv.Itoa(x) + res
	}
	if carry > 0 {
		res = "1" + res
	}
	if len(res) == 0 {
		return "0"
	}
	return res
}

func main() {
	fmt.Println(addStrings("0", "0"))
	fmt.Println(addStrings("123", "1"))
	fmt.Println(addStrings("123", "45"))
}
