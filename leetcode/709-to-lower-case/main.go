package main

import "fmt"

/*
	Don't use bult-in function
*/

/*
	naive approach
	- hashtable
*/

/*
	1st approach
	- ascii code
	0ms beats 100%
*/
func toLowerCase(str string) string {
	res := ""
	for _, c := range str {
		if c >= 'A' && c <= 'Z' {
			temp := string(c - 'A' + 'a')
			res += temp
		} else {
			res += string(c)
		}
	}
	return res
}

func main() {
	fmt.Println(toLowerCase("Hello"))
}
