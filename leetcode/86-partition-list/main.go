package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	2nd approach:
	- create 2 linked lists: 1 for nodes less than target, 1 for nodes >= target
	- put the nodes into the corresponding lists while we traversing the input
	- combine the 2 linked lists and return the result

	Time    O(n)
	Space   O(1)
	0 ms, faster than 100.00%
*/
func partition(head *ListNode, x int) *ListNode {
	dumpLess := &ListNode{0, nil}
	dumpMore := &ListNode{0, nil}
	curLess := dumpLess
	curMore := dumpMore
	cur := head
	for cur != nil {
		if cur.Val < x {
			curLess.Next = cur
			curLess = curLess.Next
		} else {
			curMore.Next = cur
			curMore = curMore.Next
		}
		cur = cur.Next
	}
	/*
		very important:
		since, after the traversal, curMore.next points to the curLess node
		we should set the next to null to avoid creating a cyclar linked list
		e.g. [1,4,3,2]
		dumpLess -> 1,2
		dumpMore -> 4,3,2
	*/
	curMore.Next = nil
	curLess.Next = dumpMore.Next
	return dumpLess.Next
}

func main() {

}
