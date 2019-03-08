package main

import (
	"fmt"
	"math"
	"sort"
)

/*
	questions to ask:
	- will there be no subarrary need to sort? all numbers are sorted? yes

	1st approach:
	1. compare the nums with its sorted result
	2. 2 pointers to look for the boundaries

	Time	O(nlogn)
	Space	O(n)
	44 ms, faster than 45.21%
*/
func findUnsortedSubarray(nums []int) int {
	clone := []int{}
	for _, num := range nums {
		clone = append(clone, num)
	}
	sort.Ints(clone)
	left := 0
	right := len(nums) - 1
	for left < right {
		if nums[left] != clone[left] && nums[right] != clone[right] {
			break
		}
		if nums[left] == clone[left] {
			left++
		}
		if nums[right] == clone[right] {
			right--
		}
	}
	if left == right {
		return 0
	}
	return right - left + 1
}

/*
	2nd approach
	- when the numbers change its direction, i call it pivot. e.g. 2, 4, 6, 5 <- 6 is the pivot point
	1. find the min after pivot
	2. find the max after pivot
	3. find the correct position of min and max

	Time	O(n)
	Space	O(1)
	24 ms, faster than 100.00%
*/
func findUnsortedSubarray1(nums []int) int {
	if len(nums) <= 1 {
		return 0
	}
	// find the min after pivot
	min := math.MaxInt64
	rising := true
	for i := 1; i < len(nums); i++ {
		if nums[i-1] > nums[i] {
			rising = false
		}
		if rising == false && nums[i] < min {
			min = nums[i]
		}
	}
	// find the max after pivot
	max := math.MinInt64
	dropping := true
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i] > nums[i+1] {
			dropping = false
		}
		if dropping == false && nums[i] > max {
			max = nums[i]
		}
	}
	// find the correct position of min and max
	left := 0
	for i := 0; i < len(nums); i++ {
		if min < nums[i] {
			left = i
			break
		}
	}
	right := 0
	for i := len(nums) - 1; i >= 0; i-- {
		if max > nums[i] {
			right = i
			break
		}
	}
	if left == right {
		return 0
	}
	return right - left + 1
}

func main() {
	fmt.Println(findUnsortedSubarray1([]int{6, 4, 8, 10, 9, 15}))
	fmt.Println(findUnsortedSubarray1([]int{2, 6, 4, 8, 10, 9}))
	fmt.Println(findUnsortedSubarray1([]int{2, 6, 4, 8, 10, 9, 15}))

	fmt.Println(findUnsortedSubarray1([]int{1, 2, 3}))
	fmt.Println(findUnsortedSubarray1([]int{3, 2, 1}))

	fmt.Println(findUnsortedSubarray1([]int{3, 2, 4}))
	fmt.Println(findUnsortedSubarray1([]int{1, 3, 2}))

	fmt.Println(findUnsortedSubarray1([]int{1}))
	fmt.Println(findUnsortedSubarray1([]int{}))
}
