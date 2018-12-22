package main

import "fmt"

// classic DP
// dfs + memorization
// 1. traverse all the paths
// 2. use cache to avoid duplicate calculation
// beats 100%
func combinationSum4(nums []int, target int) int {
	hash := make(map[int]int)
	return dfs(nums, target, hash)
}

func dfs(nums []int, n int, hash map[int]int) int {
	if n == 0 {
		return 1
	} else if n < 0 {
		return 0
	}
	if v, x := hash[n]; x {
		return v
	}
	cnt := 0
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		cnt += dfs(nums, n-num, hash)
	}
	hash[n] = cnt
	return cnt
}

func main() {
	fmt.Println(combinationSum4([]int{1, 2, 3}, 4)) // 7
}
