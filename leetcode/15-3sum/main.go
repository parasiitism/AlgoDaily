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

/*
	3rd approach: optimize the 2nd approach and dont use the hashtable to deduplicate
	- https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution

	Time	O(n^2)
	Space O(n) <-result array
	932 ms, faster than 64.31%
*/
func threeSum2(nums []int) [][]int {
	sort.Ints(nums)
	res := [][]int{}
	for i := 0; i < len(nums); i++ {
		// deduplicate:
		// dont do 2sum if the current num == last num
		// but dont skip when index == 0, cos nums[i-1] will be out of boundary
		if i == 0 || nums[i] > nums[i-1] {
			j := i + 1
			k := len(nums) - 1
			for j < k {
				temp := nums[i] + nums[j] + nums[k]
				if temp == 0 {
					o := []int{nums[i], nums[j], nums[k]}
					res = append(res, o)
					// deduplicate:
					// imagine [1,1,2,3,4,4], target 5
					// we need to skip the 1(index 1) and 4(index 4) and check if 2+3 = 5
					for j < k && nums[j] == nums[j+1] {
						j++
					}
					for j < k && nums[k-1] == nums[k] {
						k--
					}
					j++
					k--
				} else if temp < 0 {
					j++
				} else {
					k--
				}
			}
		}
	}
	return res
}

func main() {
	fmt.Println(threeSum1([]int{-1, 0, 1, 2, -1, -4}))
	fmt.Println(threeSum1([]int{-2, 0, 1, 1, 2}))
	fmt.Println(threeSum1([]int{-13, 5, 13, 12, -2, -11, -1, 12, -3, 0, -3, -7, -7, -5, -3, -15, -2, 14, 14, 13, 6, -11, -11, 5, -15, -14, 5, -5, -2, 0, 3, -8, -10, -7, 11, -5, -10, -5, -7, -6, 2, 5, 3, 2, 7, 7, 3, -10, -2, 2, -12, -11, -1, 14, 10, -9, -15, -8, -7, -9, 7, 3, -2, 5, 11, -13, -15, 8, -3, -7, -12, 7, 5, -2, -6, -3, -10, 4, 2, -5, 14, -3, -1, -10, -3, -14, -4, -3, -7, -4, 3, 8, 14, 9, -2, 10, 11, -10, -4, -15, -9, -1, -1, 3, 4, 1, 8, 1}))
}
