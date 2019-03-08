package main

import "sort"

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

func main() {

}
