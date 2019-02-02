package main

import (
	"fmt"
	"math"
)

/*
	Questions to ask:
	- not in a triangle?
	- negative values?
	- range of the num?
*/

/*
	1st approach
	- dfs
	Time	O(n)
	TLE wtf
*/
func minimumTotal(triangle [][]int) int {
	min := math.MaxInt64
	var dfs func(i, j, prevSum int)
	dfs = func(i, j, prevSum int) {
		if i+1 == len(triangle) {
			sum := prevSum + triangle[i][j]
			if sum < min {
				min = sum
			}
		} else if i < len(triangle) {
			sum := prevSum + triangle[i][j]
			if sum < min {
				dfs(i+1, j, sum)
				dfs(i+1, j+1, sum)
			}
		}
	}
	dfs(0, 0, 0)
	if min == math.MaxInt64 {
		return 0
	}
	return min
}

func main() {

	a := [][]int{}
	fmt.Println(minimumTotal(a))

	a = [][]int{
		{2},
	}
	fmt.Println(minimumTotal(a))

	a = [][]int{
		{2},
		{3, 4},
		{6, 5, 7},
		{4, 1, 8, 3},
	}
	fmt.Println(minimumTotal(a))

	a = [][]int{
		{-2},
		{-3, -4},
		{-6, -5, -7},
		{-4, -1, -8, -3},
	}
	fmt.Println(minimumTotal(a))

	a = [][]int{
		{-2},
		{3, 4},
		{-6, -5, -7},
		{-4, 1, 8, -3},
	}
	fmt.Println(minimumTotal(a))
}
