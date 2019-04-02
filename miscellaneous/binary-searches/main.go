package main

import (
	"fmt"
)

/*
	my related article
	- https://medium.com/@CalvinChankf/how-to-deal-with-lower-upper-bound-binary-search-b9ce744673df

	ref:
	- https://github.com/python/cpython/blob/master/Lib/bisect.py
*/

/*
	common
 	12345, search for 4
 	ans = index 3
*/
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

// recursive common
func RecursiveBinarySearch(arr []int, target int) int {
	min := 0
	max := len(arr) - 1
	return recursion(arr, min, max, target)
}

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

/*
	find the number than smaller or equal to the target

	e.g. 1
	12345, search for 4
	ans = index = 3

	e.g. 2
	1357, search for 4
	ans = index 1
*/
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

/*
	EndingPositionBinarySearch find the number than smaller or equal to the target

	e.g. 1
	12345, search for 4
	ans = index = 3

	e.g. 2
	1357, search for 4
	ans = index 2
*/
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

/*
	Starting Position Binary Search, also known as Lower Bound Binary Search
	1233345, search for 3
	ans = index 2
*/
func StartingPositionBinarySearch(arr []int, target int) int {
	min := 0
	max := len(arr)
	for min < max {
		mean := (min + max) / 2
		if target <= arr[mean] {
			max = mean
		} else {
			min = mean + 1
		}
	}
	return min
}

// recursive Starting Position Binary Search
func RecursiveStartingPositionBinarySearch(arr []int, target int) int {
	min := 0
	max := len(arr)
	res := startPosHelper(arr, target, min, max)
	return res
}

func startPosHelper(arr []int, target, min, max int) int {
	if min >= max {
		return min
	}
	mean := (min + max) / 2
	if target <= arr[mean] {
		return startPosHelper(arr, target, min, mean)
	}
	return startPosHelper(arr, target, mean+1, max)
}

/*
	Ending Position Binary Search = upper bound binary search - 1
	1233345, search for 3
	ans = index 4
*/
func EndingPositionBinarySearch(arr []int, target int) int {
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
	// we an either return min or max because they equal to each other after the forloop
	if arr[max] == target {
		return max
	}
	return -1
}

// recursive Ending Position Binary Search
func RecursiveEndingPositionBinarySearch(arr []int, target int) int {
	min := 0
	max := len(arr) - 1
	res := endingPosHelper(arr, target, min, max)
	if arr[res] == target {
		return res
	}
	return -1
}

func endingPosHelper(arr []int, target, min, max int) int {
	if min >= max {
		return min
	}
	mean := (min + max + 1) / 2
	if target >= arr[mean] {
		return endingPosHelper(arr, target, mean, max)
	}
	return endingPosHelper(arr, target, min, mean-1)
}

/*
	Upper Bound Binary Search
	1233345, search for 3
	ans = index 5 where the value is 4

	when the target is larger or equal to nums[i],
	left = mean + 1 because we are looking for the value that larger than target
*/
func UpperBoundBinarySearch(arr []int, target int) int {
	min := 0
	max := len(arr)
	for min < max {
		mean := (min + max) / 2
		if target >= arr[mean] {
			min = mean + 1
		} else {
			max = mean
		}
	}
	return max
}

func RecursiveUpperBoundBinarySearch(arr []int, target int) int {
	min := 0
	max := len(arr)
	res := upperHelper(arr, target, min, max)
	return res
}

func upperHelper(arr []int, target, min, max int) int {
	if min >= max {
		return min
	}
	mean := (min + max) / 2
	if target >= arr[mean] {
		return upperHelper(arr, target, mean+1, max)
	}
	return upperHelper(arr, target, min, mean)
}

/*
	e.g. a = [10, 20, 30, 40]
	print(Solution().bSearchNearest(a, 9)) <- 0
	print(Solution().bSearchNearest(a, 10)) <- 0
	print(Solution().bSearchNearest(a, 13)) <- 0
	print(Solution().bSearchNearest(a, 21)) <- 1
	print(Solution().bSearchNearest(a, 26)) <- 2
	print(Solution().bSearchNearest(a, 34)) <- 2
	print(Solution().bSearchNearest(a, 35)) <- 3
	print(Solution().bSearchNearest(a, 41)) <- 3
*/
func bSearchNearest(arr []int, target int) int {
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
	// compare and find the idx of the nearest item
	if max < 0 {
		return 0
	}
	if min > len(arr)-1 {
		return len(arr) - 1
	}
	if findAbs(target-arr[max]) < findAbs(target-arr[min]) {
		return max
	}
	return min
}

func findAbs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {

	// common
	fmt.Println("----normal----")
	a := []int{1, 2, 3, 4, 5}
	fmt.Println(CommonBinarySearch(a, 4))
	fmt.Println(RecursiveBinarySearch(a, 2))

	fmt.Println("----normal duplicate----")
	a = []int{1, 2, 2, 3, 3, 3, 4, 4, 5}
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
	fmt.Println("----lower bound---")
	c := []int{1, 2, 3, 3, 3, 4, 6}
	fmt.Println(StartingPositionBinarySearch(c, 3))
	fmt.Println(StartingPositionBinarySearch(c, 1))
	fmt.Println(StartingPositionBinarySearch(c, 5))
	fmt.Println(StartingPositionBinarySearch(c, 6))
	fmt.Println(StartingPositionBinarySearch(c, -2))
	fmt.Println(StartingPositionBinarySearch(c, 7))

	fmt.Println("----recursive lower bound---")
	fmt.Println(RecursiveStartingPositionBinarySearch(c, 3))
	fmt.Println(RecursiveStartingPositionBinarySearch(c, 1))
	fmt.Println(RecursiveStartingPositionBinarySearch(c, 5))
	fmt.Println(RecursiveStartingPositionBinarySearch(c, 6))
	fmt.Println(RecursiveStartingPositionBinarySearch(c, -2))
	fmt.Println(RecursiveStartingPositionBinarySearch(c, 7))

	fmt.Println("----ending bound ---")
	fmt.Println(EndingPositionBinarySearch(c, 3))
	fmt.Println(EndingPositionBinarySearch(c, 1))
	fmt.Println(EndingPositionBinarySearch(c, 5))
	fmt.Println(EndingPositionBinarySearch(c, 6))
	fmt.Println(EndingPositionBinarySearch(c, -2))
	fmt.Println(EndingPositionBinarySearch(c, 7))

	fmt.Println("----recursive ending bound -1 ---")
	fmt.Println(RecursiveEndingPositionBinarySearch(c, 3))
	fmt.Println(RecursiveEndingPositionBinarySearch(c, 1))
	fmt.Println(RecursiveEndingPositionBinarySearch(c, 5))
	fmt.Println(RecursiveEndingPositionBinarySearch(c, 6))
	fmt.Println(RecursiveEndingPositionBinarySearch(c, -2))
	fmt.Println(RecursiveEndingPositionBinarySearch(c, 7))

	fmt.Println("----upper bound ---")
	fmt.Println(UpperBoundBinarySearch(c, 3))
	fmt.Println(UpperBoundBinarySearch(c, 1))
	fmt.Println(UpperBoundBinarySearch(c, 5))
	fmt.Println(UpperBoundBinarySearch(c, 6))
	fmt.Println(UpperBoundBinarySearch(c, -2))
	fmt.Println(UpperBoundBinarySearch(c, 7))

	fmt.Println("----recursive upper bound ---")
	fmt.Println(RecursiveUpperBoundBinarySearch(c, 3))
	fmt.Println(RecursiveUpperBoundBinarySearch(c, 1))
	fmt.Println(RecursiveUpperBoundBinarySearch(c, 5))
	fmt.Println(RecursiveUpperBoundBinarySearch(c, 6))
	fmt.Println(RecursiveUpperBoundBinarySearch(c, -2))
	fmt.Println(RecursiveUpperBoundBinarySearch(c, 7))
}
