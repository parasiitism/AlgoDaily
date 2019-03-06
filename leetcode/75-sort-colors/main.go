package main

import "fmt"

/*
	naive approach: built-in sort / merge sort
*/

/*
	1st approach: bucket sort

	Time	O(n)
	Space	O(n)
	0 ms, faster than 100.00%
*/
func sortColors(nums []int) {
	bucket := []int{0, 0, 0}
	for _, num := range nums {
		bucket[num]++
	}
	index := 0
	for i := 0; i < len(bucket); i++ {
		if bucket[i] > 0 {
			for j := 0; j < bucket[i]; j++ {
				nums[index] = i
				index++
			}
		}
	}
}

func main() {
	a := []int{2, 0, 1, 2, 0, 1}
	sortColors(a)
	fmt.Println(a)

	a = []int{}
	sortColors(a)
	fmt.Println(a)

	a = []int{1, 2, 1}
	sortColors(a)
	fmt.Println(a)
}
