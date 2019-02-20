package main

import (
	"fmt"
	"strconv"
)

/*
	questions to ask:
	- will the start point be blocked, e.g. grid[0][0] = 1? yes
	- will the destination point be blocked, e.g. grid[-1][-1] = 1? yes
	- will the grid be empty? yes
	- will the grid have notches? no
	- will there be malformed array items, e.g. [1,2] or [1,"abc"]? no
*/

/*
	1st approach: brute force, bottom up recursively with memorization
	- intuitively go through all the path with i+1 OR j+1
	- count the path which reaches to the destination coordinate (m, n)
	- cache the count of the coordinates which we have calculated before
	- if the current grid, grid[i][j], is blocked, tell its parent that this way is blocked by return 0
	- sum up all the coordinates' count

	Time    O(m*n) 0->m, 0->n. since we cache the intermediate coordinates, we dont have duplicate sets of i, j
	Space   O(m*n) depth of recursion calls
	4 ms, faster than 79.17%
*/
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if len(obstacleGrid) == 0 || len(obstacleGrid[0]) == 0 {
		return 0
	}
	seen := make(map[string]int)
	return dfs(obstacleGrid, 0, 0, len(obstacleGrid)-1, len(obstacleGrid[0])-1, seen)
}

func dfs(grid [][]int, i, j, m, n int, seen map[string]int) int {
	key := strconv.Itoa(i) + "," + strconv.Itoa(j)
	if v, x := seen[key]; x {
		return v
	}
	if i == m && j == n {
		if grid[i][j] == 1 {
			return 0
		}
		return 1
	} else if i > m || j > n {
		return 0
	}
	if grid[i][j] == 1 {
		seen[key] = 0
		return 0
	}
	left := dfs(grid, i+1, j, m, n, seen)
	right := dfs(grid, i, j+1, m, n, seen)
	seen[key] = left + right
	return left + right
}

/*
	2nd approach: dynamic programming, iterative top down
	- the basic idea is to sum up the count from left and top
			i.e. dp[i][j] = dp[i-1][j] + dp[i][j-1]
	- https://leetcode.com/articles/unique-paths-ii/


	Time    O(m*n) iterate the 2d array
	Space   O(m*n) the dp array
*/
func uniquePathsWithObstacles1(obstacleGrid [][]int) int {
	dp := [][]int{}
	for i := 0; i < len(obstacleGrid); i++ {
		temp := []int{}
		for j := 0; j < len(obstacleGrid[0]); j++ {
			temp = append(temp, 0)
		}
		dp = append(dp, temp)
	}
	if obstacleGrid[0][0] == 1 {
		return 0
	}
	for i := 0; i < len(obstacleGrid); i++ {
		for j := 0; j < len(obstacleGrid[0]); j++ {
			if i == 0 && j == 0 {
				dp[0][0] = 1
			} else if i == 0 {
				dp[0][j] = dp[0][j-1]
				if obstacleGrid[i][j] == 1 {
					dp[0][j] = 0
				}
			} else if j == 0 {
				dp[i][0] = dp[i-1][0]
				if obstacleGrid[i][j] == 1 {
					dp[i][0] = 0
				}
			} else {
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
				if obstacleGrid[i][j] == 1 {
					dp[i][j] = 0
				}
			}
		}
	}
	return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
}

func main() {

	a := [][]int{{0}}
	fmt.Println(uniquePathsWithObstacles(a))

	a = [][]int{{1}}
	fmt.Println(uniquePathsWithObstacles(a))

	a = [][]int{{1}, {0}}
	fmt.Println(uniquePathsWithObstacles(a))

	a = [][]int{{0}, {1}}
	fmt.Println(uniquePathsWithObstacles(a))

	a = [][]int{
		{0, 0, 0},
		{0, 1, 0},
		{0, 0, 0},
	}
	fmt.Println(uniquePathsWithObstacles(a))

	a = [][]int{
		{0, 1, 0},
		{0, 1, 0},
		{0, 0, 0},
	}
	fmt.Println(uniquePathsWithObstacles(a))

	a = [][]int{
		{0, 0, 1},
		{0, 1, 0},
		{0, 0, 0},
	}
	fmt.Println(uniquePathsWithObstacles(a))

	a = [][]int{
		{0, 1, 0},
		{1, 1, 0},
		{0, 0, 0},
	}
	fmt.Println(uniquePathsWithObstacles(a))

	a = [][]int{
		{0, 0, 1},
		{0, 1, 0},
		{1, 0, 0},
	}
	fmt.Println(uniquePathsWithObstacles(a))

	a = [][]int{
		{0, 0, 0, 0},
		{0, 1, 0, 0},
		{0, 0, 0, 0},
		{0, 0, 0, 0},
	}
	fmt.Println(uniquePathsWithObstacles(a))
}
