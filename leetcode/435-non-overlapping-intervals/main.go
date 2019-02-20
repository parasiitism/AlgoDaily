package main

import (
	"fmt"
	"sort"
)

type Interval struct {
	Start int
	End   int
}

/*
	1st approach:
	1. sort the intervals by start time
	2. prepare a temporary array for nonoverlapping intervals
	3. when the current interval follows(behind and not overlap) the temp array last item, append to the temp array
	4. when the current interval overlaps but shorter than the temp array last item, replace the temp array last item, res++
	5. when the current interval overlaps with the previous interval, res++

	Time		O(nlogn) built-in sort
	Space		O(n)		 the temporary array

	8 ms, faster than 100.00%
*/
func eraseOverlapIntervals(intervals []Interval) int {
	if len(intervals) < 2 {
		return 0
	}
	// sort the intervals by start time, order by end time
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i].Start != intervals[j].Start {
			return intervals[i].Start < intervals[j].Start
		}
		return intervals[i].End < intervals[j].End
	})
	// put all the non-overlapping intervals into a temporary array
	// and put the overlapping intervals into the result
	res := 0
	nonOverlap := []Interval{}
	nonOverlap = append(nonOverlap, intervals[0])
	for i := 1; i < len(intervals); i++ {
		if intervals[i].Start >= nonOverlap[len(nonOverlap)-1].End {
			// when the current interval follows(behind and not overlap) the previous interval
			nonOverlap = append(nonOverlap, intervals[i])
		} else {
			// when the current interval overlaps but shorter than the previous temp interval
			// replace the previous interval
			if intervals[i].End < nonOverlap[len(nonOverlap)-1].End {
				nonOverlap[len(nonOverlap)-1] = intervals[i]
			}
			// 2 cases to increment the count
			// 1. the current interval has replaced previous temp interval
			// 2. the current interval overlaps with the previous interval
			res++
		}
	}
	return res
}

func main() {
	a := []Interval{
		{1, 2},
		{2, 3},
		{3, 4},
		{1, 3},
	}
	fmt.Println(eraseOverlapIntervals(a))

	a = []Interval{
		{1, 2},
		{1, 2},
		{1, 2},
		{1, 3},
	}
	fmt.Println(eraseOverlapIntervals(a))

	a = []Interval{
		{1, 2},
		{2, 3},
	}
	fmt.Println(eraseOverlapIntervals(a))

	a = []Interval{
		{1, 10},
		{2, 3},
		{3, 4},
		{4, 5},
	}
	fmt.Println(eraseOverlapIntervals(a))
}
