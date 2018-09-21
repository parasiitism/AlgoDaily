package main

import (
	"fmt"
)

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

func main() {
	result := intersection([]int{1, 2, 2, 1}, []int{2, 2})
	fmt.Println(result)
}
