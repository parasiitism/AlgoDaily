package main

import (
	"fmt"
	"math"
)

// naively search for the min for each element
// time 	O(n^2)
// space	O(1)
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

// 2 pointers
// P=slow, Q=fast, compare the arr[p]+arr[q] with calcuated minimum
// time 	O(n)
// space	O(1)
func Solution1(A []int) int {
	p := 1
	l := len(A)
	min := math.MaxUint32
	for q := 3; q < l-1; q++ {
		temp := A[p] + A[q]
		if temp < min {
			min = temp
		}
		// only set slow pointer(P) when the previous element of faster pointer is smaller
		if A[p] > A[q-1] {
			p = q - 1
		}
	}
	return min
}

func main() {
	// a := []int{5, 2, 4, 6, 3, 7}
	// a := []int{5, 2, 1, 6, 3, 7}
	// a := []int{5, 2, 4, 1, 6, 3, 7}
	a := []int{5, 2, 1, 4, 6, 3, 7}
	fmt.Println(Solution(a))
	fmt.Println(Solution1(a))
}
