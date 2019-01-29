package main

import (
	"fmt"
	"strconv"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseSecondHalf(head *ListNode) *ListNode {
	dump := &ListNode{0, head}
	slow := dump
	fast := head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	slow.Next = reverseList(slow.Next)
	return head
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	dump := &ListNode{-1, nil}
	dump.Next = head
	striker := head.Next
	for striker != nil {
		temp := dump.Next
		dump.Next = striker
		head.Next = striker.Next
		striker.Next = temp
		striker = head.Next
	}
	return dump.Next
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
	a := arr2list([]int{})
	b := reverseSecondHalf(a)
	printList(b)

	a = arr2list([]int{1})
	b = reverseSecondHalf(a)
	printList(b)

	a = arr2list([]int{1, 2})
	b = reverseSecondHalf(a)
	printList(b)

	a = arr2list([]int{1, 2, 3})
	b = reverseSecondHalf(a)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5})
	b = reverseSecondHalf(a)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5, 6})
	b = reverseSecondHalf(a)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
	b = reverseSecondHalf(a)
	printList(b)
}
