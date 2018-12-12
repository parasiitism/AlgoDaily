package main

import (
	"fmt"
)

// approach 1: just math
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

func main() {
	fmt.Println(isUgly(1))
	fmt.Println(isUgly(6))
	fmt.Println(isUgly(8))
	fmt.Println(isUgly(14))
}
