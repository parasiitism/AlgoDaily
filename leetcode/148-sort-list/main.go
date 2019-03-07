package main

import (
	"fmt"
	"sort"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	1st approach:
	1. get all the values
	2. sort the values
	3. put sorted values into the linked list

	Time	O(nlogn)
	Space	O(n)
	12 ms, faster than 100.00%
*/
func sortList0(head *ListNode) *ListNode {
	arr := []int{}
	cur := head
	for cur != nil {
		arr = append(arr, cur.Val)
		cur = cur.Next
	}
	sort.Ints(arr)
	cur = head
	i := 0
	for cur != nil {
		cur.Val = arr[i]
		cur = cur.Next
		i++
	}
	return head
}

/*
	2nd approach
	- idea like merge sort

	preq:
	- merge sort
	- merge 2 linked lists

	Time	O(N)
	Space	O(N) result
	12 ms, faster than 100.00%
*/
func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	// divide: cut the linked list into 2 halves
	slow := head
	fast := head
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	list2 := slow.Next
	slow.Next = nil
	// sort the 2 halves
	a := sortList(head)
	b := sortList(list2)
	// conquer: merge the lists
	// since the base case is: [1], [] or [2] [1] or [2] [1], the a, b must be sorted by previous division
	return mergeTwoLists(a, b)
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	curA := l1
	curB := l2
	dump := &ListNode{0, nil}
	cur := dump
	for curA != nil && curB != nil {
		if curA.Val < curB.Val {
			cur.Next = curA
			curA = curA.Next
		} else {
			cur.Next = curB
			curB = curB.Next
		}
		cur = cur.Next
	}
	if curA != nil {
		cur.Next = curA
	}
	if curB != nil {
		cur.Next = curB
	}
	// append intermediate result to result
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
	for c != nil {
		fmt.Print(c.Val, ",")
		c = c.Next
	}
	fmt.Println("---")
}

func main() {
	a := arr2list([]int{4, 2, 3, 0, 1})
	printList(sortList(a))

	a = arr2list([]int{2, 3, 0, 1})
	printList(sortList(a))

	a = arr2list([]int{2, 3, 3, 1})
	printList(sortList(a))

	a = arr2list([]int{})
	printList(sortList(a))

	a = arr2list([]int{1})
	printList(sortList(a))
}
