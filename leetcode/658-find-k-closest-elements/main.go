package main

import (
	"fmt"
)

// binary search
func bsearch(nums []int, target int) (int, int, int) {
	min := 0
	max := len(nums) - 1
	var mean int
	for min <= max {
		mean = (min + max) / 2
		if target == nums[mean] {
			return min, max, mean
		} else if target > nums[mean] {
			min = mean + 1
		} else if target < nums[mean] {
			max = mean - 1
		}
	}
	fmt.Println(min, max)
	return min, max, -1
}

func findClosestElements(arr []int, k int, x int) []int {
	if k >= len(arr) {
		return arr
	}
	min, max, mean := bsearch(arr, x)
	var target int
	if mean != -1 {
		target = mean
	} else if max == -1 {
		target = min
	} else if max == len(arr)-1 {
		target = max
	} else {
		if x-arr[max] <= arr[max+1]-x {
			target = max
		} else {
			target = max + 1
		}
	}
	fmt.Println("target", target)

	var left int
	var right int

	left = target
	right = target

	for right-left+1 < k {
	}

	return []int{left, right}
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	a := []int{1, 2, 3, 4, 5}
	b := findClosestElements(a, 3, 6)
	fmt.Println(b)
}
