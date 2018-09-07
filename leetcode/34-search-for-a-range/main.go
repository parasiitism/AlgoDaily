package main

// binary search
func searchRange(nums []int, target int) []int {

	// at first, get anyone of the index of target
	min := 0
	max := len(nums) - 1
	target_idx := -1
	for min <= max {
		mean := (min + max) / 2
		if target == nums[mean] {
			target_idx = mean
			break
		} else if target > nums[mean] {
			min = mean + 1
		} else if target < nums[mean] {
			max = mean - 1
		}
	}

	if target_idx == -1 {
		return []int{-1, -1}
	}

	// search for the lower & upper bounds
	lower := findlowerBound(nums, target, target_idx)
	upper := findUpperBound(nums, target, target_idx)

	result := []int{lower, upper}

	return result
}

// 1 2 3 3 3 3 4 5
// find 3
func findlowerBound(nums []int, target int, target_idx int) int {
	min := 0
	max := target_idx
	for min < max {
		mean := (min + max) / 2
		if target > nums[mean] {
			min = mean + 1
		} else {
			max = mean
		}
	}
	return min
}

func findUpperBound(nums []int, target int, target_idx int) int {
	min := target_idx
	max := len(nums) - 1
	for min < max {
		mean := (min + max + 1) / 2 // round to the ceiling
		if target < nums[mean] {
			max = mean - 1
		} else {
			min = mean
		}
	}
	return max
}

func main() {
}
