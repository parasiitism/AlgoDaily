package main

/*
1st attempt: classic singly linked list
beats 78.57%
*/

type Node struct {
	Val  int
	Next *Node
}

type MyLinkedList struct {
	Head   *Node
	Length int
}

/** Initialize your data structure here. */
func Constructor() MyLinkedList {
	return MyLinkedList{}
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (this *MyLinkedList) Get(index int) int {
	if index >= this.Length {
		return -1
	}
	cur := this.Head
	cnt := 0
	for cnt != index {
		if cur.Next != nil {
			cur = cur.Next
			cnt++
		}
	}
	return cur.Val
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
func (this *MyLinkedList) AddAtHead(val int) {
	temp := Node{val, nil}
	temp.Next = this.Head
	this.Head = &temp
	this.Length++
}

/** Append a node of value val to the last element of the linked list. */
func (this *MyLinkedList) AddAtTail(val int) {
	temp := Node{val, nil}
	cur := this.Head
	for cur.Next != nil { // find the tail
		cur = cur.Next
	}
	cur.Next = &temp
	this.Length++
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index > this.Length {
		return
	} else if index == 0 {
		this.AddAtHead(val)
		return
	} else if index == this.Length {
		this.AddAtTail(val)
		return
	}
	// find target position
	var prev *Node
	cur := this.Head
	cnt := 0
	for cnt != index {
		if cur.Next != nil {
			prev = cur
			cur = cur.Next
			cnt++
		}
	}
	// add
	temp := Node{val, nil}
	temp.Next = cur
	prev.Next = &temp
	this.Length++
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index >= this.Length {
		return
	}
	// find target position
	var prev *Node
	cur := this.Head
	cnt := 0
	for cnt != index {
		if cur.Next != nil {
			prev = cur
			cur = cur.Next
			cnt++
		}
	}
	if prev != nil {
		prev.Next = cur.Next
	} else {
		this.Head = cur.Next
	}
	this.Length--
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */

func main() {

}
