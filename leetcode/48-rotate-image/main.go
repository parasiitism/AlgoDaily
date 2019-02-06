package main

import "fmt"

/*
	quesions to ask:
	- number of columns = number of rows?
	- clockwise
*/

/*
	1st attempt:
	1. transpose
	2. swap columns

	if anit-clockwise:
	1. swap columns
	2. transpose

	Time		O(2n)
	Space		O(1)
	0ms beats 100%
*/
func rotate(matrix [][]int) {
	// clockwise: transpose, swap
	transpose(matrix)
	swapCols(matrix)
}

func transpose(matrix [][]int) {
	for i := 0; i < len(matrix); i++ {
		for j := i; j < len(matrix[0]); j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
}

func swapCols(matrix [][]int) {
	for i := 0; i < len(matrix); i++ {
		n := len(matrix[0]) - 1
		for j := 0; j <= n; j++ {
			if n-j > j {
				matrix[i][j], matrix[i][n-j] = matrix[i][n-j], matrix[i][j]
			}
		}
	}
}

func main() {
	a := [][]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
		{13, 14, 15, 16},
	}
	rotate(a)
	fmt.Println(a)
}
