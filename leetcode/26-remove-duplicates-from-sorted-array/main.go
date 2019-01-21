package main

import "fmt"

/*
	Questions to ask:
	- all positive?
	- all < 10?
*/

/*
  1st approach:
  - there is no in-place pop/slice in golang, i can only shift the array item by item
  - return unique items
  Time    O(n^2)
  Space   O(1)
  220ms beats 2.04%
  21jan2019
*/
func removeDuplicates1(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	cur := nums[0]
	cnt := 1
	i := 1
	total := 1
	for total < len(nums) {
		if nums[i] == cur {
			// shift to the left
			for k := i; k < len(nums); k++ {
				if k+1 == len(nums) {
					nums[k] = 0
				} else {
					nums[k] = nums[k+1]
				}
			}
		} else {
			cur = nums[i]
			i++
			cnt++
		}
		total++
	}
	return cnt
}

/*
  2nd approach:
	- 2 pointers
	- it is too slow to shift all the items, just replace the arr[slow] with arr[fast]
  - return slow
  Time    O(n)
  Space   O(1)
  60ms beats 100%
  21jan2019
*/
func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	slow := 0
	for fast := 1; fast < len(nums); fast++ {
		if nums[fast] != nums[slow] {
			slow++
			nums[slow] = nums[fast]
		}
	}
	return slow + 1
}

func main() {
	a := []int{}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{1}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{1, 1}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{1, 2}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{1, 1, 2}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{1, 2, 2}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{0, 0, 0, 1, 1, 1, 1}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)

	a = []int{0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4}
	fmt.Println(removeDuplicates(a))
	fmt.Println(a)
}
