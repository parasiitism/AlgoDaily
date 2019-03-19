package main

import "fmt"

/*
	classic approach: binary search with conditions
	- when we look for a the number lerger than the mid, we do bearch when either
		1. the pivot point is in the right hand side(which means maximum is in the right)
		2. normally when no pivot but target is <= nums[right]
	- similar logic for the left-handed side
	- However for duplicates numbers on both ends,
	we should not consider the left most number(or right most) until there are no duplicate numbers on both ends

	Time	O(logn) if no duplicates, O(n) if duplicates present on both ends
	Space	O(1)
	4ms beats 100%
*/
func search(nums []int, target int) int {
	left := 0
	right := len(nums) - 1
	for left <= right {
		// this is the trickiest part, if both ends have the same number
		// dont consider the left most number until there are no duplicate numbers on both ends
		for left < right && nums[left] == nums[right] {
			left++
		}
		// below looks the same with lc33
		mid := (left + right) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			if nums[mid] > nums[right] || target <= nums[right] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		} else {
			if nums[left] > nums[mid] || target >= nums[left] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		}
	}
	return -1
}

func main() {
	fmt.Println(search([]int{3, 1}, 1))
	fmt.Println(search([]int{1, 1, 3, 1}, 3))
	fmt.Println(search([]int{1, 1, 3, 1, 1, 1, 1}, 1))
}
