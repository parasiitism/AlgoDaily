package main

import "fmt"

/*
	2nd approach
	- brute force
	92ms beats 46.15%
	Time of Constructor O(1)
	Space of Constructor O(n)
	Time of SumRange O(n)
	Space of SumRange O(1)
*/
type NumArray struct {
	Arr []int
}

func Constructor(nums []int) NumArray {
	return NumArray{nums}
}

func (this *NumArray) SumRange(i int, j int) int {
	result := 0
	for k := i; k <= j; k++ {
		result += this.Arr[k]
	}
	return result
}

/*
	2nd approach
	- for earch item in the array, cache the sum from start
	Time of Constructor O(n)
	Space of Constructor O(n)
	Time of SumRange O(1)
	Space of SumRange O(1)
	44ms beats 100%
*/
type NumArray1 struct {
	Arr []int
}

func Constructor1(nums []int) NumArray1 {
	arr := []int{}
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
		arr = append(arr, sum)
	}
	return NumArray1{arr}
}

func (this *NumArray1) SumRange(i int, j int) int {
	if i > j {
		return 0
	} else if i == 0 {
		return this.Arr[j]
	}
	return this.Arr[j] - this.Arr[i-1]
}

func main() {
	c := Constructor([]int{-2, 0, 3, -5, 2, -1})
	fmt.Println(c.SumRange(0, 2))
	fmt.Println(c.SumRange(2, 5))
	fmt.Println(c.SumRange(0, 5))

	c1 := Constructor1([]int{-2, 0, 3, -5, 2, -1})
	fmt.Println(c1.SumRange(0, 2))
	fmt.Println(c1.SumRange(2, 5))
	fmt.Println(c1.SumRange(0, 5))
}
