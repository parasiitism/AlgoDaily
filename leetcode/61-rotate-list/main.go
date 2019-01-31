package main

import (
	"fmt"
	"strconv"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	1st approach(standard approach)
	1. form a cyclic linked list
	2. find the target head and the target tail
	3. return the target head
	Time	O(n)
	Space	O(2n)
	4ms beats 100%
*/
func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return nil
	}
	// find length and tail of the list
	tail := head
	cnt := 1 // be careful
	for tail.Next != nil {
		tail = tail.Next
		cnt++
	}
	// form a cyclic linked list
	tail.Next = head
	// find target head
	targetHead := head
	i := 0
	k = k % cnt
	for i < cnt-k {
		targetHead = targetHead.Next
		i++
	}
	// find target tail
	j := 1
	targetTail := targetHead
	for j < cnt {
		targetTail = targetTail.Next
		j++
	}
	// remove the tail.next(unlink the cyclic list)
	targetTail.Next = nil

	return targetHead
}

// helpers
func arr2list(arr []int) *ListNode {
	dump := &ListNode{0, nil}
	dumpCur := dump
	for i := 0; i < len(arr); i++ {
		dumpCur.Next = &ListNode{arr[i], nil}
		dumpCur = dumpCur.Next
	}
	return dump.Next
}

func printList(l *ListNode) {
	c := l
	s := ""
	for c != nil {
		s += strconv.Itoa(c.Val) + ","
		c = c.Next
	}
	fmt.Println(s)
}

func main() {

	a := arr2list([]int{1, 2, 3, 4, 5, 6})
	b := rotateRight(a, 0)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5, 6})
	b = rotateRight(a, 2)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5, 6})
	b = rotateRight(a, 5)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5, 6})
	b = rotateRight(a, 6)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5, 6})
	b = rotateRight(a, 7)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5, 6})
	b = rotateRight(a, 8)
	printList(b)

	a = arr2list([]int{})
	b = rotateRight(a, 8)
	printList(b)

	a = arr2list([]int{1})
	b = rotateRight(a, 8)
	printList(b)

	a = arr2list([]int{1, 2})
	b = rotateRight(a, 7)
	printList(b)
}
