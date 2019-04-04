package main

type MyCircularDeque struct {
	Head int
	Tail int
	Cap  int
	Nums []int
}

/*
	3rd approach: classic 2 pointers

	- move head and tail when we add values into the queue
	- head = tail = -1 means empty queue
	- move forward: (this.Tail - 1 + this.Cap) % this.Cap
	- move backward: this.Tail = (this.Tail - 1 + this.Cap) % this.Cap

	16 ms, faster than 100.00%
*/

/** Initialize your data structure here. Set the size of the deque to be k. */
func Constructor(k int) MyCircularDeque {
	fixedNums := make([]int, k)
	return MyCircularDeque{-1, -1, k, fixedNums}
}

/** Adds an item at the front of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) InsertFront(value int) bool {
	if this.IsFull() {
		return false
	}
	// very important
	// when we create a new entity, move our to 0
	if this.IsEmpty() {
		this.Head = 0
		this.Tail = 0
		this.Nums[this.Head] = value
		return true
	}
	this.Head = (this.Head - 1 + this.Cap) % this.Cap
	this.Nums[this.Head] = value
	return true
}

/** Adds an item at the rear of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) InsertLast(value int) bool {
	if this.IsFull() {
		return false
	}
	// very important
	// when we create a new entity, move our to 0
	if this.IsEmpty() {
		this.Head = 0
	}
	this.Tail = (this.Tail + 1) % this.Cap
	this.Nums[this.Tail] = value
	return true
}

/** Deletes an item from the front of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) DeleteFront() bool {
	if this.IsEmpty() {
		return false
	}
	if this.Head == this.Tail {
		this.Head = -1
		this.Tail = -1
		return true
	}
	this.Head = (this.Head + 1) % this.Cap
	return true
}

/** Deletes an item from the rear of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) DeleteLast() bool {
	if this.IsEmpty() {
		return false
	}
	if this.Head == this.Tail {
		this.Head = -1
		this.Tail = -1
		return true
	}
	this.Tail = (this.Tail - 1 + this.Cap) % this.Cap
	return true
}

/** Get the front item from the deque. */
func (this *MyCircularDeque) GetFront() int {
	if this.IsEmpty() {
		return -1
	}
	return this.Nums[this.Head]
}

/** Get the last item from the deque. */
func (this *MyCircularDeque) GetRear() int {
	if this.IsEmpty() {
		return -1
	}
	return this.Nums[this.Tail]
}

/** Checks whether the circular deque is empty or not. */
func (this *MyCircularDeque) IsEmpty() bool {
	return this.Head == -1 && this.Tail == -1
}

/** Checks whether the circular deque is full or not. */
func (this *MyCircularDeque) IsFull() bool {
	return (this.Tail+1)%this.Cap == this.Head
}

func main() {

}
