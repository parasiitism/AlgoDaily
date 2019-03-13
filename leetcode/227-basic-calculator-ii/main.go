package main

import (
	"fmt"
	"unicode"
)

/*
	2nd approach:
	- 1 stack for saving the numbers
	- 1 buffer for number(cos it might have more than one digit)
	- 1 buffer for operand
	- if the current character is a digit, sum up with the previous digit e.g. `"23" -> 2*10+3`
	- if the current character is an operand
	1. operate the number with the previous operand
	2. and put the result into the stack
	3. set the current character as the next operand
	- sum up all the numbers in the stack to get the result

	takeaway:
	- unicode.IsDigit()
	- rune, byte transform

	Time    O(2n)
	Space   O(n) the stack
	4 ms, faster than 97.37%
*/

func calculate(s string) int {
	stack, operand, curNum := []int{}, '+', 0
	for i := 0; i < len(s); i++ {
		if unicode.IsDigit(rune(s[i])) == true {
			curNum = curNum*10 + int(s[i]) - 48 // " sum up the multi-digit number e.g. "23" -> 2*10+3
		}
		if i+1 == len(s) || (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {
			if operand == '+' {
				stack = append(stack, curNum)
			} else if operand == '-' {
				stack = append(stack, -curNum)
			} else if operand == '*' {
				pop, stack := stack[len(stack)-1], stack[:len(stack)-1] // pop stack
				stack = append(stack, pop*curNum)                       // mutate the value and add it back
			} else if operand == '/' {
				pop, stack := stack[len(stack)-1], stack[:len(stack)-1] // pop stack
				stack = append(stack, pop/curNum)                       // mutate the value and add it back
			}
			operand = rune(s[i]) // reset operand
			curNum = 0           // reset current number
		}
	}
	result := 0 // sum up the numbers in the stack
	for _, num := range stack {
		result += num
	}
	return result
}

func main() {
	/*
		47
		1
		-1
		5
		13
		7
		6
		45
		-5
		-2147483647
	*/
	fmt.Println(calculate("3+22*2"))
	fmt.Println(calculate(" 3/2 "))
	fmt.Println(calculate(" 0-3/2"))
	fmt.Println(calculate(" 3+5 / 2"))
	fmt.Println(calculate(" 14-3/2"))
	fmt.Println(calculate("3+5/2*2"))
	fmt.Println(calculate("1+2 *5/3+6/4*2"))
	fmt.Println(calculate("100-1-2-3-4-5-6-7-8-9-10"))
	fmt.Println(calculate("0-5"))
	fmt.Println(calculate("0-2147483647"))
}
