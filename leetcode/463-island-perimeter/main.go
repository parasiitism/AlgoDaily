package main

import "fmt"

/*
	1st approach: recursive dfs, combine the perimeter of each grid

	Time    O(n)
	Space   O(n, d)
	84 ms, faster than 63.00%
*/
func islandPerimeter(grid [][]int) int {

	result := 0
	visited := make([][]bool, len(grid))
	for i := range visited {
		visited[i] = make([]bool, len(grid[i]))
	}

	// there is no hoisting in golang, we declare the function on on top
	var bfs func(i, j int)
	bfs = func(i, j int) {
		var queue []Queue
		queue = append(queue, Queue{i, j})
		for len(queue) > 0 {
			head := queue[0]
			queue = queue[1:]

			row := head.Row
			col := head.Col

			if grid[row][col] == 0 {
				result += 1
			} else if grid[row][col] == 1 && !visited[row][col] {

				visited[row][col] = true

				if row-1 >= 0 {
					queue = append(queue, Queue{row - 1, col})
				} else {
					result += 1
				}
				if row+1 < len(grid) {
					queue = append(queue, Queue{row + 1, col})
				} else {
					result += 1
				}
				if col-1 >= 0 {
					queue = append(queue, Queue{row, col - 1})
				} else {
					result += 1
				}
				if col+1 < len(grid[0]) {
					queue = append(queue, Queue{row, col + 1})
				} else {
					result += 1
				}
			}
		}
	}

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 && !visited[i][j] {
				bfs(i, j)
			}
		}
	}

	return result
}

type Queue struct {
	Row int
	Col int
}

func main() {
	a := [][]int{
		{1},
	}
	fmt.Println(islandPerimeter(a))

	a = [][]int{
		{0, 1, 0, 0},
		{1, 1, 1, 0},
		{0, 1, 0, 0},
		{1, 1, 0, 0},
	}
	fmt.Println(islandPerimeter(a))
}
