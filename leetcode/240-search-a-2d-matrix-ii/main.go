package main

import "fmt"

/*
	1st approach: many binary searches LOL
	Time O(nlogn)
	32 ms, beats 100.00%
*/
func searchMatrix(matrix [][]int, target int) bool {
	row := searchRow(matrix, target)
	if row < 0 {
		return false
	}
	col := searchCol(matrix, target)
	if row < 0 || col < 0 {
		return false
	}

	for i := row; i >= 0; i-- {
		temp := matrix[i][:col+1]
		x := binarySearch(temp, target)
		if x > -1 {
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
		} else if target > matrix[mean][0] {
			if mean+1 < len(matrix) && target >= matrix[mean+1][0] {
				min = mean + 1
			} else {
				return mean
			}
		} else {
			return mean
		}
	}
	return -1
}

func searchCol(matrix [][]int, target int) int {
	firstRow := matrix[0]
	if len(firstRow) == 0 {
		return -1
	}
	min := 0
	max := len(firstRow) - 1
	for min <= max {
		mean := (min + max) / 2
		if target < firstRow[mean] {
			max = mean - 1
		} else if target > firstRow[mean] {
			if mean+1 < len(firstRow) && target >= firstRow[mean+1] {
				min = mean + 1
			} else {
				return mean
			}
		} else {
			return mean
		}
	}
	return -1
}

func binarySearch(nums []int, target int) int {
	min := 0
	max := len(nums) - 1
	for min <= max {
		mean := (min + max) / 2
		if target < nums[mean] {
			max = mean - 1
		} else if target > nums[mean] {
			min = mean + 1
		} else {
			return mean
		}
	}
	return -1
}

func main() {

	a := [][]int{
		[]int{1, 4, 7, 11, 15},
		[]int{2, 5, 8, 12, 19},
		[]int{3, 6, 9, 16, 22},
		[]int{10, 13, 14, 17, 24},
		[]int{18, 21, 23, 26, 30},
	}
	fmt.Println(searchMatrix(a, -1))
	fmt.Println(searchMatrix(a, 5))
	fmt.Println(searchMatrix(a, 12))
	fmt.Println(searchMatrix(a, 13))
	fmt.Println(searchMatrix(a, 16))
	fmt.Println(searchMatrix(a, 30))
	fmt.Println(searchMatrix(a, 31))

	a = [][]int{}
	fmt.Println(searchMatrix(a, 69))

	a = [][]int{
		[]int{},
	}
	fmt.Println(searchMatrix(a, 69))
}
