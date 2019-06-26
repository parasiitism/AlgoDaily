package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	navie solution
	put the items into even and odd arrays
	concat them together
	time		O(n)
	space	O(n)
	beats 100% (LOL the speed is the same with the classic approach)
*/
func oddEvenList(head *ListNode) *ListNode {
	odd := []*ListNode{}
	even := []*ListNode{}
	cnt := 1
	cur := head
	for cur != nil {
		if cnt%2 == 0 {
			even = append(even, cur)
		} else {
			odd = append(odd, cur)
		}
		cur = cur.Next
		cnt++
	}
	concat := append(odd, even...)

	dump := &ListNode{0, nil}
	cur = dump
	for i := 0; i < len(concat); i++ {
		cur.Next = concat[i]
		cur = cur.Next
	}
	cur.Next = nil
	return dump.Next
}

// classic solution: inplace
// ./idea.png
// time		O(n)
// space	O(1)
func oddEvenList1(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	result := head
	odd := head
	dump := &ListNode{0, head}
	even := dump
	var oddTail *ListNode
	for odd != nil {
		temp := odd.Next
		if temp != nil {
			odd.Next = odd.Next.Next
		}
		even.Next = temp
		if odd.Next == nil {
			oddTail = odd
		}
		odd = odd.Next
		even = even.Next
	}
	oddTail.Next = dump.Next
	return result
}

func _printList(l *ListNode) {
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
	d := &ListNode{4, nil}
	e := &ListNode{5, nil}
	// f := &ListNode{6, nil}
	a.Next = b
	b.Next = c
	c.Next = d
	d.Next = e
	// e.Next = f
	_printList(oddEvenList1(a))
}
