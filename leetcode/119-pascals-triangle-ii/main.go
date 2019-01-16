package main

import "fmt"

/*
	1st approach:
	- intuitive approach according to the desc, similar to leetcode118
	Time		O(n!)
	Space		O(n!) the result
	16jan2019
*/
func getRow1(rowIndex int) []int {
	numRows := rowIndex + 1
	if numRows == 0 {
		return []int{}
	}
	if numRows == 1 {
		return []int{1}
	}
	if numRows == 1 {
		return []int{1, 1}
	}
	res := [][]int{
		{1},
		{1, 1},
	}
	for i := 2; i < numRows; i++ {
		for j := 0; j <= i; j++ {
			if j == 0 {
				res = append(res, []int{1})
			} else if j < i {
				temp := res[i-1][j-1] + res[i-1][j]
				res[i] = append(res[i], temp)
			} else {
				res[i] = append(res[i], 1)
			}
		}
	}
	return res[rowIndex]
}

/*
	2nd approach:
	- optimize the 1st approach
	- actually we just need the previous layer so we dont need a 2D array
	Time		O(n!)
	Space		O(n) the result
	16jan2019
*/
func getRow(rowIndex int) []int {
	numRows := rowIndex + 1
	if numRows == 0 {
		return []int{}
	}
	if numRows == 1 {
		return []int{1}
	}
	if numRows == 1 {
		return []int{1, 1}
	}
	res := []int{1, 1}
	for i := 2; i < numRows; i++ {
		temp := []int{}
		for j := 0; j <= i; j++ {
			if j == 0 {
				temp = append(temp, 1)
			} else if j < i {
				x := res[j-1] + res[j]
				temp = append(temp, x)
			} else {
				temp = append(temp, 1)
			}
		}
		res = temp
	}
	return res
}

func main() {
	fmt.Println(getRow(3))
	fmt.Println(getRow(4))
	fmt.Println(getRow(10))
}
