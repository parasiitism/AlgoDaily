package main

import (
	"fmt"
	"math"
)

/*
	1st approach:
	- brute force with memorization
	Time	...it is hard to determind
	Space	O(m*n)
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
