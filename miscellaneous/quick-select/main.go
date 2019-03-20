package main

import "fmt"

/*
	ref:
	- https://www.geeksforgeeks.org/quickselect-algorithm/
*/

func kSmallest(nums []int, k int) int {
	return arrange(nums, 0, len(nums)-1, k)
}

func arrange(nums []int, left int, right int, k int) int {
	if k > 0 && k <= right-left+1 {
		pIdx := partition(nums, left, right)

		fmt.Println("pIdx-left+1=>", k, pIdx, pIdx-left+1, nums)

		if pIdx-left+1 == k {
			return nums[pIdx]
		} else if pIdx-left+1 < k {
			// it means pIdx hasn't reach to the correct position, k
			// find the correct position in the right-handed side
			return arrange(nums, pIdx+1, right, k-(pIdx-left+1))
		} else {
			// it means pIdx gone beyond the correct position, k
			// find the correct position in the left-handed side
			return arrange(nums, left, pIdx-1, k)
		}
	}
	return -1
}

func partition(nums []int, left int, right int) int {
	pivot := nums[right]
	pIdx := left
	for i := left; i < right; i++ {
		if nums[i] < pivot {
			nums[i], nums[pIdx] = nums[pIdx], nums[i]
			pIdx++
		}
	}
	nums[pIdx], nums[right] = nums[right], nums[pIdx]
	return pIdx
}

func main() {
	// [11 12 22 25 38 54 64 90]
	// a := []int{64, 25, 12, 22, 11, 38, 54, 90}
	// fmt.Println(kSmallest(a, 3))
	// fmt.Println(kSmallest(a, 5))
	// fmt.Println(kSmallest(a, 1))
	// fmt.Println(kSmallest(a, 8))
	// fmt.Println(kSmallest(a, 0))
	// fmt.Println(kSmallest(a, 10))

	// [2, 4, 6, 8, 10, 12]
	a := []int{10, 2, 6, 4, 8, 12}
	fmt.Println(kSmallest(a, 5))
	// fmt.Println(kSmallest(a, 5))
	// fmt.Println(kSmallest(a, 1))
	// fmt.Println(kSmallest(a, 8))
	// fmt.Println(kSmallest(a, 0))
	// fmt.Println(kSmallest(a, 10))
}
