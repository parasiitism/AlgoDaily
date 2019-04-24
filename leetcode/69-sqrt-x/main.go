package main

import (
	"fmt"
	"math"
)

// solution 1: just use math.sqrt
func mySqrt1(x int) int {
	y := math.Sqrt(float64(x))
	return int(y)
}

/*
	2nd: upper bound binary search
	- since 1 <= x <= x^2 for all x > 0
	- we are going to search for a number that which sqaure is just right a bit larger than x

	e.g. 8
	1 2 3 4 5 6 7 8
	^             ^

	1 2 3 4 5 6 7 8
	^     ^

	1 2 3 4 5 6 7 8
		^   ^

	1 2 3 4 5 6 7 8
			^

	Time    O(logn)
	Space   O(1)
	8 ms, faster than 31.63%
	24apr2019
*/
func mySqrt2(x int) int {
	left := 1
	right := x
	if left == right {
		return x
	}
	var mid int
	for left < right {
		mid = (left + right) / 2
		if x >= mid*mid {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left - 1
}

func main() {
	fmt.Println(mySqrt2(120))
}
