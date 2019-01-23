package main

import (
	"fmt"
)

// common
// 12345, search for 4
// ans = index = 3
func CommonBinarySearch(arr []int, target int) int {
	min := 0
	max := len(arr) - 1
	for min <= max {
		mean := (min + max) / 2
		if target == arr[mean] {
			return mean
		} else if target > arr[mean] {
			min = mean + 1
		} else if target < arr[mean] {
			max = mean - 1
		}
	}
	return -1
}

// lower bound
// 1233345, search for 3
// ans = index = 2
func LowerBoundBinarySearch(arr []int, target int) int {
	min := 0
	max := len(arr) - 1
	for min < max {
		mean := (min + max) / 2
		if target <= arr[mean] {
			max = mean
		} else {
			min = mean + 1
		}
	}
	if arr[min] == target {
		return min
	}
	return -1
}

// upper bound
// 1233345, search for 3
// ans = index = 4
func UpperBoundBinarySearch(arr []int, target int) int {
	min := 0
	max := len(arr) - 1
	for min < max {
		mean := (min + max + 1) / 2
		if target >= arr[mean] {
			min = mean
		} else {
			max = mean - 1
		}
	}
	if arr[max] == target {
		return max
	}
	return -1
}

// recursive
func RecursiveBinarySearch(arr []int, target int) int {
	min := 0
	max := len(arr) - 1
	return recursion(arr, min, max, target)
}

// write this outside the main function,
// so to understand the logic of returning

/* go over all the paths
func recursion(arr []int, min int, max int, target int) int {
	if min > max {
		return -1
	}
	mean := (min + max) / 2
	if arr[mean] == target {
		return mean
	}
	left := recursion(arr, min, mean-1, target)
	right := recursion(arr, mean+1, max, target)
	if left != -1 {
		return left
	}
	return right
}
*/

// same as above but go over less paths and more concise
func recursion(arr []int, min int, max int, target int) int {
	if min > max {
		return -1
	}
	mean := (min + max) / 2
	if arr[mean] == target {
		return mean
	}
	if target < arr[mean] {
		return recursion(arr, min, mean-1, target)
	}
	return recursion(arr, mean+1, max, target)
}

func main() {
	a := []int{1, 2, 3, 4, 5}
	b := []int{1, 2, 3, 3, 3, 4, 6}
	fmt.Println(CommonBinarySearch(a, 4))
	fmt.Println(LowerBoundBinarySearch(b, 6))
	fmt.Println(UpperBoundBinarySearch(b, 6))
	fmt.Println(RecursiveBinarySearch(a, 2))
	c := []int{2, 3, 6, 8}
	fmt.Println(LowerBoundBinarySearch(c, 7))
}

// no test cases, i am lazy
// https://medium.com/@CalvinChankf/how-to-deal-with-lower-upper-bound-binary-search-b9ce744673df
