package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

// naive solution
// just put the items into an array and check
// time		O(2n)
// space	O(n)
// beats 100%
func isPalindrome(head *ListNode) bool {
	if head == nil {
		return false
	}
	arr := []int{}
	cur := head
	for cur != nil {
		arr = append(arr, cur.Val)
		cur = cur.Next
	}
	cur = head
	i := len(arr) - 1
	for cur != nil {
		if cur.Val != arr[i] {
			return false
		}
		cur = cur.Next
		i--
	}
	return true
}

func printList(l *ListNode) {
	c := l
	for c != nil {
		fmt.Println(c.Val)
		c = c.Next
	}
}

func main() {
	a := &ListNode{1, nil}
	b := &ListNode{2, nil}
	c := &ListNode{3, nil}
	d := &ListNode{3, nil}
	e := &ListNode{2, nil}
	f := &ListNode{1, nil}
	a.Next = b
	b.Next = c
	c.Next = d
	d.Next = e
	e.Next = f
	fmt.Println(isPalindrome(a))
}
