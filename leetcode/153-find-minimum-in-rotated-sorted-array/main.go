package main

import (
	"fmt"
	"math"
)

// linear
func findMin(nums []int) int {
	min := math.MaxUint32
	for i := 0; i < len(nums); i++ {
		if nums[i] < min {
			min = nums[i]
		}
	}
	return min
}

// binary search
// ...

func main() {
	ans := findMin([]int{2})
	fmt.Println(ans)
}
