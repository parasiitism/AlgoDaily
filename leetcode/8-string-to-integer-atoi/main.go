package main

import (
	"fmt"
	"math"
	"strings"
)

/*
	1st approach
	- straight forward approach
	- be careful of the corner cases
	Time 	O(n) n=length of input string
	Space O(1)
	4ms beats 100%
	15jan2019
*/
func myAtoi0(str string) int {
	sum := 0
	negative := 1
	str = strings.TrimSpace(str)
	for i := 0; i < len(str); i++ {
		if i == 0 {
			if str[i] == '+' {
				continue
			} else if str[i] == '-' {
				negative = -1
			} else if str[i]-'0' <= 9 {
				sum = int(str[i] - '0')
			} else {
				break
			}
		} else {
			if str[i]-'0' <= 9 {
				sum = sum*10 + int(str[i]-'0')
				temp := sum * negative
				if temp < math.MinInt32 {
					return math.MinInt32
				}
				if temp > math.MaxInt32 {
					return math.MaxInt32
				}
			} else {
				break
			}
		}
	}
	result := sum * negative
	if result < math.MinInt32 {
		return math.MinInt32
	}
	if result > math.MaxInt32 {
		return math.MaxInt32
	}
	return result
}

/*
	2nd approach is actaully a rewritten form of 1st
	Time 	O(n) n=length of input string
	Space O(1)
	4ms beats 100%
	15jan2019
*/
func myAtoi(str string) int {
	sum := 0
	sign := 1
	str = strings.TrimSpace(str)
	for i := 0; i < len(str); i++ {
		if i == 0 {
			if str[i] == '+' {
				continue
			} else if str[i] == '-' {
				sign = -1
			} else if str[i]-'0' <= 9 {
				sum = int(str[i] - '0')
			} else {
				break
			}
		} else {
			if str[i]-'0' <= 9 {
				sum = sum*10 + int(str[i]-'0')
				c := checkBoundries(sum, sign)
				abs := c
				if c < 0 {
					abs = c * -1
				}
				if abs != sum {
					return c
				}
			} else {
				break
			}
		}
	}
	return checkBoundries(sum, sign)
}

func checkBoundries(num int, sign int) int {
	result := num * sign
	if result < math.MinInt32 {
		return math.MinInt32
	}
	if result > math.MaxInt32 {
		return math.MaxInt32
	}
	return result
}

func main() {
	fmt.Println(myAtoi("42"))
	fmt.Println(myAtoi("   -42"))
	fmt.Println(myAtoi("4193 with words"))
	fmt.Println(myAtoi("words and 987"))
	fmt.Println(myAtoi("22 and 987"))
	fmt.Println(myAtoi(" 22 and 987"))
	fmt.Println(myAtoi(" -22 and 987"))
	fmt.Println(myAtoi(" -+22 and 987"))
	fmt.Println(myAtoi("-91283472332"))
	fmt.Println(myAtoi(" -91283472332"))
	fmt.Println(myAtoi("91283472332"))
	fmt.Println(myAtoi(" +91283472332"))
	fmt.Println(myAtoi(" -91283472332 a"))
	fmt.Println(myAtoi(" a-91283472332"))
	fmt.Println(myAtoi("9223372036854775808"))
}
