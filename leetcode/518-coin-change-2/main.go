package main

import "fmt"

// 1st attempt
// dfs with not-duplicate paths
// see euler/31/explanation.jpeg
// O(all paths) <- TLE on leetcode. Obviously, leetcode doesn't want us to traverse all the combination paths
func change(amount int, coins []int) int {
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

func main() {
	fmt.Println(change(200, []int{1, 2, 5, 10, 20, 50, 100, 200}))
	fmt.Println(change(500, []int{3, 5, 7, 8, 9, 10, 11}))
}
