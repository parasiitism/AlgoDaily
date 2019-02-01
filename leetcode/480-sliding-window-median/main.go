package main

import (
	"fmt"
	"sort"
)

/*
	1st approach
	- similar to window sum
	- but for each iteration, sort the nums
	Time    O(n*nlogn)
	Space   O(kn)
	8348ms beats 100%
*/
func medianSlidingWindow(nums []int, k int) []float64 {
	if len(nums) == 0 || k <= 0 || k > len(nums) {
		return []float64{}
	}
	acc := [][]int{}
	res := []float64{}

	// first item
	temp := []int{}
	for i := 0; i < k; i++ {
		temp = append(temp, nums[i])
	}
	acc = append(acc, temp)
	res = append(res, calMedian(temp))

	// 2nd item -> end
	for i := k; i < len(nums); i++ {
		// extract the last one from acc
		// remove the first num from acc and add the current num to the acc
		// [1,2,3], 4=> 1, [2,3,4]
		clone := []int{}
		clone = append(clone, acc[len(acc)-1]...)
		clone = clone[1:]
		clone = append(clone, nums[i])
		// append to acc
		acc = append(acc, clone)
		// cal madian
		res = append(res, calMedian(clone))
	}
	return res
}

func calMedian(nums []int) float64 {
	sortNums := []int{}
	sortNums = append(sortNums, nums...)
	sort.Ints(sortNums)
	if len(sortNums)%2 == 0 {
		half := len(sortNums) / 2
		return float64((sortNums[half-1] + sortNums[half])) / 2.0
	}
	half := len(sortNums) / 2
	return float64(sortNums[half])
}

func main() {
	fmt.Println(medianSlidingWindow([]int{}, 3))
	fmt.Println(medianSlidingWindow([]int{1, 2, 3, 4, 5, 6, 7}, 3))
	fmt.Println(medianSlidingWindow([]int{1, 3, -1, -3, 5, 3, 6, 7}, 3))
	fmt.Println(medianSlidingWindow([]int{1, 3, -1, -3, 5, 3, 6, 7}, 4))
}
