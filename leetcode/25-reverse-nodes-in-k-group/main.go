package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	1st approach:
	1. count number of nodes in the front
	2. if enough nodes in the front, reverse the k nodes in the front
	3. after the k nodes reversal, do 1,2 until the end of the linkedlist

	preq:
	1. reverse linked list
	2. count linked list

	Time	O(2n) 1 for ifEnoughNodesInFront(), 1 for moving forward
	Space	O(1)
	4 ms, faster than 100.00%
*/
func reverseKGroup(head *ListNode, k int) *ListNode {
	// since we are going to change the head, we need a dump head
	dump := &ListNode{-1, head}
	// for each group with length k
	curDump := dump
	curHead := head
	i := 1
	ifEnoughFront := ifEnoughNodesInFront(curHead, k)
	for curHead != nil && curHead.Next != nil && ifEnoughFront && i < k {
		// reverse linked list
		temp := curHead.Next
		curHead.Next = curHead.Next.Next
		temp.Next = curDump.Next
		curDump.Next = temp
		i++
		// update the curDump and curHead if k nodes have been reversed
		if i == k {
			curDump = curHead
			curHead = curDump.Next
			ifEnoughFront = ifEnoughNodesInFront(curHead, k)
			i = 1
		}
	}
	return dump.Next
}

// count the linked list nodes
func ifEnoughNodesInFront(head *ListNode, k int) bool {
	i := 0
	cur := head
	for cur != nil && i < k {
		cur = cur.Next
		i++
	}
	return i == k
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
	a := arr2list([]int{1, 2, 3, 4, 5})
	// // fmt.Println(ifEnoughNodesInFront(a, 4))
	// // fmt.Println(ifEnoughNodesInFront(a, 5))
	// // fmt.Println(ifEnoughNodesInFront(a, 6))
	printList(reverseKGroup(a, 1))

	a = arr2list([]int{1, 2, 3, 4, 5})
	printList(reverseKGroup(a, 2))

	a = arr2list([]int{1, 2, 3, 4, 5})
	printList(reverseKGroup(a, 3))

	a = arr2list([]int{1, 2, 3, 4, 5})
	printList(reverseKGroup(a, 4))

	a = arr2list([]int{1, 2, 3, 4, 5})
	printList(reverseKGroup(a, 5))
}
