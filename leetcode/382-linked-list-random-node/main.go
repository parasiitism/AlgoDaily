package main

import (
	"math/rand"
	"time"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	1st approach: naively put all the numbers into an array

	Time		O(n) constructor, O(1) pick
	Space		O(n)
	168 ms, faster than 9.09%
*/

type Solution struct {
	Nums []int
}

/** @param head The linked list's head.
Note that the head is guaranteed to be not null, so it contains at least one node. */
func Constructor(head *ListNode) Solution {
	nums := []int{}
	cur := head
	for cur != nil {
		nums = append(nums, cur.Val)
		cur = cur.Next
	}
	return Solution{nums}
}

/** Returns a random node's value. */
func (this *Solution) GetRandom() int {
	rand.Seed(time.Now().UTC().UnixNano())
	temp := rand.Intn(len(this.Nums))
	return this.Nums[temp]
}

func main() {

}
