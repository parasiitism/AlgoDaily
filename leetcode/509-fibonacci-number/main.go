package main

import "fmt"

// recursive
func fib(N int) int {
	cache := make(map[int]int)
	cache[0] = 0
	cache[1] = 1
	var f func(num int) int
	f = func(num int) int {
		if v, x := cache[num]; x {
			return v
		}
		return f(num-1) + f(num-2)
	}
	return f(N)
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
}
