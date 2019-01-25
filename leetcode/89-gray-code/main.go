package main

import "fmt"

/*
	Questions to asK:
	- n <= 0?
*/

/*
	classic approach
	- gray's reflect and prefix method ./gray_code.png
	4ms beats 100%
	Time 	O(2^n) when n=3, there are 8 items in the result
	Space	O(2^n)
	25jan2019
*/
func grayCode(n int) []int {
	if n <= 0 {
		return []int{0}
	}
	res := []int{0, 1}
	cnt := 1
	for cnt < n {
		temp := []int{}
		for i := len(res) - 1; i >= 0; i-- {
			helper := 1 << uint(cnt)
			mirrored := res[i] | helper
			temp = append(temp, mirrored)
		}
		res = append(res, temp...)
		cnt++
	}
	return res
}

func main() {
	fmt.Println(grayCode(-1))
	fmt.Println(grayCode(0))
	fmt.Println(grayCode(1))
	fmt.Println(grayCode(3))
	fmt.Println(grayCode(4))
}
