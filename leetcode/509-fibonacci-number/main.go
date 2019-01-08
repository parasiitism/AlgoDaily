package main

import "fmt"

// top-down recursive
// use a hashtable to avoid redundant calculation
// Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
// Space O(2n)	n for hashtable, n for recursive callstack
// 0ms beats 100%
func fib(N int) int {
	cache := make(map[int]int)
	cache[0] = 0
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
	return f(N)
}

// bottom-up iterative
// Time 	O(n)
// Space	O(n)
// 0ms beats 100%
func fib1(N int) int {
	arr := []int{}
	arr = append(arr, 0)
	arr = append(arr, 1)
	for i := 2; i <= N; i++ {
		arr = append(arr, arr[i-1]+arr[i-2])
	}
	return arr[N]
}

func main() {
	fmt.Println(fib(0))
	fmt.Println(fib(1))
	fmt.Println(fib(2))
	fmt.Println(fib(3))
	fmt.Println(fib(4))
	fmt.Println(fib(5))
	fmt.Println(fib(10))
	fmt.Println(fib(20))
	fmt.Println(fib(29))
	fmt.Println(fib(30))
	fmt.Println(fib(31))

	fmt.Println(fib1(0))
	fmt.Println(fib1(1))
	fmt.Println(fib1(2))
	fmt.Println(fib1(3))
	fmt.Println(fib1(4))
	fmt.Println(fib1(5))
	fmt.Println(fib1(10))
	fmt.Println(fib1(20))
	fmt.Println(fib1(29))
	fmt.Println(fib1(30))
	fmt.Println(fib1(31))
}
