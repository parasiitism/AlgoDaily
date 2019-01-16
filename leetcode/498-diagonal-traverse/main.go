package main

import "fmt"

/*
	Questions to ask:
	- M will be larger or smaller than N?
	- will there be any nudge in the matrix? e.g. [[1,2],[3], [4,5]]?
*/

/*
	1st approach:
	- put the elements into a 2D array which the indeces sum == index of the 2D array
		e.g.
		[1,2,3]
		[4,5,6]
		[7,8,9]
		2D array
		idx = 0, [1] 			<- nums[0,0] = 1
		idx = 1, [2,4] 		<- nums[0,1]=2, nums[1,0]=4
		idx = 2, [3,5,7] 	<- nums[0,2]=3 nums[1,1]=5, nums[2,0]=7
		idx = 3, [6,8] 		<- nums[1,2]=6 nums[3,0]=8
		idx = 4, [0] 			<- nums[2,2]=9
	- put the items to the result array
	- for even rows, put reversely
	Time		O(2*m*n)
	Space		O(m*n) the 2D array
	288ms beats 22.22%
	16jan2019
*/
func findDiagonalOrder(matrix [][]int) []int {
	raw := [][]int{}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if i+j < len(raw) {
				raw[i+j] = append(raw[i+j], matrix[i][j])
			} else {
				raw = append(raw, []int{matrix[i][j]})
			}
		}
	}
	result := []int{}
	for i := 0; i < len(raw); i++ {
		if i%2 == 0 {
			for j := len(raw[i]) - 1; j >= 0; j-- {
				result = append(result, raw[i][j])
			}
		} else {
			result = append(result, raw[i]...)
		}
	}
	return result
}

func main() {
	fmt.Println(findDiagonalOrder([][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}))

	fmt.Println(findDiagonalOrder([][]int{
		{1, 2},
		{3, 4},
		{5, 6},
	}))

	fmt.Println(findDiagonalOrder([][]int{
		{1, 2, 3},
		{4, 5, 6},
	}))

	fmt.Println(findDiagonalOrder([][]int{
		{1},
	}))

	fmt.Println(findDiagonalOrder([][]int{
		{},
	}))

	fmt.Println(findDiagonalOrder([][]int{}))
}
