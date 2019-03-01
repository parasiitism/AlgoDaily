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
	- will there will malformed input? no
*/

/*
	1st approach:
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

func main() {
	fmt.Println(findMinDifference([]string{"23:59", "00:00"}))
	fmt.Println(findMinDifference([]string{"23:59", "00:10", "12:34", "21:55"}))
}
