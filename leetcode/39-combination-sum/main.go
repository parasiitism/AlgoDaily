package main

import (
	"fmt"
	"sort"
	"strconv"
)

/*
naive approach: top-down recursion
TLE because there are too many duplicate calculations
func combinationSum(candidates []int, target int) [][]int {
	result := [][]int{}
	seen := make(map[string]bool)
	var dfs func(num int, path []int)
	dfs = func(num int, path []int) {
		if num == 0 {
			sort.Ints(path)
			key := ints2str(path)
			if _, x := seen[key]; !x {
				seen[key] = true
				result = append(result, path)
			}
		} else if num > 0 {
			for i := 0; i < len(candidates); i++ {
				cur := candidates[i]
				nextPath := []int{}
				nextPath = append(nextPath, path...)
				nextPath = append(nextPath, cur)
				if num < cur {
					break
				}
				dfs(num-cur, nextPath)
			}
		}
	}
	dfs(target, []int{})
	return result
}
*/

/*
	1st attempt:
	- bottom-up dynamic programming approch
	- use a hashtable to avoid duplicates
	e.g. candidates = [2,3,5], target = 8
	f[0] = []
	f[1] = []
	f[2] = [[2]]
	f[3] = [[3]]
	f[4] = [[2,2]]
	f[5] = [[2,3],[5]]
	f[6] = [[2,2,2],[3,3]]
	f[7] = [[2,2,3],[2,5]]
	f[8] = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
	beats 23.85%
*/
func combinationSum(candidates []int, target int) [][]int {
	result := [][][]int{}
	for i := 0; i <= target; i++ {
		result = append(result, [][]int{})
	}
	for i := 0; i <= target; i++ {
		futureResult := [][]int{}
		seen := make(map[string]bool)
		for j := 0; j < len(candidates); j++ {
			candidate := candidates[j]
			remain := i - candidate
			if remain < 0 {
				continue
			}
			remainResults := result[remain]
			if len(remainResults) == 0 && remain == 0 {
				futureResult = append(futureResult, []int{candidate})
			} else {
				for k := 0; k < len(remainResults); k++ {
					temp := []int{}
					temp = append(temp, remainResults[k]...)
					temp = append(temp, candidate)
					sort.Ints(temp)
					key := ints2str(temp)
					if _, x := seen[key]; x {
						continue
					}
					seen[key] = true
					futureResult = append(futureResult, temp)
				}
			}
		}
		result[i] = futureResult
	}
	return result[target]
}

func ints2str(nums []int) string {
	result := ""
	for i := 0; i < len(nums); i++ {
		result += strconv.Itoa(nums[i])
	}
	return result
}

func main() {
	fmt.Println(combinationSum([]int{2, 3, 5}, 8))
	fmt.Println(combinationSum([]int{2, 3, 6, 7}, 7))
	fmt.Println(combinationSum([]int{1, 2, 3, 4}, 15))
}
