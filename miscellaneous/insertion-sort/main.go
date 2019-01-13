package main

import "fmt"

/*
	insertion sort: https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort
	- Loop over positions in the array, starting with index 1.
	- Each new position is like the new card handed to you by the dealer,
	- and you need to insert it into the correct place in the sorted subarray to the left of that position
	Best Time			O(n)
	Average Time 	O(n^2)
	Space					O(1)
*/
func insertionSort(nums []int) {
	for i := 1; i < len(nums); i++ {
		cur := nums[i]
		for j := i - 1; j >= 0; j-- {
			if cur < nums[j] {
				nums[j+1] = nums[j]
				nums[j] = cur
			}
		}
	}
}

func insertionSort1(a []int) []int {
	for i := 1; i < len(a); i++ {
		n := a[i]
		j := i
		for j > 0 && a[j-1] > n {
			a[j] = a[j-1]
			j--
		}
		a[j] = n
	}
	return a
}

func main() {
	a := []int{64, 25, 12, 22, 11}
	insertionSort(a)
	fmt.Println(a)

	b := []int{64, 25, 12, 22, 11}
	insertionSort1(b)
	fmt.Println(b)
}
