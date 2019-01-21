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

/*
	2nd approach
	- 2 pointers: one from the front, one from the end
	- move inward by retaining the heightest amongst the arr[i] and arr[j]
	- https://leetcode.com/articles/container-with-most-water/
	Time		O(n)
	Space		O(1)
	16ms beats 100%
	21jan2019
*/
func maxArea1(height []int) int {
	if len(height) < 2 {
		return 0
	}
	max := 0
	i, j := 0, len(height)-1
	for j > i {
		h := findMin(height[i], height[j])
		a := h * (j - i)
		if a > max {
			max = a
		}
		if height[i] < height[j] {
			i++
		} else {
			j--
		}
	}
	return max
}

func main() {
	fmt.Println(maxArea1([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
}
