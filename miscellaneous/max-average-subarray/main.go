package main

import (
	"fmt"
	"math"
)

/*
	1st approach: brute force to try all posibilities

	Time	O(n^2)
	Space	O(n)
*/
func findMaxAverage0(nums []int) float64 {
	max := math.MinInt64
	cnt := 1
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := i; j < len(nums); j++ {
			sum += nums[j]
			if sum > max {
				max = sum
				cnt = j - i + 1
			}
		}
	}
	// fmt.Println(max, cnt)
	return float64(max) / float64(cnt)
}

/*
	2nd approach: kadan's algo
	- similar to leetcode 53) and 152)

	Time	O(n)
	Space	O(n)
*/
func findMaxAverage(nums []int) float64 {
	if len(nums) == 0 {
		return 0
	}
	dp := [][]int{}
	firstItem := []int{nums[0], 1} // [sum, count] count can be either heritate from the previuous item(+1) or the item itself(1)
	dp = append(dp, firstItem)
	for i := 1; i < len(nums); i++ {
		temp := []int{}
		if dp[i-1][0]+nums[i] > nums[i] {
			temp = []int{dp[i-1][0] + nums[i], dp[i-1][1] + 1}
		} else {
			temp = []int{nums[i], 1}
		}
		dp = append(dp, temp)
	}
	res := -math.MaxFloat64
	for i := 0; i < len(dp); i++ {
		if float64(dp[i][0]) > res {
			// fmt.Println(dp[i][0], dp[i][1])
			res = float64(dp[i][0]) / float64(dp[i][1])
		}
	}
	return res
}

func main() {
	// 55/6 = 9.1666...
	fmt.Println(findMaxAverage0([]int{1, 12, -5, -6, 50, 3}))
	fmt.Println(findMaxAverage([]int{1, 12, -5, -6, 50, 3}))
}
