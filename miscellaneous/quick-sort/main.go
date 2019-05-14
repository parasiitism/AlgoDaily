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

/*
	in-place version
	ref:
	- https://gist.github.com/imwally/58d6bb9bf9da098064054f73a19cdca1
	- https://www.youtube.com/watch?v=COk73cpQbFQ

	Worst Time		O(n^2): findHalf might need to iterate the rest of the array for each item
	Average	Time	O(nlogn)
	Space 				O(h)
*/
func quickSortInPlace(nums []int) {
	quick(nums, 0, len(nums)-1)
}

func quick(nums []int, start int, end int) {
	if start < end {
		pIdx := partition(nums, start, end)
		quick(nums, start, pIdx-1)
		quick(nums, pIdx+1, end)
	}
}

func partition(nums []int, start int, end int) int {
	pivot := nums[end]
	// partition idx is the index to the first item that larger than pivot
	pIdx := start
	for i := start; i < end; i++ {
		// < for ascending
		// > for descending
		if nums[i] < pivot {
			nums[i], nums[pIdx] = nums[pIdx], nums[i]
			pIdx++
		}
	}
	/*
		e.g.
		2,4,3,5,1,6,3
		^			^
		pidx		pivot

		after the swap, we will have
		2,3,1,4,5,6,3
			  ^		^
			pidx	pivot
		we have to swap the partition idx with the pivot so make sure that pivot will be in the middle
	*/
	nums[pIdx], nums[end] = nums[end], nums[pIdx]
	return pIdx
}

func main() {
	a := []int{64, 25, 12, 22, 11, 38, 38, 54, 90}
	// fmt.Println(quickSort(a))
	quickSortInPlace(a)
	fmt.Println(a)
}
