package main

/*
	questions to ask:
	- will there be duplicate values? yes but not for now...see leecode 81
*/

/*
	1st approach: binary search with conditions
	- when we look for a the number lerger than the mid, we do bearch when either
		1. the pivot point is in the right hand side(which means maximum is in the right)
		2. normally when no pivot but target is <= nums[right]
	- similar logic for the left-handed side

	Time	O(logn)
	Space	O(1)
	0ms beats 100%
*/
func search(nums []int, target int) int {
	left := 0
	right := len(nums) - 1
	for left <= right {
		mid := (left + right) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			// search right when the pivot is here OR normally nums[mid] < nums[right] and target <= nums[right]
			if nums[mid] > nums[right] || (nums[mid] < nums[right] && target <= nums[right]) {
				// it is what we do in the basic bsearch: left = mid + 1
				left = mid + 1
			} else {
				// otherwise search in another half
				right = mid - 1
			}
		} else {
			// search left when the pivot is here OR normally nums[left] < nums[mid] and target >= nums[left]
			if nums[left] > nums[mid] || (nums[left] < nums[mid] && target >= nums[left]) {
				// it is what we do in the basic bsearch: right = mid - 1
				right = mid - 1
			} else {
				// otherwise search in another half
				left = mid + 1
			}
		}
	}
	return -1
}

/*
	2nd approach: still binary search but refactor a bit for understanding

	Time	O(logn)
	Space	O(1)
	0ms beats 100%
*/
func search1(nums []int, target int) int {
	left := 0
	right := len(nums) - 1
	for left <= right {
		mid := (left + right) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			// search right when the pivot is here OR normally nums[mid] < nums[right] and target <= nums[right]
			if nums[mid] > nums[right] || target <= nums[right] {
				// it is what we do in the basic bsearch: left = mid + 1
				left = mid + 1
			} else {
				// otherwise search in another half
				right = mid - 1
			}
		} else {
			// search left when the pivot is here OR normally nums[left] < nums[mid] and target >= nums[left]
			if nums[left] > nums[mid] || target >= nums[left] {
				// it is what we do in the basic bsearch: right = mid - 1
				right = mid - 1
			} else {
				// otherwise search in another half
				left = mid + 1
			}
		}
	}
	return -1
}

func main() {
}
