package main

import (
	"fmt"
	"sort"
)

// 1st attempt
// 1. find the pivot point
// 2. find the number which is a bit larger than the pivot in 2nd half
// 3. swap the pivot and the number
// 4. sort the 2nd half
// see idea.png
// time 	O(n+n+nlogn)
// space 	O(1)
// beats 100%
func nextPermutation(nums []int) {
	pivot := -1
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i]-nums[i+1] < 0 {
			pivot = i
			break
		}
	}
	if pivot == -1 {
		// reverse
		reverse(nums, 0, len(nums)-1)
		return
	}
	target := pivot + 1
	for last := pivot + 1; last < len(nums); last++ {
		if nums[last]-nums[pivot] > 0 && nums[last]-nums[pivot] < nums[target]-nums[pivot] {
			target = last
		}
	}
	temp := nums[target]
	nums[target] = nums[pivot]
	nums[pivot] = temp
	// sort the suffix (prefix+1)
	suffix := nums[pivot+1:]
	sort.Ints(suffix)
}

func reverse(nums []int, from int, to int) {
	if from >= to {
		return
	}
	gap := (to - from) / 2
	for i := 0; i <= gap; i++ {
		temp := nums[from+i]
		nums[from+i] = nums[to-i]
		nums[to-i] = temp
	}
}

func main() {
	a := []int{1, 3, 4, 2}
	nextPermutation(a)
	fmt.Println(a)

	a = []int{1, 2, 3}
	nextPermutation(a)
	fmt.Println(a) // 132

	a = []int{3, 2, 1}
	nextPermutation(a)
	fmt.Println(a) // 123

	a = []int{1, 1, 5}
	nextPermutation(a)
	fmt.Println(a) //151

	a = []int{2, 3, 1, 3, 3}
	nextPermutation(a)
	fmt.Println(a) // 23313

	a = []int{1, 3, 2}
	nextPermutation(a)
	fmt.Println(a) // 213

	a = []int{4, 2, 0, 2, 3, 2, 0}
	nextPermutation(a)
	fmt.Println(a) // [4,2,0,3,0,2,2]
}
