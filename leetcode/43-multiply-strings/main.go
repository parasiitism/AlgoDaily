package main

import (
	"fmt"
	"strconv"
)

/*
	string conversion is not allowed
*/
func multiply0(num1 string, num2 string) string {
	a, _ := strconv.Atoi(num1)
	b, _ := strconv.Atoi(num2)
	c := a * b
	return strconv.Itoa(c)
}

/*
	ref: https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation

	Time	O(M*N)
	Space	O(M+N)
	0 ms, faster than 100.00%
*/
func multiply(num1 string, num2 string) string {
	// init 0000000...the number of digits of any 2 numbers mulitplication must <= N+M digits
	res := []int{}
	for i := 0; i < len(num1)+len(num2); i++ {
		res = append(res, 0)
	}
	// calculate
	for i := len(num1) - 1; i >= 0; i-- {
		for j := len(num2) - 1; j >= 0; j-- {
			// position1: leading digit e.g. 91, 9 is at position1
			// position2: ending digit e.g. 91, 1 is at position1
			position1 := i + j
			position2 := i + j + 1
			// multiply the digits, it must gets 2 digits result
			x := int(num1[i] - '0')
			y := int(num2[j] - '0')
			// add the carray, which was stored in the last computation
			z := x*y + res[position2]
			// put them into the result array
			res[position1] += z / 10
			res[position2] = z % 10
		}
	}
	result := ""
	started := false
	for _, c := range res {
		if !started && c == 0 {
			continue
		}
		started = true
		result += strconv.Itoa(c)
	}
	if len(result) == 0 {
		return "0"
	}
	return result
}

func main() {
	/*
	   "498828660196"
	   "840477629533"
	*/

	fmt.Println(multiply("12", "345"))
	fmt.Println(multiply("99", "99"))
	fmt.Println(multiply("1", "12"))
	fmt.Println(multiply("1", "0"))
}
