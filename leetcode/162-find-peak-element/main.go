package main

import (
	"fmt"
	"math"
)

func findPeakElement(nums []int) int {
	if len(nums) == 0 {
		return -1
	} else if len(nums) == 1 {
		return 0
	} else if len(nums) == 2 {
		if nums[0] > nums[1] {
			return 0
		} else {
			return 1
		}
	} else {
		var left int
		var right int
		for i := 0; i < len(nums); i++ {
			if i > 0 {
				left = nums[i-1]
			} else {
				left = -math.MaxUint32
			}
			x := nums[i]
			if i < len(nums)-1 {
				right = nums[i+1]
			} else {
				right = -math.MaxUint32
			}
			if x > left && x > right {
				return i
			}
		}
		return -1
	}
}

func main() {
	nums := []int{1, 2, 1}
	fmt.Println(findPeakElement(nums))
}
