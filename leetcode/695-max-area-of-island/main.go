package main

import "fmt"

/*
	1st approach
	- recursive dfs
	- when we see an one, dfs its neightbours to calculate its area and compare to the potential result
	- if it is larger than the potential result, set it as the potential result

	i think the 2nd way is to do it with an iterative dfs

	Time    O(n)
	Space   O(n) hashtable
	20 ms, faster than 80.30%
*/
func maxAreaOfIsland(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	visited := [][]bool{}
	for i := 0; i < len(grid); i++ {
		temp := []bool{}
		for j := 0; j < len(grid[0]); j++ {
			temp = append(temp, false)
		}
		visited = append(visited, temp)
	}

	resultArea := 0
	curArea := 0

	var dfs func(i int, j int)
	dfs = func(i int, j int) {
		if i < 0 || i+1 > len(grid) || j < 0 || j+1 > len(grid[0]) || visited[i][j] == true {
			return
		}
		visited[i][j] = true
		if grid[i][j] == 1 {
			curArea++
			if curArea > resultArea {
				resultArea = curArea
			}
			dfs(i-1, j)
			dfs(i+1, j)
			dfs(i, j-1)
			dfs(i, j+1)
		}
	}

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				curArea = 0
				dfs(i, j)
				curArea = 0
			} else {
				visited[i][j] = true
			}
		}
	}
	return resultArea
}

func main() {
	a := [][]int{
		{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0},
	}
	fmt.Println(maxAreaOfIsland(a))

	a = [][]int{
		{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0},
	}
	fmt.Println(maxAreaOfIsland(a))
}
