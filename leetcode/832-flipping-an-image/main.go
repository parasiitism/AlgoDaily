package main

import "fmt"

/*
	1st approach
	1. just iterate from the back of each subarray
	2. NOT the binary value
	3. put the item into the result
	Time		O(n)
	Space		O(n)
	4ms beats 100%
	23jan2019
*/
func flipAndInvertImage(A [][]int) [][]int {
	res := [][]int{}
	for i := 0; i < len(A); i++ {
		temp := []int{}
		for j := len(A[i]) - 1; j >= 0; j-- {
			x := A[i][j]
			if x == 0 {
				temp = append(temp, 1)
			} else {
				temp = append(temp, 0)
			}
		}
		res = append(res, temp)
	}
	return res
}

func main() {

	a := [][]int{}
	fmt.Println(flipAndInvertImage(a))

	a = [][]int{
		{},
	}
	fmt.Println(flipAndInvertImage(a))

	a = [][]int{
		{1},
	}
	fmt.Println(flipAndInvertImage(a))

	a = [][]int{
		{1, 1, 0},
		{1, 0, 1},
		{0, 0, 0},
	}
	fmt.Println(flipAndInvertImage(a))

	a = [][]int{
		{1, 1, 0, 0},
		{1, 0, 1, 0},
		{0, 0, 0, 1},
	}
	fmt.Println(flipAndInvertImage(a))

	a = [][]int{
		{1, 1, 0, 0},
		{1, 0, 0, 1},
		{0, 1, 1, 1},
		{1, 0, 1, 0},
	}
	fmt.Println(flipAndInvertImage(a))
}
