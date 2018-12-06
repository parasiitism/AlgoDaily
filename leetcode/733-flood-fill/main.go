package main

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

func main() {

}
