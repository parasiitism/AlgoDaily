package main

import (
	"fmt"
	"strconv"
)

// actually it works but leetcode doesn't allow unordered
func permuteUnique(nums []int) [][]int {
	// result := [][]int{}
	hash := make(map[string][]int)
	var dfs func(arr []int, path []int, prefix string)
	dfs = func(arr []int, path []int, prefix string) {
		if len(arr) == 0 {
			if _, x := hash[prefix]; !x {
				hash[prefix] = path
			}
		} else {
			for i := 0; i < len(arr); i++ {
				temp := arr[i]

				copy := []int{}
				copy = append(copy, arr...)
				trim := append(copy[:i], copy[i+1:]...)

				nextpath := []int{}
				nextpath = append(nextpath, path...)
				nextpath = append(path, temp)

				dfs(trim, nextpath, prefix+strconv.Itoa(temp))
			}
		}
	}
	dfs(nums, []int{}, "")
	result := [][]int{}
	for _, v := range hash {
		result = append(result, v)
	}
	return result
}

func main() {
	fmt.Println(permuteUnique([]int{1, 1, 2, 2}))
}
