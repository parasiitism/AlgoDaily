package main

import "fmt"

/*
	Questions to ask:
	- will there be more than one pivot? if yes, return which?
	- return what for an empty array?
	- return what for a single-element array?
	- will there be a list of the same number? e.g. [1,1,1,1,1] & [1,1,1,1,1,1]?

	i failed to come up with a correct approach to this question
	learned from others
	1.index: 0, num: 1, left: 0, right: 27
	2. index: 1, num: 7, left: 1, right: 20
	3. index: 2, num: 3, left: 8, right: 17
	4. index: 3, num: 6, left: 11, right: 11 <-- Found!!!
	Time	O(n)
	Space O(1)
*/
func pivotIndex(nums []int) int {
	right := 0
	for i := 0; i < len(nums); i++ {
		right += nums[i]
	}
	left := 0
	for i := 0; i < len(nums); i++ {
		right -= nums[i]
		if left == right {
			return i
		}
		left += nums[i]
	}
	return -1
}

func main() {
	fmt.Println(pivotIndex([]int{}))
	fmt.Println(pivotIndex([]int{1}))
	fmt.Println(pivotIndex([]int{1, 1}))
	fmt.Println(pivotIndex([]int{1, 2, 1}))
	fmt.Println(pivotIndex([]int{1, -1, 2, 2}))
	fmt.Println(pivotIndex([]int{1, -1, 2, 0, 4}))
	fmt.Println(pivotIndex([]int{1, 7, 3, 6, 5, 6}))
	fmt.Println(pivotIndex([]int{1, 7, 0, 0, 2, 6}))
	fmt.Println(pivotIndex([]int{1, 7, -1, 7, 0, 0, 2, 6}))
	fmt.Println(pivotIndex([]int{1, 1, 1, 1, 1}))
	fmt.Println(pivotIndex([]int{1, 1, 1, 1, 1, 1}))
	fmt.Println(pivotIndex([]int{-1, -1, -1, -1, -1}))
	fmt.Println(pivotIndex([]int{-1, -1, -1, -1, -1, -1}))
}
