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

	left, right := find_range(arr, k, x, target)

	return arr[left : right+1]
}

func find_range(arr []int, k int, x int, target int) (int, int) {
	var left int
	var right int

	left = target
	right = target

	for right-left+1 < k {
		if left == 0 {
			right = right + 1
		} else if right == len(arr)-1 {
			left = left - 1
		} else if Abs(x-arr[left-1]) <= Abs(x-arr[right+1]) {
			left = left - 1
		} else {
			right = right + 1
		}
	}
	fmt.Println(left, right)
	return left, right
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {

	a := []int{0, 1, 2, 2, 2, 3, 6, 8, 8, 9}
	oops := findClosestElements(a, 5, 9)
	// bsearch(a, 9)
	// min, max := abc(a, 5, 9, 9)
	// oops := a[min : max+1]
	fmt.Println(oops)

	// a := []int{1, 3}

	// fmt.Println("target no 2")
	// abc(a, 1, 2, 0)
	// abc(a, 2, 2, 0)

	// a = []int{1, 10}

	// fmt.Println("target no 9")
	// abc(a, 1, 9, 1)
	// abc(a, 2, 9, 1)

	// a = []int{1, 2, 3, 4, 5}

	// // target -1
	// fmt.Println("target -1")
	// abc(a, 1, -1, 0)
	// abc(a, 2, -1, 0)
	// abc(a, 3, -1, 0)

	// // target 1
	// fmt.Println("target 1")
	// abc(a, 1, 1, 0)
	// abc(a, 2, 1, 0)

	// // target 2
	// fmt.Println("target 2")
	// abc(a, 1, 2, 1)
	// abc(a, 2, 2, 1)
	// abc(a, 3, 2, 1)

	// // target 3
	// fmt.Println("target 3")
	// abc(a, 1, 3, 2)
	// abc(a, 2, 3, 2)
	// abc(a, 3, 3, 2)

	// // target 4
	// fmt.Println("target 4")
	// abc(a, 1, 4, 3)
	// abc(a, 2, 4, 3)
	// abc(a, 3, 4, 3)

	// // target 5
	// fmt.Println("target 5")
	// abc(a, 1, 5, 4)
	// abc(a, 2, 5, 4)
	// abc(a, 3, 5, 4)

	// fmt.Println("target no 3")
	// a = []int{1, 2, 4, 5}
	// abc(a, 1, 3, 1)
	// abc(a, 2, 3, 1)
	// abc(a, 3, 3, 1)
	// abc(a, 4, 3, 1)

	// fmt.Println("target no 3 near left")
	// a = []int{1, 2, 5, 6}
	// abc(a, 1, 3, 1)
	// abc(a, 2, 3, 1)
	// abc(a, 3, 3, 1)
	// abc(a, 4, 3, 1)

	// fmt.Println("target no 4 near left")
	// a = []int{1, 2, 5, 6}
	// abc(a, 1, 4, 2)
	// abc(a, 2, 4, 2)
	// abc(a, 3, 4, 2)
	// abc(a, 4, 4, 2)
}
