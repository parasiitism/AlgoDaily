package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	1st approach:
	- 2 pointers
	- one for the next
	- another one for the next.next
	- since we will change the head, we should use a dumphead

	Time	O(n)
	Space	O(1)
	0 ms, faster than 100.00%
*/
func swapPairs(head *ListNode) *ListNode {
	dump := &ListNode{0, head}
	cur := dump
	for cur.Next != nil && cur.Next.Next != nil {
		temp1 := cur.Next.Next
		cur.Next.Next = temp1.Next
		temp2 := cur.Next
		cur.Next = temp1
		temp1.Next = temp2
		cur = cur.Next.Next
	}
	return dump.Next
}

func main() {

}
