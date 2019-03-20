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
	Time	O(2^n)
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
			dfs(i+1, j, sum)
			dfs(i+1, j+1, sum)
		}
	}
	dfs(0, 0, 0)
	if min == math.MaxInt64 {
		return 0
	}
	return min
}

/*
	2nd approach
	- recursive dfs
	Time	O(n)
	Space	O(n+h)
	Memory Limit Execeeded
*/
func minimumTotal1(triangle [][]int) int {
	// for memorization
	ht := [][][]int{}
	for i := 0; i < len(triangle); i++ {
		temp := [][]int{}
		for j := 0; j < len(triangle); j++ {
			temp = append(temp, []int{})
		}
		ht = append(ht, temp)
	}
	// recursive dfs
	paths := dfs(triangle, 0, 0, ht)
	if len(paths) == 0 {
		return 0
	}
	// find the min
	min := paths[0]
	for i := 1; i < len(paths); i++ {
		if paths[i] < min {
			min = paths[i]
		}
	}
	return min
}

func dfs(triangle [][]int, i, j int, ht [][][]int) []int {
	if i < 0 || i >= len(triangle) || j < 0 || j >= len(triangle) {
		return []int{}
	}
	// if seen, return the cache
	if len(ht[i][j]) > 0 {
		return ht[i][j]
	}
	// cal the thing
	if i+1 == len(triangle) {
		return []int{triangle[i][j]}
	} else if i < len(triangle) {
		// sum := prevSum + triangle[i][j]
		left := dfs(triangle, i+1, j, ht)
		right := dfs(triangle, i+1, j+1, ht)
		// merge left and right
		// add node.val to each numbe in the array
		total := []int{}
		total = append(total, left...)
		total = append(total, right...)
		for k := 0; k < len(total); k++ {
			total[k] += triangle[i][j]
		}
		ht[i][j] = total
		return total
	}
	return []int{}
}

/*
	3rd approach
	- bottom up
	- select the path with min cost from bottom to top, mutate the input array
	Time	O(n)
	Space	O(1)
	4ms beats 100%
*/
func minimumTotal2(triangle [][]int) int {
	if len(triangle) == 0 {
		return 0
	}
	for i := len(triangle) - 2; i >= 0; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			left := triangle[i+1][j] + triangle[i][j]
			right := triangle[i+1][j+1] + triangle[i][j]
			triangle[i][j] = findMin(left, right)
		}
	}
	return triangle[0][0]
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {

	a := [][]int{}
	fmt.Println(minimumTotal2(a)) // 0

	a = [][]int{
		{2},
	}
	fmt.Println(minimumTotal2(a)) // 2

	a = [][]int{
		{2},
		{3, 4},
		{6, 5, 7},
		{4, 1, 8, 3},
	}
	fmt.Println(minimumTotal2(a)) // 11

	a = [][]int{
		{-2},
		{-3, -4},
		{-6, -5, -7},
		{-4, -1, -8, -3},
	}
	fmt.Println(minimumTotal2(a)) // -21

	a = [][]int{
		{-2},
		{3, 4},
		{-6, -5, -7},
		{-4, 1, 8, -3},
	}
	fmt.Println(minimumTotal2(a)) // -9
}
