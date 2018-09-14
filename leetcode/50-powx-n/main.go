package main

import (
	"fmt"
	"math"
)

// nonsense
func myPow0(x float64, n int) float64 {
	return math.Pow(x, float64(n))
}

// iterative
// 2^14
// n, a, b
// when n=14, 2^2, 1
// when n=7, 2^2*2^2, 2^2
// when n=3, 2^4*2^4, 2^4*2^2
// return 2^8*2^4*2^2=2^14
func myPow(x float64, n int) float64 {
	a := x
	b := 1.0
	count := n
	if n < 0 {
		count = -1 * count
	} else if n == 0 {
		return 1
	}
	for count > 1 {
		if count%2 == 0 {
			a = a * a
			count = count / 2
		} else {
			b = a * b
			a = a * a
			count = (count - 1) / 2
		}
	}
	if n < 0 {
		return 1 / (a * b)
	} else {
		return a * b
	}
}

func main() {
	a := myPow(2, 0)
	fmt.Println(a)
}
