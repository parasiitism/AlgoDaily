package main

import "fmt"

/*
	2nd approach(i did the 1st in python)
	- create an array of booleans, like hashtable
	- for each number, mark as seen
	- iterate the seen from 1, return the unseen number
	- if all exist, return next number of the length of nums
	Time O(n)
	Space O(n)
	beats 100%
*/
func firstMissingPositive(nums []int) int {
	seen := make([]bool, len(nums)+1)
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		if num > 0 && num < len(seen) {
			seen[num] = true
		}
	}
	for i := 1; i < len(seen); i++ {
		if seen[i] == false {
			return i
		}
	}
	return len(nums) + 1
}

func main() {
	fmt.Println(firstMissingPositive([]int{5, 3, 1})) //2
	fmt.Println(firstMissingPositive([]int{5, 4, 1, 2}))
	fmt.Println(firstMissingPositive([]int{3, 2, 1}))
	fmt.Println(firstMissingPositive([]int{2, 3}))
	fmt.Println(firstMissingPositive([]int{2}))
	fmt.Println(firstMissingPositive([]int{1}))
	fmt.Println(firstMissingPositive([]int{}))
	fmt.Println(firstMissingPositive([]int{1, 1, 1, 2, 3}))
	fmt.Println(firstMissingPositive([]int{1, 3, 2, 3, 5}))
	fmt.Println(firstMissingPositive([]int{1, 3, 2, 3, 5, -1, -10}))
}
