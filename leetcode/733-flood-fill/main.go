package main

/*
	1st approach: recursive dfs + hashtable
	- just replace the target territory with the new color
	- hastable to avoid redundant visit
*/
func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	visited := make([][]bool, len(image))
	for i := range visited {
		visited[i] = make([]bool, len(image[i]))
	}
	for i := 0; i < len(image); i++ {
		for j := 0; j < len(image[0]); j++ {
			// find target coordinate
			if i == sr && j == sc {
				dfs(image, i, j, image[i][j], newColor, visited)
			}
		}
	}
	return image
}

// explore the territory
func dfs(grid [][]int, i int, j int, origColor int, newColor int, visited [][]bool) {
	if i < 0 || i+1 > len(grid) || j < 0 || j+1 > len(grid[0]) {
		return
	}
	if grid[i][j] == origColor && !visited[i][j] {
		grid[i][j] = newColor
		visited[i][j] = true
		dfs(grid, i-1, j, origColor, newColor, visited)
		dfs(grid, i+1, j, origColor, newColor, visited)
		dfs(grid, i, j-1, origColor, newColor, visited)
		dfs(grid, i, j+1, origColor, newColor, visited)
	}
}

/*
	2nd approach: bfs + hashtable
	- just replace the target territory with the new color
	- hastable to avoid redundant visit
*/
func floodFill1(image [][]int, sr int, sc int, newColor int) [][]int {
	visited := make([][]bool, len(image))
	for i := range visited {
		visited[i] = make([]bool, len(image[i]))
	}
	for i := 0; i < len(image); i++ {
		for j := 0; j < len(image[0]); j++ {
			// find target coordinate
			if i == sr && j == sc {
				bfs(image, i, j, image[i][j], newColor, visited)
			}
		}
	}
	return image
}

type Queue struct {
	Row int
	Col int
}

func bfs(grid [][]int, i int, j int, origColor int, newColor int, visited [][]bool) {
	var queue []Queue
	queue = append(queue, Queue{i, j})
	for len(queue) > 0 {
		head := queue[0]
		row := head.Row
		col := head.Col
		queue = queue[1:]
		if grid[row][col] == origColor && !visited[row][col] {
			grid[row][col] = newColor
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

/*
	3rd approach: bfs
	- just replace the target territory with the new color
	- actually we dont need a hashtable, we can just check if the start point is newColor

	Time	O(RC)
	Space	O(RC)
	8 ms, faster than 98.88%
*/
func floodFill2(image [][]int, sr int, sc int, newColor int) [][]int {
	for i := 0; i < len(image); i++ {
		for j := 0; j < len(image[0]); j++ {
			if i == sr && j == sc && image[i][j] != newColor {
				bfs2(image, i, j, newColor)
			}
		}
	}
	return image
}

func bfs2(grid [][]int, x int, y int, newColor int) {
	origColor := grid[x][y]
	var queue []Queue
	queue = append(queue, Queue{x, y})
	for len(queue) > 0 {
		head := queue[0]
		row := head.Row
		col := head.Col
		queue = queue[1:]

		if row < 0 || row+1 > len(grid) || col < 0 || col+1 > len(grid[0]) {
			continue
		}

		if grid[row][col] == origColor {
			grid[row][col] = newColor
			queue = append(queue, Queue{row - 1, col})
			queue = append(queue, Queue{row + 1, col})
			queue = append(queue, Queue{row, col - 1})
			queue = append(queue, Queue{row, col + 1})
		}
	}
}

func main() {

}
