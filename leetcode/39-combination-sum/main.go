package main

import (
	"fmt"
	"sort"
	"strconv"
)

/*
	1st attempt:
	- iterative bottom-up dynamic programming approch
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

/*
	2nd approach:
	- recursive dfs
	- sort the input to make sure that all the later candidates are larger
	- avoid duplicate by considering the candidates only which are >= num
	beats 63.08%
*/
func combinationSum1(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	result := [][]int{}
	var dfs func(num int, path []int, fromIdx int)
	dfs = func(num int, path []int, fromIdx int) {
		if num == 0 {
			result = append(result, path)
		} else if num > 0 {
			// very important:
			// start the recursion only with the candidates which are >= fromIdx
			for i := fromIdx; i < len(candidates); i++ {
				cur := candidates[i]
				nextPath := []int{}
				nextPath = append(nextPath, path...)
				nextPath = append(nextPath, cur)
				if num < cur {
					break
				}
				// very important:
				// start the next recursion from current index(not the i+1)
				// because we need to consider duplicates numbers in candidates
				dfs(num-cur, nextPath, i)
			}
		}
	}
	dfs(target, []int{}, 0)
	return result
}

func main() {
	fmt.Println(combinationSum([]int{2, 3, 5}, 8))
	fmt.Println(combinationSum([]int{2, 3, 6, 7}, 7))
	fmt.Println(combinationSum([]int{1, 2, 3, 4}, 15))

	fmt.Println(combinationSum1([]int{2, 3, 5}, 8))
	fmt.Println(combinationSum1([]int{2, 3, 6, 7}, 7))
	fmt.Println(combinationSum1([]int{1, 2, 3, 4}, 15))
}
