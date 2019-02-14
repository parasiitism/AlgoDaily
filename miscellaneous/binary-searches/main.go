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

// find the number than smaller or equal to the target
// e.g. 1
// 12345, search for 4
// ans = index = 3
// e.g. 2
// 1357, search for 4
// ans = index = 1
func CommonBinarySearchNoLargerThanTarget(arr []int, target int) int {
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
	return max
}

// find the number than smaller or equal to the target
// e.g. 1
// 12345, search for 4
// ans = index = 3
// e.g. 2
// 1357, search for 4
// ans = index = 2
func CommonBinarySearchNoSmallerThanTarget(arr []int, target int) int {
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
	if min == len(arr) {
		return -1
	}
	return min
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

	// common
	fmt.Println("----normal----")
	a := []int{1, 2, 3, 4, 5}
	fmt.Println(CommonBinarySearch(a, 4))
	fmt.Println(RecursiveBinarySearch(a, 2))

	// smaller than or equal to
	fmt.Println("----smaller than or equal to----")
	b := []int{1, 3, 5, 7}
	fmt.Println(CommonBinarySearchNoLargerThanTarget(b, 0))
	fmt.Println(CommonBinarySearchNoLargerThanTarget(b, 2))
	fmt.Println(CommonBinarySearchNoLargerThanTarget(b, 4))
	fmt.Println(CommonBinarySearchNoLargerThanTarget(b, 6))
	fmt.Println(CommonBinarySearchNoLargerThanTarget(b, 8))

	// equal to or larger than
	fmt.Println("----equal to or larger than----")
	fmt.Println(CommonBinarySearchNoSmallerThanTarget(b, 0))
	fmt.Println(CommonBinarySearchNoSmallerThanTarget(b, 2))
	fmt.Println(CommonBinarySearchNoSmallerThanTarget(b, 4))
	fmt.Println(CommonBinarySearchNoSmallerThanTarget(b, 6))
	fmt.Println(CommonBinarySearchNoSmallerThanTarget(b, 8))

	// boundaries
	fmt.Println("----boundaries----")
	c := []int{1, 2, 3, 3, 3, 4, 6}
	fmt.Println(LowerBoundBinarySearch(c, 6))
	fmt.Println(UpperBoundBinarySearch(c, 6))
}

// no test cases, i am lazy
// https://medium.com/@CalvinChankf/how-to-deal-with-lower-upper-bound-binary-search-b9ce744673df
