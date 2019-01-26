package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	1st approach
	- use a hashtable to store the occurrence
	- iterate again to remove the nodes which occurence >= 2
	Time		O(2n)
	Space		O(n)
	4ms beats 100%
	26jan2019
*/
func deleteDuplicates1(head *ListNode) *ListNode {
	ht := make(map[int]int)
	dump := &ListNode{0, head}
	cur := dump.Next
	for cur != nil {
		if _, x := ht[cur.Val]; x {
			ht[cur.Val]++
		} else {
			ht[cur.Val] = 1
		}
		cur = cur.Next
	}
	cur = dump.Next
	prev := dump
	for cur != nil {
		if ht[cur.Val] > 1 {
			prev.Next = cur.Next
			cur = cur.Next
		} else {
			prev = prev.Next
			cur = cur.Next
		}
	}
	return dump.Next
}

/*
	2nd approach
	- store the prev node
	- if cur.val == cur.next.val, skip updating prev
	- set prev.next = the last duplicate node's next, be careful: dont update prev yet becos the next node might be another set of duplicate nodes
	Time		O(n)
	Space		O(1)
	4ms beats 100%
	26jan2019
*/
func deleteDuplicates(head *ListNode) *ListNode {
	dump := &ListNode{0, head}
	cur := dump.Next
	prev := dump
	dup := false
	for cur != nil {
		if cur.Next != nil && cur.Val == cur.Next.Val {
			cur = cur.Next
			dup = true
			continue
		}
		if dup == true {
			prev.Next = cur.Next
			cur = cur.Next
			dup = false
			continue
		}
		prev = prev.Next
		cur = cur.Next
	}
	return dump.Next
}

func printList(node *ListNode) {
	cur := node
	for cur != nil {
		fmt.Println(cur.Val)
		cur = cur.Next
	}
	fmt.Println("printList ended")
}

func main() {

	a := &ListNode{1, nil}
	b := &ListNode{2, nil}
	c := &ListNode{3, nil}
	d := &ListNode{3, nil}
	e := &ListNode{4, nil}
	f := &ListNode{4, nil}
	g := &ListNode{5, nil}
	a.Next = b
	b.Next = c
	c.Next = d
	d.Next = e
	e.Next = f
	f.Next = g
	s := deleteDuplicates(a)
	printList(s)

	a = &ListNode{1, nil}
	b = &ListNode{2, nil}
	c = &ListNode{3, nil}
	d = &ListNode{3, nil}
	e = &ListNode{4, nil}
	f = &ListNode{5, nil}
	a.Next = b
	b.Next = c
	c.Next = d
	d.Next = e
	e.Next = f
	s = deleteDuplicates(a)
	printList(s)

	a = &ListNode{1, nil}
	b = &ListNode{2, nil}
	c = &ListNode{3, nil}
	d = &ListNode{3, nil}
	a.Next = b
	b.Next = c
	c.Next = d
	s = deleteDuplicates(a)
	printList(s)

	c = &ListNode{3, nil}
	d = &ListNode{3, nil}
	e = &ListNode{4, nil}
	f = &ListNode{5, nil}
	c.Next = d
	d.Next = e
	e.Next = f
	s = deleteDuplicates(c)
	printList(s)
}
