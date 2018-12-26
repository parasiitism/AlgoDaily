package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// classic solution: fast, slow pointer
// time		O(n)
// space	O(1)
// beats 100%
func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}
	fast := head.Next
	slow := head
	for fast != nil && fast.Next != nil && slow != nil {
		if fast == slow {
			return true
		}
		fast = fast.Next.Next
		slow = slow.Next
	}
	return false
}

// another approach: hash table
// time		O(n)
// space	O(n)
// beats 43.68%
func hasCycle1(head *ListNode) bool {
	hash := make(map[*ListNode]bool)
	cur := head
	for cur != nil {
		if hash[cur] == true {
			return true
		}
		hash[cur] = true
		cur = cur.Next
	}
	return false
}

func main() {

}
