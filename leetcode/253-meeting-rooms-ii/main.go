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
	112ms beats 0%
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

/*
	2nd approach
	- sort the array
	- create an array of meeting rooms
	- each interval, search for vacancies in the meeting rooms just by comparing the last interval endTime
	- if there is no collision, put the meeting in that room, else create a new meeting room for the interval
	Time		O(nlogn) nlogn: sort; n^2:
	Space 	O(n)	result array
	112ms beats 0%
*/
func minMeetingRooms1(intervals []Interval) int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start
	})
	rooms := [][]Interval{}
	for i := 0; i < len(intervals); i++ {
		j := 0
		for ; j < len(rooms); j++ {
			room := rooms[j]
			if room[len(room)-1].End <= intervals[i].Start {
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

func main() {
	a := []Interval{
		Interval{0, 30},
		Interval{5, 10},
		Interval{15, 20},
	}
	fmt.Println(minMeetingRooms1(a))

	a = []Interval{
		Interval{7, 10},
		Interval{2, 4},
	}
	fmt.Println(minMeetingRooms1(a))

	a = []Interval{
		Interval{0, 30},
		Interval{1, 30},
		Interval{2, 20},
		Interval{3, 30},
		Interval{4, 30},
		Interval{5, 20},
	}
	fmt.Println(minMeetingRooms1(a))
}
