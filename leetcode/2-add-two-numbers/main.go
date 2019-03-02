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
	questions to ask:
	- will there be numbers larger than 9 for item node item? yes
	- the input linked lists are with different size? yes
*/

/*
	1st approach: similar to the merge part of merge sort

	Time	O(l+r)
	Space	O(l+r) the result
	12ms beats 100%
*/
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dump := &ListNode{-1, nil}
	carry := 0
	cur1 := l1
	cur2 := l2
	cur := dump
	// append left and right if both are not null
	for cur1 != nil && cur2 != nil {
		val1 := cur1.Val
		val2 := cur2.Val
		sum := val1 + val2 + carry
		var newNode *ListNode
		if sum > 9 {
			newNode = &ListNode{sum % 10, nil}
			carry = 1
		} else {
			newNode = &ListNode{sum, nil}
			carry = 0
		}
		cur.Next = newNode
		cur = cur.Next
		cur1 = cur1.Next
		cur2 = cur2.Next
	}
	// apend left if not null
	for cur1 != nil {
		sum := cur1.Val + carry
		var newNode *ListNode
		if sum > 9 {
			newNode = &ListNode{sum % 10, nil}
			carry = 1
		} else {
			newNode = &ListNode{sum, nil}
			carry = 0
		}
		cur.Next = newNode
		cur = cur.Next
		cur1 = cur1.Next
	}
	// apend right if not null
	for cur2 != nil {
		sum := cur2.Val + carry
		var newNode *ListNode
		if sum > 9 {
			newNode = &ListNode{sum % 10, nil}
			carry = 1
		} else {
			newNode = &ListNode{sum, nil}
			carry = 0
		}
		cur.Next = newNode
		cur = cur.Next
		cur2 = cur2.Next
	}
	// if there is a carry, add 1
	if carry > 0 {
		cur.Next = &ListNode{1, nil}
	}
	return dump.Next
}

/*
	2nd approach: same idea as 1st approach but shorter

	Time	O(l+r)
	Space	O(l+r) the result
	12ms beats 100%
*/
func addTwoNumbers1(l1 *ListNode, l2 *ListNode) *ListNode {
	dump := &ListNode{-1, nil}
	carry := 0
	cur1 := l1
	cur2 := l2
	cur := dump
	// append left and right if both are not null
	for cur1 != nil || cur2 != nil {
		val1 := 0
		if cur1 != nil {
			val1 = cur1.Val
		}
		val2 := 0
		if cur2 != nil {
			val2 = cur2.Val
		}
		sum := val1 + val2 + carry
		newNode := &ListNode{sum % 10, nil}
		carry = sum / 10
		cur.Next = newNode
		cur = cur.Next
		if cur1 != nil {
			cur1 = cur1.Next
		}
		if cur2 != nil {
			cur2 = cur2.Next
		}
	}
	// if there is a carry, add 1
	if carry > 0 {
		cur.Next = &ListNode{1, nil}
	}
	return dump.Next
}

// helper
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
	a := &ListNode{9, &ListNode{9, &ListNode{9, nil}}}
	b := &ListNode{9, &ListNode{9, &ListNode{9, nil}}}
	c := addTwoNumbers1(a, b)
	printList(c)
}
