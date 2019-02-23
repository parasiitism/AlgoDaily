package main

import (
	"fmt"
	"sort"
	"strconv"
)

/*
	questions to ask:
	- any duplicate numbers? yes
	- so if [0,0,0,0], expect [[0,0,0]] but not [[0,0,0],[0,0,0]], indeces[[0,1,2][1,2,3]]? yes
	- the numbers are not sorted? yes
*/

/*
	1st approach: hashtable, wrap 2sum with one more loop
	1. sort the numbers to make sure that the key will be unique
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

/*
	2nd approach: 2 pointers
	1. sort the numbers to make sure that the key will be unique
	2. for each num[i], use 2 pointers, from the front and from the end, to find the pairs which nums[i]+nums[j]+nums[k] sum up to 0
	3. use a set to deduplicate

	Time	O(n^2)
	Space	O(n)
	1156 ms, faster than 27.88%
*/
func threeSum1(nums []int) [][]int {
	sort.Ints(nums)
	triples := make(map[string][]int)
	for i := 0; i < len(nums); i++ {
		j := i + 1
		k := len(nums) - 1
		for j < k {
			temp := nums[i] + nums[j] + nums[k]
			if temp == 0 {
				key := strconv.Itoa(nums[i]) + "," + strconv.Itoa(nums[j]) + "," + strconv.Itoa(nums[k])
				o := []int{nums[i], nums[j], nums[k]}
				triples[key] = o
				j++
				k--
			} else if temp < 0 {
				j++
			} else {
				k--
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
	fmt.Println(threeSum1([]int{-1, 0, 1, 2, -1, -4}))
	fmt.Println(threeSum1([]int{-2, 0, 1, 1, 2}))
}
