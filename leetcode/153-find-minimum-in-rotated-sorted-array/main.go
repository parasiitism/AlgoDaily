package main

import (
	"fmt"
	"math"
)

// linear
func findMin0(nums []int) int {
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

/*
	suggested solution: mutated binary search
	actually i think it is hard to come up cos the "base cases" is too unusual

*/
func findMin2(nums []int) int {
	min := 0
	max := len(nums) - 1
	// make sure that there will be at least 2 numbers
	if len(nums) == 1 {
		return nums[0]
	}
	for min <= max {
		// if all numbers are sorted, left < right so that left is the mininum
		if nums[min] < nums[max] {
			return nums[min]
		}
		// get the mean
		mean := (min + max) / 2
		// since we are sure that there will be at least 2 numbers before we go down to 1 number where min == max
		// no need to check boundaries e.g. mean+1 < len(nums) && nums[mean] > nums[mean+1]
		// no need to check boundaries e.g. mean-1 >= 0 && nums[mean-1] > nums[mean]
		if nums[mean] > nums[mean+1] {
			return nums[mean+1]
		}
		if nums[mean-1] > nums[mean] {
			return nums[mean]
		}

		// always keep the pivot point e.g. 51234 -> 51 in the next iteration
		if nums[min] < nums[mean] {
			min = mean + 1
		} else {
			max = mean - 1
		}
	}
	return -1
}

// this derived solution(from suggested) is a lot easier to understand
func findMin3(nums []int) int {
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
		// always keep the pivot point e.g. 51234 -> 51 in the next iteration
		if nums[min] < nums[mean] {
			min = mean
		} else {
			max = mean
		}
	}
	// check the remains
	if nums[min] < nums[max] {
		return nums[min]
	}
	return nums[max]
}

func main() {
	fmt.Println(findMin2([]int{4}))
	fmt.Println(findMin2([]int{1, 2}))
	fmt.Println(findMin2([]int{2, 1}))
	fmt.Println(findMin2([]int{1, 2, 0}))
	fmt.Println(findMin2([]int{3, 1, 2}))
	fmt.Println("-----")
	fmt.Println(findMin2([]int{3, 4, 5, 1, 2}))
	fmt.Println(findMin2([]int{4, 5, 6, 7, 0, 1, 2}))
	fmt.Println(findMin2([]int{2, 3, 4, 5, 1}))
	fmt.Println(findMin2([]int{5, 1, 2, 3, 4}))
	fmt.Println(findMin2([]int{4, 5, 1, 2, 3}))
}
