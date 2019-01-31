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

func main() {
	a := []int{4, 3, 2, 6, 7}
	fmt.Println(maxRotateFunction(a))

	a = []int{}
	fmt.Println(maxRotateFunction(a))

	a = []int{math.MinInt32, math.MinInt32}
	fmt.Println(maxRotateFunction(a))
}
