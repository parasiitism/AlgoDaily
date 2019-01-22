package main

import "fmt"

/*
	similar approach to leetcode 54
	- set the boundaries and fill in the nodes layer by layer
	Time		O(n)
	Space		O(n) the result
	0ms beats 100%
*/
func generateMatrix(n int) [][]int {
	if n <= 0 {
		return [][]int{}
	}
	matrix := [][]int{}
	for i := 0; i < n; i++ {
		temp := []int{}
		for j := 0; j < n; j++ {
			temp = append(temp, 0)
		}
		matrix = append(matrix, temp)
	}
	minRow := 0
	maxRow := n - 1
	minCol := 0
	maxCol := n - 1
	cnt := 1
	for minRow <= maxRow && minCol <= maxCol {
		for j := minCol; j <= maxCol; j++ {
			matrix[minRow][j] = cnt
			cnt++
		}
		for i := minRow + 1; i <= maxRow; i++ {
			matrix[i][maxCol] = cnt
			cnt++
		}
		if minCol < maxCol && minRow < maxRow {
			for j := maxCol - 1; j >= minCol; j-- {
				matrix[maxRow][j] = cnt
				cnt++
			}
			for i := maxRow - 1; i > minRow; i-- {
				matrix[i][minRow] = cnt
				cnt++
			}
		}
		minRow++
		maxRow--
		minCol++
		maxCol--
	}
	return matrix
}

func main() {
	fmt.Println(generateMatrix(-1))
	fmt.Println(generateMatrix(0))
	fmt.Println(generateMatrix(1))
	fmt.Println(generateMatrix(3))
	fmt.Println(generateMatrix(4))
}
