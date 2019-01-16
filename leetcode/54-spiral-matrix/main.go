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
	Space	O(1)
	16jan2019
*/
func spiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}
	if len(matrix[0]) == 0 {
		return []int{}
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
				i, j, dir = changeDir(i, j, dir, matrix)
			}
		} else if dir == 1 {
			tempI := i + 1
			if tempI < len(matrix) && matrix[tempI][j] != math.MaxInt64 {
				i++
			} else {
				i, j, dir = changeDir(i, j, dir, matrix)
			}
		} else if dir == 2 {
			tempJ := j - 1
			if tempJ >= 0 && matrix[i][tempJ] != math.MaxInt64 {
				j--
			} else {
				i, j, dir = changeDir(i, j, dir, matrix)
			}
		} else if dir == 3 {
			tempI := i - 1
			if tempI >= 0 && matrix[tempI][j] != math.MaxInt64 {
				i--
			} else {
				i, j, dir = changeDir(i, j, dir, matrix)
			}
		}
	}
	return res
}

// return i, j, dir
func changeDir(i int, j int, dir int, matrix [][]int) (int, int, int) {
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
