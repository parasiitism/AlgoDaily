package main

import (
	"fmt"
	"sort"
	"strconv"
)

/*
	1st approach: hashtable, wrap 2sum with one more loop
	1. sort the numbers
	2. put the numbers in a hashtable, num:index as key:value
	3. for each nums[i] + nums[j], find out the num from the hashtable that they sum up to zero
	4. use a set to deduplicate

	Time	O(nlogn+n^2+n) => O(n^2)
	Space	O(n)
	1560 ms, faster than 18.40%
*/
func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	m := make(map[int]int)
	for i, num := range nums {
		m[num] = i
	}
	triples := make(map[string][]int)
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			temp := nums[i] + nums[j]
			target := 0 - temp
			if v, x := m[target]; x {
				if v > i && v > j {
					key := strconv.Itoa(nums[i]) + "," + strconv.Itoa(nums[j]) + "," + strconv.Itoa(target)
					o := []int{nums[i], nums[j], target}
					triples[key] = o
				}
			}
		}
	}
	res := [][]int{}
	for _, v := range triples {
		res = append(res, v)
	}
	return res
}

func main() {
	fmt.Println(threeSum([]int{-1, 0, 1, 2, -1, -4}))
}
