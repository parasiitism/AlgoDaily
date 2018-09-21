package main

import "fmt"

// hash table, O(n)
func intersection(nums1 []int, nums2 []int) []int {
	var hashtable = make(map[int]int)

	// remember the number of occurrences of each item
	for i := 0; i < len(nums1); i++ {
		x := nums1[i]
		if hashtable[x] == 0 {
			hashtable[x] = 1
		} else {
			hashtable[x]++
		}
	}

	result := []int{}

	// crux:
	// - if there is a duplicate item in nums2, put it into the result
	// - subtract the number of occurrences of the duplicate item
	for i := 0; i < len(nums2); i++ {
		x := nums2[i]
		if hashtable[x] > 0 {
			result = append(result, x)
			hashtable[x]--
		}
	}

	return result
}

// i wont do the binary search version here now, cos it is even simplier than question 349
// i.e. just put the duplicate items to the result. dont need to use a hashtable

func main() {
	result := intersection([]int{1, 2, 2, 1}, []int{2, 2})
	fmt.Println(result)
}
