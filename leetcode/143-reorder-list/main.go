package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	1st approach: stack
	1. put the nodes' clone in a stack
	2. count the total number of nodes
	3. traverse again the linked list and add the pop item between current node and the next node
	4. count += 2
	5. do it until we reach to the total

	Time	O(2n)
	Space	O(n)
	20 ms, faster than 12.86%
*/
func reorderList(head *ListNode) {
	if head == nil {
		return
	}
	// copy the nodes to a stack
	total := 0
	cur := head
	stack := []*ListNode{}
	for cur != nil {
		stack = append(stack, &ListNode{cur.Val, nil})
		cur = cur.Next
		total++
	}
	// insert the pop item from stack between the current node and the next node
	count := 1
	cur = head
	for count+1 < total {
		temp := cur.Next
		cur.Next = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		cur.Next.Next = temp
		cur = temp
		count += 2
	}
	// set the cur.next to nil
	if count == total {
		cur.Next = nil
	} else if cur.Next != nil {
		cur.Next.Next = nil
	}
}

/*
	1st approach: stack
	1. find the half point
	2. reverse the 2nd half
	3. merge 2 lists

	Time	O(3n)
	Space	O(1)
	8 ms, faster than 100.00%
*/
func reorderList1(head *ListNode) {
	if head == nil {
		return
	}
	// find the half point
	var parent *ListNode
	a := head
	b := head
	for b != nil && b.Next != nil {
		parent = a
		a = a.Next
		b = b.Next.Next
	}
	if parent == nil {
		return
	}
	parent.Next = nil
	// reverse the 2nd half
	reversed2nd := reverseList(a)
	// merge 2 lists
	merge2nd(head, reversed2nd)
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	cur := head
	for head.Next != nil { // since we are replacing the head.next, the loop should end when there is no next
		temp := head.Next          // the middle node
		head.Next = head.Next.Next // or head.Next.Next
		temp.Next = cur            // put the middle node in front of cur
		cur = temp                 // assign cur as head
	}
	return cur
}

func merge2nd(a *ListNode, b *ListNode) {
	curA := a
	curB := b
	for curA != nil {
		nextA := curA.Next
		nextB := curB.Next

		curA.Next = curB
		// since len(a) <= len(b)
		if nextA == nil {
			break
		}
		curB.Next = nextA

		curA = nextA
		curB = nextB
	}
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
	reorderList(a)
	printList(a)

	a = arr2list([]int{1, 2, 3, 4, 5, 6})
	reorderList(a)
	printList(a)

	a = arr2list([]int{1})
	reorderList(a)
	printList(a)

	a = arr2list([]int{1, 2})
	reorderList(a)
	printList(a)

	a = arr2list([]int{1, 2, 3})
	reorderList(a)
	printList(a)

	fmt.Println("----------------------------------------")

	a = arr2list([]int{1, 2, 3, 4, 5})
	reorderList1(a)
	printList(a)

	a = arr2list([]int{1, 2, 3, 4, 5, 6})
	reorderList1(a)
	printList(a)

	a = arr2list([]int{1})
	reorderList1(a)
	printList(a)

	a = arr2list([]int{1, 2})
	reorderList1(a)
	printList(a)

	a = arr2list([]int{1, 2, 3})
	reorderList1(a)
	printList(a)
}
