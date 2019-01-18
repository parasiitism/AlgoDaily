package main

import (
	"fmt"
	"strconv"
)

/*
	1st approach
	- just do what the desc mention
	- nothing edifying
	Time	i am not sure since it involves some math, i guess it >O(n) but
	4ms beats 75.76%
*/
func countAndSay(n int) string {
	result := "1"
	n--
	for n > 0 {
		result = buildNext(result)
		n--
	}
	return result
}

func buildNext(s string) string {
	result := ""
	cur := string(s[0])
	cnt := 1
	for i := 1; i < len(s); i++ {
		if cur == string(s[i]) {
			cnt++
		} else {
			result += strconv.Itoa(cnt) + cur
			cur = string(s[i])
			cnt = 1
		}
	}
	if cnt > 0 {
		result += strconv.Itoa(cnt) + cur
	}
	return result
}

func main() {
	fmt.Println(countAndSay(1))
	fmt.Println(countAndSay(2))
	fmt.Println(countAndSay(3))
	fmt.Println(countAndSay(4))
	fmt.Println(countAndSay(5))
}
