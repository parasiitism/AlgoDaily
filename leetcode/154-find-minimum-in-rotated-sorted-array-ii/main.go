package main

import "math"

// linear
func findMin2(nums []int) int {
	min := math.MaxUint32
	for i := 0; i < len(nums); i++ {
		if nums[i] < min {
			min = nums[i]
		}
	}
	return min
}

func main() {

}
