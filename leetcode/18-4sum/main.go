package main

import (
	"fmt"
	"sort"
	"strconv"
)

/*
	questions to ask:
	- any duplicate numbers? yes
	- so if [0,0,0,0,0], expect [[0,0,0,0]] but not [[0,0,0,0],[0,0,0,0]], indeces[[0,1,2,3][1,2,3,4]]? yes
	- the numbers are not sorted? yes
*/

/*
	1st approach: hashtable, wrap 3sum with one more loop
	1. sort the numbers to make sure that the key will be unique
	2. put the numbers in a hashtable, num:index as key:value
	3. for each nums[i] + nums[j] + nums[k], find out the num from the hashtable that they sum up to zero
	4. use a set to deduplicate

	Time	O(n^3)
	Space	O(n)
	84 ms, faster than 15.45%
*/
func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)
	m := make(map[int]int)
	for i, num := range nums {
		m[num] = i
	}
	triples := make(map[string][]int)
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			for k := j + 1; k < len(nums); k++ {
				temp := nums[i] + nums[j] + nums[k]
				want := target - temp
				if v, x := m[want]; x {
					if v > i && v > j && v > k {
						key := strconv.Itoa(nums[i]) + "," + strconv.Itoa(nums[j]) + "," + strconv.Itoa(nums[k]) + "," + strconv.Itoa(want)
						o := []int{nums[i], nums[j], nums[k], want}
						triples[key] = o
					}
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
	fmt.Println(fourSum([]int{1, 0, -1, 0, -2, 2}, 0))
	fmt.Println(fourSum([]int{-3, -1, 0, 2, 4, 5}, 2))
}
