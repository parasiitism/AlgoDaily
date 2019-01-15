package main

import (
	"fmt"
	"strings"
)

/*
	questions to ask:
	- will there be no @?
	- will there be more than one @?
	- will there be no charactors before @?
	- will there be no charactors after @?

	1st approach:
	- use split, replace and set
	Time  O(n)
  Space O(n)
	12ms beats 91.07%
	15jan2019
*/
func numUniqueEmails(emails []string) int {
	hash := make(map[string]bool)
	for i := 0; i < len(emails); i++ {
		email := emails[i]
		parts := strings.Split(email, "@")
		if len(parts) < 2 {
			continue
		}
		portions := strings.Split(parts[0], "+")
		first := portions[0]
		first = strings.Replace(first, ".", "", -1)
		if len(first) == 0 || len(parts[1]) == 0 {
			continue
		}
		em := first + "@" + parts[1]
		hash[em] = true
	}
	return len(hash)
}

func main() {
	fmt.Println(numUniqueEmails([]string{
		"test.email+alex@leetcode.com",
		"test.e.mail+bob.cathy@leetcode.com",
		"testemail+david@lee.tcode.com",
		"abc@ca.com",
		"@",
		"aaa@",
		"@ddd",
	}))
}
