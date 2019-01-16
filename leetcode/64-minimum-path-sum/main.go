package main

import (
	"fmt"
	"math"
)

/*
	1st approach:
	- recursive brute force with memorization
	Time	O(<2^(m+n)) it depends on the input
	Space	O(m+n) the depth of the routes
	220 ms beats 0.00%
*/
func minPathSum(grid [][]int) int {
	visited := [][]int{}
	for i := 0; i < len(grid); i++ {
		temp := []int{}
		for j := 0; j < len(grid[i]); j++ {
			temp = append(temp, math.MaxInt32)
		}
		visited = append(visited, temp)
	}

	min := math.MaxInt32
	var dfs func(i int, j int, sum int)
	dfs = func(i int, j int, sum int) {
		if i < 0 || i >= len(grid) || j < 0 || j >= len(grid[0]) {
			return
		}
		temp := sum + grid[i][j]
		if i == len(grid)-1 && j == len(grid[0])-1 {
			if temp < min {
				min = temp
			}
		}
		if temp >= min || temp >= visited[i][j] {
			return
		}
		visited[i][j] = temp
		dfs(i+1, j, temp)
		dfs(i, j+1, temp)
	}
	dfs(0, 0, 0)
	return min
}

/*
	2nd approach: dynamic programming
	- dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
	- https://leetcode.com/articles/minimum-path-sum/
	Time	O(m*n)
	Space	O(m*n)
	8ms beats 100%
	16jan2019
*/
func minPathSum1(grid [][]int) int {
	dp := [][]int{}
	for i := 0; i < len(grid); i++ {
		temp := []int{}
		for j := 0; j < len(grid[i]); j++ {
			temp = append(temp, 0)
		}
		dp = append(dp, temp)
	}

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if i-1 < 0 && j-1 < 0 {
				dp[i][j] = grid[i][j]
			} else if i-1 < 0 {
				dp[i][j] = grid[i][j] + dp[i][j-1]
			} else if j-1 < 0 {
				dp[i][j] = grid[i][j] + dp[i-1][j]
			} else {
				dp[i][j] = grid[i][j] + findMin(dp[i][j-1], dp[i-1][j])
			}
		}
	}
	return dp[len(grid)-1][len(grid[0])-1]
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	fmt.Println(minPathSum([][]int{
		{1, 3, 1},
		{1, 5, 1},
		{4, 2, 1},
	}))

	fmt.Println(minPathSum([][]int{
		{1, 3, 1, 3, 5},
		{1, 5, 1, 7, 8},
		{4, 2, 1, 2, 5},
	}))
}
