package main

import (
	"fmt"
	"sort"
	"strconv"
)

// actually it works but leetcode doesn't allow unordered
func permuteUnique(nums []int) [][]int {
	sort.Ints(nums)
	result := [][]int{}
	hash := make(map[string]bool)
	var dfs func(arr []int, path []int, prefix string)
	dfs = func(arr []int, path []int, prefix string) {
		if len(arr) == 0 {
			if _, x := hash[prefix]; !x {
				hash[prefix] = true
				result = append(result, path)
			}
		} else {
			for i := 0; i < len(arr); i++ {
				temp := arr[i]

				copy := []int{}
				copy = append(copy, arr...)
				trim := append(copy[:i], copy[i+1:]...)

				nextpath := []int{}
				nextpath = append(nextpath, path...)
				nextpath = append(nextpath, temp)

				// dfs [:i]+[i+1:]
				dfs(trim, nextpath, prefix+strconv.Itoa(temp))
			}
		}
	}
	dfs(nums, []int{}, "")
	return result
}

func permuteUnique1(nums []int) [][]int {
	sort.Ints(nums)
	result := [][]int{}
	seen := make([]bool, len(nums))

	var dfs func(arr []int, path []int)
	dfs = func(arr []int, path []int) {
		if len(arr) == 0 {
			result = append(result, path)
		} else {
			for i := 0; i < len(arr); i++ {
				temp := arr[i]
				if i > 0 && temp == arr[i-1] && seen[i-1] == false {
					continue
				}
				copy := []int{}
				copy = append(copy, arr...)
				trim := append(copy[:i], copy[i+1:]...)

				nextpath := []int{}
				nextpath = append(nextpath, path...)
				nextpath = append(path, temp)

				// dfs [:i]+[i+1:]
				seen[i] = true
				dfs(trim, nextpath)
				seen[i] = false
			}
		}
	}
	dfs(nums, []int{})
	return result
}

func main() {
	fmt.Println(permuteUnique1([]int{1, 1, 2, 2}))
}
