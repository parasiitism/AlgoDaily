package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// classic solution
// time		O(n)
// space 	O(1)
// beats 20% (i think leetcode has a problem in computing the time)
func removeElements(head *ListNode, val int) *ListNode {
	dump := &ListNode{0, head}
	cur := dump
	for cur.Next != nil {
		if cur.Next.Val == val {
			cur.Next = cur.Next.Next
		} else {
			cur = cur.Next
		}
	}
	return dump.Next
}

func main() {

}
