package main

import "fmt"

/*
	1st approach: brute force
	- it is similar to leetcode 200

	Time	O(m*n*p)
	Space	O(m*n)
	5796 ms, faster than 6.67%
*/
func numIslands2(m int, n int, positions [][]int) []int {
	// build empty grid
	grid := [][]int{}
	for i := 0; i < m; i++ {
		temp := []int{}
		for j := 0; j < n; j++ {
			temp = append(temp, 0)
		}
		grid = append(grid, temp)
	}
	// insert land
	res := []int{}
	for _, position := range positions {
		grid[position[0]][position[1]] = 1
		// declare visited(hashtable)
		visited := make([][]bool, len(grid))
		for i := range visited {
			visited[i] = make([]bool, len(grid[i]))
		}
		curResult := 0
		for i := 0; i < len(grid); i++ {
			for j := 0; j < len(grid[0]); j++ {
				if grid[i][j] == 1 && visited[i][j] == false {
					dfs(grid, i, j, visited)
					curResult++
				}
			}
		}
		res = append(res, curResult)
	}
	return res
}

func dfs(grid [][]int, i int, j int, visited [][]bool) {
	if i < 0 || i+1 > len(grid) || j < 0 || j+1 > len(grid[0]) || visited[i][j] == true {
		return
	}
	visited[i][j] = true
	if grid[i][j] == 1 {
		dfs(grid, i-1, j, visited)
		dfs(grid, i+1, j, visited)
		dfs(grid, i, j-1, visited)
		dfs(grid, i, j+1, visited)
	}
}

func main() {
	a := [][]int{
		{0, 0}, {0, 1}, {1, 2}, {2, 1},
	}
	fmt.Println(numIslands2(3, 3, a))

	a = [][]int{
		{0, 1}, {0, 0},
	}
	fmt.Println(numIslands2(1, 2, a))
}
