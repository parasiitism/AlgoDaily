package main

import (
	"fmt"
	"math"
)

/*
	1st approach:
	- mutate the value for visited nodes
	- change traverse direction if need
	- traverse direction priority: right, down, left, up
	Time	O(n)
	Space	O(n)
	16jan2019
*/
func spiralOrder1(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}
	if len(matrix[0]) == 0 {
		return []int{}
	}

	// return i, j, dir
	var changeDir func(i int, j int, dir int) (int, int, int)
	changeDir = func(i int, j int, dir int) (int, int, int) {
		tempDir := dir
		if tempDir == 0 { // go down
			if i+1 < len(matrix) && matrix[i+1][j] != math.MaxInt64 {
				return i + 1, j, 1
			}
			tempDir = 1
		}
		if tempDir == 1 { // go left
			if j-1 >= 0 && matrix[i][j-1] != math.MaxInt64 {
				return i, j - 1, 2
			}
			tempDir = 2
		}
		if tempDir == 2 { // go up
			if i-1 >= 0 && matrix[i-1][j] != math.MaxInt64 {
				return i - 1, j, 3
			}
			tempDir = 3
		}
		if tempDir == 3 { // go right
			if j+1 < len(matrix[i]) && matrix[i][j+1] != math.MaxInt64 {
				return i, j + 1, 0
			}
			tempDir = 0
		}
		return -1, -1, -1
	}

	dir := 0 // -1, 0, 1, 2, 3 = none, right, down, left ,up
	i, j := 0, 0
	res := []int{}
	for dir > -1 {
		res = append(res, matrix[i][j])
		matrix[i][j] = math.MaxInt64
		if dir == 0 {
			tempJ := j + 1
			if tempJ < len(matrix[i]) && matrix[i][tempJ] != math.MaxInt64 {
				j++
			} else {
				i, j, dir = changeDir(i, j, dir)
			}
		} else if dir == 1 {
			tempI := i + 1
			if tempI < len(matrix) && matrix[tempI][j] != math.MaxInt64 {
				i++
			} else {
				i, j, dir = changeDir(i, j, dir)
			}
		} else if dir == 2 {
			tempJ := j - 1
			if tempJ >= 0 && matrix[i][tempJ] != math.MaxInt64 {
				j--
			} else {
				i, j, dir = changeDir(i, j, dir)
			}
		} else if dir == 3 {
			tempI := i - 1
			if tempI >= 0 && matrix[tempI][j] != math.MaxInt64 {
				i--
			} else {
				i, j, dir = changeDir(i, j, dir)
			}
		}
	}
	return res
}

/*
	2nd approach
	- same as the above without using math.MaxInt64
	Time	O(2n)
	Space	O(n)
	16jan2019
*/
func spiralOrder2(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}
	if len(matrix[0]) == 0 {
		return []int{}
	}
	// visited
	visited := [][]int{}
	for i := 0; i < len(matrix); i++ {
		temp := []int{}
		for j := 0; j < len(matrix[i]); j++ {
			temp = append(temp, 0)
		}
		visited = append(visited, temp)
	}

	// return i, j, dir
	var changeDir func(i int, j int, dir int) (int, int, int)
	changeDir = func(i int, j int, dir int) (int, int, int) {
		tempDir := dir
		if tempDir == 0 { // go down
			if i+1 < len(matrix) && visited[i+1][j] != 1 {
				return i + 1, j, 1
			}
			tempDir = 1
		}
		if tempDir == 1 { // go left
			if j-1 >= 0 && visited[i][j-1] != 1 {
				return i, j - 1, 2
			}
			tempDir = 2
		}
		if tempDir == 2 { // go up
			if i-1 >= 0 && visited[i-1][j] != 1 {
				return i - 1, j, 3
			}
			tempDir = 3
		}
		if tempDir == 3 { // go right
			if j+1 < len(matrix[i]) && visited[i][j+1] != 1 {
				return i, j + 1, 0
			}
			tempDir = 0
		}
		return -1, -1, -1
	}

	dir := 0 // -1, 0, 1, 2, 3 = none, right, down, left ,up
	i, j := 0, 0
	res := []int{}
	for dir > -1 {
		res = append(res, matrix[i][j])
		visited[i][j] = 1
		if dir == 0 {
			tempJ := j + 1
			if tempJ < len(matrix[i]) && visited[i][tempJ] != 1 {
				j++
			} else {
				i, j, dir = changeDir(i, j, dir)
			}
		} else if dir == 1 {
			tempI := i + 1
			if tempI < len(matrix) && visited[tempI][j] != 1 {
				i++
			} else {
				i, j, dir = changeDir(i, j, dir)
			}
		} else if dir == 2 {
			tempJ := j - 1
			if tempJ >= 0 && visited[i][tempJ] != 1 {
				j--
			} else {
				i, j, dir = changeDir(i, j, dir)
			}
		} else if dir == 3 {
			tempI := i - 1
			if tempI >= 0 && visited[tempI][j] != 1 {
				i--
			} else {
				i, j, dir = changeDir(i, j, dir)
			}
		}
	}
	return res
}

/*
	3rd approach: learned from others
	https://leetcode.com/articles/spiral-matrix/
	- the basic idea is to set min and max for both row and col
	- print the nums layer by layer, one layer = right+down+left+up
	Time	O(n)
	Space	O(n)
	16jan2019
*/
func spiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}
	if len(matrix[0]) == 0 {
		return []int{}
	}
	res := []int{}
	minRow := 0
	maxRow := len(matrix) - 1
	minCol := 0
	maxCol := len(matrix[0]) - 1
	for minRow <= maxRow && minCol <= maxCol {
		for j := minCol; j <= maxCol; j++ {
			res = append(res, matrix[minRow][j])
		}
		for i := minRow + 1; i <= maxRow; i++ {
			res = append(res, matrix[i][maxCol])
		}
		if minCol < maxCol && minRow < maxRow {
			for j := maxCol - 1; j >= minCol; j-- {
				res = append(res, matrix[maxRow][j])
			}
			for i := maxRow - 1; i > minRow; i-- {
				res = append(res, matrix[i][minRow])
			}
		}
		minRow++
		maxRow--
		minCol++
		maxCol--
	}
	return res
}

func main() {

	fmt.Println(spiralOrder([][]int{}))

	fmt.Println(spiralOrder([][]int{
		{},
	}))

	fmt.Println(spiralOrder([][]int{
		{2, 5},
		{8, 4},
		{0, -1},
	}))

	fmt.Println(spiralOrder([][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}))

	fmt.Println(spiralOrder([][]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
	}))
}
