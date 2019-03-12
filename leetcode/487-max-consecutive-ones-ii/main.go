package main

import "fmt"

/*
	naive approach:
	- for each 0, expand from center if the boundaries are 1
	but it might have redundant computation
*/

/*
	1st approach:
	- optimize the naive approach

	corner case:
	- all 1

	Time	O(2n)
	Space	O(n)
	44 ms, faster than 62.50%
*/
func findMaxConsecutiveOnes(nums []int) int {
	// make [1,0,1,1,0] to [1,0,2,0]
	arr := []int{}
	count := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 1 {
			count++
			if i+1 == len(nums) {
				arr = append(arr, count)
			}
		} else {
			if count > 0 {
				arr = append(arr, count)
			}
			count = 0
			arr = append(arr, 0)
		}
	}
	// if all 1
	if count == len(nums) {
		return count
	}
	// for each "0", 202, expand from the center,the count is arr[i-1]+1+arr[i+1]
	res := 0
	for i := 0; i < len(arr); i++ {
		if arr[i] == 0 {
			temp := 1
			left := 0
			right := 0
			if i > 0 {
				left = arr[i-1]
			}
			if i < len(arr)-1 {
				right = arr[i+1]
			}
			temp += left + right
			res = findMax(res, temp)
		}
	}
	return res
}

func findMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(findMaxConsecutiveOnes([]int{1, 0, 1, 1, 0}))
	fmt.Println(findMaxConsecutiveOnes([]int{1, 0, 1, 1, 1}))
	fmt.Println(findMaxConsecutiveOnes([]int{1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1}))

	fmt.Println(findMaxConsecutiveOnes([]int{1}))
	fmt.Println(findMaxConsecutiveOnes([]int{1, 1, 1}))
}
