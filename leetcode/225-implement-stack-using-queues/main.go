package main

type MyStack struct {
	MainQueue  []int
	MinorQueue []int
}

/** Initialize your data structure here. */
func Constructor() MyStack {
	return MyStack{[]int{}, []int{}}
}

/** Push element x onto stack. */
func (this *MyStack) Push(x int) {
	for len(this.MainQueue) > 0 {
		head := this.MainQueue[0]
		this.MainQueue = this.MainQueue[1:]
		this.MinorQueue = append(this.MinorQueue, head)
	}
	this.MainQueue = append(this.MainQueue, x)
	for len(this.MinorQueue) > 0 {
		top := this.MinorQueue[0]
		this.MinorQueue = this.MinorQueue[1:]
		this.MainQueue = append(this.MainQueue, top)
	}
}

/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() int {
	head := this.MainQueue[0]
	this.MainQueue = this.MainQueue[1:]
	return head
}

/** Get the top element. */
func (this *MyStack) Top() int {
	return this.MainQueue[0]
}

/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
	return len(this.MainQueue) == 0
}

func main() {

}
