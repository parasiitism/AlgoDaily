package main

import "fmt"

/*
	questions to ask:
	- circular? az, ba are in the same group?
	- will there be other non-alpbabetic characters?
*/

/*
	1st approach
	- hashtable
	1. in each iteration, transform the string into a key(diff between characters)
	2. keep in mind that, az, ba are in the same group

	Time		O(n)
	Space		O(n)
	4 ms, faster than 100.00%
*/
func groupStrings(strings []string) [][]string {
	m := make(map[string][]string)
	for i := 0; i < len(strings); i++ {
		s := strings[i]
		t := transform(s)
		if _, x := m[t]; !x {
			m[t] = []string{s}
		} else {
			m[t] = append(m[t], s)
		}
	}
	res := [][]string{}
	for _, v := range m {
		res = append(res, v)
	}
	return res
}

func transform(s string) string {
	if len(s) <= 1 {
		return ""
	}
	res := ""
	prev := s[0]
	for i := 1; i < len(s); i++ {
		c := s[i]
		// save the diff between 2 consecetive characters
		temp := (c - prev + 26) % 26
		res += string(temp) + ","
		prev = c
	}
	return res
}

func main() {
	a := []string{"abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"}
	fmt.Println(groupStrings(a))

	a = []string{""}
	fmt.Println(groupStrings(a))

	a = []string{"a"}
	fmt.Println(groupStrings(a))
}
