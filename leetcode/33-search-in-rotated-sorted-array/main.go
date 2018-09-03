package main

import "fmt"

// requirement: Your algorithm's runtime complexity must be in the order of O(log n).
func search(nums []int, target int) int {
	min := 0
	max := len(nums) - 1
	for min <= max {
		mean := (min + max) / 2
		if target == nums[mean] {
			return mean
		} else if target < nums[mean] {
			// max = mean - 1
			if target < nums[min] && nums[mean] >= nums[min] {
				min = mean + 1
			} else {
				fmt.Println("wtf1", min, max, mean)
				max = mean - 1
			}
		} else if target > nums[mean] {
			// min = mean + 1
			if target > nums[max] && nums[mean] <= nums[max] {
				max = mean - 1
			} else {
				min = mean + 1
			}
		}
	}
	return -1
}

func main() {
}
