package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// naive approach
// iterate once for the length
// iterate one more time to remove the target node
// beats 100%
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	cnt := 0
	cur := head
	for cur != nil {
		cnt++
		cur = cur.Next
	}
	targetIdx := cnt - n
	dump := &ListNode{0, head}
	prev := dump
	cur = head
	cnt = 0
	for cur != nil {
		if targetIdx == cnt {
			prev.Next = cur.Next
			break
		}
		cnt++
		prev = prev.Next
		cur = cur.Next
	}
	return dump.Next
}

func main() {}
