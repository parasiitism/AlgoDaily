package main

import "fmt"

/*
	naive approach:
	brute force, iterate every item in the 2D array
*/

/*
	1st approach:
	- binary search to look for the target range
	- binary search to look for the item within that range
	Time 	O(logn)
	Space O(1)
	8ms
*/
func searchMatrix1(matrix [][]int, target int) bool {
	rowIdx := searchRow(matrix, target)
	if rowIdx == -1 {
		return false
	}
	targetRow := matrix[rowIdx]
	min := 0
	max := len(targetRow) - 1
	for min <= max {
		mean := (min + max) / 2
		if target < targetRow[mean] {
			max = mean - 1
		} else if target > targetRow[mean] {
			min = mean + 1
		} else {
			return true
		}
	}
	return false
}

func searchRow(matrix [][]int, target int) int {
	min := 0
	max := len(matrix) - 1
	for min <= max {
		mean := (min + max) / 2
		if len(matrix[mean]) == 0 {
			break
		}
		if target < matrix[mean][0] {
			max = mean - 1
		} else if target > matrix[mean][0] && target > matrix[mean][len(matrix[mean])-1] {
			min = mean + 1
		} else {
			return mean
		}
	}
	return -1
}

/*
	2nd approach:
	- merge the list, binary search
	Time 	O(logn)
	Space O(n)
	8ms
*/
func searchMatrix(matrix [][]int, target int) bool {
	combine := []int{}
	for i := 0; i < len(matrix); i++ {
		combine = append(combine, matrix[i]...)
	}
	min := 0
	max := len(combine) - 1
	for min <= max {
		mean := (min + max) / 2
		if target < combine[mean] {
			max = mean - 1
		} else if target > combine[mean] {
			min = mean + 1
		} else {
			return true
		}
	}
	return false
}

func main() {
	a := [][]int{
		[]int{1, 3, 5, 7},
		[]int{10, 11, 16, 20},
		[]int{23, 30, 34, 50},
	}
	fmt.Println(searchMatrix(a, 3))

	a = [][]int{
		[]int{10, 11, 16, 20},
		[]int{23, 30, 34, 50},
	}
	fmt.Println(searchMatrix(a, 3))

	a = [][]int{
		[]int{10, 11, 16, 20},
		[]int{23, 30, 34, 50},
	}
	fmt.Println(searchMatrix(a, 69))

	a = [][]int{}
	fmt.Println(searchMatrix(a, 69))

	a = [][]int{
		[]int{},
	}
	fmt.Println(searchMatrix(a, 69))
}
