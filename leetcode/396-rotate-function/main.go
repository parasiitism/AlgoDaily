package main

import (
	"fmt"
	"math"
)

/*
	Questions to ask:
	- what is the range of each number? -2^32->2^32-1 ?
	- will there be an empty array
	- how big will be the input array?
*/

/*
	1st approach
	- set B = A+A, and calculate the sum from the middle of B
		e.g. for [4, 3, 2, 6]
		4 3 2 6 4 3 2 6
						[			]
					[			]
				[			]
			[			]

	Time		O(n^2)
	Space		O(2n) for the B
	428 beats 100%
*/
func maxRotateFunction(A []int) int {
	B := []int{}
	B = append(B, A...)
	B = append(B, A...)
	max := math.MinInt64
	for i := len(A); i > 0; i-- {
		temp := 0
		for j := 0; j < len(A); j++ {
			temp += j * B[i+j]
		}
		if temp > max {
			max = temp
		}
	}
	if max == math.MinInt64 {
		return 0
	}
	return max
}

/*
	2nd approach
	- learned from others https://leetcode.com/problems/rotate-function/discuss/87842/Java-Solution-O(n)-with-non-mathametical-explaination
	F(0) = (0A) + (1B) + (2C) + (3D) + (4E)
				 (-1A) + (1B) + (2C) + (3D) + (4E)
	F(1) = (4A) + (0B) + (1C) + (2D) + (3E)
				 (3A) + (-1B) + (0C) + (1D) + (2E)
	F(2) = (3A) + (4B) + (0C) + (1D) + (2E)
	Time		O(2n)
	Space		O(n)
	8ms beats 100%
*/
func maxRotateFunction1(A []int) int {
	sum := 0
	f := 0
	// calculate the sum
	for i := 0; i < len(A); i++ {
		sum += A[i]
		f += i * A[i]
	}
	// calculate the iteration
	max := f
	for i := 1; i < len(A); i++ {
		f = f - sum + A[i-1]*len(A)
		if f > max {
			max = f
		}
	}
	return max
}

func main() {
	a := []int{4, 3, 2, 6, 7}
	fmt.Println(maxRotateFunction1(a))

	a = []int{}
	fmt.Println(maxRotateFunction1(a))

	a = []int{math.MinInt32, math.MinInt32}
	fmt.Println(maxRotateFunction1(a))
}
