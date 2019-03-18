package main

import "fmt"

/*
	1st approach: bfs
	Time	O(n^2) <- n = r*c
	Space	O(n)
	LTE
*/
func updateMatrix(matrix [][]int) [][]int {
	// init a result matrix
	clone := newMatrix(len(matrix), len(matrix[0]))
	// find the 1s in the input matrix
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			if matrix[i][j] == 1 {
				visited := newMatrix(len(matrix), len(matrix[0]))
				x := bfs(i, j, matrix, visited)
				clone[i][j] = x
			}
		}
	}
	return clone
}

type Point struct {
	X     int
	Y     int
	Steps int
}

func bfs(i, j int, matrix, visited [][]int) int {
	queue := []Point{}
	queue = append(queue, Point{i, j, 0})
	for len(queue) > 0 {
		head := queue[0]
		queue = queue[1:]
		x := head.X
		y := head.Y
		steps := head.Steps
		// check if x, y are within boundaries
		if x < 0 || x+1 > len(matrix) || y < 0 || y+1 > len(matrix[0]) {
			continue
		}
		// check if visited
		if visited[x][y] == 1 {
			continue
		}
		visited[x][y] = 1
		// check if we have reached to the target
		if matrix[x][y] == 0 {
			return steps
		} else {
			// enqueue the neighboours
			queue = append(queue, Point{x - 1, y, steps + 1})
			queue = append(queue, Point{x + 1, y, steps + 1})
			queue = append(queue, Point{x, y - 1, steps + 1})
			queue = append(queue, Point{x, y + 1, steps + 1})
		}
	}
	return -1
}

func newMatrix(rowCount, colCount int) [][]int {
	clone := [][]int{}
	for i := 0; i < rowCount; i++ {
		temp := []int{}
		for j := 0; j < colCount; j++ {
			temp = append(temp, 0)
		}
		clone = append(clone, temp)
	}
	return clone
}

/*
	2nd approach: dynamic programming
	- to avoid duplicate calculation, we can use an array to save the shortest steps to zero
	- we just need to traverse the matrix twice
	- from top to bottom
	- from bottom to top

	corner case:
	[[1, 1, 1, 1, 1],
	[1, 1, 1, 0, 1],
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1],
	[0, 1, 0, 0, 1],]

	⭐️ be careful of the 1st & last row & col,
	we should not compute the dp[i][j] for them because it affects the comparison when we do the 2nd iteration

	Time	O(2n) <- n = r*c
	Space	O(n)
	264 ms, faster than 96.67%
*/
func updateMatrix1(matrix [][]int) [][]int {
	dp := cloneMatrix(len(matrix), len(matrix[0]))
	// from top->bottom, left->right
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			if matrix[i][j] == 0 {
				dp[i][j] = 0
			} else {
				if i > 0 {
					dp[i][j] = findMin(dp[i][j], dp[i-1][j]+1)
				}
				if j > 0 {
					dp[i][j] = findMin(dp[i][j], dp[i][j-1]+1)
				}
			}
		}
	}
	// from bottom-top, right->left
	for i := len(dp) - 1; i >= 0; i-- {
		for j := len(dp[0]) - 1; j >= 0; j-- {
			if matrix[i][j] == 1 {
				if i+1 < len(dp) {
					dp[i][j] = findMin(dp[i][j], dp[i+1][j]+1)
				}
				if j+1 < len(dp[0]) {
					dp[i][j] = findMin(dp[i][j], dp[i][j+1]+1)
				}
			}
		}
	}
	return dp
}

func cloneMatrix(rowCount, colCount int) [][]int {
	clone := [][]int{}
	for i := 0; i < rowCount; i++ {
		temp := []int{}
		for j := 0; j < colCount; j++ {
			temp = append(temp, rowCount*colCount)
		}
		clone = append(clone, temp)
	}
	return clone
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	a := [][]int{
		{0, 0, 0},
		{0, 1, 0},
		{0, 0, 0},
	}
	fmt.Println(updateMatrix(a))

	a = [][]int{
		{0, 0, 0},
		{0, 1, 0},
		{1, 1, 1},
	}
	fmt.Println(updateMatrix(a))

	a = [][]int{
		{0, 0, 1},
		{0, 1, 1},
		{1, 1, 1},
	}
	fmt.Println(updateMatrix(a))

	a = [][]int{
		{1, 1, 1},
		{1, 1, 0},
		{1, 0, 0},
	}
	fmt.Println(updateMatrix(a))

	a = [][]int{
		{1, 1, 1},
		{1, 0, 0},
		{1, 0, 0},
	}
	fmt.Println(updateMatrix(a))

	a = [][]int{
		{0, 0, 1, 0, 0},
		{0, 1, 1, 1, 0},
		{1, 1, 1, 1, 1},
		{0, 1, 1, 0, 0},
		{0, 0, 1, 0, 0},
	}
	fmt.Println(updateMatrix(a))

	a = [][]int{
		{1, 1, 1, 1, 1},
		{1, 1, 1, 0, 1},
		{1, 1, 1, 1, 0},
		{1, 1, 1, 1, 1},
		{0, 1, 0, 0, 1},
	}
	fmt.Println(updateMatrix(a))

	fmt.Println("-----")

	a = [][]int{
		{0, 0, 0},
		{0, 1, 0},
		{0, 0, 0},
	}
	fmt.Println(updateMatrix1(a))

	a = [][]int{
		{0, 0, 0},
		{0, 1, 0},
		{1, 1, 1},
	}
	fmt.Println(updateMatrix1(a))

	a = [][]int{
		{0, 0, 1},
		{0, 1, 1},
		{1, 1, 1},
	}
	fmt.Println(updateMatrix1(a))

	a = [][]int{
		{1, 1, 1},
		{1, 1, 0},
		{1, 0, 0},
	}
	fmt.Println(updateMatrix(a))

	a = [][]int{
		{1, 1, 1},
		{1, 0, 0},
		{1, 0, 0},
	}
	fmt.Println(updateMatrix(a))

	a = [][]int{
		{0, 0, 1, 0, 0},
		{0, 1, 1, 1, 0},
		{1, 1, 1, 1, 1},
		{0, 1, 1, 0, 0},
		{0, 0, 1, 0, 0},
	}
	fmt.Println(updateMatrix1(a))

	a = [][]int{
		{1, 1, 1, 1, 1},
		{1, 1, 1, 0, 1},
		{1, 1, 1, 1, 0},
		{1, 1, 1, 1, 1},
		{0, 1, 0, 0, 1},
	}
	fmt.Println(updateMatrix1(a))
}
