package main

import (
	"fmt"
	"strconv"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, m int, n int) *ListNode {
	if head == nil {
		return nil
	}
	// find the parent of node[m]
	dump := &ListNode{0, head}
	i := 1
	parent := dump
	for i < m && parent != nil {
		i++
		parent = parent.Next
	}
	// reverse the linked list until n
	targetHead := parent.Next
	cur := targetHead
	for i < n && targetHead.Next != nil {
		temp := targetHead.Next
		targetHead.Next = targetHead.Next.Next
		temp.Next = cur
		cur = temp
		i++
	}
	parent.Next = cur
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
	b := reverseBetween(a, 0, 0)
	printList(b)

	a = arr2list([]int{1})
	b = reverseBetween(a, 1, 1)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5})
	b = reverseBetween(a, 2, 4)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5})
	b = reverseBetween(a, 2, 5)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5})
	b = reverseBetween(a, 1, 4)
	printList(b)

	a = arr2list([]int{1, 2, 3, 4, 5})
	b = reverseBetween(a, 1, 5)
	printList(b)
}
