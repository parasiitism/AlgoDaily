package main

import "fmt"

/*
	1st approach:
  - there is no in-place pop/slice in golang, i can only shift the array item by item
  - return unique items
  Time    O(n^2)
  Space   O(n) hashtable
  8ms beats 100%
  21jan2019
*/
func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	hash := map[int]int{}
	hash[nums[0]] = 1
	cnt := 1
	i := 1
	total := 1
	for total < len(nums) {
		num := nums[i]
		if v, x := hash[num]; x {
			if v < 2 {
				hash[num] = hash[num] + 1
				i++
				cnt++
			} else {
				// shift to the left
				for k := i; k < len(nums); k++ {
					if k+1 == len(nums) {
						nums[k] = 0
					} else {
						nums[k] = nums[k+1]
					}
				}
			}
		} else {
			hash[num] = 1
			i++
			cnt++
		}
		total++
	}
	return cnt
}

func main() {
	a := []int{1, 1, 1, 2, 2, 3}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{0, 0, 0, 1, 1, 1, 1}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{0, 0, 1, 1, 1, 1, 2, 3, 3}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{1, 2, 3, 4, 5}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)
}
