package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// naive approach
// iterate once for the length
// iterate one more time to remove the target node
// time 	O(2n)
// space 	O(1)
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

// another naive approach
// put the items into an array, and remove the target
// time 	O(n)
// space 	O(n)
// beats 19.39%
func removeNthFromEnd1(head *ListNode, n int) *ListNode {
	dump := &ListNode{0, head}
	arr := []*ListNode{dump}
	cur := head
	for cur != nil {
		arr = append(arr, cur)
		cur = cur.Next
	}
	targetIdx := len(arr) - n + 1
	arr[targetIdx-1].Next = arr[targetIdx].Next
	return dump
}

// classic approach
// 2 pointers: the gap is the n such that when fast reaches to the end, slow.next is the target
// time		O(n+target)
// space 	O(1)
// baets 19.39% i dont get it LOL
func removeNthFromEnd2(head *ListNode, n int) *ListNode {
	dump := &ListNode{0, head}
	fast := dump
	slow := dump
	for i := 0; i < n+1; i++ {
		fast = fast.Next
	}
	for fast != nil {
		slow = slow.Next
		fast = fast.Next
	}
	slow.Next = slow.Next.Next
	return dump.Next
}

func main() {}
