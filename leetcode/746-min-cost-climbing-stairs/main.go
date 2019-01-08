package main

import (
	"fmt"
	"math"
)

// 1st approach: brute force, go over all the paths and compare the costs
// Time			O(2^n) 2 options for each number in the nums
// Space		O(2^n) callstack
// TLE
func minCostClimbingStairs(cost []int) int {
	nums := []int{}
	nums = append(nums, 0)
	nums = append(nums, cost...)
	nums = append(nums, 0)
	min := math.MaxInt64
	var dfs func(idx int, pathsum int)
	dfs = func(idx int, pathsum int) {
		if idx == len(nums)-1 {
			if pathsum < min {
				min = pathsum
			}
		} else if idx < len(nums) {
			dfs(idx+1, pathsum+nums[idx])
			dfs(idx+2, pathsum+nums[idx])
		}
	}
	dfs(0, 0)
	return min
}

/*
	2nd approach: bottom-up DP, learned from others https://zhuanlan.zhihu.com/p/32980698
	e.g. [10,15,20,30]
	dp[0] = 10
	dp[1] = 15
	dp[2] = 20 + min(dp[0], dp[1]) = 20 + 10 = 30
	dp[3] = 30 + min(dp[1], dp[2]) = 20 + 15 = 35
	dp[4] = 0  + min(dp[2], dp[3]) = 0  + 30 = 30
	Time 	O(n)
	Space	O(n) the dp array
	4ms beats 100%
*/
func minCostClimbingStairs1(cost []int) int {
	if len(cost) == 0 {
		return 0
	}
	if len(cost) == 1 {
		return cost[0]
	}
	dp := make([]int, len(cost)+1)
	dp[0] = cost[0]
	dp[1] = cost[1]
	for i := 2; i < len(cost)+1; i++ {
		curCost := 0
		if i < len(cost) {
			curCost = cost[i]
		}
		dp[i] = curCost + findMin(dp[i-1], dp[i-2])
	}
	return dp[len(cost)]
}

func findMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	fmt.Println(minCostClimbingStairs1([]int{10, 15, 20}))
	fmt.Println(minCostClimbingStairs1([]int{10, 15, 20, 30}))
	fmt.Println(minCostClimbingStairs1([]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}))
}
