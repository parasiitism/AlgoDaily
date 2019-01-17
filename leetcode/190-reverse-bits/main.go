package main

import (
	"fmt"
	"math"
)

/*
	Questions to ask:
	- the leading zeros?
	- input out of bound?
*/

/*
	1st approach: classic bit op similar to leetcode 191
	Time	O(32)
	Space	O(1)
	4ms beats 100%
	17jan2019
*/
func reverseBits(num uint32) uint32 {
	var result uint32
	x := num
	n := 0
	for n < 32 {
		result = result << 1
		if x&1 == 1 {
			result = result | 1
		}
		x = x >> 1
		n++
	}
	return result
}

func main() {
	fmt.Println(reverseBits(0))
	fmt.Println(reverseBits(1))
	fmt.Println(reverseBits(43261596))
	fmt.Println(reverseBits(4294967293))
	fmt.Println(reverseBits(math.MaxUint16))
	fmt.Println(reverseBits(math.MaxUint32 - 1))
}
