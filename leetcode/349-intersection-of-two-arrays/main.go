package main

import (
	"fmt"
	"sort"
)

// hash table, O(n)
func intersection(nums1 []int, nums2 []int) []int {
	var hashtable = make(map[int]int)

	for i := 0; i < len(nums1); i++ {
		x := nums1[i]
		if hashtable[x] == 0 {
			hashtable[x] = 1
		}
	}

	for i := 0; i < len(nums2); i++ {
		x := nums2[i]
		if hashtable[x] == 1 {
			hashtable[x]++
		}
	}

	result := []int{}

	for key, value := range hashtable {
		if value > 1 {
			result = append(result, key)
		}
	}

	return result
}

// binary search, O(nlogn)
// not a good solution compared to the hashtable one, but it is better to come up with more than 1 solution
func intersection1(nums1 []int, nums2 []int) []int {
	sort.Ints(nums2)
	var hashtable = make(map[int]int)
	for i := 0; i < len(nums1); i++ {
		idx := binary_search(nums2, nums1[i])
		if idx > -1 {
			hashtable[nums2[idx]] = 1
		}
	}
	result := []int{}
	for key, _ := range hashtable {
		result = append(result, key)
	}
	return result
}
func binary_search(arr []int, target int) int {
	min := 0
	max := len(arr) - 1
	for min <= max {
		mean := (min + max) / 2
		if target == arr[mean] {
			return mean
		} else if target > arr[mean] {
			min = mean + 1
		} else if target < arr[mean] {
			max = mean - 1
		}
	}
	return -1
}

func main() {
	result := intersection([]int{1, 2, 2, 1}, []int{2, 2})
	fmt.Println(result)
}
