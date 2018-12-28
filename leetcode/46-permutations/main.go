package main

import "fmt"

// time		O(len(nums)!)
// space	O(1)
// beats 77.21%
func permute(nums []int) [][]int {
	result := [][]int{}
	var dfs func(arr []int, path []int)
	dfs = func(arr []int, path []int) {
		if len(arr) == 0 {
			result = append(result, path)
		} else {
			for i := 0; i < len(arr); i++ {
				temp := arr[i]

				copy := []int{}
				copy = append(copy, arr...)
				trim := append(copy[:i], copy[i+1:]...)

				nextpath := []int{}
				nextpath = append(nextpath, path...)
				nextpath = append(path, temp)

				dfs(trim, nextpath)
			}
		}
	}
	dfs(nums, []int{})
	return result
}

func main() {
	res := permute([]int{1, 1, 3})
	fmt.Println(res)
	fmt.Println(len(res))
}
