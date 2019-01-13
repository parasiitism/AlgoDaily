package main

import "fmt"

/*
	Selection Sort: https://en.wikipedia.org/wiki/Selection_sort
	- The selection sort algorithm sorts an array by repeatedly SELECTING the minimum element
		(considering ascending order) from unsorted part and putting it at the beginning
	- do it in-place to save some space
	Time		O(n^2)
	Space		O(1)
*/
func selectionSort(nums []int) {
	for i := 0; i < len(nums); i++ {
		min_idx := i
		for j := i; j < len(nums); j++ {
			if nums[j] < nums[min_idx] {
				min_idx = j
			}
		}
		nums[i], nums[min_idx] = nums[min_idx], nums[i]
	}
}

func main() {
	a := []int{64, 25, 12, 22, 11}
	selectionSort(a)
	fmt.Println(a)
}
