package main

import "fmt"

func search1(nums []int, target int) int {
	min := 0
	max := len(nums) - 1
	for min <= max {
		mean := (min + max) / 2
		if target == nums[mean] {
			return mean
		} else if target > nums[mean] {
			min = mean + 1
		} else if target < nums[mean] {
			max = mean - 1
		}
	}
	return -1
}

// template 2
// cant break the loop if target not found
func search2(nums []int, target int) int {
	min := 0
	max := len(nums)
	for min < max {
		mean := (min + max) / 2
		if target > nums[mean] {
			max = mean + 1
		} else {
			min = mean
		}
	}
	fmt.Println("search2", min, max)
	return min
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	target := -1
	ans := search1(nums, target)
	fmt.Println(ans)
	ans = search2(nums, target)
	fmt.Println(ans)
}
