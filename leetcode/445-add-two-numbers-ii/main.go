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
	naive approaches:
	1. translate to numbers, add them, and put the result into a linked list
	2. reverse the linked list, add them like leetcode 2), reverse the result so the most significant digit comes first
*/

/*
	1st approach: 2 stacks
	1. put the values into its corresponding stack
	2. pop the stacks, and sum up the numbers with carry
	3. if there is a carry, add 1

	Time	O(2m+2n)
	Space	O(m+n)
	16 ms, faster than 100.00%
*/
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// put the values into its corresponding stack
	stack1 := []int{}
	stack2 := []int{}
	cur1 := l1
	cur2 := l2
	for cur1 != nil {
		stack1 = append(stack1, cur1.Val)
		cur1 = cur1.Next
	}
	for cur2 != nil {
		stack2 = append(stack2, cur2.Val)
		cur2 = cur2.Next
	}
	// pop the stacks, and sum up the numbers with carry
	dump := &ListNode{-1, nil}
	carry := 0
	for len(stack1) > 0 || len(stack2) > 0 {
		v1 := 0
		if len(stack1) > 0 {
			v1 = stack1[len(stack1)-1]
			stack1 = stack1[:len(stack1)-1]
		}
		v2 := 0
		if len(stack2) > 0 {
			v2 = stack2[len(stack2)-1]
			stack2 = stack2[:len(stack2)-1]
		}
		x := v1 + v2 + carry
		carry = x / 10
		temp := dump.Next
		dump.Next = &ListNode{x % 10, nil}
		dump.Next.Next = temp
	}
	// if there is a carry, add 1
	if carry > 0 {
		temp := dump.Next
		dump.Next = &ListNode{1, nil}
		dump.Next.Next = temp
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
	c := addTwoNumbers(a, b)
	printList(c)

	a = &ListNode{7, &ListNode{2, &ListNode{4, &ListNode{3, nil}}}}
	b = &ListNode{5, &ListNode{6, &ListNode{4, nil}}}
	c = addTwoNumbers(a, b)
	printList(c)
}
