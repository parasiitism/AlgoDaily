package main

import "fmt"

/*
	1st approach: classic dynamic programming approach
	- https://www.youtube.com/watch?v=NYeVhmWsWec

	Time  O(r*c)
	Space O(r*c)
	 0 ms, faster than 100.00%
*/
func maximalSquare(matrix [][]byte) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}
	// create a dp array for caching the submatrices sizes
	dp := [][]int{}
	for i := 0; i < len(matrix); i++ {
		temp := []int{}
		for j := 0; j < len(matrix[0]); j++ {
			temp = append(temp, 0)
		}
		dp = append(dp, temp)
	}
	res := 0
	// for each cell, check if itself can complete a larger square
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			if i == 0 || j == 0 {
				dp[i][j] = int(matrix[i][j]) - int('0')
			} else if matrix[i][j] == '1' {
				dp[i][j] = findMin(dp[i-1][j-1], findMin(dp[i-1][j], dp[i][j-1])) + 1
			}
			if dp[i][j] > res {
				res = dp[i][j]
			}
		}
	}
	return res * res
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	a := '9'
	fmt.Println(int(a) - int('0'))
}
