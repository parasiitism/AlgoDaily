package main

import (
	"fmt"
	"strconv"
)

/*
	1st approach: brute force, bottom up recursively with memorizatin
	- intuitively go through all the path with i+1 OR j+1
	- count the path which reaches to the destination coordinate (m, n)
	- cache the count of the coordinates which we have calculated before
	- sum up all the coordinates' count

	Time    O(m*n) 0->m, 0->n. since we cache the intermediate coordinates, we dont have duplicate sets of i, j
	Space   O(m*n) depth of recursion calls
	0ms beats 100%
*/
func uniquePaths(m int, n int) int {
	seen := make(map[string]int)
	return dfs(0, 0, m, n, seen)
}

func dfs(i, j, m, n int, seen map[string]int) int {
	key := strconv.Itoa(i) + "," + strconv.Itoa(j)
	if v, x := seen[key]; x {
		return v
	}
	if i+1 == m && j+1 == n {
		return 1
	} else if i+1 > m || j+1 > n {
		return 0
	}
	left := dfs(i+1, j, m, n, seen)
	right := dfs(i, j+1, m, n, seen)
	seen[key] = left + right
	return left + right
}

func main() {
	fmt.Println(uniquePaths(-1, 0))
	fmt.Println(uniquePaths(0, 0))
	fmt.Println(uniquePaths(3, 2))
	fmt.Println(uniquePaths(7, 3))
	fmt.Println(uniquePaths(29, 45))
	fmt.Println(uniquePaths(100, 100))
}
