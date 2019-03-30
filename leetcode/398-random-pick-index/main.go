package main

import (
	"fmt"
	"math/rand"
	"sort"
	"time"
)

type Item struct {
	num int
	idx int
}

type Solution struct {
	items []Item
}

func Constructor(nums []int) Solution {
	items := []Item{}
	// trasform to Item
	for i, num := range nums {
		items = append(items, Item{num, i})
	}
	// sort
	sort.Slice(items, func(i, j int) bool {
		return items[i].num < items[j].num
	})
	return Solution{items}
}

func (this *Solution) Pick(target int) int {
	rand.Seed(time.Now().UTC().UnixNano())
	left := lowerBoundBinarySearch(this.items, target)
	right := lowerBoundBinarySearch(this.items, target+1)
	if left > len(this.items)-1 || this.items[left].num != target {
		return -1
	}
	diff := right - left
	temp := rand.Intn(diff)
	return this.items[left+temp].idx
}

func lowerBoundBinarySearch(arr []Item, target int) int {
	min := 0
	max := len(arr)
	for min < max {
		mean := (min + max) / 2
		if target <= arr[mean].num {
			max = mean
		} else {
			min = mean + 1
		}
	}
	return min
}

func main() {
	c := Constructor([]int{1, 2, 3, 3, 3, 4, 5, 3})
	fmt.Println("----- multiple should return 2,3,4,7-----")
	fmt.Println(c.Pick(3))
	fmt.Println("----- single -----")
	fmt.Println(c.Pick(1))
	fmt.Println(c.Pick(2))
	fmt.Println(c.Pick(4))
	fmt.Println(c.Pick(5))
	fmt.Println("-----cout of boundaries -----")
	fmt.Println(c.Pick(0))
	fmt.Println(c.Pick(6))
}
