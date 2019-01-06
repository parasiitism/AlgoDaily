package main

import "fmt"

// recursive
func permutations_recusive(input []int) [][]int {
	result := [][]int{}
	var dfs func(arr []int, path []int)
	dfs = func(arr []int, path []int) {
		if len(arr) == 0 {
			result = append(result, path)
		} else {
			for i := 0; i < len(arr); i++ {
				temp := arr[i]

				cop := []int{}
				cop = append(cop, arr...) // in golang, we must copy the slice becos when b:=a, the b is actually just a wrapper of the integers with the same address(shadow copy)
				trim := append(cop[:i], cop[i+1:]...)

				nextpath := []int{}
				nextpath = append(nextpath, path...)
				nextpath = append(nextpath, temp)

				// dfs(arr[:i]+arr[i+1:], path+[arr[i]])
				dfs(trim, nextpath)
			}
		}
	}
	dfs(input, []int{})
	return result
}

// iterative
//   1
//  ^ ^
//  2 2
//
//   2,1         1,2
//  ^ ^ ^       ^ ^ ^
//  3 3 3       3 3 3
// time		O(n!)
// space	O(1)
// beats	77.14%
func permutations_iterative(nums []int) [][]int {
	perms := [][]int{[]int{}}
	for i := 0; i < len(nums); i++ {
		new_perms := [][]int{}
		for j := 0; j < len(perms); j++ {
			perm := perms[j]
			for k := 0; k < len(perm)+1; k++ {

				// i really hate golang slice and concate
				cop := []int{}
				cop = append(cop, perm[:k]...)
				cop = append(cop, nums[i])
				cop = append(cop, perm[k:]...)

				new_perms = append(new_perms, cop)
			}
		}
		perms = new_perms
	}
	return perms
}

// CS106B
func permuteStr(str string) {
	var helper func(s string, prefix string)
	helper = func(s string, prefix string) {
		if len(s) == 0 {
			fmt.Println(prefix)
		} else {
			for i := 0; i < len(s); i++ {
				helper(s[:i]+s[i+1:], prefix+string(s[i]))
			}
		}
	}
	helper(str, "")
}

func main() {
	fmt.Println(permutations_recusive([]int{1, 2, 3, 4}))
	fmt.Println(permutations_iterative([]int{1, 2, 3, 4}))
	permuteStr("marty")
}
