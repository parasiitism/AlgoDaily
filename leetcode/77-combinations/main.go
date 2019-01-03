package main

import "fmt"

/*
	Recursive implementation similar to permutations
	Time	O(nCk)
	Space O(nCk) due to the recrusion
	beats 1.22% (python version beats 13.88%)
*/
func combine(n int, k int) [][]int {
	if k < 1 || k > n {
		return [][]int{}
	}
	result := [][]int{}
	var dfs func(nums []int, path []int)
	dfs = func(nums []int, path []int) {
		if len(path) == k {
			result = append(result, path)
		} else {
			for i := 0; i < len(nums); i++ {
				// copy thing
				nextpath := []int{}
				nextpath = append(nextpath, path...)
				nextpath = append(nextpath, nums[i])
				// dfs(nums[i+1:], path+[nums[i]])
				dfs(nums[i+1:], nextpath)
			}
		}
	}
	arr := []int{}
	for i := 0; i < n; i++ {
		arr = append(arr, i+1)
	}
	dfs(arr, []int{})
	return result
}

/*
	Recursive implementation similar to permutations(without inner functions)
	Time	O(nCk)
	Space O(nCk) due to the recrusion
	beats 9.76% better due to the inner function removal
*/
func combine1(n int, k int) [][]int {
	if k < 1 || k > n {
		return [][]int{}
	}
	return dfs(1, n, []int{}, k)
}

func dfs(start int, n int, path []int, k int) [][]int {
	result := [][]int{}
	if len(path) == k {
		return [][]int{path}
	} else {
		for i := start; i <= n; i++ {
			// copy thing
			nextpath := []int{}
			nextpath = append(nextpath, path...)
			nextpath = append(nextpath, i)
			// dfs(nums[i+1:], path+[nums[i]])
			temp := dfs(i+1, n, nextpath, k)
			result = append(result, temp...)
		}
	}
	return result
}

/*
	Iterative using a stack
	Time	O(nCk)
	Space O(nCk) the stack
	beats 12.20%
*/

func combine2(n int, k int) [][]int {
	if k < 1 || k > n {
		return [][]int{}
	}
	result := [][]int{}
	stack := []Stack{}
	stack = append(stack, Stack{1, []int{}})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if len(pop.Path) == k {
			result = append(result, pop.Path)
		} else {
			for i := pop.Start; i <= n; i++ {
				nextpath := []int{}
				nextpath = append(nextpath, pop.Path...)
				nextpath = append(nextpath, i)
				stack = append(stack, Stack{i + 1, nextpath})
			}
		}
	}
	return result
}

type Stack struct {
	Start int
	Path  []int
}

func main() {
	fmt.Println(combine(4, 2))
	fmt.Println(combine(4, 3))
	fmt.Println(combine(5, 4))

	fmt.Println(combine2(4, 2))
	fmt.Println(combine2(4, 3))
	fmt.Println(combine2(5, 4))
}
