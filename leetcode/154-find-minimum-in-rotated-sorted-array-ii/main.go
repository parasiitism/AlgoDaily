package main

import (
	"fmt"
	"math"
)

// linear
func findMin_(nums []int) int {
	min := math.MaxUint32
	for i := 0; i < len(nums); i++ {
		if nums[i] < min {
			min = nums[i]
		}
	}
	return min
}

/*
	learned from others:
	- https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/48808/My-pretty-simple-code-to-solve-it

	Time 	O(logn) -> O(n) worest if many duplicate numbers
	Time	O(1)
	8 ms, faster than 12.90%
*/
func findMin(nums []int) int {
	min := 0
	max := len(nums) - 1
	// keep 2 items at the end
	for min < max {
		mean := (min + max) / 2
		if nums[mean] > nums[max] {
			// if pivot point is on the right, search right-handed side
			min = mean + 1
		} else if nums[mean] < nums[max] {
			// right-handed side is normal, minimum must on the left or the mean itself
			max = mean
		} else {
			// we are not sure the position of minimum in mid's left or right,
			// so just let upper bound reduce one since we are finding minimum
			max--
		}
	}
	// check the remains
	return nums[min]
}

func main() {
	fmt.Println(findMin([]int{1, 1}))
	fmt.Println(findMin([]int{1, 3, 3}))
	fmt.Println(findMin([]int{3, 1, 3, 3}))
	fmt.Println(findMin([]int{3, 3, 3, 1}))
	fmt.Println(findMin([]int{2, 3, 2, 2}))
	fmt.Println(findMin([]int{2, 2, 1, 2}))
	fmt.Println(findMin([]int{10, 1, 10, 10, 10}))
}
