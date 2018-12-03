package main

type MyQueue struct {
	MainStack  []int
	MinorStack []int
}

/** Initialize your data structure here. */
func Constructor() MyQueue {
	return MyQueue{[]int{}, []int{}}
}

/** Push element x to the back of queue. */
func (this *MyQueue) Push(x int) {
	for len(this.MainStack) > 0 {
		top := this.MainStack[len(this.MainStack)-1]
		this.MainStack = this.MainStack[:len(this.MainStack)-1]
		this.MinorStack = append(this.MinorStack, top)
	}
	this.MainStack = append(this.MainStack, x)
	for len(this.MinorStack) > 0 {
		top := this.MinorStack[len(this.MinorStack)-1]
		this.MinorStack = this.MinorStack[:len(this.MinorStack)-1]
		this.MainStack = append(this.MainStack, top)
	}
}

/** Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
	top := this.MainStack[len(this.MainStack)-1]
	this.MainStack = this.MainStack[:len(this.MainStack)-1]
	return top
}

/** Get the front element. */
func (this *MyQueue) Peek() int {
	return this.MainStack[len(this.MainStack)-1]
}

/** Returns whether the queue is empty. */
func (this *MyQueue) Empty() bool {
	return len(this.MainStack) == 0
}

func main() {

}
