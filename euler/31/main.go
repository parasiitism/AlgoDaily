package main

import "fmt"

func CoinSums(n int) int {
	hash := make(map[int]int)
	return helper(n, hash)
}

func helper(n int, hash map[int]int) int {
	if n == 0 {
		return 1
	} else if n < 0 {
		return 0
	}
	if v, x := hash[n]; x {
		return v
	}
	a := helper(n-200, hash)
	b := helper(n-100, hash)
	c := helper(n-50, hash)
	d := helper(n-20, hash)
	e := helper(n-10, hash)
	f := helper(n-5, hash)
	g := helper(n-2, hash)
	h := helper(n-1, hash)
	temp := a + b + c + d + e + f + g + h
	hash[n] = temp
	return temp
}

func main() {
	fmt.Println(CoinSums(5))
	fmt.Println(CoinSums(200))
}
