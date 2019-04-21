package main

import "fmt"

/*
	1st approach:
	1. for each num, count the number of consecutive ones
	2. after count, compare with the intermediate result
	3. the final intermediate result is the reuslt

	44 ms, faster than 72.34%
*/
func findMaxConsecutiveOnes(nums []int) int {
	resMax := 0
	curMax := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 1 {
			curMax++
		}
		if nums[i] == 0 || i+1 == len(nums) {
			resMax = findMax(resMax, curMax)
			curMax = 0
		}
	}
	return resMax
}

func findMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(findMaxConsecutiveOnes([]int{1, 1, 0, 1, 1, 1}))
	fmt.Println(findMaxConsecutiveOnes([]int{1, 1, 0, 1, 1, 0}))
	fmt.Println(findMaxConsecutiveOnes([]int{}))
}
