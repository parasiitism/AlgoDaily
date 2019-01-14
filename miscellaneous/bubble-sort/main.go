package main

import "fmt"

/*
	bubble sort: https://en.wikipedia.org/wiki/Bubble_sort
	Average Time		O(n^2)
	Best Time				O(n)
	Worst Time			O(n)
	Space						O(1)
*/
func bubbleSort(nums []int) {
	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums)-1; j++ {
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
			}
		}
	}
}

func main() {
	a := []int{64, 25, 12, 22, 11, 38, 54, 90}
	bubbleSort(a)
	fmt.Println(a)
}
