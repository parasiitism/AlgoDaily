package main

import (
	"fmt"
	"sort"
)

/*
	questions to ask:
	- will there be an empty input?
	- wil there be a single interval input?

	be carefal of corner cases like [[1,4],[2,3]]
*/

type Interval struct {
	Start int
	End   int
}

/*
	1st approach
	1. sort the intervals
	2. if the start of intervals[i] <= start of intervals[i-1], replace the end with max end of intervals[i], intervals[i-1]

	Time	O(nlogn)
	Space	O(n)

	12 ms, faster than 100.00%
*/
func merge(intervals []Interval) []Interval {
	if len(intervals) < 2 {
		return intervals
	}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start
	})
	res := []Interval{}
	res = append(res, intervals[0])
	for i := 1; i < len(intervals); i++ {
		if intervals[i].Start <= res[len(res)-1].End {
			res[len(res)-1].End = findMax(intervals[i].End, res[len(res)-1].End)
		} else {
			res = append(res, intervals[i])
		}
	}
	return res
}

func findMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := []Interval{
		{1, 3},
		{2, 6},
		{8, 10},
		{15, 18},
	}
	fmt.Println(merge(a))

	a = []Interval{
		{1, 4},
		{4, 5},
	}
	fmt.Println(merge(a))

	a = []Interval{
		{1, 4},
		{2, 3},
	}
	fmt.Println(merge(a))
}
