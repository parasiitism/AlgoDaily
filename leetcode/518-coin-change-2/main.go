package main

import "fmt"

/*
	1st attempt: LTE
	dfs with not-duplicate paths
	see euler/31/explanation.jpeg
	O(all paths) <- TLE on leetcode. Obviously, leetcode doesn't want us to traverse all the combination paths
*/
func change_(amount int, coins []int) int {
	return dfs(coins, amount, 0)
}
func dfs(coins []int, n int, cur int) int {
	if n == 0 {
		return 1
	} else if n < 0 {
		return 0
	}
	cnt := 0
	for i := cur; i < len(coins); i++ {
		coin := coins[i]
		cnt += dfs(coins, n-coin, i)
	}
	return cnt
}

/*
	2nd attempt: DP, learned from others
	the idea is to divide the problem into subproblems:
	for each amount, calculate the number of different combinations using the result from smaller amount

	e.g.
	dp[amount] = dp[amount] + dp[amount-coin]
	dp[4] = 1 + dp[2]
	it means 4 can be came up with 1111 and the dp[2](the combination of 2), which is 11 and 2
	therefore
	dp[4] = 1 + 2 = 3
	see ./explanation.jpeg
*/
func change(amount int, coins []int) int {
	dp := make([]int, amount+1)
	dp[0] = 1
	for i := 0; i < len(coins); i++ {
		coin := coins[i]
		for j := 1; j <= amount; j++ {
			if j-coin >= 0 {
				dp[j] += dp[j-coin]
			}
		}
	}
	return dp[amount]
}

func main() {
	fmt.Println(change(200, []int{1, 2, 5, 10, 20, 50, 100, 200}))
	fmt.Println(change(500, []int{3, 5, 7, 8, 9, 10, 11}))
}
