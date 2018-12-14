package main

import "fmt"

// classical solution
// O(n)
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

// mediocre solution
// O(2n)
// beats 55%
func twoSum1(nums []int, target int) []int {
	hash := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		hash[nums[i]] = i
	}
	for i := 0; i < len(nums); i++ {
		remain := target - nums[i]
		v, e := hash[remain]
		if e && v != i {
			return []int{v, i}
		}
	}
	return []int{}
}

// naive solution
// O(n^2)
// bests 14%
func twoSum2(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums); j++ {
			if i != j && nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}

func main() {
	fmt.Println(twoSum1([]int{9, 2, 3, 4}, 12))
}
