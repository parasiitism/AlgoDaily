package main

import "fmt"

func permutations(input []int) [][]int {
	result := [][]int{}
	var dfs func(arr []int, path []int)
	dfs = func(arr []int, path []int) {
		if len(arr) == 0 {
			result = append(result, path)
		} else {
			for i := 0; i < len(arr); i++ {
				temp := arr[i]

				copy := []int{}
				copy = append(copy, arr...) // in golang, we must copy the slice becos when b:=a, the b is actually just a wrapper of the integers with the same address(shadow copy)
				trim := append(copy[:i], copy[i+1:]...)

				nextpath := []int{}
				nextpath = append(nextpath, path...)
				nextpath = append(path, temp)

				dfs(trim, nextpath)
			}
		}
	}
	dfs(input, []int{})
	return result
}

func main() {
	res := permutations([]int{1, 2, 3})
	fmt.Println(res)
	fmt.Println(len(res))
}
