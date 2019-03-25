package main

import (
	"fmt"
	"math"
)

/*
	classic approach: Next lexicographical permutation algorithm(use a stack)
	e.g. 43143221
	- from the end, stack up the item if num[i] > num[i+1]
	- once it encounters a smaller number from the end, this is the target we want
		e.g. 43 <1> 43221
	- i need to swap the target with the value in the stack which is just larger then it
		e.g. 43 <1> 43221 => 43 <2> 43211
	- reverse the left half and put it back to the number
		e.g. 43 <2> 43211 => 43 <2> 11234
	- combine them together and form the result
		e.g. 43 <2> 11234 => 43211234

	ref:
	- https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

	Time	O(n)
	Space	O(n)
	0 ms, faster than 100.00%
*/
func nextGreaterElement(n int) int {
	// from the end, put the ascending items into a stack
	// and find the target for swapping
	remain := n
	stack := []int{}
	target := -1
	for remain > 0 {
		cur := remain % 10
		remain /= 10
		if len(stack) == 0 || cur >= stack[len(stack)-1] {
			stack = append(stack, cur)
		} else {
			target = cur
			break
		}
	}
	if target == -1 {
		return -1
	}
	// find the least larger number(>target) in the stack
	// and swap the target with the least larger number
	next := -1
	for i := 0; i < len(stack); i++ {
		if stack[i] > target {
			next = stack[i]
			stack[i] = target
			break
		}
	}
	// combine the stack, next number, and remain to form the result
	res := 0
	cnt := 0
	for len(stack) > 0 {
		pop0 := stack[0]
		stack = stack[1:]
		res = res*10 + pop0
		cnt++
	}
	res = res + next*int(math.Pow10(cnt))
	cnt++
	res = remain*int(math.Pow10(cnt)) + res
	if res > math.MaxInt32 {
		return -1
	}
	return res
}

func main() {
	fmt.Println(nextGreaterElement(21))
	fmt.Println(nextGreaterElement(12))
	fmt.Println(nextGreaterElement(43143221))
	fmt.Println(nextGreaterElement(1999999999))

	fmt.Println(nextGreaterElement(0))
	fmt.Println(nextGreaterElement(1))
}
