package main

/*
	1st approach: recursive dfs

	Time    O(2n)
	Space   O(n) hashtable
	56 ms, faster than 7.94%
*/
func solve(grid [][]byte) {
	// visited
	visited := make([][]bool, len(grid))
	for i := range visited {
		visited[i] = make([]bool, len(grid[i]))
	}
	// traverse island
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 'O' && !visited[i][j] {
				tocuhBound := dfs(grid, i, j, visited)
				if tocuhBound == false {
					markCapture(grid, i, j)
				}
			}
		}
	}
}

func dfs(grid [][]byte, i int, j int, visited [][]bool) bool {
	if i < 0 || i+1 > len(grid) || j < 0 || j+1 > len(grid[0]) {
		return true
	}
	if visited[i][j] == true {
		return false
	}
	visited[i][j] = true
	if grid[i][j] == 'O' {
		up := dfs(grid, i-1, j, visited)
		down := dfs(grid, i+1, j, visited)
		left := dfs(grid, i, j-1, visited)
		right := dfs(grid, i, j+1, visited)
		return up || down || left || right
	}
	return false
}

func markCapture(grid [][]byte, i int, j int) {
	if i < 0 || i+1 > len(grid) || j < 0 || j+1 > len(grid[0]) {
		return
	}
	if grid[i][j] == 'O' {
		grid[i][j] = 'X'
		markCapture(grid, i-1, j)
		markCapture(grid, i+1, j)
		markCapture(grid, i, j-1)
		markCapture(grid, i, j+1)
	}
}

func main() {

}
