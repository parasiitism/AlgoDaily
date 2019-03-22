package main

import "fmt"

/*
	1st approach: recursion
	e.g.
	if the n = 3, for 11, we can add 0,1,8 to create 101,111,181
	if the n = 4, for 11, we can add 00,11,69,88,96 to create 1001 1111 1691 1881 1961

	Time	O(5^n/2) at most because one number has at most 5 options to become
	Space	O(5^n/2) callstack
	4284 ms, faster than 27.27%
*/
func findStrobogrammatic(n int) []string {
	singles := []string{"0", "1", "8"}
	pairs := []string{"00", "11", "69", "88", "96"}

	if n == 0 {
		return []string{}
	} else if n == 1 {
		return singles
	}

	res := []string{}
	// recursion:
	// add numbers in the middle
	var helper func(cnt int, s string)
	helper = func(cnt int, s string) {
		if cnt == n {
			res = append(res, s)
		} else if cnt+1 == n {
			// if there is only one place left, we should just add one digit
			pos := cnt / 2
			for i := 0; i < len(singles); i++ {
				helper(cnt+1, s[:pos]+singles[i]+s[pos:])
			}
		} else {
			// if there are many digits place left, we should add pairs in the middle
			pos := cnt / 2
			for i := 0; i < len(pairs); i++ {
				helper(cnt+2, s[:pos]+pairs[i]+s[pos:])
			}
		}
	}
	for i := 1; i < len(pairs); i++ {
		helper(2, pairs[i])
	}

	return res
}

func main() {
	fmt.Println(findStrobogrammatic(1))
	fmt.Println(findStrobogrammatic(2))
	fmt.Println(findStrobogrammatic(3))
	fmt.Println(findStrobogrammatic(4))

	a := "123"
	b := "234"
	if a > b {
		fmt.Println("ad")
	} else {
		fmt.Println("ads")
	}
}
