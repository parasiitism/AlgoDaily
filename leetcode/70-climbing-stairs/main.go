package main

import "fmt"

// bottom-up iterative
// Time 	O(n) iterate from 1 to N
// Space	O(n) for the array
// 0ms beats 100%
func climbStairs1(n int) int {
	arr := []int{}
	arr = append(arr, 1)
	arr = append(arr, 1)
	for i := 2; i <= n; i++ {
		arr = append(arr, arr[i-1]+arr[i-2])
	}
	return arr[n]
}

// top-down recursive
// use a hashtable to avoid redundant calculation
// Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
// Space O(2n)	n for hashtable, n for recursive callstack
// 0ms beats 100%
func climbStairs(n int) int {
	cache := make(map[int]int)
	cache[0] = 1
	cache[1] = 1
	var f func(num int) int
	f = func(num int) int {
		if v, x := cache[num]; x {
			return v
		}
		temp := f(num-1) + f(num-2)
		cache[num] = temp
		return temp
	}
	return f(n)
}

func main() {
	fmt.Println(climbStairs(1))
	fmt.Println(climbStairs(2))
	fmt.Println(climbStairs(3))
	fmt.Println(climbStairs(10))
	fmt.Println(climbStairs(20))
	fmt.Println(climbStairs(30))
}
