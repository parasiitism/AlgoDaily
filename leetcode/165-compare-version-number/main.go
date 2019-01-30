package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
	it seems like there is no other better ways
	1. split by .
	2. iterate and compare each section
	3. if compare result != 0, return immediately
	Time	O(n)
	Space	O(n)
	0ms beats 100%
	30jan2019
*/
func compareVersion(version1 string, version2 string) int {
	version1nums := strings.Split(version1, ".")
	version2nums := strings.Split(version2, ".")
	larger := max(len(version1nums), len(version2nums))
	for i := 0; i < larger; i++ {
		v1 := 0
		if i < len(version1nums) {
			v1, _ = strconv.Atoi(version1nums[i])
		}

		v2 := 0
		if i < len(version2nums) {
			v2, _ = strconv.Atoi(version2nums[i])
		}

		c := compare(v1, v2)
		if c != 0 {
			return c
		}
	}
	return 0
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func compare(a, b int) int {
	if a > b {
		return 1
	} else if b > a {
		return -1
	}
	return 0
}

func main() {
	fmt.Println(compareVersion("0.1", "1.1"))
	fmt.Println(compareVersion("1.0.1", "1"))
	fmt.Println(compareVersion("1.0.1", "1.1"))
	fmt.Println(compareVersion("1.1.0", "1.1"))
	fmt.Println(compareVersion("1.1.1", "1.1"))
	fmt.Println(compareVersion("7.5.2.4", "7.5.3"))
	fmt.Println(compareVersion("1.01", "1.001"))
	fmt.Println(compareVersion("1.00", "1.0"))
}
