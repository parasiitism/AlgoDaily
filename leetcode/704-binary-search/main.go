package main

import "fmt"

func search(nums []int, target int) int {
	min := 0
	max := len(nums) - 1
	for min <= max {
		middle := (min + max) / 2
		if target == nums[middle] {
			return middle
		} else if target > nums[middle] {
			min = middle + 1
		} else if target < nums[middle] {
			max = middle - 1
		}
	}
	return -1
}

func main() {
	nums := []int{}
	target := 10
	ans := search(nums, target)
	fmt.Println(ans)
}
