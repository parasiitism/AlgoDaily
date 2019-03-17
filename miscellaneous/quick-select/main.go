package main

import "fmt"

/*
	ref:
	- https://www.geeksforgeeks.org/quickselect-algorithm/
*/

func kSmallest(nums []int, k int) int {
	return arrange(nums, 0, len(nums)-1, k)
}

func arrange(nums []int, start int, end int, k int) int {
	if k > 0 && k <= end-start+1 {
		pIdx := partition(nums, start, end)

		if pIdx-start == k-1 {
			return nums[pIdx]
		} else if pIdx-start < k-1 {
			// it means pIdx hasn't reach to the correct position, k
			// find the correct position in the right-handed side
			return arrange(nums, pIdx+1, end, k-pIdx+start-1)
		} else {
			// it means pIdx gone beyond the correct position, k
			// find the correct position in the left-handed side
			return arrange(nums, start, pIdx-1, k)
		}
	}
	return -1
}

func partition(nums []int, start int, end int) int {
	pivot := nums[end]
	pIdx := start
	for i := start; i < end; i++ {
		if nums[i] < pivot {
			nums[i], nums[pIdx] = nums[pIdx], nums[i]
			pIdx++
		}
	}
	nums[pIdx], nums[end] = nums[end], nums[pIdx]
	return pIdx
}

func main() {
	// [11 12 22 25 38 54 64 90]
	a := []int{64, 25, 12, 22, 11, 38, 54, 90}
	fmt.Println(kSmallest(a, 3))
	fmt.Println(kSmallest(a, 5))
	fmt.Println(kSmallest(a, 1))
	fmt.Println(kSmallest(a, 8))
	fmt.Println(kSmallest(a, 0))
	fmt.Println(kSmallest(a, 10))
}
