package main

import (
	"fmt"
)

// attemp 1: hash table
// beats 51.63%
func singleNumber(nums []int) int {
	hash := make(map[int]bool)
	result := 0
	for i := 0; i < len(nums); i++ {
		if !hash[nums[i]] {
			hash[nums[i]] = true
			result += nums[i]
		} else {
			result -= nums[i]
		}
	}
	return result
}

func main() {
	fmt.Println(singleNumber([]int{2, 2, 1}))
	fmt.Println(singleNumber([]int{4, 1, 2, 1, 2}))
}
