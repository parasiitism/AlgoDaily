package main

import (
	"fmt"
	"sort"
	"strings"
)

/*
	1. find the positions for the bold tags
	2. sort the intervals, O(nlogn)
	3. merge the intervals
	4. put the intervals into sets
	5. construct result

	Time	O(nlogn)
	Space	O(n)
	12 ms, faster than 84.21%
*/
func addBoldTag(s string, dict []string) string {
	// find the positions for the bold tags
	intervals := [][]int{}
	for _, word := range dict {
		t := strings.Index(s, word)
		acc := 0
		for t > -1 {
			intervals = append(intervals, []int{acc + t, acc + t + len(word)})
			acc += t + 1
			t = strings.Index(s[acc:], word)
		}
	}
	// sort the intervals, O(nlogn)
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	if len(intervals) == 0 {
		return s
	}
	// merge the intervals
	merged := [][]int{
		intervals[0],
	}
	for _, interval := range intervals {
		if interval[0] <= merged[len(merged)-1][1] {
			merged[len(merged)-1][1] = max(merged[len(merged)-1][1], interval[1])
		} else {
			merged = append(merged, interval)
		}
	}
	// put the intervals into sets
	opens := make(map[int]bool)
	closes := make(map[int]bool)
	for _, m := range merged {
		opens[m[0]] = true
		closes[m[1]] = true
	}
	// construct result
	res := ""
	cnt := 0
	for i := 0; i < len(s); i++ {
		if _, x := opens[i]; x {
			res += "<b>"
			cnt++
		}
		if _, x := closes[i]; x {
			res += "</b>"
			cnt--
		}
		res += string(s[i])
	}
	if cnt > 0 {
		res += "</b>"
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := []string{"ab", "bc"}
	b := "aabcd"
	fmt.Println(addBoldTag(b, a))

	a = []string{"ccb", "a", "cc", "dc", "d"}
	b = "bacdcbcced"
	fmt.Println(addBoldTag(b, a))

	a = []string{"e", "cab", "de", "cc", "db"}
	b = "cbccceeead"
	fmt.Println(addBoldTag(b, a))

	// S := "cbccceeead"
	// word := "e"
	// t := strings.Index(S, word)
	// acc := 0
	// for t > -1 {
	// 	fmt.Println(t, acc, acc+t)
	// 	acc += t + 1
	// 	t = strings.Index(S[acc:], word)
	// }
}
