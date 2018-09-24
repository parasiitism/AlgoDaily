package main

import (
	"math"
)

// linear
func findMin2(nums []int) int {
	min := math.MaxUint32
	for i := 0; i < len(nums); i++ {
		if nums[i] < min {
			min = nums[i]
		}
	}
	return min
}

// lower bound binary search
func findMin1(nums []int) int {
	min := 0
	max := len(nums) - 1
	for min < max {
		mean := (min + max) / 2
		if nums[mean] < nums[max] {
			max = mean
		} else {
			min = mean + 1
		}
	}
	return nums[min]
}

// suggested solution: mutated binary search
// actually i think it is hard to come up cos the "base cases" is too unusual
func findMin0(nums []int) int {
	min := 0
	max := len(nums) - 1
	if len(nums) == 1 {
		return nums[0]
	}
	if nums[min] < nums[max] {
		return nums[min]
	}
	for min <= max {
		mean := (min + max) / 2
		// base cases
		if nums[mean] > nums[mean+1] {
			return nums[mean+1]
		}
		if nums[mean-1] > nums[mean] {
			return nums[mean]
		}

		// always keep the pivot point e.g. 51234, 23451
		if nums[min] < nums[mean] {
			min = mean + 1
		} else {
			max = mean - 1
		}
	}
	return -1
}

// this derived solution(from suggested) is a lot easier to understand
func findMin(nums []int) int {
	min := 0
	max := len(nums) - 1
	if len(nums) == 1 {
		return nums[0]
	}
	if nums[min] < nums[max] {
		return nums[min]
	}
	// keep 2 items at the end
	for min+1 < max {
		mean := (min + max) / 2
		// always keep the pivot point e.g. 51234, 23451
		if nums[min] < nums[mean] {
			min = mean
		} else {
			max = mean
		}
	}
	// check the remains
	if nums[min] < nums[max] {
		return nums[min]
	} else {
		return nums[max]
	}
}

func main() {
	// ans := findMin([]int{4})
	// ans := findMin([]int{1, 2})
	// ans := findMin([]int{2, 1})
	// ans := findMin([]int{1, 2, 0})
	// ans := findMin([]int{3, 1, 2})
	// ans := findMin([]int{3, 4, 5, 1, 2})
	// ans := findMin([]int{4, 5, 6, 7, 0, 1, 2})
	// ans := findMin([]int{2, 3, 4, 5, 1})
	// ans := findMin([]int{5, 1, 2, 3, 4})
	// ans := findMin([]int{4, 5, 1, 2, 3})
	// fmt.Println(ans)
}
