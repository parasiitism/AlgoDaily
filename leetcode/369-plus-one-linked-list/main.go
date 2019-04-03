package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
	1st approach: stack

	Time		O(2n)
	Space		O(n)
	0 ms, faster than 100.00%
*/
func plusOne(head *ListNode) *ListNode {
	stack := []*ListNode{}
	cur := head
	for cur != nil {
		stack = append(stack, cur)
		cur = cur.Next
	}

	carry := 1
	for i := len(stack) - 1; i >= 0; i-- {
		num := stack[i].Val + carry
		if num == 10 {
			stack[i].Val = 0
		} else {
			stack[i].Val = num
			carry = 0
		}
	}
	if carry == 1 {
		return &ListNode{1, head}
	}
	return head
}

/*
	2nd approach:
	1. reverse
	2. add one
	3. reverse back

	Time		O(3n)
	Space		O(1)
	0 ms, faster than 100.00%
*/
func plusOne1(head *ListNode) *ListNode {
	head = reverseList(head)

	cur := head
	carry := 1
	for cur != nil {
		num := cur.Val + carry
		if num == 10 {
			cur.Val = 0
		} else {
			cur.Val = num
			carry = 0
		}
		cur = cur.Next
	}

	head = reverseList(head)

	if carry == 1 {
		return &ListNode{1, head}
	}
	return head
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	cur := head
	for head.Next != nil { // since we are replacing the head.next, the loop should end when there is no next
		temp := head.Next          // the middle node
		head.Next = head.Next.Next // or head.Next.Next
		temp.Next = cur            // put the middle node in front of cur
		cur = temp                 // assign cur as head
	}
	return cur
}

func main() {

}
