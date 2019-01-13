package main

import "fmt"

/*
	quick sort: https://www.geeksforgeeks.org/quick-sort/
	- divides input array into two halves according to the pivot point recursively
	- merge two sorted halves and then return
	- this version occupies space(not in-place) !!!
	Worst Time		O(n^2): findHalf might need to iterate the rest of the array for each item
	Average	Time	O(nlogn)
	Space 				O(n)
*/
func quickSort(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}
	pivot := nums[len(nums)-1]
	left := quickSort(findHalf(nums, pivot, false))
	right := quickSort(findHalf(nums, pivot, true))
	res := []int{}
	res = append(res, left...)
	res = append(res, pivot)
	res = append(res, right...)
	return res
}

func findHalf(nums []int, target int, isMore bool) []int {
	res := []int{}
	for i := 0; i < len(nums); i++ {
		if isMore {
			if nums[i] > target {
				res = append(res, nums[i])
			}
		} else {
			if nums[i] < target {
				res = append(res, nums[i])
			}
		}
	}
	return res
}

func main() {
	a := []int{64, 25, 12, 22, 11, 38, 54, 90}
	fmt.Println(quickSort(a))
}
