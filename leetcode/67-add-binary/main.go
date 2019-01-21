package main

import (
	"fmt"
	"strconv"
)

/*
	questions to ask:
	- empty strings?
	- charactors other than 0 and 1 ?
	- the length of a and b?
*/

/*
	naive approach:
	- convert to int
	- add and return result
	however, if the input number is > 2^32, it fucks up
*/

/*
	1st approach:
	- each digit = byteA + byteB + carry
	- add the digits until no more carry, a, b
	0ms beats 100%
*/
func addBinary(a string, b string) string {
	res := ""
	carry := 0
	for carry > 0 || len(a) > 0 || len(b) > 0 {
		byteA := 0
		if len(a) > 0 {
			byteA = int(a[len(a)-1] - '0')
			a = a[:len(a)-1]
		}

		byteB := 0
		if len(b) > 0 {
			byteB = int(b[len(b)-1] - '0')
			b = b[:len(b)-1]
		}

		temp := byteA + byteB + carry

		if carry > 0 {
			carry--
		}

		if temp > 1 {
			temp = temp % 2
			carry = 1
		}
		res = strconv.Itoa(temp) + res
	}
	return res
}

func findMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(addBinary("0", "0"))
	fmt.Println(addBinary("0", "1"))
	fmt.Println(addBinary("1", "0"))
	fmt.Println(addBinary("1", "1"))
	fmt.Println(addBinary("11", "1"))
	fmt.Println(addBinary("1010", "1011"))
	fmt.Println(addBinary("1111", "111111111"))
}
