package main

import "fmt"

// 1st approach
// classic backtracking problem
// very similar to euler/31
// Time		O(nCk) pick K numbers from N numbers
// Space	O(nCk) the recursive call stack
// beats 100%
func combinationSum3(k int, n int) [][]int {
	result := [][]int{}
	var dfs func(num int, path []int, fromNum int)
	dfs = func(num int, path []int, fromNum int) {
		if num == 0 && len(path) == k {
			result = append(result, path)
		} else if len(path) < k {
			for i := fromNum; i < 10; i++ {
				nextPath := []int{}
				nextPath = append(nextPath, path...)
				nextPath = append(nextPath, i)
				dfs(num-i, nextPath, i+1)
			}
		}
	}
	dfs(n, []int{}, 1)
	return result
}

func main() {
	fmt.Println(combinationSum3(3, 7))
	fmt.Println(combinationSum3(3, 9))
	fmt.Println(combinationSum3(5, 19))
}
