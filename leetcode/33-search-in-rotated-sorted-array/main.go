package main

/*
	1st approach: still binary search but refactor a bit for understanding
	4ms
*/
func search1(nums []int, target int) int {
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

/*
	2nd approach: still binary search but refactor a bit for understanding
	4ms
*/
func search(nums []int, target int) int {
	min := 0
	max := len(nums) - 1
	for min <= max {
		mean := (min + max) / 2
		if target == nums[mean] {
			return mean
		} else if target < nums[mean] {
			// search left when target < nums[min] OR the pivot point is here(it means the min is here)
			// basic: max = mean - 1
			if nums[min] <= target || nums[min] > nums[mean] {
				max = mean - 1
			} else {
				// otherwise, search for another half
				min = mean + 1
			}
		} else {
			// search right when target < nums[max] OR the pivot point is here(it means the max is here)
			// basic: min = mean + 1
			if target <= nums[max] || nums[mean] > nums[max] {
				min = mean + 1
			} else {
				// otherwise, search for another half
				max = mean - 1
			}
		}
	}
	return -1
}

func main() {
}
