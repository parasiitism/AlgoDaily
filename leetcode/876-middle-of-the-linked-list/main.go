package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func middleNode(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	slow := head
	fast := head
	for fast != nil {
		if fast.Next != nil {
			slow = slow.Next
			fast = fast.Next.Next
		} else {
			break
		}
	}
	return slow
}

func main() {

}
