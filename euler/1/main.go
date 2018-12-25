package main

import "fmt"

func f(n int) int {
	result := 0
	for i := 1; i < n; i++ {
		if i%3 == 0 && i%5 == 0 {
			result += i
		} else if i%3 == 0 {
			result += i
		} else if i%5 == 0 {
			result += i
		}
	}
	return result
}

func main() {
	fmt.Println(f(10))
	fmt.Println(f(100))
	fmt.Println(f(1000))
}
