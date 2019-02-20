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
	1st approach: brute force, bottom up recursively with memorizatin
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
}
