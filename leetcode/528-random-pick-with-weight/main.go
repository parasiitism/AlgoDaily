package main

import (
	"fmt"
	"math/rand"
	"time"
)

/*
	1st approach: smaller or equal binary search
	e.g. [2,4,6,8]
	search 3, return index 0
	search 5, return index 1
	search 6, return index 1

	Time	O(logn)
	Space	O(n)
	668 ms, faster than 9.09%
*/
type Solution struct {
	Indeces []int
	Count   int
}

func Constructor(w []int) Solution {
	indeces := []int{}
	count := 0
	for _, weight := range w {
		indeces = append(indeces, count)
		count += weight
	}
	return Solution{indeces, count}
}

func (this *Solution) PickIndex() int {
	rand.Seed(time.Now().UTC().UnixNano())
	temp := rand.Intn(this.Count)
	return equalOrLessThanBinarySearch(this.Indeces, temp)
}

func equalOrLessThanBinarySearch(arr []int, target int) int {
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
	return max
}

func main() {
	a := []int{2, 4, 6, 8}
	fmt.Println(equalOrLessThanBinarySearch(a, 2))
	fmt.Println(equalOrLessThanBinarySearch(a, 3))
}
