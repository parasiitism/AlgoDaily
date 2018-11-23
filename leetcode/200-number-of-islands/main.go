package main

import (
	"fmt"
	"strconv"
)

// method 1: dfs, hashtable for visited island territories
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

// method 2: dfs, dummy array for visited island territories
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

// approach 3: bfs, queue for coordinates
// runtime: 4ms, beats 50.43%
func numIslands2(grid [][]byte) int {
	visited := make([][]bool, len(grid))
	for i := range visited {
		visited[i] = make([]bool, len(grid[i]))
	}
	result := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == '1' && !visited[i][j] {
				result++
				bfs(grid, i, j, visited)
			}
		}
	}
	return result
}

func bfs(grid [][]byte, i int, j int, visited [][]bool) {
	var queue []Queue
	queue = append(queue, Queue{i, j})
	for len(queue) > 0 {
		head := queue[0]
		row := head.Row
		col := head.Col
		queue = queue[1:]
		if grid[row][col] == '1' && !visited[row][col] {
			visited[row][col] = true
			if row-1 >= 0 {
				queue = append(queue, Queue{row - 1, col})
			}
			if row+1 < len(grid) {
				queue = append(queue, Queue{row + 1, col})
			}
			if col-1 >= 0 {
				queue = append(queue, Queue{row, col - 1})
			}
			if col+1 < len(grid[0]) {
				queue = append(queue, Queue{row, col + 1})
			}
		}
	}
}

type Queue struct {
	Row int
	Col int
}

func main() {
	m := [][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '0', '0', '0'},
		{'1', '1', '0', '1', '0'},
		{'0', '0', '0', '0', '1'},
	}
	fmt.Println(numIslands(m))
	fmt.Println(numIslands1(m))
	fmt.Println(numIslands2(m))
}
