package main

import "sort"

/*
	1st approach: binary search
	- for each house, binary search to look for the nearest heater(so we should sort heaters first)
	- the max diff is the result

	Time    O(nlogn+mlogn) n:heaters, m: houses
	Space   O(1)
	48 ms, faster than 100.00%
*/

func findRadius(houses []int, heaters []int) int {
	sort.Ints(heaters)
	res := -1
	for _, house := range houses {
		idx := bSearchNearest(heaters, house)
		diff := findAbs(house - heaters[idx])
		if diff > res {
			res = diff
		}
	}
	return res
}

/*
	e.g. a = [10, 20, 30, 40]
	print(Solution().bSearchNearest(a, 9)) <- 0
	print(Solution().bSearchNearest(a, 10)) <- 0
	print(Solution().bSearchNearest(a, 13)) <- 0
	print(Solution().bSearchNearest(a, 21)) <- 1
	print(Solution().bSearchNearest(a, 26)) <- 2
	print(Solution().bSearchNearest(a, 34)) <- 2
	print(Solution().bSearchNearest(a, 35)) <- 3
	print(Solution().bSearchNearest(a, 41)) <- 3
*/
func bSearchNearest(arr []int, target int) int {
	min := 0
	max := len(arr) - 1
	for min <= max {
		mean := (min + max) / 2
		if target == arr[mean] {
			return mean
		} else if target > arr[mean] {
			min = mean + 1
		} else if target < arr[mean] {
			max = mean - 1
		}
	}
	// compare and find the idx of the nearest item
	if max < 0 {
		return 0
	}
	if min > len(arr)-1 {
		return len(arr) - 1
	}
	if findAbs(target-arr[max]) < findAbs(target-arr[min]) {
		return max
	}
	return min
}

func findAbs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {

}
