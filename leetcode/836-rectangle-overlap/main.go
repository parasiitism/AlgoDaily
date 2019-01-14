package main

import "fmt"

/*
	naive approach: check if lines overlap
	Time	O(1)
*/
func isRectangleOverlap(rec1 []int, rec2 []int) bool {
	xOverlap := false
	if rec1[0] < rec2[0] && rec1[2] > rec2[0] {
		xOverlap = true
	} else if rec1[0] > rec2[0] && rec1[0] < rec2[2] {
		xOverlap = true
	} else if rec1[0] == rec2[0] {
		xOverlap = true
	}
	yOverlap := false
	if rec1[1] < rec2[1] && rec1[3] > rec2[1] {
		yOverlap = true
	} else if rec1[1] > rec2[1] && rec1[1] < rec2[3] {
		yOverlap = true
	} else if rec1[1] == rec2[1] {
		yOverlap = true
	}
	return xOverlap && yOverlap
}

func main() {
	fmt.Println(isRectangleOverlap([]int{0, 0, 2, 2}, []int{1, 1, 3, 3}))   // true
	fmt.Println(isRectangleOverlap([]int{0, 0, 1, 1}, []int{1, 0, 2, 1}))   // false
	fmt.Println(isRectangleOverlap([]int{0, 0, 3, 3}, []int{1, 1, 2, 2}))   // true
	fmt.Println(isRectangleOverlap([]int{0, 0, 1, 1}, []int{-1, -1, 2, 2})) // true
	fmt.Println(isRectangleOverlap([]int{0, 0, 2, 2}, []int{-1, -1, 1, 1})) // true
	fmt.Println(isRectangleOverlap([]int{0, 0, 2, 2}, []int{-1, 0, 1, 1}))  // true
	fmt.Println(isRectangleOverlap([]int{4, 0, 6, 6}, []int{-5, -3, 4, 2})) // false
}
