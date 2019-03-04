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
	88 ms, faster than 14.29%
*/
func maxProduct(nums []int) int {
	max := math.MinInt32
	for i := 0; i < len(nums); i++ {
		sum := 1
		for j := i; j >= 0; j-- {
			sum *= nums[j]
			if sum > max {
				max = sum
			}
		}
	}
	return max
}

/*
	2nd approach: Kadan's algorithm
	- idea similar to leetcode 53:maximum subarray
	- for each item, store the max&mix among itself, or extend the previous max&min with itself
		e.g. dp[i] chooses between dp[i-1]+nums[i] and nums[i]
	- the result is the largest dp[i]

	Time	O(n)
	Space	O(n)
	4 ms, faster than 100%
*/
func maxProduct1(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	dp_min := []int{nums[0]}
	dp_max := []int{nums[0]}
	res := math.MinInt64
	for i := 1; i < len(nums); i++ {
		if nums[i] > 0 {
			temp1 := findMin(dp_min[i-1]*nums[i], nums[i])
			temp2 := findMax(dp_max[i-1]*nums[i], nums[i])
			dp_min = append(dp_min, temp1)
			dp_max = append(dp_max, temp2)
		} else {
			temp1 := findMin(dp_max[i-1]*nums[i], nums[i])
			temp2 := findMax(dp_min[i-1]*nums[i], nums[i])
			dp_min = append(dp_min, temp1)
			dp_max = append(dp_max, temp2)
		}
	}
	for i := 0; i < len(dp_max); i++ {
		if dp_max[i] > res {
			res = dp_max[i]
		}
	}
	return res
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func findMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(maxProduct1([]int{2, 3, -2, 4}))
	fmt.Println(maxProduct1([]int{2, 3, -2, -4}))
	fmt.Println(maxProduct1([]int{-2, 0, -1}))
	fmt.Println(maxProduct1([]int{-2}))
	fmt.Println(maxProduct1([]int{1}))
}
