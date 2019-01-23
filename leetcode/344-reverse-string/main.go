package main

import "fmt"

/*
	Questions to ask:
	- is there any empty space?
	- empty input?
	- input just contains one charactor?
	- in place?
*/

/*
  the purpose of the question is to use 2 pointers, so i am just gonna implement it with 2 pointers
*/
func reverseString(s []byte) []byte {
	fmt.Println(s)
	i, j := 0, len(s)-1
	for i < j {
		s[i], s[j] = s[j], s[i]
		i++
		j--
	}
	return s
}

func main() {
	a := "abc"
	fmt.Println(reverseString([]byte(a)))
	fmt.Println(a)
}
