package main

import (
	"fmt"
	"unicode"
)

/*
	1st approach:
	- since the iterater only goes forward, we can consume the string directly
	- for each character, there are 2 things we need
		1. the character itself
		2. the count of character
	- we can use a variable, a buffer to save the current character
	- and when we do next(), we can consume the count until it reaches to 0

	Time of next(): average O(1). worst case O(n) if e.g. A9999 cos we need to traverse the rest of string to form the number 9999
	Time of hasNext(): O(1)

	8 ms, faster than 100.00%
*/

type StringIterator struct {
	S           string
	Buffer      byte
	BufferCount int
}

func Constructor(compressedString string) StringIterator {
	return StringIterator{compressedString, ' ', 0}
}

func (this *StringIterator) Next() byte {
	if this.BufferCount == 0 {
		if len(this.S) > 0 {
			// get the character
			this.Buffer = this.S[0]
			this.S = this.S[1:]
			// get multi-digit number, e.g. "23" = 2*10+3
			num := 0
			for len(this.S) > 0 {
				pop := this.S[0]
				if unicode.IsDigit(rune(pop)) == true {
					this.S = this.S[1:]
					num = num*10 + int(pop) - 48
				} else {
					break
				}
			}
			this.BufferCount = num
			// consume the buffer count
			this.BufferCount--
			return this.Buffer
		}
		return ' '
	}
	// consume the buffer count
	this.BufferCount--
	return this.Buffer
}

func (this *StringIterator) HasNext() bool {
	if this.BufferCount == 0 && len(this.S) == 0 {
		return false
	}
	return true
}

/**
* Your StringIterator object will be instantiated and called as such:
* obj := Constructor(compressedString);
* param_1 := obj.Next();
* param_2 := obj.HasNext();
 */

func main() {
	c := Constructor("L1e2t1C1o1d1e1")
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())

	c = Constructor("")
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
	fmt.Println(c.Next())
}
