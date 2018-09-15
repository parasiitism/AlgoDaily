package main

import (
	"fmt"
)

// binary search between 1 and num
func isPerfectSquare(num int) bool {
	if num <= 0 {
		return false
	}
	min := 1
	max := num
	for min <= max {
		mean := (min + max) / 2
		if mean*mean == num {
			return true
		} else if mean*mean > num {
			max = mean - 1
		} else if mean*mean < num {
			min = mean + 1
		}
	}
	return false
}

func main() {
	fmt.Println(isPerfectSquare(1))
}
