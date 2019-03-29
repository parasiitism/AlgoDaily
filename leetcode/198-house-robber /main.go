package main

import "fmt"

/*
	1st approach: dynamic programming
	- divide the problem into sub problems
	- subproblem is actually the max sum at previous index
		compare 2 things:
		1. previous previous sum sum[i-2] + money at current house nums[i]
		2. max among the sum[i-1] and the money at current house nums[i]

	Time		O(n)
	Space		O(n) dp array
	0 ms, faster than 100.00%
*/
func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}
	if len(nums) == 2 {
		return max(nums[0], nums[1])
	}
	dp := []int{}
	dp = append(dp, nums[0])
	dp = append(dp, max(nums[0], nums[1]))
	for i := 2; i < len(nums); i++ {
		cur := nums[i]
		// if we rob this house, the previous house we rob is at most at houses[i-2]
		robCur := dp[i-2] + cur
		// if we dont rob this house, the max we can rob is max(cur, prev)
		notRobCur := max(dp[i-1], cur)
		// put the max we can rob in to cache
		temp := max(robCur, notRobCur)
		dp = append(dp, temp)
	}
	return dp[len(dp)-1]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/*
	2nd approach: dynamic programming
	- look at the 1st approach, we actually just need 2 variables, dp[i-2], dp[i-1]
	- so we can optimize it by just storing the prevprev sum and the prev sum

	Time		O(n)
	Space		O(1) we just need 2 variables to store the dp
	0 ms, faster than 100.00%
*/
func rob1(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}
	if len(nums) == 2 {
		return max(nums[0], nums[1])
	}
	prevprev := nums[0]
	prev := max(nums[0], nums[1])
	for i := 2; i < len(nums); i++ {
		cur := nums[i]
		// if we rob this house, the previous house we rob is at most at houses[i-2]
		robCur := prevprev + cur
		// if we dont rob this house, the max we can rob is max(cur, prev)
		notRobCur := max(prev, cur)
		// put the max we can rob in to cache
		temp := max(robCur, notRobCur)
		// dp = append(dp, temp)
		prevprev = prev
		prev = temp
	}
	return prev
}

func main() {
	fmt.Println(rob([]int{1, 2, 3, 1}))
	fmt.Println(rob([]int{2, 7, 9, 3, 1}))
	fmt.Println(rob([]int{2, 1, 1, 2}))
	fmt.Println("-----------------------------------")
	fmt.Println(rob1([]int{1, 2, 3, 1}))
	fmt.Println(rob1([]int{2, 7, 9, 3, 1}))
	fmt.Println(rob1([]int{2, 1, 1, 2}))
}
