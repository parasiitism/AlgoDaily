package main

import "fmt"

func findNine(grid [][]int) bool {
	visited := [][]int{}
	for i := 0; i < len(grid); i++ {
		temp := []int{}
		for j := 0; j < len(grid[0]); j++ {
			temp = append(temp, 0)
		}
		visited = append(visited, temp)
	}
	return dfs(grid, visited, 0, 0)
}

func dfs(grid, visited [][]int, i, j int) bool {
	if i < 0 || i+1 > len(grid) || j < 0 || j+1 > len(grid[0]) {
		return false
	}
	// avoid visited point
	if visited[i][j] == 1 {
		return false
	}
	visited[i][j] = 1
	// check if arrive 9
	if grid[i][j] == 9 {
		return true
	} else if grid[i][j] == 0 {
		return dfs(grid, visited, i-1, j) || dfs(grid, visited, i+1, j) || dfs(grid, visited, i, j-1) || dfs(grid, visited, i, j+1)
	}
	return false
}

func main() {
	a := [][]int{
		{0, 0, 0, 0},
		{0, 1, 0, 1},
		{0, 0, 0, 0},
		{0, 0, 1, 9},
	}
	fmt.Println(findNine(a))

	a = [][]int{
		{0, 0, 0, 0},
		{0, 1, 0, 1},
		{0, 0, 0, 1},
		{0, 0, 1, 9},
	}
	fmt.Println(findNine(a))

	a = [][]int{
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 1, 0, 0, 0, 0},
		{0, 0, 0, 1, 0, 0, 0, 0},
		{0, 0, 1, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 1, 0, 0, 0, 0},
		{0, 0, 0, 1, 1, 1, 0, 1},
		{0, 0, 1, 9, 0, 0, 0, 0},
	}
	fmt.Println(findNine(a))

	a = [][]int{
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 1, 0, 0, 0, 0},
		{0, 0, 0, 1, 0, 0, 0, 0},
		{0, 0, 1, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 1, 0, 0, 0, 0},
		{0, 0, 0, 1, 1, 1, 0, 1},
		{0, 0, 1, 9, 0, 0, 1, 0},
	}
	fmt.Println(findNine(a))
}
