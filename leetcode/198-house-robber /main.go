package main

import "fmt"

/*
	1st approach: dynamic programming
	- divide the problem into sub problems
	- subproblem is actually the max sum at previous index
		compare 2 things:
		1. previous previous sum[i-2] + money at current house nums[i]
		2. previous sum[i-1]

	e.g. [1,100,2,3,1000]
	dp[0] = 1
	dp[1] = 100
	dp[2] = max(dp[0]+2, dp[1]) = 100
	dp[3] = maxdp[1]+3, dp[2]) = 103
	dp[4] = max(dp[2]+1000, dp[3]) = 1100

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
		// if we dont rob this house, the max we can rob the previous house
		notRobCur := dp[i-1]
		// put the max we can rob into the cache
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
		// if we dont rob this house, the max we can rob the previous house
		notRobCur := prev
		// put the max we can rob into the cache
		temp := max(robCur, notRobCur)
		// dp = append(dp, temp)
		prevprev = prev
		prev = temp
	}
	return prev
}

/*
	3rd approach: dynamic programming
	- more concise

	Time		O(n)
	Space		O(1) we just need 2 variables to store the dp
	0 ms, faster than 100.00%
*/
func rob2(nums []int) int {
	prevprev := 0
	prev := 0
	for i := 0; i < len(nums); i++ {
		cur := nums[i]
		// put the max we can rob into the cache
		temp := max(prevprev+cur, prev)
		// dp = append(dp, temp)
		prevprev = prev
		prev = temp
	}
	return prev
}

/*
	follow-up: print the path as well
*/
func rob3(nums []int) (int, []int) {
	prevprev := 0
	prevprevArr := []int{}
	prev := 0
	prevArr := []int{}
	for i := 0; i < len(nums); i++ {
		cur := nums[i]
		// put the max we can rob into the cache
		temp := max(prevprev+cur, prev)
		tempArr := prevArr
		if prevprev+cur > prev {
			temp = prevprev + cur
			tempArr = append(prevprevArr, cur)
		} else {
			temp = prev
		}
		prevprev = prev
		prevprevArr = prevArr
		prev = temp
		prevArr = tempArr
	}
	return prev, prevArr
}

func main() {
	fmt.Println(rob([]int{1, 2, 3, 1}))
	fmt.Println(rob([]int{2, 7, 9, 3, 1}))
	fmt.Println(rob([]int{2, 1, 1, 2}))
	fmt.Println(rob([]int{100, 1, 2, 3, 1000}))
	fmt.Println("-----------------------------------")
	fmt.Println(rob1([]int{1, 2, 3, 1}))
	fmt.Println(rob1([]int{2, 7, 9, 3, 1}))
	fmt.Println(rob1([]int{2, 1, 1, 2}))
	fmt.Println(rob1([]int{100, 1, 2, 3, 1000}))
	fmt.Println("-----------------------------------")
	fmt.Println(rob2([]int{1, 2, 3, 1}))
	fmt.Println(rob2([]int{2, 7, 9, 3, 1}))
	fmt.Println(rob2([]int{2, 1, 1, 2}))
	fmt.Println(rob2([]int{100, 1, 2, 3, 1000}))
	fmt.Println("-----------------------------------")
	fmt.Println(rob3([]int{1, 2, 3, 1}))
	fmt.Println(rob3([]int{2, 7, 9, 3, 1}))
	fmt.Println(rob3([]int{2, 1, 1, 2}))
	fmt.Println(rob3([]int{100, 1, 2, 3, 1000}))
}
