package main

import (
	"fmt"
	"math"
)

/*
	1st approach:
	- idea similar to prefix sum
	- generate all subarrays to compare with the intermediate result

	Time	O(n^2)
	Space	O(1)
	84 ms, faster than 7.06%
*/
func maxSubArray(nums []int) int {
	max := math.MinInt64
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := i; j >= 0; j-- {
			sum += nums[j]
			if sum > max {
				max = sum
			}
		}
	}
	return max
}

func main() {
	fmt.Println(maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))
}
