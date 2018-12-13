package main

import (
	"fmt"
)

// classical solutino
// beats 100%
func twoSum(nums []int, target int) []int {
	hash := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		v, e := hash[nums[i]]
		if e {
			return []int{v, i}
		}
		hash[target-nums[i]] = i
	}
	return []int{}
}

func main() {
	fmt.Println(twoSum([]int{9, 2, 3, 4}, 12))
}
