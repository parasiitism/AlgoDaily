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
	Questions to ask:
	- emppty list?
	- list of nil head?
	- duplicate values?
*/

/*
	0th approach: naive way
	- iterate the list and put all the values into an array
	- sort the array
	- make that array into a linked list
	Time	O(NlogN) N=n*k
	Space	O(N)
	12ms beats 91.67%
*/
func mergeKLists0(lists []*ListNode) *ListNode {
	a := []int{}
	for i := 0; i < len(lists); i++ {
		cur := lists[i]
		for cur != nil {
			a = append(a, cur.Val)
			cur = cur.Next
		}
	}
	sort.Ints(a)
	dumpHead := &ListNode{0, nil}
	cur := dumpHead
	for i := 0; i < len(a); i++ {
		cur.Next = &ListNode{a[i], nil}
		cur = cur.Next
	}
	return dumpHead.Next
}

/*
	1st approach
	- idea like merge sort
	Time	O(N)
	Space	O(N)
	96 ms, faster than 36.89%
*/
func mergeKLists(lists []*ListNode) *ListNode {
	res := &ListNode{0, nil}
	for i := 0; i < len(lists); i++ {
		// merge like merge sort
		curA := lists[i]
		curB := res.Next
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
		res.Next = dump.Next
	}
	return res.Next
}

/*
	2nd approach: reuse the sorted 2 lists

	100 ms, faster than 35.66%
*/
func mergeKLists1(lists []*ListNode) *ListNode {
	dump := &ListNode{0, nil}
	for i := 0; i < len(lists); i++ {
		temp := mergeTwoLists(dump.Next, lists[i])
		dump.Next = temp
	}
	return dump.Next
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

func printList(node *ListNode) {
	cur := node
	for cur != nil {
		fmt.Println(cur.Val)
		cur = cur.Next
	}
}

func main() {
	one := &ListNode{1, nil}
	five := &ListNode{5, nil}
	nine := &ListNode{9, nil}
	one.Next = five
	five.Next = nine

	two := &ListNode{2, nil}
	four := &ListNode{4, nil}
	two.Next = four

	three := &ListNode{3, nil}
	six := &ListNode{6, nil}
	three.Next = six

	m := mergeKLists([]*ListNode{one, two, three})
	printList(m)
}
