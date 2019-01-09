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
	1st approach
	- sort the array
	- create an array of meeting rooms
	- each interval, search for vacancies in the meeting rooms
	- if there is no collision, put the meeting in that room, else create a new meeting room for the interval
	Time		O(nlogn+n^2) nlogn: sort; n^2: search for vacancies by each interval
	Space 	O(n)	result array
	112ms, no beat because leetcode is recently updating the graph distribution
*/
func minMeetingRooms(intervals []Interval) int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start
	})
	rooms := [][]Interval{}
	for i := 0; i < len(intervals); i++ {
		j := 0
		for ; j < len(rooms); j++ {
			room := rooms[j]
			cop := []Interval{}
			cop = append(cop, room...)
			cop = append(cop, intervals[i])
			if canAttendMeetings(cop) {
				break
			}
		}
		if j < len(rooms) {
			rooms[j] = append(rooms[j], intervals[i])
		} else {
			rooms = append(rooms, []Interval{intervals[i]})
		}
	}
	return len(rooms)
}

func canAttendMeetings(intervals []Interval) bool {
	for i := 1; i < len(intervals); i++ {
		if intervals[i].Start < intervals[i-1].End {
			return false
		}
	}
	return true
}

func main() {
	a := []Interval{
		Interval{0, 30},
		Interval{5, 10},
		Interval{15, 20},
	}
	fmt.Println(minMeetingRooms(a))

	a = []Interval{
		Interval{7, 10},
		Interval{2, 4},
	}
	fmt.Println(minMeetingRooms(a))

	a = []Interval{
		Interval{0, 30},
		Interval{1, 30},
		Interval{2, 20},
		Interval{3, 30},
		Interval{4, 30},
		Interval{5, 20},
	}
	fmt.Println(minMeetingRooms(a))
}
