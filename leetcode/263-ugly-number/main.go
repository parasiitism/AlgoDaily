package main

import (
	"fmt"
)

// approach 1: just math
// beats 5.43%
// however when i use "temp == 0 || r != 0", it beats 100% and I dont know why
func isUgly(num int) bool {
	// 2
	for {
		r := num % 2
		temp := num / 2
		if temp == 0 || r != 0 {
			break
		}
		num = temp
	}
	// 3
	for {
		r := num % 3
		temp := num / 3
		if temp == 0 || r != 0 {
			break
		}
		num = temp
	}
	// 5
	for {
		r := num % 5
		temp := num / 5
		if temp == 0 || r != 0 {
			break
		}
		num = temp
	}
	return num == 1
}

// 2nd attempt
// dfs recursive
// again beats 5.43%
// however when i use "temp == 0 || r != 0", it beats 100% and I dont know why
func isUgly1(num int) bool {

	// base cases
	if num == 0 {
		return false
	}
	if num == 1 || num == 2 || num == 3 || num == 5 {
		return true
	}

	// check the children
	if num%2 == 0 {
		return isUgly(num / 2)
	}
	if num%3 == 0 {
		return isUgly(num / 3)
	}
	if num%5 == 0 {
		return isUgly(num / 5)
	}

	return false
}

func main() {
	fmt.Println(isUgly(1))
	fmt.Println(isUgly(6))
	fmt.Println(isUgly(8))
	fmt.Println(isUgly(14))
}
