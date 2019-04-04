package main

import (
	"fmt"
)

type MyCircularQueue struct {
	Head  int
	Tail  int
	Size  int
	Queue []int
}

/** Initialize your data structure here. Set the size of the queue to be k. */
func Constructor(k int) MyCircularQueue {
	fixedNums := make([]int, k)
	return MyCircularQueue{-1, -1, k, fixedNums}
}

/** Insert an element into the circular queue. Return true if the operation is successful. */
func (this *MyCircularQueue) EnQueue(value int) bool {
	if this.IsFull() {
		return false
	}
	if this.IsEmpty() {
		this.Head = 0
	}
	this.Tail = (this.Tail + 1) % this.Size
	this.Queue[this.Tail] = value
	return true
}

/** Delete an element from the circular queue. Return true if the operation is successful. */
func (this *MyCircularQueue) DeQueue() bool {
	if this.IsEmpty() {
		return false
	}
	// for DeQueue, we dont need to care about the value on nums[i] after we i++,
	// becos we will override it later

	// it means there is only one value in the queue
	if this.Head == this.Tail {
		this.Head = -1
		this.Tail = -1
		return true
	}
	// move forward our head
	this.Head = (this.Head + 1) % this.Size
	return true
}

/** Get the front item from the queue. */
func (this *MyCircularQueue) Front() int {
	if this.IsEmpty() {
		return -1
	}
	return this.Queue[this.Head]
}

/** Get the last item from the queue. */
func (this *MyCircularQueue) Rear() int {
	if this.IsEmpty() {
		return -1
	}
	return this.Queue[this.Tail]
}

/** Checks whether the circular queue is empty or not. */
func (this *MyCircularQueue) IsEmpty() bool {
	return this.Head == -1
}

/** Checks whether the circular queue is full or not. */
func (this *MyCircularQueue) IsFull() bool {
	return (this.Tail+1)%this.Size == this.Head
}

func main() {
	obj := Constructor(3)
	obj.EnQueue(1)
	obj.EnQueue(2)
	fmt.Println(obj.EnQueue(3))
	fmt.Println(obj.EnQueue(4), obj)
	fmt.Println(obj.IsFull())
	fmt.Println(obj.DeQueue())
	fmt.Println(obj.IsFull())
	fmt.Println(obj.EnQueue(4))
	fmt.Println(obj.IsFull())
	fmt.Println(obj.Front())
	fmt.Println(obj.Rear())
}
