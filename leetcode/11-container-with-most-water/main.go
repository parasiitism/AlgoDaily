package main

import "fmt"

/*
	1st approach:
	- naive brute force
	Time		O(n^2)
	Space		O(1)
	368ms beats 34.48%
	21jan2019
*/
func maxArea(height []int) int {
	if len(height) < 2 {
		return 0
	}
	max := 0
	for i := 1; i < len(height); i++ {
		localmax := 0
		for j := 0; j < i; j++ {
			h := findMin(height[i], height[j])
			a := h * (i - j)
			if a > localmax {
				localmax = a
			}
		}
		if localmax > max {
			max = localmax
		}
	}
	return max
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	fmt.Println(maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
}
