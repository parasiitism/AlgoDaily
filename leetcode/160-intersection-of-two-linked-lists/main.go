package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

// naive approach: for each node in listA, search the target in listB
// O(n^2)
// not gonna implement

// better approach: hash table
// it is similar to "Find Duplicate" O(m+n) but O(m) space
// my goal here is to study linked list so im not gonna implement

/*
	best approach: linked list traversal
	O(m+n), space O(1)
	beats 94.74%
	the crux is the ending condition

	for arrays without intersection, there are 2 condition

	same length [1,2,3], [4,5,6]:
	both end the for loop becox nil == nil, and the result is p1 = nil
	p1 order 1,2,3,nil
	p2 order 4,5,6,nil

	different length [1,2,3], [4,5,6,7]:
	both end the for loop becox nil == nil, BUT they(p1,p2) travelled both linkedlists
	p1 order 1,2,3,nil,4,5,6,7,nil
	p2 order 4,5,6,7,nil,1,2,3,nil
*/

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return nil
	}
	p1, p2 := headA, headB
	for p1 != p2 {
		if p1 != nil {
			p1 = p1.Next
		} else {
			p1 = headB
		}
		if p2 != nil {
			p2 = p2.Next
		} else {
			p2 = headA
		}
	}
	if p1 != p2 {
		return nil
	}
	return p1
}

func main() {
	var a *ListNode
	var b *ListNode
	if a == b {
		fmt.Println("adad")
	} else {
		fmt.Println("5678")
	}
}
