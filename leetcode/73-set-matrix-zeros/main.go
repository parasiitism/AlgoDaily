package main

import "fmt"

/*
	Questions to ask:
	- will there be other numbers/characters?
	- is the input array a legit rectangle? any notches?
*/

/*
	naive approach
	- save the x, y in an array for zeros
	- iterate the input k times to set zeros
	Time	O(kn)
	Space	O(n)
	not gonna implement
*/

/*
	1st approach
	- hashtable to save the coordinates of zeros
	Time	O(2n)
	Space	O(n) depends on the occurence of zeros
	28ms beats 52.38%
	31jan2019
*/
func setZeroes(matrix [][]int) {
	targetI := make(map[int]bool)
	targetJ := make(map[int]bool)

	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == 0 {
				targetI[i] = true
				targetJ[j] = true
			}
		}
	}

	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if _, x := targetI[i]; x {
				matrix[i][j] = 0
			}
			if _, x := targetJ[j]; x {
				matrix[i][j] = 0
			}
		}
	}
}

func main() {
	/*
		{1, 0, 1},
		{0, 0, 0},
		{1, 0, 1},
	*/
	a := [][]int{
		{1, 1, 1},
		{1, 0, 1},
		{1, 1, 1},
	}
	setZeroes(a)
	fmt.Println(a)

	/*
		{1, 1, 0},
		{1, 1, 0},
		{0, 0, 0},
	*/
	a = [][]int{
		{1, 1, 1},
		{1, 1, 1},
		{1, 1, 0},
	}
	setZeroes(a)
	fmt.Println(a)

	/*
		{0, 0, 0, 0},
		{0, 4, 5, 0},
		{0, 3, 1, 0},
	*/
	a = [][]int{
		{0, 1, 2, 0},
		{3, 4, 5, 2},
		{1, 3, 1, 5},
	}
	setZeroes(a)
	fmt.Println(a)
}
