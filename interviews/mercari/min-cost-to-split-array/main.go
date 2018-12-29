package main

import (
	"fmt"
	"math"
)

func Solution(A []int) int {
	l := len(A)
	min := math.MaxUint32
	for p := 1; p < l; p++ {
		for q := p + 2; q < l-1; q++ {
			temp := A[p] + A[q]
			if temp < min {
				min = temp
			}
		}
	}
	return min
}

func Solution1(A []int) int {
	p := 1
	l := len(A)
	min := math.MaxUint32
	for q := 3; q < l-1; q++ {
		temp := A[p] + A[q]
		if temp < min {
			min = temp
		}
		if A[p] > A[q-1] {
			p = q - 1
		}
	}
	return min
}

func main() {
	a := []int{5, 2, 4, 6, 3, 7}
	fmt.Println(Solution(a))
	fmt.Println(Solution1(a))
}
