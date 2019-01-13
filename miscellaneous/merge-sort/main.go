package main

import "fmt"

/*
	merge sort: https://www.geeksforgeeks.org/merge-sort/
	- divides input array in two halves recursively
	- merge two sorted halves and then return
	- this version occupys space(not in-place)
	- first divide, second process; the procedure is similar to post order traversal
	Time	O(nlogn)
	Space O(n)
*/
func mergeSort(nums []int) []int {
	// divide
	if len(nums) == 1 {
		return nums
	}
	mean := len(nums) / 2
	arr1 := mergeSort(nums[:mean])
	arr2 := mergeSort(nums[mean:])
	// merge 2 sorted arrays
	i, j := 0, 0
	result := []int{}
	for i < len(arr1) && j < len(arr2) {
		if arr1[i] < arr2[j] {
			result = append(result, arr1[i])
			i++
		} else {
			result = append(result, arr2[j])
			j++
		}
	}
	if i < len(arr1) {
		result = append(result, arr1[i:]...)
	}
	if j < len(arr2) {
		result = append(result, arr2[j:]...)
	}
	return result
}

func main() {
	a := []int{64, 25, 12, 22, 11, 38, 54, 90}
	fmt.Println(mergeSort(a))
}
