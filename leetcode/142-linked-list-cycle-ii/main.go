package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// easy way: hashtable
// time		O(n)
// space 	O(n)
// beats 44.44%
func detectCycle(head *ListNode) *ListNode {
	hash := make(map[*ListNode]bool)
	cur := head
	for cur != nil {
		if hash[cur] == true {
			return cur
		}
		hash[cur] = true
		cur = cur.Next
	}
	return nil
}

// classic approach
// 1. check if there is a cycle
// 2. slow pointer => a+b+c+b= 2(a+b) <= fast pointer
// 													a=c
// see ./idea.jpeg
// time 	O(n)
// space	O(1)
// beats 100%
func detectCycle1(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	fast := head.Next
	slow := head
	for fast != nil && fast.Next != nil && slow != nil {
		if fast == slow {
			break
		}
		fast = fast.Next.Next
		slow = slow.Next
	}
	// no cycle
	if fast != slow {
		return nil
	}
	slow = head
	fast = head.Next
	for slow != fast {
		slow = slow.Next
		fast = fast.Next
	}
	return slow // fast
}

func main() {

}
