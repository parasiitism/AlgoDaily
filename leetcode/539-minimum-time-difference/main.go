package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

/*
	questions to ask:
	- so 23:59 -> 00:00 has only 1 minute difference? yes
	- are the input sorted? no
	- will there be malformed input? no
	- will there be empty input? yes
	- will there be duplicate input? yes
*/

/*
	1st approach: sort
	1. transform the input times to a list of number: hour*60+minute,
	dont forget to put its temp+1440 as well due to the cases like 23:59, 00:00 => 1
	2. sort the numbers
	3. find the min diff between any consecetive numbers, times[i]-times[i-1]
*/
func findMinDifference(timePoints []string) int {
	times := []int{}
	for _, tp := range timePoints {
		hm := strings.Split(tp, ":")
		h := hm[0]
		m := hm[1]
		hour, _ := strconv.Atoi(h)
		minute, _ := strconv.Atoi(m)
		temp := hour*60 + minute
		times = append(times, temp, temp+1440)
	}
	sort.Ints(times)
	result := 1440
	for i := 1; i < len(times); i++ {
		if times[i]-times[i-1] < result {
			result = times[i] - times[i-1]
		}
	}
	return result
}

/*
	2nd approach: bucket
	1. transform the input times to a list of number: hour*60+minute,
	dont forget to put its temp+1440 as well due to the cases like 23:59, 00:00 => 1
	2. since the total number of minutes are definite, we can create a bucket with 1440*2 for it
	3. find the min diff between any consecetive numbers, times[i]-times[i-1]
*/
func findMinDifference1(timePoints []string) int {
	if len(timePoints) < 2 {
		return 0
	}
	bucket := []int{}
	for i := 0; i < 2880; i++ {
		bucket = append(bucket, 0)
	}
	for _, tp := range timePoints {
		hm := strings.Split(tp, ":")
		h := hm[0]
		m := hm[1]
		hour, _ := strconv.Atoi(h)
		minute, _ := strconv.Atoi(m)
		t1 := hour*60 + minute
		t2 := t1 + 1440
		bucket[t1]++
		bucket[t2]++
	}
	result := 1440
	last := -1
	for idx, t := range bucket {
		if t > 1 {
			return 0
		} else if t > 0 {
			if last == -1 {
				last = idx
			} else {
				if idx-last < result {
					result = idx - last
				}
				last = idx
			}
		}
	}
	return result
}

func main() {
	fmt.Println(findMinDifference1([]string{"23:59", "00:00"}))
	fmt.Println(findMinDifference1([]string{"23:59", "00:00", "00:00"}))
	fmt.Println(findMinDifference1([]string{"23:59", "00:10", "12:34", "21:55"}))
	fmt.Println(findMinDifference1([]string{
		"04:57", "13:29", "07:50", "02:59", "07:07", "02:17", "02:52", "00:11", "09:37", "01:15",
		"16:14", "11:45", "13:58", "22:11", "23:04", "17:09", "16:09", "05:55", "02:53", "20:33",
		"19:44", "08:01", "03:03", "00:27", "16:06", "16:06", "07:09", "21:33", "03:48", "07:29",
		"04:22", "04:10", "07:40", "12:02", "01:38", "12:04", "11:20", "23:48", "06:48", "21:49",
		"04:52", "13:38", "22:58", "21:07", "08:51", "16:16", "08:30", "13:21", "07:36", "16:06",
	}))
}
