package main

import (
	"math"
)

// surprisingly, i passed the judge even though leetcode suggests that it is a TLE solution
// O(nk) => O(n^2)
func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j-i <= k && j < len(nums); j++ {
			if math.Abs(float64(nums[i]-nums[j])) <= float64(t) {
				return true
			}
		}
	}
	return false
}

func main() {

}
