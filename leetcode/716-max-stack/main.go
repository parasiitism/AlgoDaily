package main

import "fmt"

/*
	Common approach
	- store the value and max for each item so the push(), pop(), top(), peek() are O(1)
	- but PopMax() inevitably needs to find top-most max item and update the top items' max, it takes O(n)
	60ms beats 57.14%
	26jan2019
*/

type Item struct {
	Val int
	Max int
}

type MaxStack struct {
	Stack []Item
}

/** initialize your data structure here. */
func Constructor() MaxStack {
	return MaxStack{[]Item{}}
}

func (this *MaxStack) Push(x int) {
	if len(this.Stack) == 0 {
		this.Stack = append(this.Stack, Item{x, x})
		return
	}
	max := this.PeekMax()
	if x > max {
		this.Stack = append(this.Stack, Item{x, x})
	} else {
		this.Stack = append(this.Stack, Item{x, max})
	}
}

func (this *MaxStack) Pop() int {
	if len(this.Stack) == 0 {
		return -1
	}
	temp := this.Stack[len(this.Stack)-1]
	this.Stack = this.Stack[:len(this.Stack)-1]
	return temp.Val
}

func (this *MaxStack) Top() int {
	if len(this.Stack) == 0 {
		return -1
	}
	return this.Stack[len(this.Stack)-1].Val
}

func (this *MaxStack) PeekMax() int {
	if len(this.Stack) == 0 {
		return -1
	}
	return this.Stack[len(this.Stack)-1].Max
}

func (this *MaxStack) PopMax() int {
	if len(this.Stack) == 0 {
		return -1
	}
	// rmeove max
	max := this.PeekMax()
	var temp Item
	i := len(this.Stack) - 1
	for ; i >= 0; i-- {
		if max == this.Stack[i].Val {
			temp = this.Stack[i]
			clone := []Item{}
			clone = append(clone, this.Stack[:i]...)
			clone = append(clone, this.Stack[i+1:]...)
			this.Stack = clone
			break
		}
	}

	// update items' max
	for ; i < len(this.Stack); i++ {
		cur := this.Stack[i]
		if i > 0 {
			prev := this.Stack[i-1]
			if cur.Val > prev.Max {
				this.Stack[i].Max = cur.Val
			} else {
				this.Stack[i].Max = prev.Max
			}
		} else {
			this.Stack[i].Max = cur.Val
		}
	}

	return temp.Val
}

func main() {
	// s := Constructor()
	// s.Push(5)
	// s.Push(1)
	// s.Push(5)
	// fmt.Println(s.Top())     // 5
	// fmt.Println(s.PopMax())  // pop 5
	// fmt.Println(s.Top())     // 1
	// fmt.Println(s.PeekMax()) // 5
	// fmt.Println(s.Pop())     // pop 1
	// fmt.Println(s.Top())     // 5

	s := Constructor()
	s.Push(5)
	s.Push(1)
	fmt.Println(s.PopMax())
	fmt.Println(s.PeekMax())
	fmt.Println(s.PopMax())
	fmt.Println(s.Stack)
}
