package main

import (
	"fmt"
	"sort"
)

// 1st approach
// 1. sort the input
// 2. traverse all the paths using a hashtable to avoid duplicates
// it is hard to determind the Time Complexity, it depends on the input
// beats 38.89%
func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	result := [][]int{}
	var dfs func(num int, path []int, fromIdx int)
	dfs = func(num int, path []int, fromIdx int) {
		if num == 0 {
			result = append(result, path)
		} else {
			seen := make(map[int]bool)
			for i := fromIdx; i < len(candidates); i++ {
				cur := candidates[i]
				if _, x := seen[cur]; x {
					continue
				}
				seen[cur] = true
				if cur > num {
					break
				}
				nextPath := []int{}
				nextPath = append(nextPath, path...)
				nextPath = append(nextPath, cur)
				dfs(num-cur, nextPath, i+1)
			}
		}
	}
	dfs(target, []int{}, 0)
	return result
}

// 2nd approach
// 1. sort the input
// 2. traverse all the paths but skipping the repeated numbers to avoid duplicates instead of using a hashtable
// it is hard to determind the Time Complexity, it depends on the input
// beats 100%
func combinationSum2_(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	result := [][]int{}
	var dfs func(num int, path []int, fromIdx int)
	dfs = func(num int, path []int, fromIdx int) {
		if num == 0 {
			result = append(result, path)
		} else {
			for i := fromIdx; i < len(candidates); i++ {

				// skip if the current candidate is the same with the previuous one
				if i > fromIdx && candidates[i] == candidates[i-1] {
					continue
				}

				cur := candidates[i]
				// break if current candidate is larger than target because the candidates are sorted(the later candidates must larger than target)
				if cur > num {
					break
				}
				nextPath := []int{}
				nextPath = append(nextPath, path...)
				nextPath = append(nextPath, cur)
				dfs(num-cur, nextPath, i+1)
			}
		}
	}
	dfs(target, []int{}, 0)
	return result
}

func main() {
	fmt.Println(combinationSum2_([]int{10, 1, 2, 7, 6, 1, 5}, 8))
	fmt.Println(combinationSum2_([]int{2, 5, 2, 1, 2}, 5))
	fmt.Println(combinationSum2_([]int{14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21, 29, 24, 17, 27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34, 18, 12}, 27))
}
