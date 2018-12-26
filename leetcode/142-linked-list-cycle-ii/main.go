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

func main() {

}
