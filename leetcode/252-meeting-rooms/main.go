package main

import "sort"

type Interval struct {
	Start int
	End   int
}

/*
	naive approach: brute force
	- for each item, compare the start & end with the rest of the items
	Time		O(n^2)
	Space	O(1)
	not gonna implement
*/

/*
	1st approach
	- sort the array, compare the item[i].start and item[i-1].end
	- takeaway: use sort.slice() to sort a list of structs https:godoc.org/sort#Slice
	Time		O(nlogn)
	Space	O(1)
	12ms beats 100%
*/
func canAttendMeetings(intervals []Interval) bool {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start
	})

	for i := 1; i < len(intervals); i++ {
		if intervals[i].Start < intervals[i-1].End {
			return false
		}
	}
	return true
}

func main() {

}
