package main

import (
	"fmt"
	"strconv"
)

// method 1: dfs, hashtable
// runtime: 32ms, beats 9.4%
func numIslands(grid [][]byte) int {
	visited := make(map[string]bool)
	result := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			key := strconv.Itoa(i) + "," + strconv.Itoa(j)
			_, existed := visited[key]
			if grid[i][j] == '1' && !existed {
				dfs(grid, i, j, visited)
				result++
			}
		}
	}
	return result
}

func dfs(grid [][]byte, i int, j int, visited map[string]bool) {
	if i < 0 || i+1 > len(grid) || j < 0 || j+1 > len(grid[0]) {
		return
	}
	key := strconv.Itoa(i) + "," + strconv.Itoa(j)
	_, existed := visited[key]
	if grid[i][j] == '1' && !existed {
		key := strconv.Itoa(i) + "," + strconv.Itoa(j)
		visited[key] = true
		dfs(grid, i-1, j, visited)
		dfs(grid, i+1, j, visited)
		dfs(grid, i, j-1, visited)
		dfs(grid, i, j+1, visited)
	}
}

// method 2: dfs, dummy array
// runtime: 0ms, beats 100%
func numIslands1(grid [][]byte) int {
	visited := make([][]bool, len(grid))
	for i := range visited {
		visited[i] = make([]bool, len(grid[i]))
	}
	result := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == '1' && !visited[i][j] {
				dfs1(grid, i, j, visited)
				result++
			}
		}
	}
	return result
}

func dfs1(grid [][]byte, i int, j int, visited [][]bool) {
	if i < 0 || i+1 > len(grid) || j < 0 || j+1 > len(grid[0]) {
		return
	}
	if grid[i][j] == '1' && !visited[i][j] {
		visited[i][j] = true
		dfs1(grid, i-1, j, visited)
		dfs1(grid, i+1, j, visited)
		dfs1(grid, i, j-1, visited)
		dfs1(grid, i, j+1, visited)
	}
}

func main() {
	m := [][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '0', '0', '0'},
		{'1', '1', '0', '1', '0'},
		{'0', '0', '0', '0', '1'},
	}
	fmt.Println(numIslands1(m))
}
