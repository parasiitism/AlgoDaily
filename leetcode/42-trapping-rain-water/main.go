package main

import "fmt"

/*
	1st approach:
	1. go forward to record the max among previous items
	2. go backward to record the max among previous items
	3. calculate the trap volumn for each index

	forward = 	[0 0 1 1 2 2 2 2 3 3 3 3]
	backward =  [3 3 3 3 3 3 3 2 2 2 1 0]
	result =		[0 0 1 0 1 2 1 0 0 1 0 0]
	result = 		1+1+2+1+1 = 6

	32 ms, faster than 15.73%
*/
func trap(height []int) int {
	// go forward to record the max among previous items
	max := 0
	forward := []int{}
	for i := 0; i < len(height); i++ {
		h := height[i]
		forward = append(forward, max)
		max = findMax(max, h)
	}
	// go backward to record the max among previous items
	max = 0
	backward := []int{}
	for i := len(height) - 1; i >= 0; i-- {
		h := height[i]
		backward = append([]int{max}, backward...)
		max = findMax(max, h)
	}
	// calculate the trap volumn for each index
	res := 0
	for i := 0; i < len(height); i++ {
		f := forward[i]
		b := backward[i]
		m := findMin(f, b)
		if m > height[i] {
			res += m - height[i]
		}
	}
	return res
}

func findMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	fmt.Println(trap([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}))
}
