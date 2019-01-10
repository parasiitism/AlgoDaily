package main

import (
	"fmt"
	"sort"
)

/*
	naive approach
	- replace the zeros with the nums2 items
	- sort the nums1
	Time	O(nlogn)
	Space	O(1)
	0ms, no beats
*/
func merge(nums1 []int, m int, nums2 []int, n int) {
	j := 0
	for i := 0; i < len(nums1); i++ {
		if nums1[i] == 0 && j < len(nums2) {
			nums1[i] = nums2[j]
			j++
		}
	}
	sort.Ints(nums1)
}

func main() {
	a := []int{1, 2, 3, 0, 0, 0}
	b := []int{2, 5, 6}
	merge(a, 3, b, 3)
	fmt.Println(a)

	a = []int{-1, 0, 0, 3, 3, 3, 0, 0, 0}
	b = []int{1, 2, 2}
	merge(a, 3, b, 3)
	fmt.Println(a)
}
