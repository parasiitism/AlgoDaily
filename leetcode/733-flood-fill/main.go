package main

// approach 1
// dfs: just replace the target territory with the new color
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

// approach 2
// queue
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

func main() {

}
