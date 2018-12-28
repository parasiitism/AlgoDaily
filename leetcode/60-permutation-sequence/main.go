package main

import (
	"fmt"
	"strconv"
)

// easiest way to do it
// but i got TLE
func getPermutation(n int, k int) string {
	result := []string{}
	var dfs func(arr []int, path string)
	dfs = func(arr []int, path string) {
		if len(arr) == 0 {
			result = append(result, path)
		} else {
			for i := 0; i < len(arr); i++ {
				temp := strconv.Itoa(arr[i])

				copy := []int{}
				copy = append(copy, arr...)
				trim := append(copy[:i], copy[i+1:]...)

				nextpath := path + temp

				dfs(trim, nextpath)
			}
		}
	}
	input := []int{}
	for i := 1; i <= n; i++ {
		input = append(input, i)
	}
	dfs(input, "")
	return result[k-1]
}

func main() {
	fmt.Println(getPermutation(3, 3))
}
