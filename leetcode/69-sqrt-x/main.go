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

// lower bound binary search based on 1 <= x <= x^2 for all x > 0
func mySqrt2(x int) int {
	min := 1
	max := x
	if min == max {
		return x
	}
	var middle int
	for min < max {
		middle = (min + max) / 2
		if middle*middle == x {
			return middle
		} else if middle*middle < x {
			min = middle + 1
		} else if middle*middle > x {
			max = middle
		}
	}
	return min - 1
}

func main() {
	fmt.Println(mySqrt2(120))
}
