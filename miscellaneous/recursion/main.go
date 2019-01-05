package main

import (
	"fmt"
	"strconv"
)

// introdution to backtracking
func printBinary(num int) {
	var helper func(num int, prefix string)
	helper = func(num int, prefix string) {
		if num == 0 {
			fmt.Println(prefix)
		} else {
			helper(num-1, prefix+"0")
			helper(num-1, prefix+"1")
		}
	}
	helper(num, "")
}

func printDecimal(num int) {
	var helper func(num int, prefix string)
	helper = func(num int, prefix string) {
		if num == 0 {
			fmt.Println(prefix)
		} else {
			for i := 0; i < 10; i++ {
				helper(num-1, prefix+strconv.Itoa(i))
			}
		}
	}
	helper(num, "")
}

func main() {
	printBinary(3)
	printDecimal(2)
}
