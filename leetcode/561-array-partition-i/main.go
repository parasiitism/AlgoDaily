package main

import (
	"fmt"
	"sort"
)

/*
	1st approach
	- sort
	- sum all the pairs
	Time	O(logn)
	Space	O(1)
	140ms beats 5.48%
	23jan2019
*/
func arrayPairSum(nums []int) int {
	sum := 0
	sort.Ints(nums)
	for i := 0; i < len(nums); i += 2 {
		temp := findMin(nums[i], nums[i+1])
		sum += temp
	}
	return sum
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/*
	2nd approach
	- optimize the 1st approach
	- actually when u sort the array, the left item must be smaller than the right
	Time	O(logn)
	Space	O(1)
	128ms beats 12.33%
	23jan2019
*/
func arrayPairSum1(nums []int) int {
	sum := 0
	sort.Ints(nums)
	for i := 0; i < len(nums); i += 2 {
		sum += nums[i]
	}
	return sum
}

func main() {
	fmt.Println(arrayPairSum1([]int{1, 4, 3, 2}))
	fmt.Println(arrayPairSum1([]int{1, 4, 3, 2, -3, -4, -3, -2}))
}
