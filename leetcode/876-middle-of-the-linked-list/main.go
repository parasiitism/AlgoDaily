package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	Questions to ask:
	- empty?
	- if one element, return what?
	- if two element, return what?
*/

/*
	navie approach
	- iterate once for finding the length
	- iterate again for stopping at length/2
	Time 	O(2n)
	Space O(1)
	not gonna implement
*/

/*
	classic approach
	- 2 pointers
	Time 	O(n)
	Space O(1)
	0ms beats 100%
	26jan2019
*/
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
