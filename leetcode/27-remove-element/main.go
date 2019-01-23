package main

import "fmt"

/*
	1st approach is in js using the inplace removal(splice)

  2nd approach
  - 2 pointers
  - itereate once, if the slow pointer == val, swap the element to the rigth
  Time  O(n)
  Space O(1)
  0ms beats 100%
  23jan2019
*/
func removeElement(nums []int, val int) int {
	i := 0
	j := 0
	for j < len(nums) {
		if nums[i] != val {
			i++
		} else if nums[j] != val {
			nums[i], nums[j] = nums[j], nums[i]
			i++
		}
		j++
	}
	return i
}

func main() {
	a := []int{3, 2, 2, 3}
	fmt.Println(removeElement(a, 2))
	fmt.Println(a)

	a = []int{0, 1, 2, 2, 3, 0, 4, 2}
	fmt.Println(removeElement(a, 2))
	fmt.Println(a)
}
