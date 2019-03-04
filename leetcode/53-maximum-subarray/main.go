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

/*
	2nd approach: dynamic programming, kadan's algorithm
	- for each item, store the max among itself, or extend the previous max with itself
		e.g. dp[i] chooses between dp[i-1]+nums[i] and nums[i]
	- the result is the largest dp[i]

	Time	O(n)
	Space	O(n)
	4 ms, faster than 100.00%

	ref:
	- https://www.youtube.com/watch?v=2MmGzdiKR9Y
*/
func maxSubArray1(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	dp := []int{nums[0]}
	for i := 1; i < len(nums); i++ {
		temp := findMax(dp[i-1]+nums[i], nums[i])
		dp = append(dp, temp)
	}
	res := math.MinInt64
	for i := 0; i < len(dp); i++ {
		if dp[i] > res {
			res = dp[i]
		}
	}
	return res
}

func findMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/*
	3rd approach: dynamic programming, kadan's algorithm
	- for each item, store the max among itself, or extend the previous max with itself
		e.g. dp[i] chooses between dp[i-1]+nums[i] and nums[i]
	- the result is the largest dp[i]
	- optimize the 2nd approach by using store one variable for dp array cos for each item
	we just need to compare with previous item result

	Time	O(n)
	Space	O(1)
	4 ms, faster than 100.00%

	ref:
	- https://www.youtube.com/watch?v=2MmGzdiKR9Y
*/
func maxSubArray2(nums []int) int {
	dp := math.MinInt32
	res := math.MinInt32
	for i := 0; i < len(nums); i++ {
		dp = findMax(dp+nums[i], nums[i])
		res = findMax(res, dp)
	}
	return res
}

/*
	another solution: divide and conquer: O(nlogn)
	ref:
	- https://leetcode.com/problems/maximum-subarray/discuss/20497/Python-O(n)-solution-and-divide-and-conquer-O(nlogn)-solution
	- https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
*/

func main() {
	fmt.Println(maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))

	fmt.Println(maxSubArray1([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))

	fmt.Println(maxSubArray2([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))
}
