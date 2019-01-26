package main

import "sort"

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	0th approach: naive way
	- iterate the list and put all the values into an array
	- sort the array
	- make that array into a linked list
	Time	O(NlogN) N=len(l1)+len(l2)
	Space	O(N)
	4ms beats 100%
*/
func mergeTwoLists0(l1 *ListNode, l2 *ListNode) *ListNode {
	a := []int{}
	cur := l1
	for cur != nil {
		a = append(a, cur.Val)
		cur = cur.Next
	}
	cur = l2
	for cur != nil {
		a = append(a, cur.Val)
		cur = cur.Next
	}
	sort.Ints(a)
	dumpHead := &ListNode{0, nil}
	cur = dumpHead
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
	4ms beats 100%
*/
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
	for curA != nil {
		cur.Next = curA
		curA = curA.Next
		cur = cur.Next
	}
	for curB != nil {
		cur.Next = curB
		curB = curB.Next
		cur = cur.Next
	}
	// append intermediate result to result
	return dump.Next
}

func main() {

}
