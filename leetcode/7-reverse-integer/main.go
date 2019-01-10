package main

import (
	"fmt"
	"math"
)

/*
	naive approach
	- get the digits in a reversed order and save them into an array
	- put them back together to form an integer
	P.S the idea is simple but there are pitfall in testcases
	- negative
	- 2^31 <= result <= 2^31-1
	- if use string operation, be careful of the leading zero
	Time	O(2logx)
	Space	O(logx) the array which saves the digits
	4ms, no beats because of leetcode update
*/
func reverse1(x int) int {
	temp := x
	sign := 1
	if x < 0 {
		sign = -1
		temp *= -1
	}
	arr := []int{}
	for temp > 0 {
		arr = append(arr, temp%10)
		temp /= 10
	}
	result := 0
	for i := 0; i < len(arr); i++ {
		result = result*10 + arr[i]
	}
	result *= sign
	if result < math.MinInt32 || result > math.MaxInt32 {
		return 0
	}
	return result
}

/*
	2nd approach: optimize the 1st approach
	- dont put the digits into an array, calculate the result in the same loop
	Time	O(logx)
	Space	O(1)
	4ms, no beats because of leetcode update
*/
func reverse(x int) int {
	temp := x
	sign := 1
	if x < 0 {
		sign = -1
		temp *= -1
	}
	result := 0
	for temp > 0 {
		pop := temp % 10
		temp /= 10
		result = result*10 + pop
	}
	result *= sign
	if result < math.MinInt32 || result > math.MaxInt32 {
		return 0
	}
	return result
}

func main() {
	fmt.Println(reverse(123))
	fmt.Println(reverse(-123))
	fmt.Println(reverse(120))
	fmt.Println(reverse(8463847412))  // 2^31 reversed
	fmt.Println(reverse(-8463847412)) // 2^31 reversed negative
	fmt.Println(reverse(7463847412))  // 2^31-1 reversed
	fmt.Println(reverse(-7463847412)) // 2^31-1 reversed negative
}
