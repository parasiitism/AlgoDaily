package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
	1st approach:
	1. get all combinations of the numbers from input
	2. compare and find the combinations with the target time

	be careful of the corner cases:
	- 00:00
	- 07:07
	- 11:11

	Time	O(1) only need to compate 4^4=256 combinations with the target
	Space	O(1) bucket size 1440
	4 ms, faster than 6.45% <= the implementation is ugly
*/
func nextClosestTime(time string) string {
	// translate the time to number hour*60+minute
	target := transformTime(time)
	// get the digits from input
	hm := strings.Replace(time, ":", "", -1)
	a := string(hm[0])
	b := string(hm[1])
	c := string(hm[2])
	d := string(hm[3])
	candidates := a + b + c + d
	// bucket for all minutes in one day
	bucket := []bool{}
	for i := 0; i < 1440; i++ {
		bucket = append(bucket, false)
	}
	// get all the combinations of the numbers
	var dfs func(s string)
	dfs = func(s string) {
		if len(s) == 4 {
			x := s[:2] + ":" + s[2:]
			temp := transformTime(string(x))
			if temp > -1 {
				bucket[temp] = true
			}
			return
		}
		for i := 0; i < len(candidates); i++ {
			dfs(s + string(candidates[i]))
		}
	}
	dfs("")
	// find the next time
	res := 1440
	for idx, slot := range bucket {
		if slot == true {
			if idx > target && idx < res {
				res = idx
			}
		}
	}
	if res == 1440 {
		for idx, slot := range bucket {
			if slot == true {
				t := idx + 1440
				if t > target && idx < res {
					res = idx
				}
			}
		}
	}
	// fmt.Println(res)
	if res == 1440 {
		if a == "0" || b == "0" || c == "0" || d == "0" {
			return "00:00"
		}
		return time
	}
	// construct the result
	h := ""
	if res/60 < 10 {
		h = "0" + strconv.Itoa(res/60)
	} else {
		h = strconv.Itoa(res / 60)
	}
	m := ""
	if res%60 < 10 {
		m = "0" + strconv.Itoa(res%60)
	} else {
		m = strconv.Itoa(res % 60)
	}
	return h + ":" + m
}

func transformTime(time string) int {
	hm := strings.Split(time, ":")
	h := hm[0]
	m := hm[1]
	hour, _ := strconv.Atoi(h)
	minute, _ := strconv.Atoi(m)
	if hour > 23 || minute > 59 {
		return -1
	}
	return hour*60 + minute
}

func main() {
	/*
		19:39
		22:22
		15:11
		13:10
		21:01
		00:00
		00:10
		00:00
		08:00
		09:00
		11:11
		11:21
	*/
	fmt.Println(nextClosestTime("19:34")) // 19:39
	fmt.Println(nextClosestTime("23:59")) // 22:22
	fmt.Println(nextClosestTime("13:59")) // 15:11
	fmt.Println(nextClosestTime("13:05")) // 13:10
	fmt.Println(nextClosestTime("21:00")) // 21:01
	fmt.Println(nextClosestTime("00:00")) // 00:00
	fmt.Println(nextClosestTime("00:01")) // 00:10
	fmt.Println(nextClosestTime("07:07")) // 00:00
	fmt.Println(nextClosestTime("07:08")) // 08:00
	fmt.Println(nextClosestTime("05:59")) // 09:00
	fmt.Println(nextClosestTime("11:11")) // 11:11
	fmt.Println(nextClosestTime("11:12")) // 11:21
}
