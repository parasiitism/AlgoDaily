package main

import "fmt"

func kSmallest(nums []int, k int) int {
	return arrange(nums, 0, len(nums)-1, k)
}

func arrange(nums []int, left int, right int, k int) int {
	if k > 0 && k <= len(nums) {
		pIdx := partition(nums, left, right)
		if pIdx+1 == k {
			return nums[pIdx]
		} else if pIdx+1 < k {
			return arrange(nums, pIdx+1, right, k)
		} else {
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
	// [11, 12, 22, 25, 38, 54, 64, 90]
	a := []int{64, 25, 12, 22, 11, 38, 54, 90}
	fmt.Println(kSmallest(a, 0))
	fmt.Println(kSmallest(a, 1))
	fmt.Println(kSmallest(a, 2))
	fmt.Println(kSmallest(a, 3))
	fmt.Println(kSmallest(a, 4))
	fmt.Println(kSmallest(a, 5))
	fmt.Println(kSmallest(a, 6))
	fmt.Println(kSmallest(a, 7))
	fmt.Println(kSmallest(a, 8))
	fmt.Println(kSmallest(a, 9))

	fmt.Println("-----")

	// [2, 4, 6, 8, 10, 12, 14, 16]
	a = []int{10, 12, 2, 4, 8, 6}
	fmt.Println(kSmallest(a, 0))
	fmt.Println(kSmallest(a, 1))
	fmt.Println(kSmallest(a, 2))
	fmt.Println(kSmallest(a, 3))
	fmt.Println(kSmallest(a, 4))
	fmt.Println(kSmallest(a, 5))
	fmt.Println(kSmallest(a, 6))
	fmt.Println(kSmallest(a, 7))
}
